---
layout: post
title: SQL Server Trace Flags
date: '2016-06-22 12:39:20 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- SQL
- sql server
- SQL Server 2016
- trace flags
- upgrade
---

With the release of SQL Server 2016 there will be a wave of upgrades happening over the next twelve months. I've written before about upgrading SQL Server and today I wanted to talk about something special to consider when upgrading.

Trace flags.

Trace flags change the default behavior for queries inside of SQL Server at the server, session, or query level. I’m not a fan of setting trace flags for the entire instance unless there is a good reason to do so. I prefer more granular settings, such as the session or query level. And I only want to use trace flags when I know exactly what it will do. (With SQL 2016 I can also <a href="https://msdn.microsoft.com/en-us/library/mt629158.aspx" target="_blank">configure a database scoped option</a> to mimic the behavior of trace flags such as for cardinality estimates, but that is a post for a different day).

You can find a partial list of <a href="https://msdn.microsoft.com/en-us/library/ms188396.aspx" target="_blank">documented trace flags available at MSDN</a>. I say partial because you can find definitions <a href="https://social.technet.microsoft.com/wiki/contents/articles/13105.trace-flags-in-sql-server.aspx" target="_blank">on TechNet</a> or <a href="http://www.sqlservice.se/updated-microsoft-sql-server-trace-flag-list/" target="_blank">outside of MSDN</a>. Check with Microsoft Support about whether a trace flag is supported before using it.
<h2>How To Set a Trace Flag in SQL Server</h2>
Setting a trace flag is easy enough. One option is to enable the trace flag when the instance is started. This is done by adding a startup parameter inside SQL Server Configuration Manager (SSCM):

<a href="https://thomaslarock.com/wp-content/uploads/2016/06/sscm_startup_parameters.png"><img class="aligncenter size-medium wp-image-17417" src="https://thomaslarock.com/wp-content/uploads/2016/06/sscm_startup_parameters-265x315.png" alt="sql server trace flags" width="265" height="315" /></a>

You can then verify the setting after the restart by looking in the error log:

<a href="https://thomaslarock.com/wp-content/uploads/2016/06/startup_parameters.jpg"><img class="aligncenter size-medium wp-image-17415" src="https://thomaslarock.com/wp-content/uploads/2016/06/startup_parameters-465x315.jpg" alt="sql server trace flags" width="465" height="315" /></a>

Or, you can enable the trace flag for your connection using the <a href="https://msdn.microsoft.com/en-us/library/ms187329.aspx" target="_blank">DBCC TRACEON statement</a>:
<pre lang="tsql">DBCC TRACEON (1222)
GO</pre>
Or, if you want to set the trace flag globally for all connections, you can use this syntax:
<pre lang="tsql">DBCC TRACEON (1222, -1)
GO</pre>
Another option is to use the QUERYTRACEON hint. This is the technique I use for my <a href="https://sqlbits.com/Sessions/Event15/Cardinality_Estimates_in_Microsoft_SQL_Server" target="_blank">cardinality talks</a>, where I toggle the behavior of the cardinality estimator using query trace flags. For example, if I am running a SQL Server 2016 instance and want to revert to the legacy cardinality estimator I would use the following syntax at the end of the query:
<pre lang="tsql">OPTION (QUERYTRACEON 9481)</pre>
Take note that this query hint option is <a href="https://support.microsoft.com/en-us/kb/2801413" target="_blank">only supported for a handful of trace flags</a>.
<h2>SQL Server Upgrades and Trace Flags</h2>
When it comes to SQL Server upgrades I find the use of trace flags to be overlooked. Trace flags get set and remain in place for long periods of time, and in that time people forget that the trace flags are running. As a result, they take a database backup from an older server, restore it to the newer instance, and then scratch their head when something has changed.

In my experience dozens of configuration options get made to database servers over time. Despite all best efforts at documenting each and every option used it seems inevitable that something gets missed.

This is why I put together <a href="https://thomaslarock.com/2013/03/upgrading-to-sql-2012-ten-things-you-dont-want-to-miss/" target="_blank">checklists</a> for <a href="https://thomaslarock.com/2014/06/upgrading-to-sql-server-2014-a-dozen-things-to-check/" target="_blank">upgrading SQL Server</a>. With so many moving parts it is difficult to remember everything you need to check. If you want a wonderful free tool to capture details of your SQL instances (including trace flags and OS details) you should <a href="https://sqlpowerdoc.codeplex.com/" target="_blank">check out SQL Power Doc over on Codeplex</a>.
<h2>How To Find What SQL Server Trace Flags Are Running</h2>
In addition to what is listed above (examine the properties in SSCM or read the SQL Server errorlog) other ways exist for you to find what trace flags are running.

The easiest way to find SQL Server trace flags is to run the <a href="https://msdn.microsoft.com/en-us/library/ms187809.aspx" target="_blank">DBCC TRACESTATUS command</a>:
<pre lang="tsql">DBCC TRACESTATUS WITH NO_INFOMSGS 
GO</pre>
This returns a result set that shows you the trace flag, the status, and if the flag is global or for the current session only.

Another way to get these details would be to query the registry, but that always seems messy to me. You could <a href="https://naturalselectiondba.wordpress.com/2016/04/21/sql-server-use-powershell-to-find-what-trace-flags-are-running/" target="_blank">use Powershell and the EnumActiveGlobalTraceFlags() function</a> to also capture the currently running trace flags. Bear in mind that you only get back information on trace flags configured to run globally.

Nobody likes surprises when it comes to upgrading or migrating SQL Server instances. Trace flags get set and forgotten. I'm hoping that this post will help people to remember.