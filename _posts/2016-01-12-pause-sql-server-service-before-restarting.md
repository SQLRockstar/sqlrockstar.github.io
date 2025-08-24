---
layout: post
title: Pause SQL Server Service Before Restarting
date: '2016-01-12 15:18:14 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- microsoft
- MSSQL
- pause
- service
- sql server
---

Many a system administrator has been faced with the task of rebooting a server during the middle of the working day. This timing is the least desired option, as server reboots are often done during off-hours and weekends. But there are times when reboots are needed during the day.

Reboots during the day get a bit uneasy when the server is a database server because most end-users would rather chew tinfoil than have a database server go offline for even five minutes during the day, interrupting their work. In an ideal world there would be a way for you to (1) allow end-users to finish their work and (2) not allow any new users to connect to the instance until the reboot is completed.

Turns out such an option already exists, and it's been right in front of our nose the entire time:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/pause_service.jpg" rel="attachment wp-att-17265"><img class="aligncenter size-full wp-image-17265" src="https://thomaslarock.com/wp-content/uploads/2016/01/pause_service.jpg" alt="pause_service" width="412" height="488" /></a>

By <a href="https://msdn.microsoft.com/en-us/library/hh403394.aspx" target="_blank">pausing the SQL Server service before restarting the instance</a> we allow end users to continue their work uninterrupted and we also stop any new connections to the instance. This is a nicer way of telling people to "get out" of the database in order for the server to be rebooted. I wouldn't leave the server <a href="http://dba.stackexchange.com/questions/84307/60-minutes-to-shut-down-sql-server-service" target="_blank">paused for 60 minutes of course</a>, but I would rather use this method than forcibly disconnect users and rollback their transactions.

When a server is paused you will see messages similar to this in the SQL Server error log:
<pre> Error: 17142, Severity: 14, State: 0.
 SQL Server service has been paused. No new connections will be allowed. To resume the     
 service, use SQL Computer Manager or the Services application in Control Panel.

 Error: 18456, Severity: 14, State: 13.
 Login failed for user ''. Reason: SQL Server service is paused. 
 No new connections can be accepted at this time. [CLIENT: &lt;local machine&gt;]
</pre>
&nbsp;

Next time you are worried about rebooting during the day think about the pause button instead. It might be a nice compromise for your end-users.