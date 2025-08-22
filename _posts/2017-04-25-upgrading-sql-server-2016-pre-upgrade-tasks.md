---
layout: post
title: 'Upgrading to SQL Server 2016: Pre-upgrade tasks'
date: '2017-04-25 13:36:45 +0000'
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

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016.jpg"><img class="aligncenter size-medium wp-image-17808" src="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016-560x297.jpg" alt="Upgrading to SQL Server 2016" width="560" height="297"></a>

In our <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-reasons-upgrading/" target="_blank" rel="noopener noreferrer">previous post</a>&nbsp;on upgrading to SQL Server 2016 we talked about the reasons you might have for wanting to upgrade. For this post, we will look at the pre-upgrade checklist items you should consider before upgrading to SQL Server 2016.

After you have decided that upgrading is something you want, you will need to start putting together a project plan. The simplest plan involves three steps:

1. <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-pre-upgrade-tasks/" target="_blank" rel="noopener noreferrer">Pre-upgrade tasks</a>
2. <a href="https://thomaslarock.com/2017/04/upgrading-to-sql-server-2016-upgrade-tasks/" target="_blank" rel="noopener noreferrer">Upgrade tasks</a>
3. <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-post-upgrade-tasks/" target="_blank" rel="noopener noreferrer">Post-upgrade tasks</a>

Seems simple, right? Well, it can be, especially if you take the time to review the details.&nbsp;Before the upgrade project begins you need to do a lot of legwork. Trust me when I tell you that the extra legwork now will save you headaches later. Here is a checklist of items to review before your data is migrated.
<h2>1. Know your path(s)</h2>
To get to SQL Server 2016 you can <a href="https://docs.microsoft.com/en-us/sql/database-engine/install-windows/supported-version-and-edition-upgrades#upgrades-from-earlier-versions-to-includesscurrentincludessscurrent-mdmd" target="_blank" rel="noopener noreferrer">upgrade directly from</a>:
• SQL Server 2014
• SQL Server 2012 SP2
• SQL Server 2008R2 SP3
• SQL Server 2008 SP4

If you are running SQL Server 2005 or earlier, you need to upgrade to an intermediate version before upgrading to SQL Server 2016.

For those folks running SQL Server 2000 instances (yes we KNOW you still exist) you are not able to upgrade directly to SQL Server 2016 without first upgrading to an intermediary version.
<h2>2. Licensing changes</h2>
Starting with SQL Server 2012 licensing is done per-core, not per-socket. There will result in licensing changes for SQL Server 2016 compared to your current version. But SQL Server 2016 Standard edition does allow for Server + CAL licensing, too. Because of the change from socket to core, in-place upgrades may come with a hefty cost increase.

Also worth mentioning is that <a href="https://blogs.msdn.microsoft.com/sqlreleaseservices/sql-server-2016-service-pack-1-sp1-released/" target="_blank" rel="noopener noreferrer">SQL Server 2016 SP1 allows for many features that were once Enterprise-only</a> such as Availability Groups, data compression, partitioning, Columnstore, etc. Evaluate licensing costs and the list of features now available in Standard edition prior to starting any upgrade project.
<h2>3. Know your options</h2>
<div data-offset-key="5ahe4-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="5ahe4-0-0"><span class="hardreadability"><span data-offset-key="5ahe4-0-0">As complex as upgrading to SQL Server 2016 may appear, all upgrades are one of two scenarios: in-place or side-by-side</span></span><span data-offset-key="5ahe4-1-0">.</span></div>
</div>
<div data-offset-key="qa9j-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="qa9j-0-0"><span data-offset-key="qa9j-0-0">&nbsp;</span></div>
</div>
<div data-offset-key="2eq36-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="2eq36-0-0"><span class="hardreadability"><span data-offset-key="2eq36-0-0">In-place upgrades</span><span data-offset-key="2eq36-0-1"> are when you upgrade the current instance of SQL Server by running the installation wizard</span></span><span data-offset-key="2eq36-1-0">. These are the easiest to perform but the hardest to rollback. They have the potential for the smallest amount of downtime. There is no need to move to a new database server. </span><span class="veryhardreadability"><span data-offset-key="2eq36-2-0">The server retains the current name allowing for application to connect without any changes (providing the applications support the new version of SQL Server)</span></span><span data-offset-key="2eq36-3-0">.</span></div>
</div>
<div data-offset-key="d6u4a-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="d6u4a-0-0"><span data-offset-key="d6u4a-0-0">&nbsp;</span></div>
</div>
<div data-offset-key="bd75e-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="bd75e-0-0"><span class="veryhardreadability"><span data-offset-key="bd75e-0-0">Side-by-side upgrades</span><span data-offset-key="bd75e-0-1"> are when you install the new version of SQL Server as a new instance on the existing server (or a new server, which is what I prefer especially for production scenarios) and migrate databases over as necessary</span></span><span data-offset-key="bd75e-1-0">. </span><span class="hardreadability"><span data-offset-key="bd75e-2-0">The fresh SQL Server installation allows for thorough testing of the system before bringing it online for production</span></span><span data-offset-key="bd75e-3-0">. It also allows for more options for rollback. The use of DNS aliases help to redirect applications to the new server.</span></div>
</div>
<div data-offset-key="23hf5-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="23hf5-0-0"><span data-offset-key="23hf5-0-0">&nbsp;</span></div>
</div>
<div data-offset-key="4cu1i-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="4cu1i-0-0"><span data-offset-key="4cu1i-0-0">There is also the concept of a </span><span data-offset-key="4cu1i-0-1">rolling upgrade</span><span data-offset-key="4cu1i-0-2">. </span><span class="veryhardreadability"><span data-offset-key="4cu1i-1-0">This is when a high-availability feature such as mirroring, clustering, or Availability Groups allows you to upgrade a secondary node, failover, and continue upgrading all nodes until you upgrade the primary node, and then fail back if needed</span></span><span data-offset-key="4cu1i-2-0">. During an upgrade, some downtime may </span><span class="passivevoice"><span data-offset-key="4cu1i-3-0">be required</span></span><span data-offset-key="4cu1i-4-0">. Rolling upgrades can </span><span class="complexword"><span data-offset-key="4cu1i-5-0">minimize</span></span><span data-offset-key="4cu1i-6-0"> but are not always guaranteed to </span><span class="complexword"><span data-offset-key="4cu1i-7-0">eliminate</span></span><span data-offset-key="4cu1i-8-0"> downtime. </span><span class="veryhardreadability"><span data-offset-key="4cu1i-9-0">The less downtime allowed, the more expensive the project (usually), as it includes several different types of resources – human and physical</span></span><span data-offset-key="4cu1i-10-0">.</span></div>
</div>
<h2>4. Gather inventory details</h2>
You&nbsp;must&nbsp;gather information about the servers and the database instances that are in scope for upgrading to SQL Server 2016. There are many tools available to help you collect these details such as <a href="https://www.microsoft.com/en-us/download/details.aspx?id=7826" target="_blank" rel="noopener noreferrer">Microsoft Assessment and Planning (MAP) Toolkit</a> and <a href="https://sqlpowerdoc.codeplex.com/" target="_blank" rel="noopener noreferrer">SQL Power Doc</a>, as well as <a href="http://www.solarwinds.com/downloads" target="_blank" rel="noopener noreferrer">3rd party tools</a>.

Gathering a list of server and database names may not be enough, you will want to collect details about the databases as well. Even a simple count of tables is a valuable piece of information to have. If you have 873 tables at the start, then you&nbsp;need&nbsp;to verify you have 873 when you are done. Same for stored procedures. Consider collecting details at the column level, too. Make certain that datatypes and collations are intact, view definitions haven’t changed, etc.

You need to collect details on the in-house and third party vendor applications using the database server. List out the availability requirements for every application using the instance and you need to include the applications that are connecting remotely.

Also worth noting is any application specific configurations that&nbsp;are applied to the server O/S, the database instance, and the database itself. You need to know what non-default configurations are in use by the application using the instance.

This might seem like overkill for many reading this, but if you have ever had the unpleasant situation where a table was missed because of a migration and/or upgrading to SQL Server 2016, you will know it can be quite valuable.
<h2>5. Data Migration Assistant</h2>
<div data-offset-key="5ahe4-0-0" data-editor="4dsv3" data-block="true">
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="5ahe4-0-0"><span class="hardreadability"><span data-offset-key="5ahe4-0-0">The Data Migration Assistant (DMA) will help to identify any breaking or behavioral changes as well as deprecated features</span></span><span data-offset-key="5ahe4-1-0">. The</span><span class="hardreadability"><span data-offset-key="5ahe4-2-0">&nbsp;DMA will identify issues that need resolution before upgrading to the desired version of SQL Server</span></span><span data-offset-key="5ahe4-3-0">.</span></div>
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="5ahe4-0-0"></div>
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="5ahe4-0-0"><span class="hardreadability"><span data-offset-key="dcqun-0-0">You should be aware that the DMA is like a consultant: it doesn't fix everything that is wrong, it advises you on what actions you should take</span></span><span data-offset-key="dcqun-1-0">. </span><span class="hardreadability"><span data-offset-key="dcqun-2-0">The actions the DMA recommends will come in two forms: those actions to done before a migration, and those actions done post-migration</span></span><span data-offset-key="dcqun-3-0">. The DMA is good at finding what I call the "stub-your-big-toe" things that need fixing before a migration. </span><span class="hardreadability"><span data-offset-key="dcqun-4-0">But it is not foolproof, it may not identify every last detail specific for your application systems</span></span><span data-offset-key="dcqun-5-0">. You will need to play the role of an actual DBA when migrating to a new version.&nbsp;</span></div>
</div>
<h2>6. Deprecated features</h2>
With each new version of SQL Server there are some features that are marked as deprecated. Deprecated does not mean the features have been removed, it means that the features will possibly be removed in a future version. You should not use deprecated features for any new development work. The list of deprecated database engine features for SQL Server 2016 is&nbsp;<a href="https://docs.microsoft.com/en-us/sql/database-engine/deprecated-database-engine-features-in-sql-server-2016" target="_blank" rel="noopener noreferrer">here</a>.
<h2>7. Discontinued features</h2>
With SQL Server 2016, Microsoft started publishing a list of discontinued items. These items&nbsp;are removed from SQL Server. You can see the list of discontinued items <a href="https://docs.microsoft.com/en-us/sql/database-engine/discontinued-database-engine-functionality-in-sql-server-2016" target="_blank" rel="noopener noreferrer">here</a>. You should review these items and make certain your applications are not relying on a feature that will not be there.
<h2>8. Breaking changes</h2>
Did you know that Microsoft <a href="https://docs.microsoft.com/en-us/sql/database-engine/breaking-changes-to-database-engine-features-in-sql-server-2016" target="_blank" rel="noopener noreferrer">publishes a list of breaking changes</a> for each version of SQL Server? Well, you do now. You should review them to the point that they are familiar to you. You don't have to memorize them all.&nbsp;Become familiar with them so that if something odd happens you can think to yourself "...hey, is this odd behavior listed in the breaking changes section of the Books Online (BOL)"?
<h2>9. Behavioral changes</h2>
Previous versions of SQL Server have published a list of behavioral changes for the database engine. Similar to the breaking changes, the behavioral changes are changes that could still affect you in an adverse way. They are worth reviewing, and they are also things that the DMA is likely to never report back to you about because they aren't things that *will* break, but things that *could* break.

I was not able to find a BOL entry for SQL Server 2016 for the database engine. There are pages for Analysis Services, Integration Services, and Reporting Services. You could always review the previous versions over at the <a href="https://technet.microsoft.com/en-us/library/cc707785(v=sql.110).aspx" target="_blank" rel="noopener noreferrer">SQL Server 2012 page</a> and use that as a starting list.
<h2>10. Read the release notes</h2>
Because you're a geek, that's why. Take a few minutes and <a href="https://docs.microsoft.com/en-us/sql/sql-server/sql-server-2016-release-notes" target="_blank" rel="noopener noreferrer">read the release notes</a>. No, they aren't as funny as the release notes for apps on your phone, but they can be useful for you to review anyway. It's good to have as complete a picture as possible for the new version should something not work as expected, and there are details in the release notes you may not find elsewhere.
<h2>11. New environment requirements</h2>
Updating your server O/S should be part of the upgrading to SQL Server 2016 project plan.

Microsoft lists the minimum requirements for installing SQL Server 2016 <a href="https://docs.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server" target="_blank" rel="noopener noreferrer">on this page</a>. But, those are the *minimums* there. Chances are if your servers don't already meet those requirements then you aren't looking to upgrade anytime soon anyway. But if you are upgrading, then it might be time to upgrade your hardware as well. Heck, you may even consider going virtual (if you aren't already), which still requires you to examine your hardware requirements.

But here's the real reason you will want to upgrade your hardware: new features. Let's say that you are thinking of upgrading to SQL Server 2016 to take advantage of Hekaton. Considering there is a lot of shiny new things in SQL Server 2016, you'll want to do the extra legwork here to scope out what hardware you'll need. Otherwise, you won’t be able to leverage many of the new features.
<h2>12. Take baselines</h2>
Collect performance baselines before you begin the upgrade process. If you don’t then you won’t have any way of knowing if performance is better or worse when the upgrade is complete. Since each SQL Server implementation is unique, there will be different performance metrics that are&nbsp;illbe to you and your business users.

You must also include a baseline of the current server operating system. Perfmon works well for this, but there are <a href="http://www.solarwinds.com/database-performance-analyzer" target="_blank" rel="noopener noreferrer">many 3rd party tools that can capture these details as well</a>. If you are using Perfmon, you can output the counters to a file and then use the <a href="https://pal.codeplex.com/" target="_blank" rel="noopener noreferrer">Performance Analysis of Logs (PAL) tool</a> to analyze the output.

Know how your system is expected to grow over time. For physical implementations, this means you will try to size the physical server for end-of-life expectations. For virtualized servers, you will try to size for your performance needs now and expand later as needed.
<h2>13. Capture workloads</h2>
You can use the <a href="https://docs.microsoft.com/en-us/sql/tools/distributed-replay/sql-server-distributed-replay" target="_blank" rel="noopener noreferrer">Distributed Replay feature</a> to capture a production workload from a source server and replay it on a target server. Doing so will help to assess the impact of upgrading SQL Server by comparing the workload performance against both systems. Distributed Replay is most useful for scenarios that have high concurrency and a single client cannot simulate the workload properly.

The <a href="https://blogs.msdn.microsoft.com/datamigration/2017/03/24/dea-2-0-how-to-use-database-experimentation-assistant/" target="_blank" rel="noopener noreferrer">Database Experimentation Assistant</a> is a new tool currently available in Technical Preview. It uses Distributed Reply along with R services to give the user a way to do A/B testing of workloads. Using statistical analysis of workloads allows for greater confidence when upgrading to newer versions of SQL Server.
<h2>14. Testing the Server O/S</h2>
Tools like <a href="https://iperf.fr/" target="_blank" rel="noopener noreferrer">iPerf</a> and <a href="https://github.com/Microsoft/diskspd" target="_blank" rel="noopener noreferrer">DskSpd</a>&nbsp;can test the server network and disk performance to verify it is as expected before installing SQL Server. These tools are good at helping to identify if there are any possible configuration issues with the network and disk layout. It is better to check for such issues&nbsp;now before the installation of SQL Server 2016 begins.
<h2>15. Take backups</h2>
Before you start any upgrade process make certain you take backups of everything; databases, application files, and the server O/S. Sometimes you can utilize a VM snapshot (or checkpoint) to help with this process. I would recommend that when it comes to backups to consider the <a href="https://www.hanselman.com/blog/TheComputerBackupRuleOfThree.aspx" target="_blank" rel="noopener noreferrer">Computer Backup Rule of Three</a>.

Also worth knowing: backups are only good if they can be restored. So, you will want to test the restore process before you move forward with upgrading.

<span data-offset-key="8cgnf-0-0">In the event of a rollback during the upgrade process, you must decide how to handle potential data loss. </span><span class="hardreadability"><span data-offset-key="8cgnf-1-0">For example, if you are running a production parallel scenario the business may need to redo a full day’s worth of data entry</span></span><span data-offset-key="8cgnf-2-0">. It’s better to have those discussions now, not later.</span>
<h2>Summary</h2>
The above pre-upgrade checklist items are a great starting point for any upgrading to SQL Server 2016 project. They form the foundation for gathering information about your server and databases you want prior to any upgrade taking place. With this information, you will save yourself time and avoid frustrations with upgrading to SQL Server 2016.

In the <a href="https://thomaslarock.com/2017/04/upgrading-to-sql-server-2016-upgrade-tasks" target="_blank" rel="noopener noreferrer">next post</a>, we will look at the tasks that take place during the upgrade itself.

Don't forget that you can also&nbsp;<a href="http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X" target="_blank" rel="noopener noreferrer">download and read the upgrade whitepaper</a> I wrote for SolarWinds. It contains additional information and a set of reference links that I believe you will find useful.