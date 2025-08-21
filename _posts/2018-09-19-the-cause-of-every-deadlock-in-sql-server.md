---
layout: post
title: The Cause of Every Deadlock in SQL Server
date: '2018-09-19 14:00:37 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
- SQL Server 2017
- SQL Server Performance
tags:
- blocking
- deadlock information
- Deadlocks
- locking
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/09/deadlock.png"><img class="aligncenter size-full wp-image-19329" src="https://thomaslarock.com/wp-content/uploads/2018/09/deadlock.png" alt="the cause of every deadlock in SQL Server" width="900" height="527" /></a>

&nbsp;

First, a quick definition and example for those that don’t know what deadlocks are inside of a database.

A deadlock happens when two (or more) transactions block each other by holding locks on resources each of the transactions also needs.

For example:

Transaction 1 holds a lock on Table A.

Transaction 2 holds a lock on Table B.

Ok, now Transaction 1 requests a lock on Table B, and is blocked by Transaction 2.

And Transaction 2 requests a lock on Table A, and is blocked by Transaction 1.

Transaction 1 cannot complete until Transaction 2 is complete. And Transaction 2 cannot complete until Transaction 1 is complete. This is a cyclical dependency and results in a <strong>deadlock</strong>. Deadlocks can involve more than two transactions, but two is the most common scenario.

&nbsp;
<h2>What causes deadlocks?</h2>
The database engine does not seize up and start deadlocking transactions because it's tired. Certain conditions must exist in order for a deadlock to happen. Every one of the conditions needs someone, somewhere, to be using the database.

Deadlocks are the result of application code combined with a database schema resulting in access patterns which lead to a cyclical dependency.

That’s right. I said it. <strong>Application code causes deadlocks</strong>.

It is up to the database administrator to work with the application developer to resolve deadlocks. (A fine example of where the issue is not the DBAs <span style="text-decoration: underline;">fault</span>, but it is now their <span style="text-decoration: underline;">problem</span>.)

And before I go any further, let me offer you some advice. If you believe updating your stats is a way to prevent deadlocks in SQL Server, then you should find a new line of work. Actually, stay right where you are. Drop me an email. I charge reasonable rates. Thanks.

&nbsp;
<h2>Deadlocking != Blocking</h2>
Another thing worth noting is deadlocking is not the same as blocking. This point is often overlooked. Blocking is to be expected in a relational database. Deadlocks are not.

A typical response to blocking and deadlocking is “Can you update the stats and rebuild indexes so it all goes away?” My answer would be, “Yes. Can I help you with your design?"

Oh, and you do not need large tables with indexes to cause a deadlock. Blocking and deadlocks can happen on small tables, as well.

Look, no one likes to admit they built something horrible. Chances are everything worked fine when built, but as the data changes, so could the need for an updated design. If you are a database developer do not take offense when someone says, "We need to examine the design, the data, and the code.” It is a simple fact: Things change over time.

&nbsp;
<h2>Finding deadlocks</h2>
Here is a link to <a href="/blog/blogs.msdn.com/bartd/archive/2006/09/09/Deadlock-Troubleshooting_2C00_-Part-1.aspx" target="_blank" rel="noopener">Bart Duncan's blog series</a> that <a href="http://blogs.msdn.com/bartd/archive/2006/09/09/Deadlock-Troubleshooting_2C00_-Part-1.aspx" target="_blank" rel="noopener">helps to explain deadlocking</a> as well as the use of trace flag T1222. If you are experiencing deadlocks and want to turn this on now, simply issue the following statement:
<pre lang="tsql">DBCC TRACEON (1222, -1)</pre>
The flag will start logging detailed deadlock information to the error log. The details from this trace flag are much easier to understand than the <a href="https://support.microsoft.com/en-us/kb/832524" target="_blank" rel="noopener">original Klingon returned by T1204</a>. Unfortunately, this trace flag disappears after the next service restart. If you want the trace flag always enabled, you need to add -T1222 as a <a href="http://msdn.microsoft.com/en-us/library/ms190699.aspx" target="_blank" rel="noopener">startup parameter to your instance</a>.

The default Extended Event system health session will show detailed deadlock information also. Use the following code to examine deadlock details:
<pre lang="tsql">SELECT XEvent.query('(event/data/value/deadlock)[1]') AS DeadlockGraph
FROM ( SELECT XEvent.query('.') AS XEvent
FROM ( SELECT CAST(target_data AS XML) AS TargetData
FROM sys.dm_xe_session_targets st
JOIN sys.dm_xe_sessions s
ON s.address = st.event_session_address
WHERE s.name = 'system_health'
AND st.target_name = 'ring_buffer'
) AS Data
CROSS APPLY
TargetData.nodes
('RingBufferTarget/event[@name="xml_deadlock_report"]')
AS XEventData ( XEvent )
) AS src;
</pre>
There are more ways to discover if deadlocks are happening. You could use SQL Server Profiler (or a server trace), as well as Performance Monitor (i.e., Perfmon) counters. Each method will be reset upon a server restart. You need to capture the deadlock details for historical purposes, if desired.

&nbsp;
<h2>Resolving deadlocks</h2>
Resolving a deadlock requires an understanding of why the deadlocks are happening. Once you know there is a deadlock, and you review the deadlock information, you have some options.

I’ve collected a handful of tips and tricks over the years to use to cut the chances deadlocks happen. Always consult with the application team before making any of these changes.

1. Using a <a href="https://www.simple-talk.com/sql/learn-sql-server/using-covering-indexes-to-improve-query-performance/">covering index</a> can reduce the chance of a deadlock caused by bookmark lookups.

2. Creating indexes to <a href="http://sqlmag.com/blog/should-i-index-my-foreign-key-columns">match your foreign key columns</a>. This can reduce your chances of having deadlocks caused by cascading referential integrity.

3. When writing code, it is useful to keep transactions as short as possible. Access objects in the same logical order when it makes sense to do so.

4. Consider using one of the <a href="https://msdn.microsoft.com/en-us/library/tcbchxcb(v=vs.110).aspx">row-version based isolation levels</a> READ COMMITTED SNAPSHOT or SNAPSHOT.

5. The <a href="https://msdn.microsoft.com/en-us/library/ms186736.aspx">DEADLOCK_PRIORITY session variable</a> will specify the relative importance the current session. This allows the current session to continue processing if deadlocked with another session.

6. You can trap for the deadlock error number using TRY…CATCH logic and then retry the transaction.

&nbsp;
<h2>Summary</h2>
The impact of a deadlock on end-users is a mixture of confusion and frustration. Retry logic is helpful, but having to retry a transaction results in longer end-user response times. This leads to the database as a performance bottleneck, and pressures the DBA and application teams to track down the root cause and fix the issue.

As always, I hope this information helps you when you encounter deadlocks in your shop.