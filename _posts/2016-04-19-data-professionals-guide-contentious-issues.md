---
layout: post
title: 'Why You''re Wrong: The Data Professional’s Guide To Contentious Issues'
date: '2016-04-19 11:10:03 +0000'
categories:
- Database Design
- MSSQL
- Musings
- SQL MVP
tags:
- DAC
- NULLs
- objects
- ORM
- schemas
- server core
- sql server
- Triggers
---

[caption id="attachment_17355" align="aligncenter" width="500"]<a href="http://michaeljswart.com/2011/01/ridiculously-unnormalized-database-schemas-part-one/"><img class="wp-image-17355 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/04/codd.png" alt="Codd hates you: Data Professional’s Guide To Contentious Issues" width="500" height="300" /></a> Image courtesy of Michael J. Swart: http://michaeljswart.com/[/caption]

The Internet is an angry place.

Lots of angry people, <a href="http://lifehacker.com/5811255/why-you-cant-win-an-argument-on-the-internet">arguing with strangers</a> over useless topics, or <a href="http://www.cnet.com/news/watch-snoop-dogg-get-very-angry-at-bill-gates/">blaming former executives about things that they cannot fix</a>. So many people trying to show that they are the smartest person in the room. So much wasted energy.

Except, of course, when it comes to <a href="http://www.datamodel.com/index.php/2016/01/21/database-design-throwdown-texas-style/" target="_blank">arguing about databases, or data</a>. Such debates are worth every minute if only to watch the other persons head explode when you tell them how wrong they are to use NULLs, or using tbl_ for table names, or tabs instead of spaces.

I’m here to put an end to the debates. Today we will examine the data professional's guide to contentious issues.

You’re welcome.
<h2>SQL pronunciations</h2>
First and foremost is the fact that most <a href="http://english.stackexchange.com/questions/7231/how-is-sql-pronounced" target="_blank">don’t know how to even pronounce ‘SQL Server’</a>. Is it ‘sequel’, or do we sound out the letters ‘Ess-Queue-Ell’? Early in my career I was repeatedly corrected to include ‘Microsoft’ whenever I said ‘sequel’ server because Sybase also had SQL Server and it was confusing. For that person. They had issues. Anyway, it is rare for me to hear anyone say ‘ess-queue-ell’ server these days, but those that do are well respected and I’d be an idiot to think about correcting them publicly on anything even when they are quite wrong. And don’t get me started on the whole <a href="https://dev.mysql.com/doc/refman/5.7/en/what-is-mysql.html" target="_blank">MySQL crowd</a>.
<h2>Maintenance plans</h2>
We all start out with zero knowledge of SQL Server, and we often end up using <a href="https://msdn.microsoft.com/en-us/library/ms187658.aspx" target="_blank">maintenance plans</a> to handle backups and other tasks. Then, as our knowledge increases, we realize that <a href="https://ola.hallengren.com/" target="_blank">custom scripts work best for these tasks</a>. And then, some of us go WAY out of their way to <span style="text-decoration: line-through;">tell</span> mock the folks using maintenance plans how wrong they are for doing so. I really don’t care what you use, as long as you are <a href="http://minionware.net/" target="_blank">using something</a> and that something would be custom scripts.
<h2>Object Relational Mapping (ORM) tools</h2>
When used properly, ORM tools such as nHibernate and Entity Framework (EF) can add value to your business. Unfortunately they are rarely used properly, making ORMs one of the most hated things touching your data other than <a href="https://twitter.com/trumpdba" target="_blank">@TrumpDBA</a>. If you want happy servers, good performance, and data quality then <a href="http://blog.waynesheffield.com/wayne/archive/2012/06/orm-tools/" target="_blank">don’t use ORMs</a>.
<h2>Database tools on servers</h2>
Installing database management tools, such as SQL Server Management Studio (SSMS), on your database servers can be viewed as a security risk by your audit team. But for the people that can’t stand working from a command line (see next item), the thought of a server without SSMS drives them into fits of rage. The fact is there is no reason to install management tools on the server itself. You can connect remotely just fine. And those times that you can’t? You know, for the one or two edge cases? Well, that’s when you have script(s) ready to be run from the command line.
<h2>Server Core</h2>
Server core is a wonderful way for you to <a href="https://thomaslarock.com/2013/03/administering-sql-server-running-on-server-core/" target="_blank">keep data professionals away from your database that shouldn’t belong touching it anyway</a>. For the data professionals that can’t live without a GUI, server core is a nightmare. I can’t wait to see how they react to SQL Server on Linux.
<h2>Triggers</h2>
Triggers, once a necessity to maintain referential integrity for your data, are still a favorite for many. They allow you to do wonderful things such as increase administrative overhead, cause performance problems, and modify data without anyone knowing. <a href="https://thomaslarock.com/2009/03/sql-database-triggers/" target="_blank">Your life as a data professional is better without them</a>. Let’s agree to leave them in the 1990s where they belong.
<h2>Schemas</h2>
About the only time I see schemas are inside of the AdventureWorks database. Every other database appears to use the dbo schema and nothing else. No, I don’t know why, but I suspect it is because permissions are hard. While the use of schemas make <a href="http://stackoverflow.com/questions/19384019/ownership-chaining-not-working-between-two-schemas-in-the-same-database" target="_blank">ownership chaining more difficult at times</a> just because something is a tad bit harder at times isn’t a valid reason for avoiding it altogether. If that were the case then we’d have people arguing against the use of Server Core (oh, wait…)
<h2>Object Naming</h2>
Objects should be given names that help another person to understand what they are, or what they contain. A common way to do this is “<a href="https://msdn.microsoft.com/en-us/library/aa260976(v=vs.60).aspx" target="_blank">Hungarian notation</a>”, which leaves us with common prefixes such as sp_*, vw_* and one of my all-time favorites tbl_*. None of these bother me; all I ask for is consistency throughout the schema to make things easier for anyone trying to understand what they are looking at.
<h2>Remote Dedicated Admin Connections</h2>
Another line item for the audit team: not allowing the use of the Dedicated Admin Connection (DAC). Because, you know, someone could use that to perform admin tasks. It’s as if those pesky auditors don’t trust anyone! Well, remind the auditors that since you don’t allow management tools to be installed on the server (see above), and you may not always be able to remote to the server (or <a href="https://azure.microsoft.com" target="_blank">walk into the datacenter</a>), it’s a good idea to have the <a href="https://msdn.microsoft.com/en-us/library/ms190468.aspx" target="_blank">DAC enabled for remote connections</a>.
<h2>Tabstops</h2>
I can’t believe that “tabs versus spaces” is even a topic for discussion at all. The answer is tabs, people. And the tabstop should equal four spaces. Anything else is an abomination. Oh, and your KEYWORDS need to be in UPPERCASE otherwise I’m not debugging your code. Let’s move on.
<h2>Test Matches Production</h2>
I’ve lost many hours of my life trying to root out performance issues based upon the statement “it ran fine in test”. Test data rarely matches production data, and if you have run your code against 10 rows and it suddenly chokes the production server’s 10 million rows, that’s not my fault. Your test data MUST match your production data. If you can’t have test match production, you should at least have an idea of the production volumes you will be hitting, or <a href="https://thomaslarock.com/2015/07/how-to-recreate-sql-server-statistics-in-a-different-environment/" target="_blank">perhaps grab the stats</a>. Or just test in production because we know that’s what you’ve been doing anyway.

The above is really only a partial list of the silly arguments I’ve seen people have over the years. While I’ve shared my opinions on the issues above, I feel it necessary to remind you that there is never one right answer. It always comes down to cost, benefits, and risk.

Well, except for triggers. And NULLs.

I hate them both and you are wrong for using them.