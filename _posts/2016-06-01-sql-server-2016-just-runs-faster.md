---
layout: post
title: 'SQL Server 2016: It Just Runs Faster'
date: '2016-06-01 11:03:48 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server Performance
tags:
- boost
- Data Platform
- faster
- launch
- microsoft
- performance
- SQL
- SQL Database
- SQL Server 2016
---

Today is the day that <a href="https://www.microsoft.com/en-us/server-cloud/products/sql-server/" target="_blank" rel="noopener">SQL Server 2016 will officially launch</a>. I've been using SQL 2016 since some of the early CTP builds last year and I love the direction that Microsoft is headed with their entire data platform. I'm not just saying that because I'm a fanboi, either. I mean I *am* a fanboi, but that is not the point here.

There are many blogs already available on new features available in SQL Server 2016. I thought about doing similar posts myself but today I thought instead of listening to me go on about how SQL Server 2016 is full of unicorns and rainbows I would show you what other people are saying about this release.

Let's start with the Product Support Services (PSS) team at Microsoft.

SQL Server 2016 has a ton of new features as well as upgrades to existing features. The PSS team has put together a series of blog posts on the new features and capabilities in SQL Server 2016. You can find a <a href="https://sqlwithmanoj.com/2016/05/31/microsoft-pss-sql-2016-series-it-just-runs-faster-may-updates/" target="_blank" rel="noopener">summary page here</a>. I wanted to list out today the current set of links for everyone to see:
<ul>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/02/25/sql-2016-it-just-runs-faster-dbcc-scales-7x-better/" target="_blank" rel="noopener">SQL 2016 – It Just Runs Faster: DBCC Scales 7x Better</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/01/sql-2016-it-just-runs-faster-dbcc-extended-checks/" target="_blank" rel="noopener">SQL 2016 – It Just Runs Faster: DBCC Extended Checks</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/03/sql-2016-it-just-runs-faster-native-spatial-implementations/" target="_blank" rel="nofollow noopener">SQL 2016 – It Just Runs Faster: Native Spatial Implementation(s)</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/04/sql-server-parallel-query-placement-decision-logic/" target="_blank" rel="nofollow noopener">SQL Server Parallel Query Placement Decision Logic</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/08/sql-2016-it-just-runs-faster-tvps-with-spatial-columns/" target="_blank" rel="nofollow noopener">SQL 2016 – It Just Runs Faster: TVPs with Spatial Column(s)</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/10/sql-2016-it-just-runs-faster-spatial-index-builds-faster/" rel="nofollow">SQL 2016 – It Just Runs Faster: Spatial Index Builds Faster</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/15/sql-2016-it-just-runs-faster-t1117-and-t1118-changes-for-tempdb-and-user-databases/" rel="nofollow">SQL 2016 – It Just Runs Faster: -T1117 and -T1118 changes for TEMPDB and user databases</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/17/sql-2016-it-just-runs-faster-automatic-tempdb-configuration/" rel="nofollow">SQL 2016 – It Just Runs Faster: Automatic TEMPDB Configuration</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/22/sql-2016-it-just-runs-faster-ldf-stamped/" rel="nofollow">SQL 2016 – It Just Runs Faster: LDF Stamped</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/25/sql-2016-it-just-runs-faster-instant-file-initialization/" rel="nofollow">SQL 2016 – It Just Runs Faster: Instant File Initialization</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/03/30/sql-2016-it-just-runs-faster-automatic-soft-numa/" rel="nofollow">SQL 2016 – It Just Runs Faster: Automatic Soft NUMA</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/01/sql-2016-it-just-runs-faster-updated-scheduling-algorithms/" rel="nofollow">SQL 2016 – It Just Runs Faster: Updated Scheduling Algorithms</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/06/sql-2016-it-just-runs-faster-dynamic-memory-object-cmemthread-partitioning/" rel="nofollow">SQL 2016 – It Just Runs Faster: Dynamic Memory Object (CMemThread) Partitioning</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/07/sql-2016-it-just-runs-faster-sos_rwlock-redesign/" rel="nofollow">SQL 2016 – It Just Runs Faster: SOS_RWLock Redesign</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/12/sql-2016-it-just-runs-faster-indirect-checkpoint-default/" rel="nofollow">SQL 2016 – It Just Runs Faster: Indirect Checkpoint Default</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/15/sql-2016-it-just-runs-faster-larger-data-file-writes/" rel="nofollow">SQL 2016 – It Just Runs Faster: Larger Data File Writes</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/19/sql-2016-it-just-runs-faster-multiple-log-writer-workers/" rel="nofollow">SQL 2016 – It Just Runs Faster: Multiple Log Writer Workers</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/22/sql-2016-it-just-runs-faster-column-store-uses-vector-instructions-sseavx/" rel="nofollow">SQL 2016 – It Just Runs Faster: Column Store Uses Vector Instructions (SSE/AVX)</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/27/sql-2016-it-just-runs-faster-bulk-insert-uses-vector-instructions-sseavx/" rel="nofollow">SQL 2016 – It Just Runs Faster – BULK INSERT Uses Vector Instructions (SSE/AVX)</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/04/28/sql-2016-it-just-runs-faster-alwayson-log-transport-reduced-context-switches/" rel="nofollow">SQL 2016 – It Just Runs Faster: AlwaysOn Log Transport Reduced Context Switches</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/05/03/sql-2016-it-just-runs-faster-alwayson-parallel-compression-improved-algorithms/" rel="nofollow">SQL 2016 – It Just Runs Faster: AlwaysOn Parallel Compression / Improved Algorithms</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/05/05/sql-2016-it-just-runs-faster-alwayson-aes-ni-encryption/" rel="nofollow">SQL 2016 – It Just Runs Faster – AlwaysOn AES-NI Encryption</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/05/10/sql-2016-it-just-runs-faster-in-memory-optimized-database-worker-pool/" rel="nofollow">SQL 2016 – It Just Runs Faster: In-Memory Optimized Database Worker Pool</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/05/12/sql-2016-leverages-on-demand-msdtc-startup/" rel="nofollow">SQL 2016 – Leverages On Demand MSDTC Startup</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/psssql/2016/05/18/sql-2016-it-just-runs-faster-xevent-linq-reader/" rel="nofollow">SQL 2016 – It Just Runs Faster: XEvent Linq Reader</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/sqlserverstorageengine/2016/09/26/sql-server-2016-it-just-runs-faster-always-on-availability-groups-turbocharged/" target="_blank" rel="noopener">SQL 2016 – It Just Runs Faster: Always On Availability Groups Turbocharged</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/bobsql/2016/11/08/how-it-works-it-just-runs-faster-non-volatile-memory-sql-server-tail-of-log-caching-on-nvdimm/" target="_blank" rel="noopener">Non-Volatile Memory SQL Server Tail Of Log Caching on NVDIMM</a></li>
 	<li><a href="https://blogs.msdn.microsoft.com/bobsql/2016/11/29/how-it-works-it-just-runs-faster-auto-soft-numa/" target="_blank" rel="noopener">How It Works (It Just Runs Faster): Auto Soft NUMA</a></li>
</ul>
&nbsp;

That's not even the full list of new features, either. But I know what you are thinking. You are thinking that I've just provided a bunch of links from an internal team at Microsoft so of course they would say wonderful things about SQL Server 2016. https://blogs.msdn.microsoft.com/bobsql/2016/11/08/how-it-works-it-just-runs-faster-non-volatile-memory-sql-server-tail-of-log-caching-on-nvdimm/

Okay then, how about this slide I was shown during the SQL Server 2016 reviewer's workshop a few weeks back showing some performance benchmarks:

<a href="https://thomaslarock.com/wp-content/uploads/2016/05/SQL-Reviewers-2016-Raghu-keynote.jpg"><img class="aligncenter size-medium wp-image-17386" src="https://thomaslarock.com/wp-content/uploads/2016/05/SQL-Reviewers-2016-Raghu-keynote-560x315.jpg" alt="SQL Server Record Breaking Performance" width="560" height="315" /></a>

Not bad, huh? But I know what you are thinking. You are thinking that's just a marketing slide showing testing results with third party Microsoft partners so of course they would say wonderful things about SQL Server 2016.

Okay then, how about this image showing a handful of <a href="https://news.microsoft.com/analyst-reports/#sm.001h8mco51dzkcwhpkh1fwebvjzqb" target="_blank" rel="noopener">Gartner reports</a>:

<a href="https://thomaslarock.com/wp-content/uploads/2016/05/gartner.jpg"><img class="aligncenter size-medium wp-image-17388" src="https://thomaslarock.com/wp-content/uploads/2016/05/gartner-560x315.jpg" alt="Gartner shows Microsoft as a leader" width="560" height="315" /></a>

Not bad, huh? If you still don't believe that SQL Server 2016 is full of unicorns and rainbows then I would encourage you to try it for yourself. You can be up and running with an <a href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-portal-sql-server-provision/" target="_blank" rel="noopener">Azure VM in less than 15 minutes</a>. Don't want to try Azure? Okay then, why not <a href="https://blogs.technet.microsoft.com/dataplatforminsider/2016/03/31/microsoft-sql-server-developer-edition-is-now-free/" target="_blank" rel="noopener">download to developer edition of SQL Server for free</a>. That's right, it's free. It costs you NOTHING to test drive SQL Server these days.

Last year during my keynote speech at the PASS Summit in Seattle I stated that Microsoft was "the makers of the best data platform, bar none, on the planet."

I meant it then, and I mean it now.

Performance benchmark testing backs up that statement. Gartner agrees as well. I am certain that if you gave it a try, you would understand why.