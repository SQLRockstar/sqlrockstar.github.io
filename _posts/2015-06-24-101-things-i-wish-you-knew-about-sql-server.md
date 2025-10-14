---
layout: post
title: 101 Things I Wish You Knew About SQL Server
date: '2015-06-24 08:36:25 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- Airplane wine
- DBA
- sql server
- Things I Write While High on Bacon
---

<a href="https://thomaslarock.com/wp-content/uploads/2015/06/bacon101.jpg"><img class="aligncenter wp-image-16748 size-full" src="https://thomaslarock.com/wp-content/uploads/2015/06/bacon101.jpg" alt="bacon101" width="1100" height="620" /></a>Last week I was visiting the SolarWinds home office in Austin and hanging with my fellow Head Geeks. Our conversations often cover a wide range of topics and at times even turn into teaching lessons for each other. I get to learn about networks, storage, virtualization, monitoring, etc. and I get to teach my fellow Head Geeks a few things too. At some point last week I uttered the words "I'm going to write a blog post about the things I wish you knew about SQL Server".

These aren’t absolute truths (except for number 44). They are just things I want everyone to know about SQL Server and being a SQL Server DBA.

So, here they are. As always, you're welcome.
<ol>
	<li>SQL Server will do what you tell it to do. I find that <a href="https://thomaslarock.com/wp-content/uploads/2015/06/pebkac.jpg" target="_blank">PEBKAC</a> is often the root cause for many issues.</li>
	<li>DBAs get paid for performance, but we <a href="http://bit.ly/1J2zzzJ" target="_blank">keep our jobs with recovery</a>.</li>
	<li><a href="https://thomaslarock.com/2013/04/how-to-survive-any-database-disaster/" target="_blank">HA &lt;&gt; DR</a>. If you can't recover, <a href="http://blogs.technet.com/b/cansql/archive/2015/01/27/mvp-series-7-ways-to-lose-your-dba-job.aspx" target="_blank">you can't keep your job</a>. See previous item.</li>
	<li>Memory, CPU, disk, and network are all finite resources. Leave room for growth.</li>
	<li>95% of all workloads will run just fine on modest hardware. Don't listen to fools that architect crazy solutions for edge cases that won't happen.</li>
	<li>Backups (AKA <a href="http://www.techopedia.com/definition/23340/database-dump" target="_blank">database dumps</a>). You need them. Store them someplace safe, and on a different server. See number 2.</li>
	<li><a href="https://ola.hallengren.com/" target="_blank">Maintenance</a> is mandatory. Find, or make, a window for rebuilding indexes, updating stats, running DBCC CHECKDB, and taking backups. See number 2.</li>
	<li>Don't forget to <a href="https://msdn.microsoft.com/en-us/library/ms178578.aspx" target="_blank">backup security certificates</a>, too. See number 2.</li>
	<li>Monitor for unused, misused, and <a href="http://www.sqlskills.com/blogs/kimberly/removing-duplicate-indexes/" target="_blank">duplicate indexes</a>. These are just adding overhead you don't need.</li>
	<li>Identity values can, and do, <a href="http://www.sqlservercentral.com/Forums/Topic1367161-392-1.aspx" target="_blank">run out</a>. Be prepared.</li>
	<li>Set the <a href="https://msdn.microsoft.com/en-us/library/ms178067.aspx?f=255&amp;MSPPError=-2147217396" target="_blank">min and max memory configuration</a> for your instance.</li>
	<li>Data and logs go on different disks. This isn't necessarily about performance, it's <a href="https://support.microsoft.com/en-us/kb/2033523" target="_blank">also about recovery</a>. See number 2.</li>
	<li>One lane of traffic is not enough. Dual NICs and a big, fat pipe are what you want.</li>
	<li>But you can always <a href="https://thomaslarock.com/2012/08/keep-calm-and-blame-the-network/" target="_blank">blame the network anyway</a>.</li>
	<li>Know the <a href="https://thomaslarock.com/2013/04/how-to-survive-any-database-disaster/" target="_blank">RTO and RPO</a> for your applications. See number 2.</li>
	<li>When troubleshooting, sometimes the <a href="http://math.ucr.edu/home/baez/physics/General/occam.html" target="_blank">simplest answer is the right one</a>.</li>
	<li>Focus on wait events and logical I/O when performance tuning. They help you <a href="http://www.mssqltips.com/sqlservertip/3256/quickly-pinpoint-sql-server-performance-issues-with-solarwinds-database-performance-analyzer/" target="_blank">find the root cause the fastest</a>.</li>
	<li>The best clustered index keys are <a href="http://www.sqlskills.com/blogs/kimberly/more-considerations-for-the-clustering-key-the-clustered-index-debate-continues/" target="_blank">unique, narrow, static, and ever increasing.</a></li>
	<li>Just because you <a href="https://msdn.microsoft.com/en-us/library/ms143432.aspx" target="_blank">can create 999 indexes on a table</a> doesn't mean you should.</li>
	<li>Put system objects on a different filegroup than user objects. Oh, and you should be using filegroups. You are, right?</li>
	<li>Learn how to restore filegroups.</li>
	<li>Use SET NOCOUNT ON to <a href="https://msdn.microsoft.com/en-us/library/ms189837.aspx" target="_blank">reduce network traffic</a>.</li>
	<li>Avoid SELECT * <a href="https://www.simple-talk.com/sql/t-sql-programming/ten-common-sql-programming-mistakes/" target="_blank">in production code</a>. Look to return only the data that is necessary.</li>
	<li>Use <a href="http://sqlblog.com/blogs/aaron_bertrand/archive/2009/10/11/bad-habits-to-kick-avoiding-the-schema-prefix.aspx" target="_blank">schema and object owner when qualifying objects</a>, it reduces lookup costs and makes you look like a smart developer.</li>
	<li>Enable the "optimize for ad-hoc workloads" <a href="https://msdn.microsoft.com/en-us/library/cc645587.aspx" target="_blank">option</a>, unless you know you are the edge case such that this setting won't help you.</li>
	<li><a href="http://sqlblog.com/blogs/jonathan_kehayias/archive/2010/01/19/tuning-cost-threshold-of-parallelism-from-the-plan-cache.aspx" target="_blank">Adjust your cost threshold for parallelism</a> BEFORE you consider adjusting your MAXDOP setting.</li>
	<li>Know your NUMA. When configuring memory and MAXDOP, <a href="http://blogs.msdn.com/b/cindygross/archive/2011/01/28/the-ins-and-outs-of-maxdop.aspx" target="_blank">keeping everything inside one NUMA node is a nice to have</a>.</li>
	<li>Query governor is an easy way to <a href="https://msdn.microsoft.com/en-us/library/ms191219.aspx" target="_blank">stop bad queries before they happen</a>.</li>
	<li><a href="http://logicalread.solarwinds.com/sql-server-tempdb-best-practices-placement-w01/#.VYmLxRNVhBc" target="_blank">Optimize your tempdb for performance</a>.</li>
	<li>The only way to know your backup succeeded is to <a href="https://www.simple-talk.com/sql/database-administration/statistical-sampling-for-verifying-database-backups/" target="_blank">test by doing a restore</a>. See number 2.</li>
	<li>Don't nest views. <a href="https://www.simple-talk.com/sql/performance/the-seven-sins-against-tsql-performance/" target="_blank">Just don't</a>.</li>
	<li><a href="https://msdn.microsoft.com/en-us/library/bb964719.aspx" target="_blank">Enable backup compression</a> for your server, it's often worth the extra CPU.</li>
	<li><a href="https://msdn.microsoft.com/en-us/library/cc280449.aspx" target="_blank">Row and Page compression</a> are useful options as well, and often overlooked.</li>
	<li><a href="https://thomaslarock.com/2013/04/how-to-survive-any-database-disaster/" target="_blank">Build a recovery strategy</a> BEFORE you build a backup strategy. See number 2.</li>
	<li>Auto-shrink is the Peyton Manning of SQL Server. It looks like a great idea but you are <a href="http://www.pro-football-reference.com/players/M/MannPe00/gamelog/post/" target="_blank">often disappointed in the end result</a>.</li>
	<li><a href="http://www.sqlskills.com/blogs/erin/sql-server-baselines-series-on-sqlservercentral-com/" target="_blank">Baseline for performance</a>. Without baselines and metrics you have no idea if something is truly a problem or not.</li>
	<li>Don't RDP to a server and launch SSMS, or Profiler, in an attempt to fix a production issue. Learn to work remotely.</li>
	<li>Learn how to <a href="https://msdn.microsoft.com/en-us/library/dd239405.aspx" target="_blank">use scripted installs</a>.</li>
	<li>Server core is a great way to keep people away from your database servers that <a href="https://thomaslarock.com/2013/03/administering-sql-server-running-on-server-core/" target="_blank">shouldn't be touching them anyway</a>.</li>
	<li>Use <a href="https://www.simple-talk.com/sql/database-administration/sql-server-database-growth-and-autogrowth-settings/" target="_blank">autogrowth</a> but not the default growth values. Monitor for growth events and minimize their occurrence.</li>
	<li>If you don't care about your CEO reporting on incorrect data, or your CIO going to jail, then <a href="http://www.jasonstrate.com/2012/06/the-side-effect-of-nolock/" target="_blank">NOLOCK is the query hint for you</a>!</li>
	<li>Keep your transactions short.</li>
	<li><a href="https://thomaslarock.com/2009/03/sql-database-triggers/" target="_blank">Triggers are awful</a>, awful little creatures.</li>
	<li>But NULLs are <a href="https://thomaslarock.com/2014/09/isnull-title-null-is-an-unknown-not-empty/" target="_blank">far worse</a>.</li>
	<li>Security should not be an afterthought when writing code. <a href="http://www.troyhunt.com/2015/06/free-recorded-webinar-on-pluralsight.html" target="_blank">Assume that SQL injection is a virus and it will infect you at some point</a>. Build accordingly.</li>
	<li><a href="http://www.sqlskills.com/blogs/kimberly/instant-initialization-what-why-and-how/" target="_blank">Instant file initialization is a good thing</a>. You should be using this.</li>
	<li>Despite having zero enhancements since being introduced in SQL 2008, I still think <a href="http://www.amazon.com/gp/product/B004VHAZAS/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B004VHAZAS&amp;linkCode=as2&amp;tag=sq0f-20" target="_blank">Policy Based Management is a good thing</a> that people should be using more.</li>
	<li>Then again, I think <a href="https://msdn.microsoft.com/en-us/library/hh245198.aspx" target="_blank">Powershell should be used by more</a>, too. If your DBA can't work a command line, don't let them touch your data.</li>
	<li>SQL Server assumes a "cold cache" when building a query plan because disk storage is the last thing you should be worried about when it comes to performance.</li>
	<li>Object statistics are the <a href="https://msdn.microsoft.com/en-us/library/ms190397.aspx" target="_blank">most important piece of metadata in your database</a>. Bad, or missing, stats will lead to bad query plans.</li>
	<li><a href="http://www.thetelegram.com/Opinion/Columnists/2014-05-06/article-3713659/Bad-data-leads-to-bad-decisions/1" target="_blank">Bad data leads to bad decisions</a>.</li>
	<li><a href="https://thomaslarock.com/2013/01/designing-a-database-7-things-you-dont-want-to-do/" target="_blank">Great database performance starts with great database design</a>.</li>
	<li>Enforce <a href="https://msdn.microsoft.com/en-us/library/ms161959.aspx" target="_blank">password policies</a> for your SQL logins.</li>
	<li><a href="http://www.mssqltips.com/sqlservertip/1155/sql-server-2005-error-log-management/" target="_blank">Recycle your SQL Server error logs</a>.</li>
	<li>Script SQL login and database user permissions nightly. You never know when you'll need them during a DR event. See number 2.</li>
	<li>SQL Server Agent alerts are useful, and <a href="https://thomaslarock.com/2015/01/5-things-didnt-know-sql-agent/" target="_blank">hardly used</a>.</li>
	<li>Deadlocks are often the result of <a href="https://www.simple-talk.com/sql/database-administration/handling-deadlocks-in-sql-server/" target="_blank">application logic and data access patterns</a>. The engine doesn't just get "tired" and start deadlocking.</li>
	<li>Testing against 10, 100, and 1000 rows is not an accurate test against a production workload.</li>
	<li>Table variables are <a href="https://support.microsoft.com/en-us/kb/305977" target="_blank">not "in-memory" only</a>, and are often not as good a choice as a temp table.</li>
	<li>For a performance boost learn how to <a href="http://www.mssqltips.com/sqlservertip/1941/striping-sql-server-database-backups/" target="_blank">stripe your backups</a>. Then, learn how to restore a striped backup. See number 2.</li>
	<li>Resource governor is a great way to throttle workloads as needed, <a href="http://sqlblog.com/blogs/greg_low/archive/2015/06/03/plan-cache-pollution-avoiding-it-and-fixing-it.aspx" target="_blank">especially workloads that bloat your plan cache</a>.</li>
	<li>Sometimes a scan is better than a seek. <a href="http://www.red-gate.com/community/books/sql-server-execution-plans-ed-2" target="_blank">Learn how to read a query plan</a>.</li>
	<li><a href="http://sqlha.com/2013/04/29/alwayson-is-the-new-activepassive-and-activeactive/" target="_blank">AlwaysOn is a marketing term, not a feature</a>. Availability Groups is what you meant to say.</li>
	<li>Learn how to <a href="http://www.amazon.com/gp/product/1430219661/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=1430219661&amp;linkCode=as2&amp;tag=sq0f-20&amp;linkId=QYB6576DHM3XM7UF" target="_blank">build a cluster</a>.</li>
	<li>Learn how to <a href="http://www.amazon.com/gp/product/1430219661/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=1430219661&amp;linkCode=as2&amp;tag=sq0f-20&amp;linkId=QYB6576DHM3XM7UF" target="_blank">break a cluster</a>.</li>
	<li>Learn how to <a href="http://www.amazon.com/gp/product/1430219661/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=1430219661&amp;linkCode=as2&amp;tag=sq0f-20&amp;linkId=QYB6576DHM3XM7UF" target="_blank">repair a cluster</a>.</li>
	<li>Application code is <a href="https://www.facebook.com/156491659260/photos/pb.156491659260.-2207520000.1435079406./10152996950159261/?type=1&amp;theater" target="_blank">responsible for 100% of all performance issues</a>. #hardtruth</li>
	<li>Know <a href="https://msdn.microsoft.com/en-us/library/ms187809.aspx" target="_blank">what trace flags are running</a> on your system.</li>
	<li>Keep as many of your servers configured in the exact same way. This saves time troubleshooting.</li>
	<li>Before you write something yourself you should know there are many free scripts on the internet for you to use. But, sometimes, you get what you pay for.</li>
	<li><a href="https://www.pinterest.com/pin/12455336441357332/" target="_blank">Data lasts longer than code</a>. Treat it right.</li>
	<li>However, <a href="http://media-cache-ec0.pinimg.com/originals/dc/81/ff/dc81ffd6de3df7ad8fd8d0ab2e3604da.jpg" target="_blank">data will confess to anything</a> if you torture it long enough.</li>
	<li>Know what the installer <a href="https://thomaslarock.com/2014/08/know-installer-database/" target="_blank">just did to your database server</a>.</li>
	<li>Use <a href="https://thomaslarock.com/2012/02/still-using-windows-logins-for-your-databases-youre-doing-it-wrong/" target="_blank">Windows AD groups, not Windows Logins</a>. There should be a separation of duties with regards to allowing data access.</li>
	<li>Custom <a href="https://msdn.microsoft.com/en-us/library/ms187936.aspx" target="_blank">database</a> roles and <a href="https://msdn.microsoft.com/en-us/library/ee677610.aspx" target="_blank">server</a> roles are a great way to provide custom permissions.</li>
	<li>Ordering and sorting of data consumes resources. Do it as few times as possible. Sometimes, it's best done in the application layer.</li>
	<li>Task manager is a <a href="https://channel9.msdn.com/Shows/Data-Exposed/7-Ways-Your-Server-is-Lying-To-You" target="_blank">dirty, filthy liar</a>.</li>
	<li>Understand how to work with large data sets <a href="http://sqlperformance.com/2013/03/io-subsystem/chunk-deletes" target="_blank">without filling up the transaction log</a>.</li>
	<li>Every now and then, <a href="https://msdn.microsoft.com/en-us/library/ms177862.aspx?f=255&amp;MSPPError=-2147217396" target="_blank">go look at the system views, functions, and stored procedures</a>. You will learn something new and useful.</li>
	<li><a href="https://msdn.microsoft.com/en-us/library/ms143694.aspx" target="_blank">Multiple instances of SQL Server on a server</a> know nothing of each other. It's up to you to make sure they play nice.</li>
	<li>Don't install services (SSRS, SSIS, SSAS) onto a server "just in case". Only install the services that are needed.</li>
	<li>Assign a <a href="https://www.simple-talk.com/sql/database-administration/how-to-get-sql-server-security-horribly-wrong/" target="_blank">strong password to the 'sa' login, then disable it</a>. You don't need it, and neither does anyone else, especially a vendor. Use a different account for sysadmin activities.</li>
	<li>If your vendor requires the use of the 'sa' account, go find another vendor.</li>
	<li>If the vendor code creates a loopback linked server, go find another vendor.</li>
	<li>You can't mirror a database <a href="https://thomaslarock.com/2014/12/wrong-database-mirroring/" target="_blank">using an actual mirror</a>, no matter how hard you try.</li>
	<li><a href="https://thomaslarock.com/2012/08/why-datatypes-matter-3-ways-they-can-hurt-performance/" target="_blank">Implicit conversions can be avoided</a> providing someone is willing to do the extra work.</li>
	<li>Over allocation of host resources leads to over commit of host resources, and that's <a href="https://thomaslarock.com/2013/04/doing-it-wrong-virtualizing-sql-server/" target="_blank">bad for everyone</a>. Leave room for growth.</li>
	<li>Comments in code are <a href="http://www.explainxkcd.com/wiki/index.php/1421:_Future_Self" target="_blank">notes to "future you"</a>. Be nice to your future self and remind them what in the hell you were thinking.</li>
	<li>Learn how to make use of <a href="http://blogs.msdn.com/b/dbrowne/archive/2012/05/21/how-to-add-a-hostname-alias-for-a-sql-server-instance.aspx" target="_blank">DNS aliases</a>, it makes swapping servers around much easier when you don't need to update connection strings.</li>
	<li>Practice <a href="https://thomaslarock.com/2014/01/restore-the-master-database-in-sql-server-2012/" target="_blank">recovering the master database</a>. See number 2.</li>
	<li>Make sure you know the last time the <a href="https://thomaslarock.com/2015/03/how-to-find-when-sql-server-wait-stats-were-last-cleared/" target="_blank">SQL Server performance metrics have been reset</a>, otherwise you may overlook the root cause of an issue.</li>
	<li>Junior DBAs know how to react. Senior DBAs know how to be <a href="https://thomaslarock.com/2012/06/how-one-hour-of-action-can-give-you-150-hours-of-satisfaction/" target="_blank">proactive</a>.</li>
	<li>Make sure you can <a href="https://www.simple-talk.com/sql/database-administration/rollback-and-recovery-troubleshooting-challenges-and-strategies/" target="_blank">rollback</a>, when necessary.</li>
	<li>Practice <a href="https://thomaslarock.com/2014/06/upgrading-to-sql-server-2014-a-dozen-things-to-check/" target="_blank">upgrading SQL Server</a> in a variety of ways, especially rolling upgrades.</li>
	<li>Capacity planning is often a worthless endeavor. You can't predict the future. There's always someone that decides to load 1TB of data without telling anyone.</li>
	<li>You'll still get blamed for there not being enough disk space.</li>
	<li>You can't fix stupid.</li>
	<li>Bad code and bad database design will <a href="https://thomaslarock.com/2013/10/really-just-spend-thousands-new-hardware/" target="_blank">bring good hardware to its knees</a>, always.</li>
	<li><a href="https://thomaslarock.com/2013/12/what-is-your-macguffin/" target="_blank">Empathy is the most important skill a DBA can have</a>. Arrogance is the least important skill, yet often found in great abundance in the IT world.</li>
	<li>Everyone starts out with <a href="http://www.sqlskills.com/blogs/paul/ignorance-is-not-stupidity/" target="_blank">zero knowledge of SQL Server</a>.</li>
	<li><a href="http://www.datamodel.com/index.php/2013/12/03/10-tips-for-the-minimalist-dba/" target="_blank">The best DBA is a lazy DBA</a>. Driven, but lazy.</li>
</ol>
&nbsp;

That's all I came up with during my flight(s) home last week. I'm sure I could add more to the list and likely will over time.

Enjoy!