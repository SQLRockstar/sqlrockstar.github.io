---
layout: post
title: 8 Ways To Be Successful With Microsoft Azure SQL Database
date: '2016-08-04 08:05:25 +0000'
categories:
- Cloud Computing
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server Performance
tags:
- Azure
- database
- microsoft
- SQL
---

<a href="https://thomaslarock.com/wp-content/uploads/2014/03/cloud-copy.jpg"><img class="aligncenter wp-image-11279 size-full" src="https://thomaslarock.com/wp-content/uploads/2014/03/cloud-copy.jpg" alt="How To Be Successful With Microsoft Azure SQL Database" width="425" height="283" /></a>

I've been working with Microsoft Azure SQL Database on and off for more than six years now. Over that time a mistake I continue to see with Microsoft Azure SQL Database deployments is how users don't think of it as a distinct platform from SQL Server. They view Microsoft Azure SQL Database as any other instance (or version) of SQL Server.

When I hear stories about failing to migrate to Microsoft Azure SQL Database with a brute-force-single-click, I will ask follow up questions. I have found a common pattern in the answers: lack of strategy.

I've compiled here a list of strategies that you want to consider when moving to Microsoft Azure SQL Database. <span style="line-height: 1.5;">Failure to plan is the same as planning to fail, and this list is going to keep your Microsoft Azure SQL Database</span><span style="line-height: 1.5;"> projects moving forward. </span>
<h2>1. Build Your Disaster Recovery Plan First</h2>
I am amazed at how contentious this topic is for administrators looking at Microsoft Azure SQL Database. The idea that there is no native BACKUP command is a conversation stopper. It's not difficult to get a transaction-consistent copy of your data, it just requires a different method than the Earthed version of SQL Server.

Part of the reason for this is because Microsoft Azure SQL Database is a more advanced version of SQL Server. And, as any SQL Server expert will tell you, restoring backups to earlier versions is not allowed. You need to resort to <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-cloud-migrate/" target="_blank">using BCP methods and tools like Visual Studio</a> in order to get the job done. It's not hard to get done, it's just different.

You currently manage your own disaster recovery plans for SQL Server right now (I hope), so the idea that you need to do the same for Microsoft Azure SQL Database should not come as a surprise. Fortunately, this is built in to Azure itself. You can <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-business-continuity/" target="_blank">check out all the wonderful details about how Microsoft has implemented business continuity planning into Azure SQL Database.</a>

You need to understand your own data story, workloads, and recovery point objectives (RPO) and recovery time objectives (RTO). Microsoft Azure SQL Database is designed to fit a set of data stories. Make sure your story is a match.

With the continuing advances being implemented inside of Microsoft Azure SQL Database the traditional backup/restore methods will soon be obsolete.
<h2>2. Plan For Adequate Resources</h2>
Microsoft Azure SQL Database offers <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-service-tiers/" target="_blank">many different tiers of service</a>. You should know that Azure also <a href="https://azure.microsoft.com/en-us/services/sql-data-warehouse/" target="_blank">offers SQL Data Warehouse</a>, in case you need something other than a traditional OLTP relational engine. In either case you need to have an understanding of your performance expectations compared to the performance reality offered by the various service tiers.

If you believe that you can spin up a low-level service tier Microsoft Azure SQL Database and get the same performance as an Earthed version of SQL Server, then you are in for a surprise.
<h2>3. Testing Your Tools</h2>
You already have a core set of tools in your shop. Do you know if they will work effectively against a Microsoft Azure SQL Database datasource? I've seen customers and clients make the mistake of assuming that their existing tools will work (or that they won't work at all).

Take the time to see which tools will work, which ones you need, and how much budget you have for tools, people, or both.
<h2>4. Breaking Changes</h2>
I've already mentioned that Microsoft Azure SQL Database is a different platform than Earthed versions of SQL Server. If you are looking to use Microsoft Azure SQL Database and expecting it to behave in the exact same way as the on-premises version then you will have a sad face. I'm always surprised to hear of a client or customer tell me "we were expecting [feature] to work, but it doesn't". On the flip side, Microsoft Azure SQL Database often has wonderful features that don't exist in the on-premises version of SQL Server (yet).

Microsoft <a href="http://msdn.microsoft.com/en-us/library/windowsazure/ff394115.aspx" target="_blank">publishes a list of supported features</a>. Do not assume that your existing code (or schema) will port to Microsoft Azure SQL Database without any issues. In some cases you will need to make changes to existing code and schemas in order to get a solution deployed. Visual Studio does a wonderful job of helping you to take an existing on-premises database and getting it deployed to Microsoft Azure SQL Database, I gave an example of this during SQL Saturday Austin earlier this year.

If you fail to spend the time researching adequately then you will end up as one of those who tried moving to Microsoft Azure SQL Database and ended up moving back.
<h2>5. Try It Again</h2>
Many years ago applications were designed in such a way that they did not assume they would always stay connected to their data source. Roughly 20 years ago or so a new breed of applications were being built that took an opposite approach: they assumed they would always stay connected. When you go to the Cloud, however, you cannot assume you will always stay connected.

One of the strengths of Microsoft Azure SQL Database is the high availability you are given. This HA architecture means that at some point you will lose your connection, likely as a result of a failover. For that reason I tell all my customers and clients that they must have retry logic built into their applications. It's like stepping back in time, really, to when it was a best practice to have retry logic in our apps. Those days are coming around again as people understand that there is a tradeoff for having a platform focused on HA technology.
<h2>6. Troubleshooting Errors</h2>
One area where you will need to learn some new skills is troubleshooting. As a DBA you already have some basic troubleshooting skills. All you need to port those skills to Microsoft Azure SQL Database is to know where to look for signs of trouble. Conversely, if you are the type of person that <a href="https://thomaslarock.com/2013/03/administering-sql-server-running-on-server-core/" target="_blank">screams in terror at the thought of using Server Core</a> then Microsoft Azure SQL Database is probably not your slice of cheese.

The first thing I do to help others understand how to troubleshoot issues with Microsoft Azure SQL Database is to understand the differences between basic connectivity errors and basic Microsoft Azure SQL Database errors. Being able to lump issues into one of those two buckets at the start really saves time. Microsoft Azure SQL Database <a href="http://msdn.microsoft.com/en-us/library/windowsazure/ee336238.aspx" target="_blank">also offers a handful of DMOs</a> that help you find additional details about the issues and possible root causes. You will find yourself spending a lot of time looking in the <a href="https://msdn.microsoft.com/en-us/library/dn270018.aspx" target="_blank">sys.event_log</a> and <a href="https://msdn.microsoft.com/en-us/library/dn269986.aspx" target="_blank">sys.database_connection_stats</a> views. You can also check this link to see if any of the Azure datacenters are experiencing issues by <a title="Windows Azure Status" href="http://www.windowsazure.com/en-us/support/service-dashboard/" target="_blank">visiting the Azure Service Dashboard</a>.
<h2>7. Tuning For Performance</h2>
I often hear people bemoan the fact that much of Microsoft Azure SQL Database is not in their control. They can't touch the hardware, they can't use tools like Profiler to diagnose issues, and they can't adjust any server configuration settings. At first I found myself agreeing with them until two thoughts came to mind.

First, not being able to control everything is a liberating feeling. Just knowing that so many options are off the table makes my job easier when diagnosing performance issues. It is true that the number of "nerd knobs" at my disposal is lower than I am used to having, but that means I get to spend time on things that have real impact such as application code.

And that is important because of the second reason: <em><strong>the number one reason for all performance problems in the history of databases is due to application code</strong></em>. Think about it. Your database server was running fine until you created the database and connected your applications!

Whenever I see folks having to touch hardware in order to help scale performance it is often because they aren't allowed to touch code (thanks SharePoint!). Well, with Microsoft Azure SQL Database, code is the one thing you <em>can</em> touch. It is often the root cause of the problem anyway!

Great database performance starts with great database design. If you are moving to Microsoft Azure SQL Database then now is the time to focus on the database design and application code. Tools such as <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-query-performance/" target="_blank">Database Query Performance Insight</a> and <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-advisor/" target="_blank">SQL Database Advisor</a> make this easier to understand for non-DBAs.

The way this is trending, the role of traditional DBAs and database consultants brought in for performance tuning will change, and fast.
<h2>8. Understanding Your Bill</h2>
You need to <a href="http://www.windowsazure.com/en-us/support/understand-your-bill/" target="_blank">understand what you will (and will not) be charged for when using Microsoft Azure SQL Database</a>. This is essential as you look to include things such as capacity planning and volumetrics. You need to design with billing in mind, otherwise you run the risk of deploying a solution that costs way more than you anticipated.

Those are the strategies I have seen users fail to include when moving to Microsoft Azure SQL Database. Any one of them alone is enough of a pain point for someone to decide not to consider Microsoft Azure SQL Database. Combine a few of them together and it is easy to understand why Microsoft Azure SQL Database may not be on the table as a viable option for some projects.

Make the time to address each of those strategies and you will find yourself set up for a chance at success when using Microsoft Azure SQL Database.