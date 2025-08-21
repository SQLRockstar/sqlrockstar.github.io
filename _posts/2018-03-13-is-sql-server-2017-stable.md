---
layout: post
title: Is SQL Server 2017 Stable?
date: '2018-03-13 14:06:38 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server 2017
- SQL Server Performance
tags:
- microsoft
- sql server
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/sql-2017-ludicrous.gif"><img class="aligncenter size-full wp-image-18764" src="https://thomaslarock.com/wp-content/uploads/2018/03/sql-2017-ludicrous.gif" alt="is sql server 2017 stable" width="375" height="198" /></a>

There I was, talking about upgrading to SQL Server 2017 at SQL Konferenz last month. Despite the title of the talk, I was not expecting such a question. But there it was: "Is SQL Server 2017 stable enough to use?"

I stopped. I wanted to laugh. And scream. And cry. I know there are no silly questions, but this one was close. I collected my thoughts and asked for clarification.

"Are you asking because Microsoft stopped deploying service packs for SQL Server?"

"Yes, that's what I want to hear you talk about."

I thought this to be the real reason for the question. I was already short on time but decided that this was worth a two-minute sermon. I also decided that it was worth blogging about. I suspect others have similar questions about SQL Server 2017 and instead of waiting for them to find me I'm going to share my thoughts here.

&nbsp;
<h2>A Brief History of Azure SQL Database</h2>
The first part of my answer focused on Azure SQL Database. I had two points to make. First, was that for a period of time in 2016, the code base for SQL Database and SQL Server were identical. Since that time, SQL Database has been slightly ahead on features. You can see this today with items like the data classification feature that was in SQL Database before being added to SSMS 17.5 later.

The second part is related to the first. Azure is a huge sandbox for Microsoft to use to test new features. By the time a feature arrives in SQL Server it has been tested against millions of workloads. This has been the case for many years now. Microsoft has talked about features being "cloud-first, but not cloud-only". That meant they deployed features to Azure as part of their test-driven development methods. In short, customers need not worry about the stability of a feature in SQL Server 2017.

&nbsp;
<h2>The Modern Servicing Model</h2>
The second part of my answer focused on the <a href="https://blogs.msdn.microsoft.com/sqlreleaseservices/announcing-the-modern-servicing-model-for-sql-server/" target="_blank" rel="noopener">new service model announced by Microsoft last year</a>. Starting with SQL Server 2017, Microsoft will no longer make service packs available. Historically, customers would wait for SP1 of a product before they would consider it "stable". The thought was that SP1 would include all the bug fixes found since the RTM version and thus would be more reliable. However, that is an antiquated way of thinking in the DevOps world of Continuous Integration and Continuous Delivery. In that world, you don't wait for a service pack. Your builds are stable and only need minor fixes.

Starting with SQL Server 2017, Microsoft will release cumulative updates (CUs) and general distribution release (GDRs) as needed. CUs will be delivered once a month for 12 months, and then once a quarter for the next 4 years. That means you will have a total of 28 CUs delivered during the five-year support lifecycle.

What this means is that you should not think of SQL Server 2017 as some piece of brand new technology. Instead, you should think of it as SQL Server 2016 with a bunch of CUs and a handful of new features, all of which has been thoroughly tested against millions of workloads.

&nbsp;
<h2>Summary</h2>
Yes, SQL Server 2017 is stable.

But don't take my word for it, go try it for yourself. <a href="https://www.microsoft.com/en-us/sql-server/sql-server-downloads" target="_blank" rel="noopener">SQL Server 2017 Developer edition is free</a>. Install and see for yourself it is stable enough for your needs.