---
layout: post
title: Microsoft Azure Threat Detection Types
date: '2018-01-11 15:13:34 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL Azure
- SQL MVP
tags:
- Audit
- Azure
- microsoft
- security
- threat detection
---

Not enough people know about the Audit and Threat Detection feature in Microsoft Azure. So, I'm hoping to help spread the word today. I decided to write a post to help explain the Microsoft Azure Threat Detection types.

First, you should know that it is crazy simple to enable Audit and Threat Detection for your Azure SQL Database. All you need to do is navigate to your Azure SQL instance, locate 'Auditing &amp; Threat Detection" in the left column, enable the features, point to a storage account, add an email address, and click 'Save'. That's it, you are done.

&nbsp;

<img class="aligncenter size-large wp-image-18542" src="https://thomaslarock.com/wp-content/uploads/2018/01/enable_audit_threat_detection-600x369.jpg" alt="Enable audit and threat detection for azure" width="600" height="369" />

&nbsp;

If you hate GUIs but love security, then you are in luck because you can <a href="https://docs.microsoft.com/en-us/azure/sql-database/scripts/sql-database-auditing-and-threat-detection-powershell" target="_blank" rel="noopener">enable the feature using Powershell</a>, if desired. If you click on the 'Threat Detection Types' you will see a blade and the following options:

&nbsp;

<img class="aligncenter size-full wp-image-18537" src="https://thomaslarock.com/wp-content/uploads/2018/01/azure-threat-detection-types.jpg" alt="Azure Threat Detection Types" width="329" height="209" />

&nbsp;

There are no descriptions for any of these threat types. <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-threat-detection" target="_blank" rel="noopener">Here is the documentation for the feature</a>, they don't mention these types there, either. That's why I'm writing this post, so that you can understand more about those types.
<h2>Azure Threat Detection: Anomalous Client Login</h2>
The Audit and Threat Detection service will detect unusual and high-risk access activities. This detection is based upon behavioral analytics and anomaly detection. Here are some examples:

- If someone has logged in from an unusual location (so, a change in the access pattern)
- If a new user has logged in for the first time (so, a change in the access patterns of database principals)
- The attempt to brute force credentials (Say, a high number of failed logins with different credentials)
- A potentially harmful application was used to access the database

Here's what an anomalous login alert could look like:

&nbsp;

<img class="aligncenter size-large wp-image-18547" src="https://thomaslarock.com/wp-content/uploads/2018/01/audit_threat_detection_login_alert-378x600.jpg" alt="audit_threat_detection_anomalous_login" width="378" height="600" />

&nbsp;
<h2>Azure Threat Detection: SQL Injection Vulnerability</h2>
This threat detection type indicates that your application has generated a faulty SQL statement in the database. This is an indication that your application is vulnerable to a SQL injection attack. There are a few possible reasons for the generation of a faulty statement:

- There exists a defect in your application that is causing the faulty SQL statement
- User input is not being sanitized properly, resulting in a faulty SQL statement
- You are not using parameters in your dynamic SQL
- You are not using stored procedures

When the Threat Detection service sees this activity, it logs it as a vulnerability. The service will alert you, giving you a chance to investigate and remediate the issue before it is exploited. Think of SQL Injection Vulnerability as a warning signal, telling you in advance to fix the issue before it becomes a problem.
<h2></h2>
<h2>Azure Threat Detection: SQL Injection</h2>
This SQL Injection threat type is triggered when an active exploit is happening against an identified vulnerability. SQL injection attacks are often a random series of SQL statements in an effort to see what, if any, data can be returned. An attacker will start with a series of statements that will return pieces of information that they can then use to build upon their attack statements, ultimately resulting in a significant data breach. The Treat Detection service will alert you when the attack is happening. However, the service will avoid filling your inbox. It will only send so many emails per hour. So, if you get an email, you should act upon it quickly. Just because you didn't get an email for a few minutes doesn't mean the attack has stopped.

You can use the following demo application <a href="https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2FMicrosoft%2Fazure-sql-security-sample&amp;data=02%7C01%7Cgiladm%40microsoft.com%7C62d1a8ac8cd843041d2408d50ac4c581%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C636426762618096233&amp;sdata=91Ll7Zt5bLoTRm603It6Ztf1OSo5BNndAz%2FFbQTJOAs%3D&amp;reserved=0">https://github.com/Microsoft/azure-sql-security-sample</a> to simulate both alerts.

All of these alerts can be easily found in the <a href="https://azure.microsoft.com/en-us/services/security-center/" target="_blank" rel="noopener">Azure Security Center</a>. You can view threats detected against a database, instance, or even the subscription level.

&nbsp;
<h2>Summary</h2>
Take a moment and think how you are currently monitoring for SQL injection attacks. Chances are the answer is "we aren't". The Audit and Threat Detection feature in Microsoft Azure is worth the effort to migrate your workloads to Microsoft Azure.

Data security and privacy should be your top priority. Microsoft Azure is making it easy for you, all you have to do is enable the feature and input an email address.

It's that easy to help protect yourself against SQL injection attacks.