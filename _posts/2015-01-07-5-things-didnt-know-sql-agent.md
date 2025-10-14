---
layout: post
title: 5 Things You Didn’t Know About SQL Agent
date: '2015-01-07 21:26:57 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- sql agent
- sql server
---

<a href="http://www.microsoft.com/en-us/server-cloud/products/sql-server/default.aspx" target="_blank">Microsoft SQL Server</a> comes with a boatload of additional components. One component is the <a href="http://msdn.microsoft.com/en-us/library/ms189237(v=sql.110).aspx" target="_blank">SQL Agent</a> service. The purpose of the SQL Agent is to serve as a job scheduler. Many experienced DBAs use jobs running inside the SQL Agent to perform routine tasks such as backups, updating statistics, and rebuilding indexes as needed.

While the presence of SQL Agent may be known to many, I always find people to be surprised by the existence of one or more items on this list.

So here you go, five things that you didn't know about the SQL Agent.
<h3>1. SQL Agent Specific Performance Objects</h3>
<a href="http://technet.microsoft.com/en-us/library/cc749249.aspx" target="_blank">Performance Monitor</a> (aka, PerfMon) has a <a href="http://blogs.msdn.com/b/jimmymay/archive/2008/10/15/perfmon-objects-counters-thresholds-utilities-for-sql-server.aspx" target="_blank">wealth of metrics that are likely familiar to any DBA</a>. Items such as <a href="http://www.sqlskills.com/blogs/paul/page-life-expectancy-isnt-what-you-think/" target="_blank">Page Life Expectancy</a>, <a href="https://www.sqlskills.com/blogs/jonathan/new-article-online-great-sql-server-debates-buffer-cache-hit-ratio/" target="_blank">Buffer Cache Hit Ratio</a>, and <a href="http://msdn.microsoft.com/en-us/library/ms178072.aspx" target="_blank">CPU Utilization</a> are some of the common counters collected by any experienced administrator.

What is not as well known about the counters installed right alongside the usual suspects are the counters specific for SQL Agent.

Yep, these exist:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_performance_counters.png"><img class="aligncenter size-medium wp-image-11926" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_performance_counters-422x315.png" alt="sql_agent_performance_counters" width="422" height="315" /></a>

You can get all the details on these objects over at <a href="http://technet.microsoft.com/en-us/library/ms190382.aspx">http://technet.microsoft.com/en-us/library/ms190382.aspx</a>.

Oddly enough, there is no DMV similar to <a href="http://msdn.microsoft.com/en-us/library/ms187743(v=sql.110).aspx" target="_blank">sys.dm_os_performance_counters</a> available to query for these details on the SQL Agent. You would need to write a query against the msdb database in order to collect the information that is readily available from these counters. Depending upon your needs, these counters may be preferred over querying the msdb database directly.
<h3>2. SQL Agent Log file</h3>
Most everyone knows that there is an error log for SQL Server. Not everyone is aware that a log also exists for SQL Agent. You can find it inside of SQL Server Management Studio:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_error_log.png"><img class="aligncenter size-full wp-image-11928" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_error_log.png" alt="sql_agent_error_log" width="408" height="299" /></a>

Double clicking on one of the logs displayed inside of SSMS will open up the <a href="http://msdn.microsoft.com/en-us/library/dd206996.aspx" target="_blank">Log File Viewer</a>, and from there you can see all of the logs available for you to browse:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_error_log1.png"><img class="aligncenter size-medium wp-image-11929" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_error_log1-391x315.png" alt="sql_agent_error_log1" width="391" height="315" /></a>

What I like about this viewer is that it automatically sorts all events by date, regardless of log, as you enable viewing by clicking specific logs in the corresponding checkboxes. This can be valuable when trying to troubleshoot oddball issues that affect things both internal and external to SQL Server.
<h3>3. SQL Agent Alerts</h3>
Not many people are using this feature of SQL Agent, mostly due to the rise of <a href="http://www.solarwinds.com/database-performance-analyzer-sql-server.aspx" target="_blank">3<sup>rd</sup> party products</a> over the past 15 years that allow for centralized alerting of your SQL Server. But the native alerting feature inside of SQL Server is fairly robust in what it can offer.

Need to be alerted if there is database corruption? What about if there is a T-SQL syntax error? How about for a hardware error? All of those things are possible out of the box with SQL Server:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_alert.png"><img class="aligncenter size-medium wp-image-11930" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_alert-352x315.png" alt="sql_agent_alert" width="352" height="315" /></a>

As a DBA I know that my first priority must be my ability to recover data. Therefore, I believe in protecting myself from failure in a variety of ways. No matter what is the preferred alerting tool for the enterprise I always like to configure some alerts within SQL Agent as a failsafe for items such as database corruption. Better to be alerted more than once for a significant failure than never at all.
<h3>4. SQL Agent Multiserver Administration</h3>
Another feature that has been unknown to many DBAs for years is the concept of multi-server administration. That's right, you can configure one of your SQL Server instances to act as a centralized system to control others.

It’s easy to launch the wizard with a simple right-click:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_multiserver.png"><img class="aligncenter size-medium wp-image-11931" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_multiserver-560x282.png" alt="sql_agent_multiserver" width="560" height="282" /></a>

You can configure one server to be ‘Master’, and additional servers to be the ‘Target’. I always advise using a non-production (or dedicated) server to serve as Master, so as to not interfere with any production workloads.

The advantage here is that you can create one job on the Master server and have it executed on all of the Target servers. This can make your administration efforts much less complex.
<h3>5. SQL Agent Auto Restart</h3>
You can configure SQL Agent to auto restart both itself and SQL Server in case either service quits unexpectedly. Just right-click on the SQL Agent service inside of SSMS:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_auto_restart.png"><img class="aligncenter size-medium wp-image-11932" src="https://thomaslarock.com/wp-content/uploads/2015/01/sql_agent_auto_restart-351x315.png" alt="sql_agent_auto_restart" width="351" height="315" /></a>

And now should SQL Agent service stop unexpectedly it will attempt to restart itself. Not a bad thing to have handy, especially if you are relying on jobs to be executed!

There you go, five things you may not have known about SQL Agent inside of SQL Server.