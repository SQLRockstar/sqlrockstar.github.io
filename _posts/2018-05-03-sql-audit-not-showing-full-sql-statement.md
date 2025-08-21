---
layout: post
title: SQL Audit Not Showing Full SQL Statement
date: '2018-05-03 10:44:31 +0000'
categories:
- Data Security and Privacy
- Database Design
- MSSQL
- SQL MVP
- SQL Server 2017
tags:
- data privacy
- data security
- sql audit
---

I noticed some MSDN forum posts regarding SQL Audit not showing the full SQL statement. To the end user, it appears that SQL Audit is truncating of SQL statements. I decided to write a quick post to help clear up the confusion for large SQL statements and how they appear in SQL Audit.

No, it's <a href="https://social.msdn.microsoft.com/Forums/en-US/b6a30a54-e927-400d-9b7f-422961325fb5/database-audit-feature-logs-sql-statements-partiallytrimmed-is-this-a-bug?forum=sqlsecurity" target="_blank" rel="noopener">not a bug</a>, but yes, the <a href="https://social.msdn.microsoft.com/Forums/sqlserver/en-US/b3834e6a-7d8c-4e6e-b334-0fcad4dd7270/sql-audit-strips-comments-in-sql-statements?forum=sqldatabaseengine#97f1abd3-6b18-413f-9fe8-a6bdbb02efa3" target="_blank" rel="noopener">statements may appear trimmed</a>. Let me explain.

First, let's set up an audit that will capture a large statement. How large is large?

The <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-get-audit-file-transact-sql?view=sql-server-2017" target="_blank" rel="noopener">fn_get_audit_file documentation</a> defines large as: "<em>too large to fit in the write buffer</em>". This is referring to the size of the 'statement' column, defined as NVARCHAR(4000). For any statement larger than that it will need to be broken into distinct lines, identified by the sequence_number column.

Let's see what this looks like in action.

I will create the Server Audit first that outputs to a flat file on my laptop:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_log.jpg"><img class="aligncenter size-large wp-image-19004" src="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_log-600x552.jpg" alt="sql audit log large text" width="600" height="552" /></a>

&nbsp;

I have also included the code for you here:
<pre lang="tsql">CREATE SERVER AUDIT [LargeTextAudit]
TO FILE 
(	FILEPATH = N'C:\TeamData\AuditLogs\'
	,MAXSIZE = 0 MB
	,MAX_ROLLOVER_FILES = 2147483647
	,RESERVE_DISK_SPACE = OFF
)
WITH
(	QUEUE_DELAY = 1000
	,ON_FAILURE = CONTINUE
)
ALTER SERVER AUDIT [LargeTextAudit] WITH (STATE = ON)
GO
</pre>
OK, next we create a Database Audit Specification. I will capture any SELECT statement executed against the sysobjects table:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_db_specification_large_text.jpg"><img class="aligncenter size-large wp-image-19005" src="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_db_specification_large_text-600x274.jpg" alt="sql audit large text database specification" width="600" height="274" /></a>

&nbsp;

And here is the code for that database specification:
<pre lang="tsql">CREATE DATABASE AUDIT SPECIFICATION [LargeTextAudit]
FOR SERVER AUDIT [LargeTextAudit]
ADD (SELECT ON OBJECT::[sys].[sysobjects] BY [dbo])
WITH (STATE = ON)
GO
</pre>
Now we need to write a statement that will be larger than 8k. I will use dynamic SQL for this task. Here's the sample code that I've used for...a long time. Now get off my lawn:
<pre lang="tsql">DECLARE @LongString VARCHAR(8000)
	, @Replicate VARCHAR(8000)
	, @From VARCHAR(8000)

SELECT @LongString='SELECT TOP 1 name,'''
	,@Replicate=replicate('SQLRockstar',9000)
	,@From=''' FROM sysobjects'

exec(@LongString+@Replicate+@From)
</pre>
After enabling the database specification and the server audit, execute the code. Then open the audit log viewer:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_view_large_text_ANNOTATED.jpg"><img class="aligncenter size-large wp-image-19008" src="https://thomaslarock.com/wp-content/uploads/2018/05/sql_audit_view_large_text_ANNOTATED-600x393.jpg" alt="sql audit view large text truncated" width="600" height="393" /></a>

&nbsp;

We can see there are three rows for this one statement. You can also see the sequence number column to the right in the output window. And it is also in the text box below.

If you are using the fn_get_audit_file function, the sequence number is there, too.

I hope this clears up the confusion for SQL Audit and showing large SQL statements. If you happen to be in Antwerp for <a href="https://techorama.be/" target="_blank" rel="noopener">Techorama</a> later this month, I have a session on SQL Audit you might be interested in attending. We'll talk about SQL Audit for both Earthed and Cloud versions of SQL Server.