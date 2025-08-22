---
layout: post
title: 'Upgrading to SQL Server 2016: Post-upgrade tasks'
date: '2017-04-25 14:05:51 +0000'
categories:
- MSSQL
- SQL MCM
- SQL MVP
- SQL Server Performance
tags:
- migrating
- migration
- mistakes
- sp_refreshview
- sql server
- SQL Server 2016
- upgrade
- upgrading
---

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016.jpg"><img class="aligncenter size-medium wp-image-17808" src="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016-560x297.jpg" alt="Upgrading SQL Server 2016" width="560" height="297"></a>

In the <a href="https://thomaslarock.com/2017/04/upgrading-to-sql-server-2016-upgrade-tasks/" target="_blank" rel="noopener noreferrer">last post</a>, we reviewed the options for upgrading SQL Server 2016.&nbsp;After upgrading SQL Server you need to perform a series of tasks to verify the databases are ready. You want to do this before the server is&nbsp;handed over to the end users for further testing. This post will provide you a checklist of items to review after the upgrade is complete.
<h2>1. Take backups</h2>
Right now. Before you do anything else. You're a DBA. Backups should be in your DNA. You should have taken one prior to the start of upgrading to SQL Server 2016, and you had better take one right now and again before you turn that database over to your end users.
<h2>2. DBCC CHECKDB</h2>
One of your post-migration or upgrade tasks should be to run the following statement:
<pre lang="tsql">DBCC CHECKDB WITH DATA_PURITY;</pre>
This statement will check your data for values that are no longer valid for the column datatype. For databases created prior to SQL 2005 (and you *know* they are still out there), this step is important. For databases created in SQL 2005 and later, the DATA_PURITY check is done automatically with a regular CHECKDB.

But what about a database that was created in SQL 2000, migrated (poorly) to a SQL 2008 instance, and left in the SQL 2000 (80) backward compatibility mode? What about that little feller? Do you want to assume that the DATA_PURITY check has been getting done? Here's a thought: just go run it yourself anyway.

Also worth noting that column integrity checks are not performed when the PHYSICAL_ONLY option is used.
<h2>3. DBCC UPDATEUSAGE</h2>
While not as critical as the DATA_PURITY command noted previously, this one still has a place in any migration or upgrade process:
<pre lang="tsql">DBCC UPDATEUSAGE(db_name);</pre>
This command will help fix any page count inaccuracies that are resulting in the sp_spaceused stored procedure returning wrong results. Be aware that it can take some time to run depending upon table or database size. Ideally, you would run this on a regular basis for one of the following reasons:

• You suspect that you are seeing incorrect values returned for sp_spaceused.
• Your database has a high volume of DDL statements (CREATE, ALTER, or DROP).
<h2>4. Updating Statistics</h2>
This&nbsp;is&nbsp;a MUST for any migration or upgrade checklist:
<pre lang="tsql">USE db_name; 
GO 
EXEC sp_updatestats;</pre>
This command will update the statistics for all the tables in your database. It issues the UPDATE STATISTICS command, which warrants mentioning because you *may* want to use&nbsp;the FULLSCAN option. I'm the type of person that would rather be safe than sorry. Therefore I would execute this:
<pre lang="tsql">USE db_name; 
GO 
EXEC sp_MSforeachtable @command1='UPDATE STATISTICS ? WITH FULLSCAN';</pre>
Bottom line: don't forget to update the statistics after upgrading to SQL Server 2016. Failure to do so could result in your queries running longer as you start your testing. The end result is a waste of time while you troubleshoot all possible bottlenecks. With SQL Server 2016 there is also a new Cardinality Estimator (CE). Since the query optimizer relies on accurate statistics for plan estimation purposes, you will want your statistics are as accurate as possible before you begin any testing.

Take care of the stats now and you won’t have to worry about them later.
<h2>5. Refresh view definitions</h2>
Believe it or not, every now and then someone will build a view that spans into another database on the same instance. And, in what may be a complete surprise to many, sometimes these views will go across a linked server as well. The point here is the view may not be contained to data&nbsp;on that single instance. In what could be the most dramatic twist of all, sometimes these views are created using a SELECT * syntax.

I know, I know…what are the odds that you could have such code in your shop? But it happens. And when you have bad code on top of views that go to other databases (or views of views of views of whatever else some sadistic person built) you are going to want to use sp_refreshview to refresh those views.

If you are migrating a database to a new server then consider refreshing your views using sp_refreshview. Most of the time it won’t do anything for you, just like a burger topped with veggie bacon. But there is that one chance where it will dramatically improve performance and your customer will be happy as a result. Using sp_refreshview is a lot like flossing: it doesn’t take much effort, and the end result is usually worth it.

(Beware that previous versions of SQL Server Management Studio (SSMS) had a bug related to sp_refreshview, <a href="https://thomaslarock.com/2014/06/upgrading-to-sql-server-2014-a-dozen-things-to-check/" target="_blank" rel="noopener noreferrer">check out the comments in this post</a> for more details.)
<h2>6. Check compatibility levels</h2>
If you have upgraded&nbsp;SQL Server within the past ten years then you have noticed how the compatibility level is not set to the newest version after the migration is complete. You must set the compatibility level yourself. With SQL Server 2016 this becomes more important than in previous versions due to the new Cardinality Estimator (CE).

There is a great whitepaper from Joe Sack that details the good, the bad, and the ugly with the new CE. The TL;DR version of the whitepaper is this: you'll want to take advantage of the new CE except for the times when you won't. Part of this is knowing which compatibility level you are using. I'd recommend you update every database on the SQL Server 2016 instance to compatibility mode 130 and test, test, test. [This assumes that you have baselined performance for your critical queries before the migration so you can verify if the new CE is working for or against you.]
<h2>7. Verify counts of objects</h2>
Remember the counts of objects such as tables and stored procedures that you took before? Now is when you want to review those counts. Make sure you have the same number of objects that you started with prior to the upgrade and migration. Remember the SQL Server upgrade motto: No table left behind!
<h2>8. Check Configurations</h2>
As part of the pre-upgrade tasks, we collected details on the in-house and third party vendor applications using the database server. We also collected information about the specific configurations applied to the server O/S, database instance, and the database itself.&nbsp;Review those details now to&nbsp;confirm the configurations were applied to the new server.

The use of a POC test system saves you a lot of time with the ‘after’ phase. A POC allows you to work through any issues early on in test and incorporate them into your upgrade plans. Also worth mentioning again is how easy Azure makes this for you.

This is also a good time to mention that sometimes it is worth running “production parallel”, where you have two systems running at the same time, both are considered production. How the data is kept in sync is up to you, but the idea is that the business users get a chance to verify that the new system is working as expected.
<h2>Summary</h2>
Upgrades are a necessary part of any development lifecycle. The chances of having a successful upgrade increase with the amount of planning and preparation you invest in building a proper upgrade process. If you are planning on upgrading to SQL Server 2016&nbsp;use these series of posts as a guide to put together your checklist.

If you haven't started building up your SQL 2016 migration or upgrade checklist yet, now is the time. Include the items listed above. They will save you pain, I promise.

Don't forget that you can also&nbsp;<a href="http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X" target="_blank" rel="noopener noreferrer">download and read the upgrade whitepaper</a> I wrote for SolarWinds. It contains more information as well as a set of tips and reference links that you will find useful.