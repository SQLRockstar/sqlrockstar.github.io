---
layout: post
title: 'HOW TO: Solve General SQL Server Connectivity Issues'
date: '2017-03-02 19:49:43 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- connections
- Error
- sql server
---

<a href="https://thomaslarock.com/wp-content/uploads/2017/03/SQLServerConnectivity.png"><img class="aligncenter size-full wp-image-17730" src="https://thomaslarock.com/wp-content/uploads/2017/03/SQLServerConnectivity.png" alt="SQL Server Connectivity" width="486" height="204" /></a>One time, at a company I heard about, there was a development team having issues connecting to one of the SQL Server database servers. The DBAs were called to investigate, they reviewed the instance and found nothing different than any of the hundreds of SQL Server instances they managed. The developers were certain the DBAs were incompetent fools that didn't know how to configure a server correctly, so they decided to help. They found a blog post about SQL Server connectivity and sent the DBA team a link to the post with the following instructions:

"Make certain you have configured the server in the exact way as outlined in this blog post."

[Because, you know, that's how database servers should be administered, by following the directions of some random blog post and not by the team of DBAs that managed to have <strong>hundreds</strong> of instances running for <strong>years</strong> without any trouble. By the way, if this describes how you administer your database servers then I want you to stop working in IT immediately. Wait. Don't quit until AFTER you've contacted me for help. Thanks. But I digress...]

After a bit of back and forth about the issue, the developers finally located the root cause: they were opening more than 32,767 connections to the server, causing SQL to refuse connections at that point.

Through the years I have found that many issues with SQL Server are common things to diagnose and fix. One such area is with connections. Microsoft has published a page for <a href="https://support.microsoft.com/en-us/help/4009936/solving-connectivity-errors-to-sql-server" target="_blank">solving general SQL Server connectivity issues</a>. This page is perfect for you or anyone you know that has suffered from one of the following error messages:
<blockquote><em>A network-related or instance-specific error occurred while establishing a connection to SQL Server</em>
<em>No connection could be made because the target machine actively refused it</em>
<em>SQL Server does not exist or access denied</em>
<em>PivotTable Operation Failed: We cannot locate a server to load the workbook Data Model</em>
<em>Cannot generate SSPI context</em>
<em>Login failed for user</em>
<em>Timeout Expired</em>
<em>The timeout period elapsed prior to obtaining a connection from the pool</em></blockquote>
The page will also help guide you through the steps for connecting to SQL server using a UDL file.

The wizard is good, but not perfect. For example, it wouldn't have told me that the developer was doing something silly by opening more than 30k connections at once. But it will help you to determine if you have configured your SQL Server properly for connections. And that's a start.

Together with the page for <a href="https://support.microsoft.com/en-us/help/10179/troubleshooting-alwayson-issues" target="_blank">troubleshooting AlwaysOn issues</a> and the page for <a href="https://support.microsoft.com/en-in/help/10085/troubleshooting-connectivity-issues-with-microsoft-azure-sql-database" target="_blank">troubleshooting connectivity issues with Microsoft Azure SQL Database</a>, these three pages should be bookmarked for quick reference. In fact, that's what I've done here: <a href="https://thomaslarock.com/sql-server-connectivity/" target="_blank">https://thomaslarock.com/sql-server-connectivity/</a>

So now you can find all the pages in one place. I will add links to new pages as they become available. If you know of a page that should be included just leave a comment for me to review.