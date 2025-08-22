---
layout: post
title: What Does a DBA Do All Day?
date: '2017-02-14 03:26:46 +0000'
categories:
- MSSQL
- Professional Development
- SQL MVP
- SQL Server Performance
tags:
- automation
- Azure
- DBA
---

What does a DBA do all day?

It is clear to me that no one, except for database administrators, has any idea:
<blockquote class="twitter-tweet" data-lang="en">
<p dir="ltr" lang="en">What do DBAs do</p>
— SwiftOnSecurity (@SwiftOnSecurity) <a href="https://twitter.com/SwiftOnSecurity/status/723274377651871745">April 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I've read many articles <a href="http://www.techrepublic.com/article/just-what-does-a-dba-do-all-day/" target="_blank">over the years</a> that help people understand tasks involved for the DBA role. I've <a href="https://thwack.solarwinds.com/community/solarwinds-community/geek-speak_tht/blog/2017/01/05/accidental-dba-the-first-100-days" target="_blank">written a few myself</a>, including <a href="http://amzn.to/2lH1MFA" target="_blank">a book</a> I have mentioned once or twice before here.

Today I want to help everyone understand what a DBA does all day long. I have put together a summary of the tasks that I find are common for the DBA role. This is a partial list of the items that came to my mind right away. No, not every DBA will be doing all these tasks but chances are they will do one or more:

<strong>Recovery</strong> - If you can't recover data, you can't keep your job. This is the number one task for any DBA.
<strong>Backups</strong> - Having backups makes your ability to recover a bit easier.
<strong>Performance</strong> - Performance tuning and optimization of queries that we didn't write, against databases we didn't design. DBAs get paid for performance but we keep our jobs with recovery. (see above)
<strong>Standards</strong> - Working with other teams to agree upon a set of database standards for your shop.
<strong>Risk</strong> - Assessing risk, working with auditors, outlining security and access control.
<strong>Installation</strong> - Installing database software on servers.
<strong>Configuration</strong> - Configuration of database servers.
<strong>Monitoring</strong> - Monitoring database servers for performance, including maintenance for things like indexes, corruption, etc.
<strong>Capacity</strong> - Helping to plan for future growth.
<strong>Troubleshooting</strong> - Being able to respond to issues and locate the root cause quickly.
<strong>HA/DR</strong> - Help architect an effective business continuity plan.
<strong>ETL</strong> - Integration and migration of data between systems.
<strong>Development</strong> - Writing stored procedures, designing tables.

That's quite a list! It looks like one of <a href="https://thomaslarock.com/2010/09/a-better-dba-job-description-for-everyone/" target="_blank">those horrible job postings I've ranted about before</a>. But the list does help frame the DBA role for others to understand.
<h2>Vertical vs. Horizontal Role</h2>
The above list helps others to understand why the DBA role is as a <strong>vertical role</strong>. These roles have a focus on the immediate tasks completed by a single person on a daily/weekly/monthly basis. This is why you hear the phrase "the best DBA is never seen nor heard". If a DBA is doing their job well then the number of issues are minimal. And so they don't need to leave their cube except for nourishment and some limited human contact.

To have less people questioning what we do all day long we need to transform the DBA role into a <strong>horizontal role</strong>. A horizontal role is one that thinks about, and includes, other teams. With the DBA role so focused on data, and data the most critical asset any company owns, it makes sense for the DBA to work across teams and not alone. DBAs must make certain that data is being treated right as it flows in, around, and out.
<h2>Automation is Key</h2>
With so many tasks to manage, and only so many hours in the day, DBAs turn to automation to get the job done. Sure, it would be great to hire additional staff to offload the work. But headcount is harder to come by than a few PowerShell scripts. Automation is key to transforming the DBA role from vertical to horizontal.

You know who does automation well these days? Cloud providers, that's who. Check out this list of services from <a href="https://azure.microsoft.com/en-us/" target="_blank">Azure</a>:

<strong>Recovery</strong> - <a href="https://azure.microsoft.com/en-us/blog/azure-sql-database-point-in-time-restore/" target="_blank">Point-in-time restore</a>
<strong>Backups</strong> - <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-automated-backups" target="_blank">Automated backups</a>
<strong>Performance</strong> - <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-query-performance" target="_blank">Query Performance Insight</a>
<strong>Standards</strong> - <a href="https://azure.microsoft.com/en-us/services/sql-database/?b=16.50" target="_blank">Managed services</a>
<strong>Risk</strong> - <a href="https://winbuzzer.com/2017/02/11/microsoft-azure-sql-database-threat-detection-launching-april-2017-xcxwbn/" target="_blank">Threat detection</a>
<strong>Installation</strong> - Did I mention the <a href="https://azure.microsoft.com/en-us/services/sql-database/?b=16.50" target="_blank">managed services</a> yet?
<strong>Configuration</strong> - OK, now I know I have mentioned <a href="https://azure.microsoft.com/en-us/services/sql-database/?b=16.50" target="_blank">managed services</a>
<strong>Monitoring</strong> - <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-advisor" target="_blank">Database advisor</a>
<strong>Capacity</strong> - Seriously folks, its a <a href="https://azure.microsoft.com/en-us/services/sql-database/?b=16.50" target="_blank">managed service</a>
<strong>Troubleshooting</strong> - <a href="https://docs.microsoft.com/en-us/azure/application-insights/app-insights-detect-triage-diagnose" target="_blank">Application Performance Insight</a>
<strong>HA/DR</strong> - <a href="https://azure.microsoft.com/en-us/services/site-recovery/" target="_blank">Disaster Recovery Service</a>
<strong>ETL</strong> - <a href="https://azure.microsoft.com/en-us/solutions/hybrid-integration/" target="_blank">Hybrid integration</a>
<strong>Development</strong> - <a href="https://msdn.microsoft.com/en-us/library/jj556244(v=vs.113).aspx" target="_blank">Entity Framework</a>

You can <a href="https://aws.amazon.com/products/?nc2=h_ql_ny_livestream_blu" target="_blank">find similar tools deployed by Amazon AWS</a>. That's right, the top two cloud providers are automating away the core DBA tasks. This is happening, right in front of our eyes, whether you want to believe in Cloud or not.

The days of tuning queries and rebuilding indexes is ending, one page at a time.
<h2>What Will a DBA Do All Day?</h2>
So if all the common core tasks are being automated away, what will the future DBA be doing?

The answer is simple: It's all about the data. It's always been about the data.

The future of the DBA is in building solutions, not tables and indexes. It's in understanding how data is being used, not in how data is stored. The future is analyzing data, not in how it is administered.

The future view must also be a horizontal view, one that applies the logic and analytical skills that DBAs already possess, across teams.

Because the DBA that works in a silo, in a vertical role, with a only a vertical view, won't be around much longer.