---
layout: post
title: Changing Default Database File Locations in SQL Server 2016
date: '2017-06-21 14:12:45 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- backups
- database
- default
- files
- registry
---

At some point in your career as a data professional you will need to change the default database file locations in SQL Server 2016. The default locations are set upon installation of SQL Server. During the installation process you will see the Database Engine Configuration screen:

<a href="https://thomaslarock.com/wp-content/uploads/2017/06/SQL-install-database-file-defaults.png"><img class="aligncenter wp-image-17914 size-large" src="https://thomaslarock.com/wp-content/uploads/2017/06/SQL-install-database-file-defaults-600x452.png" alt="Default Database Files Locations SQL Server 2016" width="600" height="452" /></a>

This is the best time and place to set the defaults to be something other than the default SQL Server installation folder. Historically, you would create distinct drives for data files, transaction log files, and backups. This was done in an effort to maximize performance for your SQL Server. These days, with flash drives and OBR10 (OBR10 = One Big RAID 10), the performance gains are negligible for a majority of workloads. I will continue to advocate distinct drives, however, for one important reason:

<strong>Recovery.</strong>

Placing data, logs, and backups on distinct drives allows for you to maximize your ability to recover data if needed. As we all know, <strong>if you can't recover, you can't keep your job as a data professional</strong>. By creating distinct drives during the installation of SQL Server you reduce your risk of not being able to recover. (For you storage admins out there, you should understand this risk. If you choose to put data, log, and backups on a single LUN, or a single datastore, you are at risk for data loss. End of line.)

If you are using an unattended installation script to install SQL Server, the syntax for this would be similar to the following:
<pre lang="tsql">; Default directory for the Database Engine user databases. 
SQLUSERDBDIR="E:\SQL\Data"
; Default directory for the Database Engine user database logs. 
SQLUSERDBLOGDIR="F:\SQL\Logs"
; Default directory for the Database Engine backup files. 
SQLBACKUPDIR="G:\SQL\Backups" 
</pre>
Of course you don't always have the opportunity to control the installation of SQL Server. As a result, when you create a database in SQL Server and do not specify a file location for your data and log files SQL Server will rely on the default database file locations as defined in the server properties. You can see these properties for yourself by right-clicking on the instance name inside of SQL Server Management Studio (SSMS) and navigating to the ‘Database Settings’ tab:

For example, using an Azure image means that SQL Server is already installed. Chances are when you look at the data file properties inside of SSMS you see something like this:

<a href="https://thomaslarock.com/wp-content/uploads/2017/06/database-defaults.png"><img class="aligncenter size-large wp-image-17915" src="https://thomaslarock.com/wp-content/uploads/2017/06/database-defaults-600x524.png" alt="database defaults" width="600" height="524" /></a>

This leaves you with the following options for changing the default database files locations for SQL Server 2016.

<strong>For databases already created</strong>, you will need to take the database offline, move the files, update the database to know where the new files are located, and then bring the database online. <a href="https://docs.microsoft.com/en-us/sql/relational-databases/databases/move-user-databases" target="_blank" rel="noopener">Here is a link that describes the process in a bit more detail</a>. Note that this will have no affect on where the backups are located. More on that later.

<strong>For databases you want to create</strong>, you can specify the data and log file locations when creating a database. The syntax would be similar to this:
<pre lang="tsql">CREATE DATABASE [PorkChopExpress]
 ON  PRIMARY 
( NAME = N'PorkChopExpress', FILENAME = N'E:\SQL\Data\PorkChopExpress.mdf'
, SIZE = 1048576KB , FILEGROWTH = 262144KB )
 LOG ON 
( NAME = N'PorkChopExpress_log', FILENAME = N'F:\SQL\Logs\PorkChopExpress_log.ldf'
, SIZE = 262144KB , FILEGROWTH = 131072KB )
GO
</pre>
Note that this option will not affect where the backups are located. More on that later.

The <strong>third option is to edit the registry settings for the instance</strong>. This is the second best option overall, with the first being to set the defaults upon installing SQL Server 2016. Editing the registry is also the option I advocate to clients and customers using Azure images. It's included in my checklist scripts run after provisioning an instance inside an Azure VM and before the creation of user databases.

I like this option because it helps the users that can't help themselves. They have no idea about this stuff, so it is up to us as data professionals to create an environment that helps them to minimize their risk.

Remember I promised more about database backups later? Well, now is later. <strong>By editing the registry we can change the default locations for database files, transaction log files, and database backups</strong>. That's what I consider #SQLWinning.

Changing the registry settings is easy enough, we can update the file locations inside of SSMS. It is important to note that updating the default file locations inside of SSMS will NOT migrate the current data and log files to the new directories. These changes will only apply to new databases created and backed up from this point forward. Also warrants mentioning that making changes to the registry settings will <strong>require a restart of the SQL Server service</strong> in order for the changes to be applied to new databases going forward.

In fact, after you make your change in the SSMS, hit the little button at the top that says ‘Script’ and check out what is being done behind the scenes:
<pre lang="tsql">EXEC xp_instance_regwrite N'HKEY_LOCAL_MACHINE'
	, N'Software\Microsoft\MSSQLServer\MSSQLServer'
	, N'DefaultData'
	, REG_SZ
	, N'E:\SQL\Data'
GO
EXEC xp_instance_regwrite N'HKEY_LOCAL_MACHINE'
	, N'Software\Microsoft\MSSQLServer\MSSQLServer'
	, N'DefaultLog'
	, REG_SZ
	, N'F:\SQL\Logs'
GO
</pre>
<h2>Summary</h2>
Changing the default database file locations in SQL Server 2016 is easy enough to get done. You have a handful of options for this task. My preference is to have the defaults set upon installation. If that is not an option, then editing the registry is the next best choice, followed by manually creating databases and backups. At the end of the day you want to create a safe environment for your end users that helps them to minimize the risk of data loss.