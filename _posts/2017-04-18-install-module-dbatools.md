---
layout: post
title: Install-Module dbatools
date: '2017-04-18 10:37:14 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- administration
- dbatools
- Powershell
- sql server
---

There are a lot of moving parts to any application system. One such moving part is the creation and dependence upon the use of <a href="https://docs.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine" target="_blank" rel="noopener">linked servers inside of SQL Server</a>. These linked servers give users the ability to write queries as if the data was local by <a href="https://technet.microsoft.com/en-us/library/ms190406(v=sql.105).aspx" target="_blank" rel="noopener">referencing a four-part name</a>. I've written before about the use of <a href="https://thomaslarock.com/2013/05/top-3-performance-killers-for-linked-server-queries/" target="_blank" rel="noopener">linked servers and the performance issues that may arise</a>. Today I want to talk about something more fundamental about linked servers: connectivity.

Creating a linked server is fairly straightforward, you can read the reference <a href="https://docs.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine" target="_blank" rel="noopener">here</a>. You have a handful of ways to handle authentication between the instances. <a href="https://msdn.microsoft.com/en-us/library/aa560998.aspx" target="_blank" rel="noopener">These methods</a> include using the security context for the current login, for the current user, or passing along remote credentials. The one you choose will depend on your needs and requirements. The specific method chosen isn't important for today's post. Today is more about the failure to communicate between servers.

Connections between servers can fail for a variety of reasons. Permissions get changed, AD accounts get modified (or removed), passwords get reset. And sometimes the use of a linked server gets lost over time. It was not uncommon for me to migrate databases to a new server and find out weeks later that a linked server was needed. At some point in my career, I had been bitten enough times by linked servers failing to connect that I built a way to automate the checking of the linked server connections. I wrote about it <a href="https://www.mssqltips.com/sqlservertip/2017/script-to-check-all-your-linked-server-connections-for-sql-server/" target="_blank" rel="noopener">here</a>, and I even <a href="https://thomaslarock.com/2016/03/sql-server-linked-server-connection-test/" target="_blank" rel="noopener">updated the script recently</a>. And I would have put that script into GitHub by now if not for last February, while at <a href="http://sqlkonferenz.de/" target="_blank" rel="noopener">SQL Konferenz in Darmstadt, Germany</a>, I was struck with an idea.

While having some post-event German beverages I was talking with William Durkin (<a href="http://www.williamdurkin.com/" target="_blank" rel="noopener">blog</a> | <a href="https://twitter.com/sql_williamd" target="_blank" rel="noopener">@sql_williamd</a>) regarding the <a href="https://dbatools.io/" target="_blank" rel="noopener">DBAtools.io project</a>. This project is wonderful for migrating data between servers, or even an entire instance. I noticed that there was no cmdlet for testing a linked server connection. I asked "hey, do you think that might be something useful?" William said yes, and off I went to email Chrissy LeMaire (<a href="https://dbatools.io/blog/" target="_blank" rel="noopener">blog</a> | <a href="https://twitter.com/cl" target="_blank" rel="noopener">@cl</a>).

A few emails later I found myself connecting to the dbatools.io GitHub repo and merging my cmdlet into the project. So <a href="https://dbatools.io/functions/test-dbalinkedserverconnection/" target="_blank" rel="noopener">that's where my code now sits</a>, for everyone to use.

You could download my specific cmdlet easily, but what you should do is download all the DBAtools.io goodness. DBAtools.io is in the Microsoft Powershell gallery, so installing DBAtools as easy as running this command:
<pre lang="powershell">Install-Module dbatools</pre>
<a href="https://thomaslarock.com/wp-content/uploads/2017/04/install_dba_tools.jpg"><img class="aligncenter size-large wp-image-17770" src="https://thomaslarock.com/wp-content/uploads/2017/04/install_dba_tools-600x272.jpg" alt="Install-Module dbatools" width="600" height="272" /></a>

And then you can run any of the commands easily. Ever want to safely remove a database? There's a cmdlet for that: <a href="https://dbatools.io/functions/remove-dbadatabasesafely/" target="_blank" rel="noopener">Remove-DbaDatabaseSafely</a>. You can <a href="https://dbatools.io/functions/" target="_blank" rel="noopener">find a cmdlet</a> for just about everything. And, if you don't see one, you can contribute to the project and <a href="https://github.com/sqlcollaborative/dbatools/blob/master/contributing.md" target="_blank" rel="noopener">add the missing cmdlet to the project</a>.

For a while now I have been meaning to take all the scripts I've used over the years and get them loaded to my GitHub repo for everyone to use and modify as they see fit. I like the idea of contributing to this project instead. I'm not going to spend time trying to market and pimp my scripts at my own repo, it's easier for me to share what I can over at <a href="http://dbatools.io/" target="_blank" rel="noopener">dbatools.io</a>. I'd rather contribute to the larger project there than have a bunch of scripts here.
<h2>Summary</h2>
The <a href="http://dbatools.io/" target="_blank" rel="noopener">dbatools.io</a> project is awesome. I like it and I think you should, too. I've contributed and I think you should, too. Being a part of the <a href="http://dbatools.io/" target="_blank" rel="noopener">dbatools.io</a> team reminds me of what it was like when I was first starting out as a DBA and I exchanged ideas with a handful of folks I would meet at conferences. If you are just getting started in SQL Server administration, are looking for some tools, and want an easy way to learn some PowerShell, then <a href="http://dbatools.io/" target="_blank" rel="noopener">dbatools.io</a> is the place for you.