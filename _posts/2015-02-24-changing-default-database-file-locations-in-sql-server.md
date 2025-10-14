---
layout: post
title: Changing Default Database File Locations in SQL Server 2014
date: '2015-02-24 08:58:32 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- Data
- default
- log
- server
- SQL
---

When you create a database in SQL Server and do not specify a file location for your data and log files SQL Server will rely on the default database file locations as defined in the server properties. You can see these properties for yourself by right-clicking on the instance name inside of SQL Server Management Studio (SSMS) and navigating to the ‘Database Settings’ tab:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/server_properties.jpg"><img class="aligncenter size-full wp-image-11979" src="https://thomaslarock.com/wp-content/uploads/2015/02/server_properties.jpg" alt="server_properties" width="481" height="422" /></a>

If we create a simple database we can verify that the files are written to these directories:
<pre lang="tsql">CREATE DATABASE TestFileLoc
GO

SELECT filename
FROM sys.sysaltfiles
WHERE name LIKE 'TestFileLoc%';
</pre>
The second query returns the locations of our data and log files, which we see are the defaults:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/results.png"><img class="aligncenter size-full wp-image-11981" src="https://thomaslarock.com/wp-content/uploads/2015/02/results.png" alt="results" width="500" height="90" /></a>

Changing the defaults is easy enough, we can just update the file locations inside of SSMS. I will create two new folders (C:\SQL\Data\ and C:\SQL\Logs\) to store the data and log files for new databases. It is important to note that updating these locations will NOT migrate the current data and log files to the new directories. These changes will only apply to new databases created from this point forward.

Let’s update the settings to point to the new directories:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/server_properties_updated.jpg"><img class="aligncenter size-full wp-image-11982" src="https://thomaslarock.com/wp-content/uploads/2015/02/server_properties_updated.jpg" alt="server_properties_updated" width="481" height="422" /></a>

Press OK, and we’ll run our create database script, modifying the database name, and the results now look like this:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/results_updated.png"><img class="aligncenter size-full wp-image-11983" src="https://thomaslarock.com/wp-content/uploads/2015/02/results_updated.png" alt="results_updated" width="537" height="117" /></a>

Whoa, what happened here?

First, like I said earlier, updating those defaults will not migrate existing files. You can see that in the first two rows of the result set. Second, setting the default locations requires a restart of the SQL instance for the changes to take effect. The reason why is because the default locations come from reading registry values.

In fact, after you make your change in the SSMS, hit the little button at the top that says ‘Script’ and check out what is being done behind the scenes:
<pre lang="tsql">EXEC xp_instance_regwrite N'HKEY_LOCAL_MACHINE'
	, N'Software\Microsoft\MSSQLServer\MSSQLServer'
	, N'DefaultData'
	, REG_SZ
	, N'C:\SQL\Data'
GO
EXEC xp_instance_regwrite N'HKEY_LOCAL_MACHINE'
	, N'Software\Microsoft\MSSQLServer\MSSQLServer'
	, N'DefaultLog'
	, REG_SZ
	, N'C:\SQL\Logs'
GO
</pre>
If we restart the instance and then run our create database script again. This time you should see the expected results:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/really_updated.png"><img class="aligncenter size-full wp-image-11984" src="https://thomaslarock.com/wp-content/uploads/2015/02/really_updated.png" alt="really_updated" width="537" height="151" /></a>

&nbsp;

I’d suggest that you configure these directories when you are installing SQL Server. You will find the option for this on the ‘Database Engine Configuration’ screen as follows:

<a href="https://thomaslarock.com/wp-content/uploads/2015/02/install.jpg"><img class="aligncenter size-full wp-image-11985" src="https://thomaslarock.com/wp-content/uploads/2015/02/install.jpg" alt="install" width="553" height="415" /></a>

By doing this during the installation you can avoid the need to restart the service at a later date to make this simple change.

Or you could specify the data and log file locations when creating your database, a good habit that everyone should have! The syntax for that would be similar to this:
<pre lang="tsql">CREATE DATABASE [PorkChopExpress]
 ON  PRIMARY 
( NAME = N'PorkChopExpress', FILENAME = N'C:\SQL\Data\PorkChopExpress.mdf' , SIZE = 1048576KB , FILEGROWTH = 262144KB )
 LOG ON 
( NAME = N'PorkChopExpress_log', FILENAME = N'C:\SQL\Logs\PorkChopExpress_log.ldf' , SIZE = 262144KB , FILEGROWTH = 131072KB )
GO
</pre>
I still prefer to set the default values, in order to help those that might not have good habits formed yet.

In the above examples you will note that I've placed everything on the C:\ drive. This is <span style="text-decoration: underline;">not</span> a recommended best practice. <strong>Please don't put your database files (and backups) onto the C:\ drive.</strong> You should have dedicated drives for data files, transaction logs, and backups. There are two main reasons why you want to have distinct drives. First is performance. But performance is becoming less of a concern as we transition away from spinning pieces of rust and into the world of flash arrays and virtual SANs.

The second reason, and to me the most important, is recovery. If you put your data, log, and backups onto the same drive and that drive fails, then your recovery options become much more limited. As a DBA I know my number one job is recovery, so I am less likely to take risks when it comes to recovery.

As Steve Jones (<a href="http://www.sqlservercentral.com/blogs/steve_jones/" target="_blank">blog</a> | <a href="http://twitter.com/way0utwest" target="_blank">@way0utwest</a>) would remind us all: "Good resume. Good backup. You only need one."