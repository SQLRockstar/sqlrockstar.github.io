---
layout: post
title: 'Upgrading to SQL Server 2016: Reasons for upgrading'
date: '2017-04-25 13:35:22 +0000'
categories:
- Featured
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

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016.jpg"><img class="aligncenter size-medium wp-image-17808" src="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016-560x297.jpg" alt="Upgrading to SQL Server 2016" width="560" height="297" /></a>When discussions about upgrading to SQL Server 2016 are brought up the usual first question is this: "Why should we upgrade?" Someone, somewhere, wants to know why they should take a perfectly good system that runs just fine and make a bunch of changes.

There exist many valid reasons to upgrade to the latest version of SQL Server. Database and system administrators do not take on upgrade projects simply because we like to make changes and watch things break. There are new performance features, new security features, and new scalability features in SQL Server 2016 that make it worth the time and effort to upgrade.

Here is a short list of reasons why anyone might consider upgrading to SQL Server 2016.
<h2>1. New Features in SQL Server 2016</h2>
With any new version of SQL Server we always have something shiny to play with. By upgrading to SQL Server 2016 we can take advantage of the following new features:
<ul>
 	<li><a href="https://msdn.microsoft.com/en-us/library/mt163865.aspx">Always Encrypted</a></li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/mt130841.aspx">Dynamic Data Masking</a></li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/dn765131.aspx">Row Level Security</a></li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/dn935011.aspx">Stretch Database</a></li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/dn935015.aspx">Temporal tables</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/30/sql-2016-it-just-runs-faster-automatic-soft-numa/">Automatic soft NUMA</a></li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/dn817826.aspx">Query Store</a></li>
</ul>
We also have enhancements to features introduced in recent versions:
<ul>
 	<li><a href="https://msdn.microsoft.com/en-us/library/dn133186.aspx">In-Memory OLTP</a> enhancements</li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/hh510230.aspx">Always On Availability Groups</a> enhancements</li>
 	<li><a href="https://msdn.microsoft.com/en-us/library/gg492088.aspx">Updateable non-clustered columnstore</a> indexes</li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/02/25/sql-2016-it-just-runs-faster-dbcc-scales-7x-better/">DBCC CHECKDB</a> enhancements</li>
</ul>
For a complete list of all the things in SQL Server 2016 that have been enhanced, check out <a href="https://thomaslarock.com/2016/06/sql-server-2016-just-runs-faster/" target="_blank" rel="noopener noreferrer">SQL Server 2016: It Just Runs Faster</a>.
<h2>2. Supportability</h2>
End of support is fast approaching for earlier versions. This means no new service packs or updates. Yes, you can purchase extended support, but it is costly. Microsoft has extended support for Win2008 and SQL 2008, that doesn’t mean it’s a good thing to keep using them. At some point you need to let go of that Windows NT 4.0 box running SQL Server 6.5. Just let it go and transport yourself into the 21st century.
<h2>3. Vendor Requirements</h2>
You may be using software from a third-party vendor that has strict requirements about which version of SQL Server you can be using. Yes, this goes both ways, it could require newer versions, and it could require older versions. You should check with your vendor. That's what a good DBA would do.
<h2>4. Company or Industry Standard</h2>
Some companies may not allow for you to be running more than one full major version behind for any software product. And some industries may have those requirements, too. And don’t forget the auditors, they like to have their own suggestions. I also found upgrades to be a good time to revisit such standards and make sure they still apply. And, if they do, the upgrades also offered the opportunity to do some cleaning up of stuff on servers you aren't using anymore. Like IE 6.
<h2>5. Scalability</h2>
The SQL Server engine has had many enhancements in the past ten years to address scalability concerns. I listed a few of those above (Columnstore, Availability Groups, In-Memory OLTP), but the engine itself has been updated to include things like new cardinality estimation techniques to help build better query plans based upon the distribution of your data. Upgrading to SQL Server 2016 will bring you greater scalability opportunities than previous versions.
<h2>Summary</h2>
This post was meant to highlight a handful of reasons as to why you would want to upgrade to SQL Server 2016. You might be interested in new features. Or you might be forced to keep your version current. Or you might be looking for a reason to retire some older servers and migrate your data to something shiny and new.

In the <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-pre-upgrade-tasks/" target="_blank" rel="noopener noreferrer">next post</a>, we will take a look at the tasks you need to perform prior to the upgrade taking place.

Don't forget that you can also <a href="http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X" target="_blank" rel="noopener noreferrer">download and read the upgrade whitepaper</a> I wrote for SolarWinds. It contains additional information as well as a set of tips and reference links that I believe you will find useful.