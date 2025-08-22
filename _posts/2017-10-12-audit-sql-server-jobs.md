---
layout: post
title: Audit SQL Server Jobs
date: '2017-10-12 13:27:10 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL Azure
- SQL MVP
tags:
- data privacy
- data security
- database audit specification
- SQL
- sql audit
- sql server
- sql server audit
---

I don't see a lot of questions or discussions around the use of <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine" target="_blank" rel="noopener">SQL Server Audit</a>. To me, SQL Server Audit is one of those features that doesn't get enough love and attention. That's why I've decided to take the time today to show how to use SQL Server Audit to audit SQL Server jobs.

We can use SQL Server Audit to track just about anything. In this post I will show you how to create an audit for SQL Server jobs. If anyone adds, deletes, or modifies a job you can track who did what, and when.

[I'm limiting the scope of this post to SQL Agent jobs only. Feel free to do the research regarding job steps and schedules. This post should help you get that done.]

We will start by identifying the objects in scope for the audit. When a user creates a job through SQL Server Management Studio (SSMS), the sp_add_job system procedure is executed. A little digging reveals the objects used by SSMS:

<a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-add-job-transact-sql" target="_blank" rel="noopener">sp_add_job</a>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-update-job-transact-sql" target="_blank" rel="noopener">sp_update_job</a>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-delete-job-transact-sql" target="_blank" rel="noopener">sp_delete_job</a>

Each of those procedures will insert, update, and delete from the following table:

<a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-tables/dbo-sysjobs-transact-sql" target="_blank" rel="noopener">msdb.dbo.sysjobs</a>

Note that a user (or 3rd party vendor) could try to update the sysjobs table directly, so it's important that we scope our audit to all possibilities. That's why we will audit both the procedures and the underlying table.

Now that we know the objects, we will start to create the audit. First, we will want to create a <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/create-a-server-audit-and-database-audit-specification" target="_blank" rel="noopener">Server Audit</a>. This is the "kitchen sink" for SQL Server Audit, as it catches everything and determines where to send the event output. For this example I will keep things simple and output everything to a file on my laptop. You can see my settings here:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit.jpg"><img class="aligncenter size-large wp-image-18073" src="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-563x600.jpg" alt="SQL Server Audit" width="563" height="600" /></a>

Next, we want to create a <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/create-a-server-audit-and-database-audit-specification" target="_blank" rel="noopener">Database Audit Specification</a> for the msdb database. We will limit the focus to the procedures and table listed earlier. The result will look like this:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-database-specification-msdb.jpg"><img class="aligncenter size-large wp-image-18080" src="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-database-specification-msdb-600x258.jpg" alt="SQL Server Audit Database Specification msdb" width="600" height="258" /></a>

Now, enable both the database specification and the server audit. Otherwise you won't capture any events or have them logged for output.

Now we are ready to test. Let's use SSMS to create a job. Here's a simple example, no steps or schedules, just a name:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-sql-agent-job-1.jpg"><img class="aligncenter size-large wp-image-18081" src="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-sql-agent-job-1-600x543.jpg" alt="SQL Server Audit SQL Agent Job" width="600" height="543" /></a>

Next, check the audit log to see the events:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-log-file.jpg"><img class="aligncenter size-large wp-image-18082" src="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-log-file-600x350.jpg" alt="SQL Server Audit Log File" width="600" height="350" /></a>

As expected, it captured the execution of the sp_add_job stored procedure. It also captured the insert statement that the sp_add_job calls.

Let's finish the test. We will modify then delete the job using SSMS. The audit log will now look like this:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-log-file-all.jpg"><img class="aligncenter size-large wp-image-18083" src="https://thomaslarock.com/wp-content/uploads/2017/10/sql-server-audit-log-file-all-600x368.jpg" alt="SQL Server Audit Log File" width="600" height="368" /></a>

The delete is at the top, and the update is in focus. We have captured both the execution of the procedures as well as the update and delete to the sysjobs table.
<h2>Summary</h2>
I think SQL Server Audit is a great feature. But it can take a lot of clicks to get it right. That's true for a lot of Microsoft products and features though. Microsoft is great at providing a framework to get the job done. I've often likened it to a tinker set. You get all the pieces, but you still need to put it together.

But the #hardtruth here is that you shouldn't need to hire an expensive DBA to click 1,000 times in SSMS to configure an audit. The good news is that the <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing" target="_blank" rel="noopener">Azure version of audit is much easier to use</a>.

I'm hopeful that the simplicity found in Azure will make its way to the Earthed version.

Someday.