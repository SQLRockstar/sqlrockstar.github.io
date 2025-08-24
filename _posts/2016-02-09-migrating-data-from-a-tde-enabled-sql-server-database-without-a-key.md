---
layout: post
title: Migrating Data From a TDE Enabled SQL Server Database Without a Key
date: '2016-02-09 13:20:34 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- BACPAC
- BCP
- microsoft
- sql server
- TDE
- Transparent Data Encryption
---

At some point in our lives we have lost or misplaced our car keys. It seems to be a right of passage for most and a daily ritual for others. But at the end of the day we know that, if needed, we can get a new key made.

The same is not true for database keys and <a href="https://msdn.microsoft.com/en-us/library/bb934049.aspx" target="_blank">Transparent Data Encryption (TDE)</a>. TDE was designed to protect “data at rest”, which is a fancy way of saying that if you enable TDE on a database you cannot restore that database to a different server without the corresponding security certificate.

This sounds like a good thing, because you don’t want your backups <a href="http://www.huffingtonpost.com/2012/03/30/lost-data-cartridges_n_1390258.html" target="_blank">falling off the back of a truck and into the wrong hands</a>. And the backups can be restored to the same server, so they are not completely worthless. But the fact remains that if you lose your keys, your recovery options are limited.
<h2>How to enable TDE</h2>
Enabling TDE is easy enough, you can follow the <a href="https://msdn.microsoft.com/en-us/library/bb934049.aspx">instructions found here</a>, or you can use this quick t-sql snippet to create a database, populate some data, and enable TDE:
<pre lang="tsql">USE master
GO
--create database
CREATE DATABASE [TDE]
GO
--create table
USE [TDE]
GO
CREATE TABLE [dbo].[tbl_foo](
	[col1] [int] NOT NULL
) ON [PRIMARY]
GO
--insert some data
INSERT INTO [dbo].[tbl_foo] ([col1]) VALUES (1)
INSERT INTO [dbo].[tbl_foo] ([col1]) VALUES (2)
INSERT INTO [dbo].[tbl_foo] ([col1]) VALUES (3)
INSERT INTO [dbo].[tbl_foo] ([col1]) VALUES (4)
INSERT INTO [dbo].[tbl_foo] ([col1]) VALUES (5)
GO
--swicth to master, create master key
USE master
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'UseStrongPasswordHere1';
GO
--create certificate
CREATE CERTIFICATE MyServerCert WITH SUBJECT = 'MyCertificate';
GO
--switch back to database
USE TDE
GO
--create database key
CREATE DATABASE ENCRYPTION KEY
WITH ALGORITHM = AES_128
ENCRYPTION BY SERVER CERTIFICATE MyServerCert
GO
--enable encryption
ALTER DATABASE TDE
SET ENCRYPTION ON
GO
</pre>
Once TDE is enabled, you will find that if you try to restore that database to a new server it will fail with an error message similar to this:
<pre lang="tsql">Msg 33111, Level 16, State 3, Line 2
Cannot find server certificate with thumbprint '0x83EA01EDED800BDA21580D62283B8E277F57BE40'.
Msg 3013, Level 16, State 1, Line 2
RESTORE DATABASE is terminating abnormally.
</pre>
If you don’t have the certificate then you are out of luck. You won’t be able to do the restore to a different server. And auditors everywhere sleep well at night because they have ‘enable TDE’ as a checkbox somewhere and they know that this is reducing the risk your data may be exposed.

I said reduce, not eliminate.
<h2>Migrating data from a TDE enabled SQL Server database</h2>
TDE protects data at rest, but not data in flight. And it doesn’t protect you from having a user BCP out all the data to flat files to be used elsewhere. This is an easy thing to script, here’s what we used to do when migrating from <span style="text-decoration: line-through;">Sybase</span> SAP before migration tools existed:
<pre lang="tsql">SELECT 'bcp ' + DB_NAME() + '..' + name 
+ ' out "F:\Data\bcp\' + name 
+ '.dat" -c -t"^" -r"|" -e"F:\Data\bcp\' + name 
+ '.err" -T -SSQL2014 > "F:\Data\bcp\' + name 
+ '.out"'
FROM sys.objects
WHERE type = 'U'
</pre>
That, along with read permissions, was good enough to get a quick BCP of all tables. We would then use the output files to BCP the data back into a different database. Today I suppose we would use <a href="http://sqlmag.com/powershell/bulk-copy-data-sql-server-powershell">Powershell</a>, but either method will work when migrating data from a TDE enabled database.

The trick with such methods are the extra steps for dropping foreign keys, constraints, and indexes before trying to load the data, then rebuilding everything after the fact. Like I said, migration tools didn’t exist back then, we just rolled everything together with a little bit of code and moved on.

These days there’s something better than scripting. We have the concept of a BACPAC, which contains the database schema and data. Exporting your database to a BACPAC is easy, and it requires at least GRANT VIEW DEFINITION and db_datareader permissions. You can then use SQL Server Management Studio (SSMS) to create the BACPAC file:

<a href="https://thomaslarock.com/wp-content/uploads/2016/02/bacpac-locations.png" rel="attachment wp-att-17292"><img class="aligncenter size-large wp-image-17292" src="https://thomaslarock.com/wp-content/uploads/2016/02/bacpac-locations-600x556.png" alt="I can store BACPAC files locally or in Azure storage." width="600" height="556" /></a>

Note that the default location for theBACPAC file is at “C:\Users\Administrator\Documents\SQL Server Management Studio\DAC Packages”. We also have the option here to save directly to Azure storage.

After the export is complete we can crack open the BACPAC file to examine the contents. Just rename the BACPAC file to a .zip file and we are in business. Check out what we can find in the model.xml file:

<a href="https://thomaslarock.com/wp-content/uploads/2016/02/model_info.png" rel="attachment wp-att-17293"><img class="aligncenter size-large wp-image-17293" src="https://thomaslarock.com/wp-content/uploads/2016/02/model_info-600x492.png" alt="The model.xml file shows our database was encrypted." width="600" height="492" /></a>

That’s right, this BACPAC file shows that the database we pulled from was encrypted. Next, let’s navigate the to the data directory, find our table, and open with a tool like Visual Studio to see the (unencrypted!) data:

<a href="https://thomaslarock.com/wp-content/uploads/2016/02/VS.png" rel="attachment wp-att-17294"><img class="aligncenter size-full wp-image-17294" src="https://thomaslarock.com/wp-content/uploads/2016/02/VS.png" alt="Unencrypted data from BACPAC file. " width="596" height="179" /></a>

But our database has TDE enabled, shouldn’t our data at rest be protected? Nope. Remember, this is a BCP of your data. TDE doesn’t help with BCP, it only protects the database backup file. A BACPAC is not a database backup.

This BACPAC can now be imported as a new database on a new server, no certificate needed. See how easy it is using SSMS:

<a href="https://thomaslarock.com/wp-content/uploads/2016/02/import.png" rel="attachment wp-att-17295"><img class="aligncenter size-large wp-image-17295" src="https://thomaslarock.com/wp-content/uploads/2016/02/import-600x556.png" alt="import" width="600" height="556" /></a>

And there you have it, a restore of a TDE enabled SQL Server Database without a key. Well, OK, it’s really just a BCP out and in of the data. But here’s the main point:

<strong>Your BACPAC of the TDE enabled database contains data, and that data is not encrypted.</strong>

No, this isn’t a bug. This is how the technology works. If you want to make certain that a BACPAC cannot be read then you should consider the use of <a href="http://windows.microsoft.com/en-us/windows-vista/bitlocker-drive-encryption-overview" target="_blank">file or volume encryption</a>.

I would also advise you to find a way to search your environment for BACPAC files. You could use a PowerShell script like this one:
<pre lang="powershell"># PowerShell script to list the bacpac files
$Dir = Get-ChildItem C:\Users -recurse
$List = $Dir | where {$_.extension -eq ".bacpac"}
$List | Format-Table fullname
</pre>
However that script is only looking at a specific folder. Running it against the entire server would take a bit of time to complete, and I can’t imagine trying to run this against all workstations, so it might be worth thinking about a group policy or something similar. Of course that won’t prevent BACPAC files from being saved with a different extension.

At the end of the day, <em>any user that can read your data is a potential security risk</em>. Even if you were to find a way to prohibit them from saving data to files you will not be able to prevent them from remembering the data they are working with.

This isn’t to say that data security is futile, but it’s worth understanding the risks associated.
<h2>Summary</h2>
Enabling TDE does not protect your BACPAC files, just your database backups. If you are relying on TDE to protect your data at rest then allowing users to create BACPAC files will put you at risk. But no more risk than any other user choosing to run a SELECT statement and save the data somewhere (or perhaps <a href="https://powerbi.microsoft.com/en-us/" target="_blank">just use PowerBI to open a connection and import to Excel</a>).

If you are concerned about BACPAC files laying about your environment I would recommend that you consider encrypting files locally.

Lastly, this is not a bug! I cannot stress that enough. Please don’t yell at Microsoft for how BCP works. Although, feel free to <a href="https://connect.microsoft.com/SQLServer/feedback/details/2340724" target="_blank">cast a vote for this Connect item</a>.