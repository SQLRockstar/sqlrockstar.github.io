---
layout: post
title: Auditing Linked Servers
date: '2018-02-08 13:43:41 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
- SQL Server 2016
- SQL Server 2017
tags:
- data security
- Microsoft SQL Server
- sql audit
---

Last month I noticed this tweet from <a href="https://twitter.com/sqlprincess" target="_blank" rel="noopener">@SQLPrincess</a> on #sqlhelp, asking if there was a way to find out what happened to a linked server:

https://twitter.com/SQLPrincess/status/956939134236426245

The short answer is that SQL Server does not track this information by default. You need to be auditing linked servers for modifications before they happen.

I did my best to reply, suggesting the use of <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine" target="_blank" rel="noopener">SQL Audit</a>:

https://twitter.com/SQLRockstar/status/956957054710833153

I suggested setting up an audit against the <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-servers-transact-sql" target="_blank" rel="noopener">sys.servers table</a>. But that's the wrong approach. The correct approach is to examine the system stored procedures used to create, alter, or delete linked servers.

Here's a list of the system stored procedures that can affect the sys.servers table:

- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlinkedserver-transact-sql" target="_blank" rel="noopener">sp_addlinkedserver</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addserver-transact-sql" target="_blank" rel="noopener">sp_addserver</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropserver-transact-sql" target="_blank" rel="noopener">sp_dropserver</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlinkedsrvlogin-transact-sql" target="_blank" rel="noopener">sp_addlinkedsrvlogin</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-droplinkedsrvlogin-transact-sql" target="_blank" rel="noopener">sp_droplinkedsrvlogin</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-serveroption-transact-sql" target="_blank" rel="noopener">sp_serveroption</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-setnetname-transact-sql" target="_blank" rel="noopener">sp_setnetname</a>

Our goal here is to track who has added, removed, or modified a linked server in any way, and when the action happened. SQL Audit is perfect for tracking these events, but you will need to configure this audit manually.

Getting the audit up and running is simple enough. First, we will create the Server Audit object. This is the object that will tell SQL Server where and how to store the captured audit log events. Here's is a quick version to get you started, we will create a Server Audit named 'LinkedServer':
<pre lang="tsql">CREATE SERVER AUDIT [LinkedServer]
TO FILE 
(	FILEPATH = N'C:\TeamData\AuditLogs\LinkedServer\'
	,MAXSIZE = 0 MB
	,MAX_ROLLOVER_FILES = 2147483647
	,RESERVE_DISK_SPACE = OFF
)
WITH
(	QUEUE_DELAY = 1000
	,ON_FAILURE = CONTINUE
)
ALTER SERVER AUDIT [LinkedServer] WITH (STATE = ON)
GO
</pre>
The Server Audit exists and is running. We next create a Database Specification Audit named 'LinkedServerMaster'. We will track EXECUTE statements for the system stored procedures listed earlier:
<pre lang="tsql">USE [master]
GO

CREATE DATABASE AUDIT SPECIFICATION [LinkedServerMaster]
FOR SERVER AUDIT [LinkedServer]
ADD (EXECUTE ON OBJECT::[sys].[sp_addlinkedserver] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_addserver] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_dropserver] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_addlinkedsrvlogin] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_droplinkedsrvlogin] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_serveroption] BY [dbo]),
ADD (EXECUTE ON OBJECT::[sys].[sp_setnetname] BY [dbo])
WITH (STATE = ON)
GO
</pre>
OK, the audit objects are in place, so we next create a linked server. Notice I'm using an instance of SQL 2012 for the audit and connecting to an instance of SQL2016:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/linked_server.jpg"><img class="aligncenter wp-image-18637 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/02/linked_server-600x544.jpg" alt="auditing linked servers" width="600" height="544" /></a>

&nbsp;

Now, let's check the audit logs and see if we have any results (click to embiggen):

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/audit_linked_server.jpg"><img class="aligncenter wp-image-18639 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/02/audit_linked_server-600x484.jpg" alt="auditing linked servers" width="600" height="484" /></a>

&nbsp;

Success! We've captured details on the creation of the linked server along with options set and logins created.
<h2>Summary</h2>
SQL Audit is a great way to capture details on who is making changes to your instance, and when. However, as mentioned before, you must have an audit configured prior to any linked server issue happening. If you are interested in this audit, I'd recommend you configure the audit right after SQL Server is installed.

&nbsp;