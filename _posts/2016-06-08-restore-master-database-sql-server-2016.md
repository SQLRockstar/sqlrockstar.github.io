---
layout: post
title: 'HOW TO: Restore the Master Database in SQL Server 2016'
date: '2016-06-08 10:42:32 +0000'
categories:
- MSSQL
- SQL MCM
- SQL MVP
- SQL Server Performance
tags:
- database
- master
- restore
- SQL Server 2016
---

I like having a routine. Most people do, I suppose. There's some comfort in knowing what lies ahead, what comes next. This is also true for when you need to restore the master database in SQL Server 2016.

The same holds true for restoring the master database in SQL Server 2016, because it's the same routine as <a title="HOW TO: Restore the Master Database in SQL Server 2014" href="https://thomaslarock.com/2014/05/restore-master-database-sql-server-2014/" target="_blank">what I posted for SQL Server 2014</a>, which is the same routine as <a title="HOW TO: Restore the Master Database in SQL Server 2012" href="https://thomaslarock.com/2014/01/restore-the-master-database-in-sql-server-2012/" target="_blank">what I posted for SQL Server 2012</a>. If you only click on one link, click on the 2012 link because that has the details on how to properly test that the restore worked.

For those of you too lazy to click on the links, I will summarize the steps for you here:

1. Using SQL Configuration manager, stop the SQL Server instance
2. Open a command window or Powershell session
3. In that command window, start the instance executable in maintenance mode using a secret command known only to people that have read my posts
4. Open a second command window or Powershell session and connect to the server instance using SQLCMD
5. Restore master from within that SQLCMD window
6. Using SQL configuration manager, restart instance

One thing to note here is that the instructions I provided assume you will be opening your command line sessions with 'Run as Administrator'. If you don't do that, bad things may happen. What bad things? This bad thing:

<a href="https://thomaslarock.com/wp-content/uploads/2016/06/error.jpg"><img class="aligncenter wp-image-17399 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/06/error-560x238.jpg" alt="restore master database" width="560" height="238" /></a>

"Your SQL Server installation is either corrupt or has been tapered with (Error getting instance ID from name.).  Please uninstall then re-run setup to correct this problem"

Or this bad thing:

<a href="https://thomaslarock.com/wp-content/uploads/2016/06/error_hadr.jpg"><img class="aligncenter wp-image-17400 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/06/error_hadr-513x315.jpg" alt="restore master database" width="513" height="315" /></a>

"RegOpenKeyEx of "Software\Microsoft SQL Server\MSSQL13.SQL2016\MSSQLServer\HADR" failed."

My first thought when seeing this was trying to figure out what had gone wrong with the installation. I spent about seven (7) seconds thinking about the possible installation issues and then started thinking about user permissions for the command window. Once I switched to running the command window or Powershell session as an administrator, all was good.

That’s all there is to it, again. While SQL Server 2016 has been <a href="https://thomaslarock.com/2016/06/sql-server-2016-just-runs-faster/" target="_blank">making a lot of headlines with all of the shiny new things inside</a>, the steps to restore the master database has not changed.

You're welcome.