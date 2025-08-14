---
layout: page
title: "SQL Server Upgrades"
date: 2017-04-25 19:10:19 +0000
author: sqlrockstar
original_url: https://thomaslarock.com/sql-server-upgrades/
---
Ask a DBA about SQL Server upgrades and listen to the replies: "Upgrades are difficult." "Upgrades are painful." "Everything breaks." There is uncertainty with upgrading any database server. There are also painful memories. The truth is that the upgrade process itself is straightforward. It is easy for someone to install new software on new hardware and then restore backups. It is easy to understand why anyone would be cautious about upgrading a database server. Data, and databases, are the most critical asset any company owns. The secret to a successful upgrade is understanding the impact of early decisions. Small decisions at the start have major ramifications later. SQL Server upgrades can be either simple or complex. Simple upgrades are taking a database server and upgrading in some manner. Complex upgrades are best planned as any IT project. Complex upgrades include upgrading clusters, or multi-instance servers. But even simple SQL Server upgrades can be high-pressure situations with lots of moving parts that need execution in the correct order. Multiple business units are involved in each step of the process, adding to the complexity. As if that wasn’t enough pressure, at some point you will need to decide if you must rollback to the earlier version. If you do decide to rollback, you had better have a solid plan in place. Do not leave anything to chance. Don’t think of a rollback plan as a failure option. Think of your rollback plan as a way for your business users to be confident that if something goes wrong that the system(s) can be restored to an acceptable working condition. I've written a handful of posts over the years on the topic of upgrading SQL Server, so I decided to put together a page that contains links to all the posts. I am hopeful that you will find everything you need here for a successful SQL Server upgrade or migration project. 

## Upgrading to SQL Server 2016

[Upgrading to SQL Server 2016: Reasons for upgrading](https://thomaslarock.com/2017/04/upgrading-sql-server-2016-reasons-upgrading/) [Upgrading to SQL Server 2016: Pre-upgrade tasks](https://thomaslarock.com/2017/04/upgrading-sql-server-2016-pre-upgrade-tasks/) [Upgrading to SQL Server 2016: Upgrade tasks](https://thomaslarock.com/2017/04/upgrading-to-sql-server-2016-upgrade-tasks/) [Upgrading to SQL Server 2016: Post-upgrade tasks](https://thomaslarock.com/2017/04/upgrading-sql-server-2016-post-upgrade-tasks/) I've also written a whitepaper for SolarWinds that you can [download here](http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X), it contains all the information you need to get started with your upgrade project. Here are links to earlier posts I have written about upgrading SQL Server: 

## Upgrading to SQL Server 2014

[Upgrading to SQL Server 2014: A Dozen Things to Check](https://thomaslarock.com/2014/06/upgrading-to-sql-server-2014-a-dozen-things-to-check/)

## Upgrading to SQL Server 2012

[Upgrading to SQL Server 2012: Ten Things You Don't Want to Miss](https://thomaslarock.com/2013/03/upgrading-to-sql-2012-ten-things-you-dont-want-to-miss/)

## External References for Upgrading SQL Server

Microsoft has plenty of documentation for you, check out the MSDN article '[Upgrade SQL Server](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server)' to get started. The [DBAtools.io](https://dbatools.io/) project will help with migrating databases and server objects. The [SQL Power Doc on CodePlex](https://sqlpowerdoc.codeplex.com/) can help you gather inventory details. You can use [Performance Analysis of Logs (PAL)](https://pal.codeplex.com/) to gather baseline metrics before and after the upgrade process is complete. Don't forget that you can also [download and read the upgrade whitepaper](http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X) I wrote for SolarWinds. I hope you find the information on this page useful.