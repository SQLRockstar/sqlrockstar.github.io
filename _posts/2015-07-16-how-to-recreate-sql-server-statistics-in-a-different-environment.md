---
layout: post
title: 'HOW TO: Recreate SQL Server Statistics In a Different Environment'
date: '2015-07-16 14:35:00 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- sql server
- Statistics
---

Did you know table and index statistics are the most important piece of metadata for your database?

The reason for this has to do with how SQL Server (and other database engines) build query execution plans. The query optimizer builds an execution plan based upon the statistical data available at the time. If you have bad statistics you are gong to have sub-optimal plans, with poor performance being the result.

Statistics are so important for performance that we have a <a href="https://ola.hallengren.com/sql-server-index-and-statistics-maintenance.html" target="_blank">host</a> of <a href="http://minionware.net/" target="_blank">scripts</a> and <a href="https://www.simple-talk.com/sql/performance/sql-server-statistics-questions-we-were-too-shy-to-ask/" target="_blank">tips</a> and <a href="http://www.databasejournal.com/features/mssql/sql-server-index-statistics.html" target="_blank">tricks</a> on how to keep your statistics as up to date as possible. Even novice administrators reach for the UPDATE STATISTICS statement whenever they have a performance issue they can't solve right away and they need a quick fix.

Knowing that statistics are so important you might think it crazy for trying to find a way to adjust the statistics in order to make SQL Server think it has more rows than it really does.

Why would anyone want to do this? Great question. I can think of three reasons why this would be important.

First, <strong>you may not have enough space to do a restore</strong>. You may find that you don’t have enough space on your local machine to restore that 30TB production database. This makes it hard to research performance issues at times, which leads to developers being granted access to production in order to do some “break-fix” repair work. That’s not ideal.

Second, <strong>agile can be woefully inadequate for performance testing</strong>. Just because that code works against 100 rows in development doesn’t mean it will run well against millions of rows in production. Most agile coding seems to focus on functionality first and rarely considers the effects of increased data volumes as time goes on. Being able to manipulate the object statistics allows for enhanced testing plans and a better chance at a successful production deployment.

Lastly, <strong>you may not want people to see your data</strong>. You may need help from someone, say at Microsoft support, but you need to keep your data private. You can provide them the object DDL and allow them to examine query plans without them seeing your all of your sensitive data. More on this later.
<h2>The UPDATE STATISTICS Statement</h2>
Now that I know why I might want to do this, I need to figure out what is possible. Lucky for me the <a href="https://msdn.microsoft.com/en-us/library/ms187348" target="_blank">UPDATE STATISTICS entry over at MSDN</a> lists some extra options at the bottom of the syntax that appear to be helpful:
<pre>&lt;update_stats_stream_option&gt;  ::=     
      [ STATS_STREAM = stats_stream ]     
      [ ROWCOUNT = numeric_constant ]     
      [ PAGECOUNT = numeric_contant ]
</pre>
&nbsp;

And further down the page you will find this remark:
<pre>&lt;update_stats_stream_option&gt;
Identified for informational purposes only. Not supported. Future compatibility 
is not guaranteed.
</pre>
&nbsp;

I have no idea why this MSDN entry would even include the syntax for what appears to be an undocumented option. But they did, so now I’m curious to know how to use these options. A quick <span style="text-decoration: line-through;">Google</span> Bing search and I come back with <a href="http://blogs.msdn.com/b/queryoptteam/archive/2006/07/21/674350.aspx" target="_blank">this blog post</a>.

The post has an example of how to use the syntax for the ROWCOUNT and PAGECOUNT options only. What good is altering the ROWCOUNT and PAGECOUNT if you don’t know the distribution of the data? Not much, if you ask me. The object statistics contain more than just rowcounts and pagecounts, there is a <a href="https://www.simple-talk.com/sql/learn-sql-server/statistics-in-sql-server/" target="_blank">histogram</a> as well that tells the optimizer the distribution of the data for the object. I know I need to recreate the histogram data somehow.

So that’s when I decided to stop <span style="text-decoration: line-through;">Googling</span> <span style="text-decoration: line-through;">Binging</span> <span style="text-decoration: line-through;">Banging</span> searching for details on an undocumented feature and I dropped an email to Tim Chapman (<a href="http://blogs.technet.com/b/mspfe/" target="_blank">blog</a>, <a href="https://twitter.com/chapmandew" target="_blank">@chapmandew</a>) who was shocked to hear that I had no idea about these undocumented features. I asked about the STATS_STREAM option and got back a reply that was like a siren song:

“That’s the histogram.”

Tim, you can sing that to me again, anytime. This is one of those times where I remember how much I love working with SQL Server and to find something new after all these years.
<h2>How To Recreate SQL Server Statistics In a Different Environment</h2>
First, let’s grab a query we can examine in detail. I’ll use this one inside of AdventureWorks2014. It’s a simple join and it results in 121,317 rows being returned.
<pre lang="tsql">SELECT *
FROM Production.Product p
INNER JOIN Sales.SalesOrderDetail s 
	ON s.ProductID = P.ProductID
</pre>
I will turn on 'Include Actual Execution Plan' inside of SQL Server Management Studio (SSMS) and see that the query plan has this shape:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/exec-plan.png"><img class="aligncenter size-full wp-image-16926" src="https://thomaslarock.com/wp-content/uploads/2015/07/exec-plan.png" alt="exec-plan" width="908" height="243" /></a>

All good so far. What I want to do now is take these two tables and recreate them in a different environment but schema only, no data. I will script out the DDL for the two tables by right-clicking on the database name inside of SSMS and navigating to the ‘Generate Scripts’ task:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/script-edit.png"><img class="aligncenter wp-image-16936 size-large" src="https://thomaslarock.com/wp-content/uploads/2015/07/script-edit-600x498.png" alt="script-edit" width="600" height="498" /></a>

For this example I will select my Production.Product table:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/product-edit.png"><img class="aligncenter size-full wp-image-16929" src="https://thomaslarock.com/wp-content/uploads/2015/07/product-edit.png" alt="product-edit" width="729" height="678" /></a>

Click next and on the following screen we want to find the Advanced button:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/advanced-edit.png"><img class="aligncenter size-full wp-image-16930" src="https://thomaslarock.com/wp-content/uploads/2015/07/advanced-edit.png" alt="advanced-edit" width="729" height="678" /></a>

Hidden inside of the advanced options is this little gem:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/stats-edit.png"><img class="aligncenter size-full wp-image-16931" src="https://thomaslarock.com/wp-content/uploads/2015/07/stats-edit.png" alt="stats-edit" width="542" height="481" /></a>

That’s right, I can script out the stats and the histogram! Here’s what they will look like when done (binary value truncated for displaying here):

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/update.png"><img class="aligncenter size-full wp-image-16932" src="https://thomaslarock.com/wp-content/uploads/2015/07/update.png" alt="update" width="463" height="123" /></a>

If you were thinking "hey, how can I get this without using the GUI and generating a script" you are not alone because I was wondering the same thing and found that the <a href="https://msdn.microsoft.com/en-us/library/ms174384" target="_blank">DBCC SHOW_STATISTICS command allows for the STATS_STREAM option</a>. And, just as with the UPDATE STATISTICS command, it has the same message about it being included for informational purposes only. So, this command will return the same information as the DDL script we are generating:
<pre lang="tsql">DBCC SHOWSTATISTICS ("Sales.SalesOrderDetail", PK_SalesOrderDetail_SalesOrderID_SalesOrderDetailID)
WITH STATS_STREAM
</pre>
What this means is we can script this action if so desired and make it a part of a repeatable testing process. That's good to know.

OK, we've got what we need, now let’s put these to work for us. Next, I will create an empty database:
<pre lang="tsql">CREATE DATABASE TestStats</pre>
Now we will run the DDL but I am only going to create the tables, not update any statistics yet. Why? Because I want to know the plan shape before I modify the underlying stats, just as a reasonable check. So let's create the tables and run our SELECT statement and take a look at the plan:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/query.png"><img class="aligncenter size-full wp-image-16933" src="https://thomaslarock.com/wp-content/uploads/2015/07/query.png" alt="query" width="877" height="238" /></a>

OK, that’s good, it’s a very different plan, and that’s because the stats on the table reflect there is no data. So now I will run the statements to create and update the statistics from AdventureWorks2014 and let’s look at the estimated plan now:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/query2.png"><img class="aligncenter size-full wp-image-16934" src="https://thomaslarock.com/wp-content/uploads/2015/07/query2.png" alt="query2" width="928" height="242" /></a>

The plan is identical to the one from AdventureWorks2014, as expected. Success!

This means it is possible for me to adjust the stats WITHOUT the need to load actual data. That allows for me to examine query plans between environments for any of the use cases described at the beginning.

Remember when I promised "more on this later"? Well, that time is now.

The histograms we migrated contain data for the leading column of the index. I want you to understand that there is <em><span style="text-decoration: underline;">some</span></em> data that will be migrated and it is <em><span style="text-decoration: underline;">possible</span></em> that this data could be considered sensitive. For an example of this let me show you what happens if I run the DBCC SHOW_STATISTICS command against an index in the Person.Address table in AdventureWorks2014 as follows:

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/sensitive.png"><img class="aligncenter size-full wp-image-16941" src="https://thomaslarock.com/wp-content/uploads/2015/07/sensitive.png" alt="sensitive" width="820" height="609" /></a>

So, yeah, be careful out there.

As great as all of this might seem I must remind you that YOU ARE SCREWING WITH YOUR STATS! Put things back when you are done! Don't make me use more exclamation points! I’d advise that when you do this kind of testing you create new, empty databases that no one is using. Otherwise you run the risk of having the alterations affecting performance for others, causing more pain and grief than necessary.

Not to mention the phone calls telling you all the queries are returning zero rows. Nobody wants that.

Enjoy!
