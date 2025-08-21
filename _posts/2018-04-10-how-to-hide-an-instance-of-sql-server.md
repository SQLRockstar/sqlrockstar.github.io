---
layout: post
title: How To Hide an Instance of SQL Server
date: '2018-04-10 12:11:43 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL Server 2017
tags:
- microsoft
- sql server
- sql server 2017
---

If you have ever wanted to hide an instance of SQL Server, this is the post for you. Read on.

When you launch SQL Server Management Studio (SSMS), you see the option to connect to an instance. If desired, you have the ability to browse instances running on your network. Just click on the dropdown and at the bottom there is a 'Browse for more...' option:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server.jpg"><img class="aligncenter size-large wp-image-18937" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server-600x396.jpg" alt="how to hide instance of SQL Server" width="600" height="396" /></a>

&nbsp;

This allows you to browse for local or network instances. I have four instances running on my laptop you see them displayed in this list:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_SSMS_list.jpg"><img class="aligncenter size-large wp-image-18938" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_SSMS_list-568x600.jpg" alt="how to hide instance of SQL Server SSMS list" width="568" height="600" /></a>

&nbsp;

Let's assume one of these instances is double top secret and we don't want users to see the instance name. That's possible through SQL Server Configuration Manager (SSCM). Open up SSCM and navigate to your SQL Server instances:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_SSCM_list.jpg"><img class="aligncenter size-large wp-image-18939" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_SSCM_list-600x440.jpg" alt="how to hide instance of SQL Server SSCM list" width="600" height="440" /></a>

&nbsp;

In SSCM, expand SQL Server Network Configuration, right-click 'Protocols' for the instance you want to hide, then select 'Properties':

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_properties.jpg"><img class="aligncenter size-large wp-image-18940" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_properties-600x440.jpg" alt="how to hide instance of SQL Server properties" width="600" height="440" /></a>

&nbsp;

On the Flags tab, in the 'Hide Instance' box, select Yes, and then click OK to close the dialog box:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_flags.jpg"><img class="aligncenter wp-image-18941 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_flags-490x600.jpg" alt="how to hide instance of SQL Server flags" width="490" height="600" /></a>

&nbsp;

The dialogue box says to restart SQL to apply the changes, but that is not the case for this specific change. Any new connection will not be able to see this instance listed. Here's what I see after closing SSMS and trying to browse again:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_success.jpg"><img class="aligncenter size-large wp-image-18942" src="https://thomaslarock.com/wp-content/uploads/2018/04/how_to_hide_instance_SQL_Server_success-568x600.jpg" alt="how to hide instance of SQL Server success" width="568" height="600" /></a>

&nbsp;

There you go, an easy way to hide your SQL Server instance from anyone that is browsing your network.