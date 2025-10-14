---
layout: post
title: 'HOW TO: Find When SQL Server Wait Stats Were Last Cleared'
date: '2015-03-23 09:20:57 +0000'
categories:
- MSSQL
- SQL MCM
- SQL MVP
tags:
- Microsoft SQL Server
- server
- SQL
- wait stats
- waits
---

<a href="https://thomaslarock.com/wp-content/uploads/2015/03/question.jpg"><img class="alignright size-full wp-image-12007" src="https://thomaslarock.com/wp-content/uploads/2015/03/question.jpg" alt="question" width="288" height="294" /></a>For years I have found myself often needing these three pieces of information with regards to SQL Server:

When was the last time the server was restarted?

When was the last time the SQL instance was restarted?

When was the last time the SQL Server wait stats were cleared?

If the server itself is restarted, then the answer to all three questions is roughly the same point in time. I find a full-server reboot to be a rare occurrence these days. It is more common for an administrator to restart the SQL Server instance, not the entire server, to clear up a performance problem or perhaps change a configuration setting. There are a handful of ways for you to find out when the SQL Server service was last restarted. You could look inside the SQL Server error log, or you could find the create date for tempdb, or you could query the time the default trace started. Each is valid to give you an idea of the instance restart.

Restarting the instance will also reset the details in DMVs such as sys.dm_os_wait_stats. This is the DMV that contains what I consider to be the most important for any instance of SQL Server: the wait stats. It is also possible to reset the wait stats without restarting SQL Server. This means we could have <em><strong>three</strong></em> different points of interest in time. That means I will want a script to check for each date.
<h3>How To Find When SQL Server Was Restarted</h3>
Finding the time of the last SQL Server restart is very easy. Starting in SQL 2008R2 we could query the sys.dm_os_sys_info system DMV to return that piece of information:
<pre lang="tsql">SELECT sqlserver_start_time AS [SQLRestart]
FROM sys.dm_os_sys_info</pre>
OK, that's simple enough. And we can use that same system DMV in order to find the last time the server itself was restarted. We just need to do a little math on the ms_ticks column like this:
<pre lang="tsql">SELECT DATEADD(ms, -ms_ticks, GETDATE()) AS [ServerRestart]
FROM sys.dm_os_sys_info</pre>
So, getting those two pieces of information is very easy. What about if wait stats are reset?
<h3>How To Reset Wait Stats in SQL Server</h3>
You can reset the details of SQL Server wait stats using the following command:
<pre lang="tsql">DBCC SQLPERF ('sys.dm_os_wait_stats', CLEAR)
</pre>
This will reset the details found in the sys.dm_os_wait_stats system DMV. Unfortunately there is no easy way to tell when that DBCC SQLPERF command was executed. It isn't logged to the errorlog, and there is no DMV that tracks this information. So any solution will estimate, at best, when this command may have executed.

Enter Ivan Penkov. You don't know Ivan? He's the person that suggested <a href="http://blogs.msdn.com/b/sqlosteam/archive/2011/11/12/when-was-sys-dm-os-wait-stats-last-cleared.aspx" target="_blank">we could use the SQLTRACE_INCREMENTAL_FLUSH_SLEEP wait event to estimate when wait stats may have been last cleared</a>. Thanks for that Ivan, much appreciated.

The code for this is simple enough:
<pre lang="tsql">SELECT DATEADD(ms, -wait_time_ms, GETDATE()) AS [DMVRestart]
FROM sys.dm_os_wait_stats
WHERE wait_type = 'SQLTRACE_INCREMENTAL_FLUSH_SLEEP'</pre>
<h3>Putting It All Together</h3>
We have three queries against two system DMVs in order to return these three points of interest in time. I can take those queries and put them into a quick script. As always, here is the usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

You can also download a copy of the script <a href="http://1drv.ms/1Exo9za" target="_blank">here</a>.
<pre lang="tsql">/*=============================================
  File: SQL_Server_last_restart.sql

  Author: Thomas LaRock, https://thomaslarock.com/contact-me/  
  https://thomaslarock.com/2015/03/how-to-find-when-wait-stats-were-last-cleared

  Summary: This script will return the following items:
		1. The last time the server was rebooted
		2. The last time the SQL instance was restarted
		3. The last time DBCC SQLPERF('sys.dm_os_wait_stats', CLEAR) was executed

  Variables:
    None

  Date: March 19th, 2015

  SQL Server Versions: SQL2008R2, SQL2012, SQL2014

  You may alter this code for your own purposes. You may republish
  altered code as long as you give due credit. 

  THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
  OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT
  LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR
  FITNESS FOR A PARTICULAR PURPOSE.

=============================================*/

/*=============================================
 Drop/create our temp table
=============================================*/
IF EXISTS (SELECT * FROM tempdb.dbo.sysobjects 
	WHERE id = OBJECT_ID(N'tempdb.dbo.#tmp_RestartTime')
	AND type IN (N'U'))
	DROP TABLE #tmp_RestartTime
GO

CREATE TABLE #tmp_RestartTime
	(Name VARCHAR(20),
	RestartDate DATETIME)
GO


/*=============================================
 Get the ServerRestart time, insert into #tmp_RestartTime 
=============================================*/
INSERT INTO #tmp_RestartTime
SELECT 'ServerRestart', DATEADD(ms, -ms_ticks, GETDATE())
FROM sys.dm_os_sys_info


/*=============================================
 Get the SQLRestart time, insert into #tmp_RestartTime 
=============================================*/
INSERT INTO #tmp_RestartTime
SELECT 'SQLRestart', sqlserver_start_time
FROM sys.dm_os_sys_info


/*=============================================
 Get the DMVRestart time, insert into #tmp_RestartTime 
=============================================*/
INSERT INTO #tmp_RestartTime
SELECT 'DMVRestart', DATEADD(ms, -wait_time_ms, GETDATE())
FROM sys.dm_os_wait_stats
WHERE wait_type = 'SQLTRACE_INCREMENTAL_FLUSH_SLEEP'


/*=============================================
 Return result from #tmp_RestartTime
=============================================*/
SELECT *
FROM #tmp_RestartTime

</pre>
I hope you find this script useful for those times that you need to know these three pieces of information.