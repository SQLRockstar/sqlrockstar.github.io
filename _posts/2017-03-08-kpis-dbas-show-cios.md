---
layout: post
title: KPIs For DBAs to Show Their CIOs
date: '2017-03-08 11:54:53 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- KPI
- Professional Development
- SQL
---

Last week I found this question about KPIs on #sqlhelp
<blockquote class="twitter-tweet" data-lang="en">
<p dir="ltr" lang="en">Anyone have any good KPI's for DBA's? Our director wants us to come up with some Key Performance Indicators. Any articles? <a href="https://twitter.com/hashtag/sqlhelp?src=hash">#sqlhelp</a></p>
— SS7 (@sqlsurfer7) <a href="https://twitter.com/sqlsurfer7/status/836587874933948416">February 28, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

It's a great question, and there is no right answer here. I made an effort to help narrow the focus by asking for more details. Soon I realized that there was no way this was going to get solved on Twitter, and that a blog post might help. So that's what I am doing today. You're welcome.

First, let's make sure everyone understands that KPIs is an acronym for <a href="http://searchcrm.techtarget.com/definition/key-performance-indicator" target="_blank">Key Performance Indicators</a>. KPIs are metrics that help support defined goals and targets. While the specific KPIs will change from one shop to another, KPIs in general share some common characteristics:

- They reflect strategic value drivers
- Are based on valid data
- Must be easy to comprehend
- Are always relevant
- Provide context
- Empower users
- Lead to positive action

And lastly, while KPIs are metrics, not all metrics are KPIs.

Often the KPI goals and targets are set by the business. But not always. It is perfectly valid for a DBA (or their manager) to assign KPIs to the servers and databases they administer. KPIs are unique for every shop, and for every role. There is no one set of KPIs that will work universally for all DBAs. What I want to do today is share with you some possible KPI metrics that you may consider including.

A couple of things to note before we get started. First, whatever KPIs you choose should support goals and targets for your manager. And your manager has goals and targets to support their manager. And upwards it goes until you get to the CEO, who also reports to the Board of Directors. So choose wisely, you want to make sure your efforts to collect and report on these KPIs have value to others.

Second, these KPIs aren't always for things you are responsible for, but things you are expected to report upon. For example, you may not be in charge of storage, but you are likely to report the amount of disk space available. The reality is that as a DBA there are a lot of things you are responsible for that you can't control (hello Sharepoint! *waves*)

Here's my list. Let me know if there is something I've missed and I will add it to the list.
<h2>Uptime</h2>
This metric floats to the top of the list for most IT administrators. And it makes sense that you would report on the servers, applications, and the data as having a high percentage of uptime. I have two issues with using uptime as a metric. First is that <a href="http://windowsitpro.com/windows/microsoft-and-google-war-nines" target="_blank">no one can agree what uptime means</a>. Oh, sure, we can just say that the system is available implies it is "up". But if I need to kick users off for six hours on a Sunday in order to do maintenance, is that really uptime? Well, the server isn't down, so it must be up, right? Wrong. That's why I advocate using these distinct time metrics: uptime, downtime, and maintenance.

The second issue I have is when people take credit for uptime despite not having any part in keeping the server available. I consider uptime as a KPI to be applicable only when you have personally configured high availability (HA) options. But as a KPI for a standalone server, it may not. Why? Well, since Microsoft is the one that wrote the O/S, and they wrote SQL Server, they might deserve a tad bit more credit about the platforms being stable to the point that it doesn't need to be rebooted frequently. I won't tell you to not use uptime as a metric, but I am going to tell you that if you are using uptime then you need to provide more context about the activities you do that directly affect uptime.
<h2>Backups</h2>
The <a href="https://thomaslarock.com/2017/02/what-does-a-dba-do-all-day/" target="_blank">number one priority for any DBA is recovery</a>. And you can't recover without backups. You should be reporting on the number of databases (system and user) that have current backups, where 'current' is applicable to your business requirements. You should also report that these backups have been archived to tape. Oh, and it wouldn't hurt to report if the server itself has been backed up to tape. And yes, I think it is weird that I am talking about tape in the year 2017 but as a DBA I believe in the <a href="https://www.hanselman.com/blog/TheComputerBackupRuleOfThree.aspx" target="_blank">Computer Backup Rule of Three</a>.
<h2>Restores</h2>
Because backups are worthless unless they can be restored, you should report on the success you have restoring random backups. If you don't know what I'm talking about, go read my <a href="https://www.simple-talk.com/sql/database-administration/statistical-sampling-for-verifying-database-backups/" target="_blank">post about using statistical sampling</a> methods to help verify your backups are successful.
<h2>Availability</h2>
Similar to uptime, but also with an idea of recovery, is a KPI for 'availability'. This would be a measure of the data being available when needed. So, you could have 99.999% uptime but your end users may need to wait for you to restore production to test one day to debug an issue. How long will they wait? That's the number you want to report on, the amount of time your business end users are waiting for the data they need to become available. This could apply to a lot of things, too, such as ETL loads, or FTPing files. For example, let's say your business needs to recover data from last week, and you have to recall a tape from cold storage. The process could take a day or two, then the restore time. You should track this number.
<h2>Maintenance</h2>
You should be performing maintenance on your databases on a regular basis, and thus report on the success of these jobs over time. Chances are your boss, and their boss, have no idea about these jobs. You should raise awareness about activities such as these, as they perform a valuable service to help the business meet their goals (and I bet your bosses would like to report this KPI up the chain, too).
<h2>Failed jobs</h2>
Another standard for most DBA KPI dashboards is reporting on the number of failed jobs for the day/week/month. I would also include the total number of jobs being executed, in order to give some perspective on the volume of work being administered. And while we are discussing this, you might want to break the jobs down into individual job steps and report on those, too.
<h2>Capacity Planning</h2>
Capacity planning is about as much fun as a root canal, except the root canal allows you the opportunity to be unconscious while it happens. I used to get asked for capacity forecasts every quarter and they were never right. Why? Because someone would decide to fill up a database drive with 100GB of XML documents, or they would load 500GB of data into a database, or decide to reorder the columns on a table and fill up a 140GB transaction log drive. The point is that you can forecast all you want but you never know what the end users are going to do next. At the end of the month you compare your estimate to reality and wonder "how come we were so far off?" Users, that's how come.

Still, there are ways for you to get some info from your databases in order to make an educated guess. And you can have some fun with this, too. For example, you could calculate the amount of space needed should each data file have 3 (or more) growth events in the next month and report some huge number as a high-end estimate. Just focus on the trend over time and you'll find out who the data hoarders are in your shop (HINT: It's everyone). At some point, the volume of data will hit a point where failovers may become more trouble than you were expecting, so you want to capture this metric. <a href="http://www.edwinmsarmiento.com/how-to-forecast-database-disk-capacity-if-you-dont-have-a-monitoring-tool/" target="_blank">Here's one way to get that done</a>.
<h2>Number of Servers and Databases</h2>
This was a metric I was asked for frequently. And even though I could never understand the value, I suspect my boss used it as a way to measure the workload. But I know some DBAs out there that are responsible for thousands of instances during their shift, so I felt silly reporting back that we had just a few hundred servers and a few thousand databases. But this is a decent metric to track over time, and it can help you build a case for additional headcount when the time comes.
<h2>Resource consumption</h2>
Another possible KPI would be to report on the resources (CPU, memory, disk, network) consumed by servers and/or databases over time. You could even report on the amount of locking/blocking/deadlocking happening. Conventional wisdom says that you want the resources consumed to be as low as possible, but those of us that have been running virtual database servers for more than 10 years now will tell you that having a host at more than 80% CPU isn't necessarily a bad thing anymore. Oh, and this is where you can report on wait stats, too. Might be interesting to know what the largest waits are for your database servers.
<h2>Query Performance</h2>
If you are going to report on resource consumption then you will want to break it down into specific queries. I'd suggest limiting it to the top 3 or 5 for each wait or resource. But it would also benefit to focus on the queries that have been identified as mission critical, even if they aren't at the top of the list.
<h2>Responsiveness</h2>
If you have a ticketing system then you should report on the number of tickets created and time to resolution. Your goal should be to have a minimal number of tickets created. If the number of tickets, or the time to resolution, show an increase, you could use this KPI combined with the number of servers and databases KPI to justify headcount. You could also include "time to troubleshoot" as a KPI here, by tracking the number of hours spent resolving performance issues and outages.
<h2>Configurations</h2>
OK, let's assume that we have an idea of the number of servers and databases that we are managing. What you want to know next is how many of those servers are in a <a href="https://blogs.msdn.microsoft.com/troy_aults_blog/2015/08/31/desired-state-configurationdsc-for-sql-server/" target="_blank">desired state configuration</a>, and how many are not. And, for those that are not, understanding why not. Tools such as <a href="https://sqlpowerdoc.codeplex.com/" target="_blank">SQL Power Doc</a> are a great way to document the configuration of your database servers and instances.
<h2>Security or Risk Assessment</h2>
As someone who takes data privacy and security seriously, I am a big fan of having a KPI dedicated to security. I'd report on the number of servers that don't have the 'sa' account disabled, or databases that have code that could be open to SQL injection attacks, or a server that isn't enforcing a password policy for SQL logins. You could even report on the number of servers that have not gone through penetration testing in the past 6 or 12 months. Even reporting on the number of critical events in the Windows Security log would be better than nothing.

That's my list of KPIs For DBAs to Show Their CIOs. It is not meant to be an exhaustive list, but a guide to help you get started. As I stated earlier, your list is going to be unique for your shop. Your business, your infrastructure architecture, and even your manager will influence your KPIs. If you have a KPI that you believe should be included, please share.