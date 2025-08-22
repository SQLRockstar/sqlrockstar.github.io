---
layout: post
title: Killing the "SQL Server is a Memory Hog" Myth
date: '2017-08-16 16:02:12 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- memory
- myth
- sql server
---

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/pig-fly.jpg"><img class="aligncenter wp-image-18003 size-full" src="https://thomaslarock.com/wp-content/uploads/2017/08/pig-fly.jpg" alt="Killing the &quot;SQL Server is a Memory Hog&quot; Myth" width="613" height="428" /></a>

&nbsp;

At least once a week I read or hear the familiar refrain, “SQL Server is a memory hog,” or “SQL Server uses all the memory.” If you, or anyone you know, are saying these things, I am here today to tell you something.

No.

Just no.

Stop. Saying. <a href="https://communities.vmware.com/thread/517152" target="_blank" rel="noopener">This</a>.

It’s like hearing <a href="https://www.youtube.com/watch?v=TBLIYbNxsNs" target="_blank" rel="noopener">fingernails on a chalkboard</a> when people say such things. It’s time to put an end to this myth.

(And by the way, you’re welcome.)

First up, let's get something straight...

&nbsp;
<h2>SQL Server Is a Software Program</h2>
That’s right. SQL Server is a piece of software. And software programs are good at doing what they have been programmed to do. Typically, software programs are programmed and configured by humans.

That’s where you come in, my fellow humans.

SQL Server will, by design, <a href="https://technet.microsoft.com/en-us/library/aa337525(v=sql.105).aspx" target="_blank" rel="noopener">read data pages from disk into memory</a>. SQL Server will store as many pages as you tell it to store, and will only evict them from memory as needed. My conclusion, for which I’ve done no research, is that <strong>95% of the people complaining about SQL Server using all the memory on a server are 100% responsible for not configuring SQL Server memory properly</strong>.

And there’s the crux of the problem. The people that don’t understand how SQL Server uses memory also don’t understand that it is up to them to decide how much memory SQL Server will use.

That’s the #hardtruth folks. It’s been you all along.

(Editor’s note: I think Oracle/UNIX folks don’t have these complaints about memory because Windows makes it easier to see memory consumption in Task Manager. Perhaps this myth would have died a long time ago if it weren’t for giving RDP access to people who don’t understand how SQL Server works, or that Task Manager is a dirty, filthy liar. But I digress.)

&nbsp;
<h2>95 &lt; 100</h2>
For those Generation Next-ers out there (people who install software by clicking Next-Next-Finish), you should know that SQL Server will not try to use all the available memory for data pages. The default setting allows for SQL Server to dynamically manage the memory consumption and it will not allocate more than 95% of the total physical memory.

For those of us <span style="text-decoration: line-through;">old</span> experienced enough to remember database servers with 8GB of RAM, that 95% is close enough to “all” for appearance's sake. And SQL Server has other memory needs than just database pages. Over the years, we have seen <a href="https://thomaslarock.com/2014/06/estimating-memory-requirements-in-sql-server-2014/" target="_blank" rel="noopener">different data objects share the buffer cache with data pages</a>. These days we can query the <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-memory-clerks-transact-sql" target="_blank" rel="noopener">sys.dm_os_memory_clerks</a> dynamic management view to find out how much of our memory is assigned to the various memory clerks.

The bottom line is that 95% is not 100%. SQL Server will not try to use all the memory by default. And setting the minimum memory will not cause SQL Server to start allocating memory, either. SQL Server will not allocate pages without being asked to do so.

By a human, most likely.

&nbsp;
<h2>Deciding the Max Memory Setting</h2>
Assuming you have gotten this far, you understand that <strong>you are responsible for how much memory SQL Server will use</strong>. The next logical question becomes: What should the max memory be set to by default?

I have no idea. And neither does anyone else. If someone tells you they know exactly how much memory your SQL Server needs they are either (1) lying, (2) trying to sell you something, or (3) both.

There is no shortage of formulas out there for prognosticating the initial amount of memory to set as a max value for SQL Server. I’ve even seen suggestions that you use the size of a database to guess at your max memory setting. That’s absurd. It’s not the size of the database that determines the amount of memory needed, it’s the workload that matters.

Here is the formula I offer to clients and customers that ask for help with finding a max memory setting. This formula assumes you are trying to right-size the memory for a dedicated database server (engine only, no SSAS, SSRS, SSIS, etc., or any other significant applications), and this is for physical servers (but holds mostly true for virtualized servers, too):
<ul>
 	<li>Take physical memory (say, 128 GB RAM)</li>
 	<li>Subtract memory for the O/S itself (1 GB for every 8 GB of RAM; 16 GB in this example)</li>
 	<li>Subtract memory needed for thread stack size (the number of worker threads multiplied by thread size; typical example for a x64, 4 CPU system would be 512 * 2 = 1024 MB, or 1 GB here)</li>
</ul>
&nbsp;

That would give us a max memory setting of about 111 GB in this example. Again, this doesn’t consider any other applications that might be running. The formula also does not consider the use of features such as Columnstore indexes or In-Memory OLTP. Those features will require you to adjust your settings further.

Once you arrive at your number, you set your max memory and then monitor memory consumption, adjusting the settings as necessary. The 111 is not an absolute, it is meant as a decent starting point in the absence of any other information regarding the specific workload for the server.

&nbsp;
<h2>Do You Need More Memory?</h2>
This is a common question that comes up in SQL Server and memory discussions. How do you know if you need more?

The first thing you need to know is if memory is the resource constraint you are facing. If so, then yeah, maybe you need more memory. One way to know is if your instance is using all the memory you assigned following the formula above. Another is if you are seeing memory errors in the SQL error logs. Still another way to know is if you are seeing a lot of disk activity (because SQL Server is not able to keep pages in memory). Any one of those items could mean that you need to allocate more memory to your instance.

However, it could be the case that by adding more memory you end up hurting performance. For example, in a virtualized environment it could be possible that the additional memory is spread over physical NUMA cores, resulting in slower performance than if the entire memory could fit inside one NUMA core.

I advocate that you monitor memory consumption over time, noting if you are trending upwards. Measuring and monitoring memory consumption is the best way to understand if your database server needs more memory.

Anything else is just a wild guess.

&nbsp;
<h2>Summary</h2>
It’s not SQL Server, it’s you.

You have been in control all along.

It’s about time you understand, and accept, that you are responsible for what SQL Server is doing.

Blaming SQL Server for using all the memory that you have allowed it to access is like blaming a coffee maker for using all the water you placed inside.