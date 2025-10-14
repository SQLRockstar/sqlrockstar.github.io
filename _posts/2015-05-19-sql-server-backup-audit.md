---
layout: post
title: SQL Server Backup Audit
date: '2015-05-19 11:54:26 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
---

I had a question come up last week from someone that wanted to know a few basic facts about their SQL Server backups for audit purposes. The facts they wanted were straightforward:
<ol>
	<li>Who took the backup?</li>
	<li>When was it taken?</li>
	<li>Where was it written?</li>
</ol>
Simple questions that are answered with a simple script. As usual, here's the standard disclaimer for those that need this sort of thing:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

You can also download a copy of the script <a href="http://1drv.ms/1c2Pn9w" target="_blank">here</a>. You're welcome, as always.
<pre lang="tsql">/*=============================================
  File: SQL_Server_backup_audit.sql

  Author: Thomas LaRock, https://thomaslarock.com/contact-me/
  https://thomaslarock.com/2015/05/sql-server-backup-audit

  Summary: This code will return details regarding the login used to take 
      a database backup, which database, when the backup completed, and 
	  where the backup was written.

  Date: May 19th, 2015

  SQL Server Versions: SQL2000, SQL2005, SQL2008, SQL2008 R2, SQL2012, SQL2014

  You may alter this code for your own purposes. You may republish
  altered code as long as you give due credit. 

  THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
  OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT
  LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR
  FITNESS FOR A PARTICULAR PURPOSE.

=============================================*/

SELECT bs.[user_name],
[bs].[backup_start_date], 
[bs].[backup_finish_date], 
[bs].[database_name] as [source_database_name], 
[bmf].[physical_device_name] 
FROM msdb..backupset bs
INNER JOIN msdb..backupmediafamily bmf 
ON [bs].[media_set_id] = [bmf].[media_set_id] 
ORDER BY [bs].[backup_finish_date] DESC
</pre>
Here's what the query and a sample output would look like:<a href="https://thomaslarock.com/wp-content/uploads/2015/05/sql_server_backup_audit.png"><img class="aligncenter size-medium wp-image-12104" src="https://thomaslarock.com/wp-content/uploads/2015/05/sql_server_backup_audit-560x211.png" alt="sql_server_backup_audit" width="560" height="211" /></a>

A few things to note here. First, the login being used is likely to be the service account used to run SQL Server agent (or whatever you are using to run automated backups). For an audit purpose you are likely going to want to look for logins other than that service account.

However, someone could simply update your backup process to output the backup to a different location. That's what really spurred this question, the person wanted to know if a backup was being done and written to Azure storage. Fortunately those details are captured inside of the msdb database. You can see in the picture here that I've written a couple of backups to an Azure storage container.

Lastly, we've recorded the time of the backup activity, as well as the name of the source database.

You can take this script and use it to alert upon anything out of the ordinary, such as backups happening at odd times, by rogue logins, or going to non-default locations.

Enjoy!