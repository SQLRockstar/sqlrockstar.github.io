---
layout: post
title: Using Non-default Ports for SQL Server
date: '2016-12-14 11:50:36 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
tags:
- Data
- default port
- security
- sql server
---

Last week at SQL Live I gave a talk "Configuring SQL Server like a Microsoft Certified Master". It's a session Tim Chapman (<a href="https://blogs.msdn.microsoft.com/sql_pfe_blog/" target="_blank">blog</a> | <a href="https://twitter.com/chapmandew" target="_blank">@chapmandew</a>) and I built previously and I've made an effort to keep updated. I remember we wanted to call it "Configuring SQL Server Like a Boss", but thought it boring to watch someone click 'next' a few dozen times and then 'finish'.

On one slide I mention the use of named instances, non-default ports, firewalls, and anti-virus exclusions. What I didn't mention during the session was how one of those items has the potential to create the largest SQL Server nerd fight since <a href="https://thomaslarock.com/2013/03/administering-sql-server-running-on-server-core/" target="_blank">server core was introduced</a>. Here is the slide I was using during the point in the session:

<a href="https://thomaslarock.com/wp-content/uploads/2016/12/2016-Config-SQL.jpg"><img class="aligncenter wp-image-17602 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/12/2016-Config-SQL-560x315.jpg" alt="Non-default Ports SQL Server" width="560" height="315" /></a>

My advice to the attendees was to use each of the items listed. I am not saying that this is an absolute rule, mind you, but in the absence of information about systems, servers, applications, etc., I would configure SQL Server to be a named instance, <a href="https://msdn.microsoft.com/en-us/library/ms177440.aspx" target="_blank">using a non-default port</a>, using a firewall, and making sure that the data and log files were excluded from anti-virus scans. That's how I roll. You are free to do you as you see fit, and I'll be me.

The contentious issue here is using non-default ports for SQL Server. The argument against non-default ports typically goes something like this:

"It's <a href="https://www.schneier.com/crypto-gram/archives/2002/0515.html#1" target="_blank">security by obscurity</a>."
"It's difficult to remember all those different port numbers."
"An attacker can do a port scan in less than three seconds."

All those items are true. I am not here today, writing this post, to dispute their veracity. I'm not interested in watching a nerd fight (OK, maybe just a little one).

I am here today to help you understand the bigger picture.

First, security by obscurity is not always a bad thing. Do a little research and you can find <a href="https://danielmiessler.com/study/security-by-obscurity/#gs.pTcCqcg" target="_blank">plenty</a> of <a href="https://www.schneier.com/blog/archives/2008/06/security_throug_1.html" target="_blank">examples</a> where <a href="http://www.theregister.co.uk/2011/10/05/security_by_obscurity/" target="_blank">security by obscurity</a> has a valid use case. No, it's not for everyone, in every situation. Don't be silly. But, much as there is always someone to point out some edge case server they work with that has a unique workload such that WidgetX won't work for them, I am here to remind you that edge cases exist with regards to security, too.

Second, you should know that there are tools out there to <a href="http://www.solarwinds.com/topics/it-inventory-management" target="_blank">help you keep track of your inventory</a>, and things like port numbers. You should also know that other DBAs in the world manage systems (Oracle, DB2, and the artist formerly known as Sybase) that assign non-default ports all the damn time, so it's not impossible for a human to keep track of such things. Am I the only one that knows how to use a DNS alias?

Lastly, yes, an attacker can do a port scan in just a few seconds. But if a non-default port causes an attacker to take longer, allowing me to detect the activity, that is a good thing in my book. And it's not just an attacker from the outside we need to worry about. Sometimes you want folks on the accounting team to have to slow down and ask questions about why they can't connect to a server, it forces everyone to double check that their request for data is a legitimate one.

All that aside, there is one final point I want to present for consideration.

Let's assume that you continue to install default instances of SQL Server, using the default port of 1433, and you do not use the windows firewall. Now, let's assume that an attacker gains entry to your servers and database instances and you have a data breach. Now, let's assume that there is a formal review about the incident.

You are asked to come to a room. You sit across from a group of people. They ask you questions about your role. They ask questions about the server, the database, and security.

You explain to them how SQL Server works, the difference between default and named instances, and why security by obscurity is a bad, bad thing. "Completely useless" you tell them.

Then, as you are getting ready to leave, someone does their best <a href="https://www.youtube.com/watch?v=eNvzRnotGsY" target="_blank">Columbo impersonation and asks you just one more thing</a>:

"Is it possible to run SQL Server on a non-default port?"

Think about what answer you would want to give at that moment.

Think again about your answer, and your reasons, your justifications for using the default port.

Now think about your answer as if your job, or jail time, depends on it.

I know what my answers would be. How about yours?