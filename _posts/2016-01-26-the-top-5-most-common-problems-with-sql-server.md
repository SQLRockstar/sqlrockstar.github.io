---
layout: post
title: The Top 5 Most Common Problems With SQL Server
date: '2016-01-26 07:24:27 +0000'
categories:
- Featured
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- Database Design
- design
- indexes
- microsoft
- performance
- problems
- sql server
- Troubleshooting
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/do-not-enter-rz-lg.jpeg" rel="attachment wp-att-17281"><img class="aligncenter size-full wp-image-17281" src="https://thomaslarock.com/wp-content/uploads/2016/01/do-not-enter-rz-lg.jpeg" alt="Top 5 Most Common Problems With SQL Server" width="509" height="339" /></a>I've been working with SQL Server since what seems like forever ++1. The truth is I haven't been a production DBA in more than 6 years (I <a href="http://www.solarwinds.com/head-geeks/thomas-larock.aspx" target="_blank" rel="noopener">work in marketing now</a>, in case you didn't know). That means I will soon hit a point in my life where I will be an ex-DBA for the same period of time as I was a production DBA (about seven years).

I am fortunate that I still work with SQL Server daily. I am still consulted from time to time on various projects and performance troubleshooting. It helps keep my skills sharp. I also get to continue to build content as part of my current role, which is a wonderful thing because one of the best ways to learn something is to try to teach it to others.

All of this means that over the years I've been able to compile a list of issues that I would consider to be common with SQL Server (and other database platforms like Oracle, no platform is immune to such issues). These are the issues that are often avoidable but not always easy to fix once they have become a problem. The trick for senior administrators such as myself is to help teams understand the costs, benefits, and risks of their application design options so as to avoid these common problems.

So, here is my list of the top 5 most common problems with SQL Server.
<h2>Indexes</h2>
Indexes are the number one cause of problems with SQL Server. That doesn't mean SQL Server doesn't do indexes well. These days SQL Server does indexing quite well, actually. No, the issue with indexes and SQL Server have to do with how easy it easy for users to make mistakes with regards to indexing. Missing indexes, wrong indexes, too many indexes, outdated statistics, or a lack of index maintenance are all common issues for users with little to no experience (what we lovingly call 'accidental DBAs').

I know, this area covers a LOT of ground. The truth is that with a little bit of regular maintenance a lot of these issues disappear. Keep in mind that your end-users don't get alerted that the issue is with indexing. They just know that their queries are taking too long, and that's when your phone rings. It's up to you to <a href="https://www.simple-talk.com/sql/performance/tune-your-indexing-strategy-with-sql-server-dmvs/" target="_blank" rel="noopener">know and understand how indexing works</a> and how to design proper maintenance.
<h2>Poor designs decisions</h2>
Everyone agrees that great database performance starts with great database design. Yet we still have issues with poor datatype choices, <a href="https://www.simple-talk.com/sql/performance/the-seven-sins-against-tsql-performance/" target="_blank" rel="noopener">the use of nested views</a>, lack of data archiving, <a href="https://thomaslarock.com/2012/01/do-you-make-these-5-database-design-mistakes/" target="_blank" rel="noopener">and relational databases with no primary or foreign keys defined</a>.

Seriously. No keys defined. At all. You might as well have a bunch of Excel spreadsheets tied together with PowerShell, deploy them to a bunch of cluster nodes with flash drives and terabytes of RAM, and then market that as PowerNoSQL. You're welcome.

It is difficult to make changes to a system once it has been deployed to production. This means that poor design choices are something that will linger for years. And that bad design often forces developers to make decisions that end up with...
<h2>Bad code</h2>
Of course saying 'bad code' is subjective. Each of us has a different definition of bad. To me the phrase 'bad code' covers examples such as unnecessary cursors, incorrect WHERE clauses, and a reliance on user-defined functions (because T-SQL should work similar to C++, apparently). Bad code on top of bad design will lead to concurrency issues, resulting in things like <a href="https://www.simple-talk.com/sql/database-administration/the-dba-as-detective-troubleshooting-locking-and-blocking/" target="_blank" rel="noopener">blocking, locking</a>, and <a href="https://www.simple-talk.com/sql/database-administration/handling-deadlocks-in-sql-server/" target="_blank" rel="noopener">deadlocks</a>.

Because of the combination of bad code on top of poor design there has been a significant push to make the querying of a database something that can be automated. The end result has been a rise in the use of...
<h2>ORMs</h2>
Object-Relational Mapping (ORM) tools have been around for a while now. I often refer to such tools as code-first generators. When used properly they can work well. Unfortunately they often are not used properly, with the result being bad performance and wasted resources. ORMs are so frequent a problem that it has become easy to identify that they are the culprit. It's like instead of wiping their fingerprints from a crime scene the ORM will instead find a way to leave fingerprints, hair, and blood behind, just to be certain we know it is them.

You can find lots of blog entries on the internet regarding performance problems with ORMs. One of my favorites is <a href="http://blog.waynesheffield.com/wayne/archive/2012/06/orm-tools/" target="_blank" rel="noopener">this one</a>, which provides a summary of all the ways something can go wrong with an ORM deployment.
<h2>Default configurations</h2>
Because it's easy to click 'Next, Next, OK' and install SQL Server without any understanding about the default configuration options. This is also true for folks that have virtualized instances of SQL Server. There's a good chance the server admins also choose default options that may not be best for SQL Server. Things like <a href="https://support.microsoft.com/en-us/kb/2806535" target="_blank" rel="noopener">MAXDOP</a>, <a href="http://logicalread.solarwinds.com/sql-server-tempdb-best-practices-initial-sizing-w01/#.VqaXZVMrJBw" target="_blank" rel="noopener">tempdb configuration</a>, <a href="https://msdn.microsoft.com/en-us/library/ms190925.aspx" target="_blank" rel="noopener">transaction log placement and sizing</a>, and <a href="https://support.microsoft.com/en-us/kb/315512" target="_blank" rel="noopener">default filegrowth</a> are all examples of options that you can configure before turning over the server to your end users.

Seeing similar issues time and again made me want to build an entire talk dedicated to helping people understand how to configure SQL Server for performance. You can <a href="http://launch.solarwinds.com/Configuring_SQL_Server_MCM_07092015_SQLS_Web_REG.html?CMP=SOC-DB-TW-SQLMCM07092015-DPASS-WEB-X" target="_blank" rel="noopener">watch the webinar I did with Tim Chapman here</a>.

The above list of five items is not scientific by any means, these are the problem that I find to be the most common. Think of them as buckets. When you are presented with troubleshooting performance, or even reviewing a design, these buckets help you to rule out the common issues and allow you to then sharpen your focus.