---
layout: post
title: 'HOW TO: Improve Database Performance Without Changing Code'
date: '2015-10-06 14:58:17 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
- SQL Server Performance
- Virtualization
tags:
- database
- optimize
- performance
---

<a href="https://thomaslarock.com/wp-content/uploads/2015/10/great-db-rz.png"><img class="size-full wp-image-17092 alignright" src="https://thomaslarock.com/wp-content/uploads/2015/10/great-db-rz.png" alt="great-db-rz" width="375" height="168" /></a>I’ve stated before that great database performance starts with great database design. So, if you want a great database design you must find someone with great database experience. But where does a person get such experience?

We already know that <a href="http://www.quoteyard.com/good-judgment-comes-from-experience-and-experience-comes-from-bad-judgment/" target="_blank">great judgment comes from great experience, and great experience comes from bad judgment</a>. That means great database experience is the result of bad judgment repeated over the course of many painful years.

So I am here today to break this news to you. <strong>Your database design stinks</strong>.

There, I said. But someone had to be the one to tell you. I know this is true because I see many bad database designs out in the wild, and someone is creating them. So I might as well point my finger in your direction, dear reader.

We all wish we could change the design or code but there are times when it is not possible to make changes. As database usage patterns push horrible database designs to their performance limits database administrators are then handed an impossible task: Make performance better but <span style="text-decoration: underline;"><em>don’t touch anything</em></span>.

Imagine that you take your car to a mechanic for an oil change. You tell the mechanic they can’t touch the car in any way, not even open the hood. Oh, and you need it done in less than an hour. Silly, right? That is just as silly as when you go to your database administrator and say: “we need you to make this query faster and you can’t touch the code”.

Lucky for us the concept of "throwing money at the problem” is not new as <a href="https://www.youtube.com/watch?v=xHTNu5UQvH4" target="_blank">shown by this ancient IBM commercial</a>.

Of course throwing money at the problem does not always solve the performance issue. This is the result of not knowing what the issue is to begin with. You don’t want to be the one to spend six figures on new hardware to solve an issue with query blocking.

Even after ordering the new hardware it takes time before arrival, installation, and the issue resolved. What can you do in the meantime to improve performance without touching code?

I put together this list of items to help you fix database performance issues without touching code. Use this as a checklist to research and take action upon before blaming code. Some of these items cost no money, but some items (such as buying flash drives) might. What I wanted to do was to provide a starting point for things you can research and do yourself.

As always: You’re welcome.
<h3><strong>Examine your plan cache</strong></h3>
If you need to tune queries then you need to know what queries have run against your instance. A quick way to get such details is to look inside the plan cache. I’ve written before about how <a href="http://sqlmag.com/database-performance-tuning/sql-server-plan-cache-junk-drawer-your-queries" target="_blank">the plan cache is the junk drawer of SQL Server</a>. Mining your plan cache for performance data can help you yield improvements such as <a href="http://www.sqlskills.com/blogs/kimberly/plan-cache-adhoc-workloads-and-clearing-the-single-use-plan-cache-bloat/" target="_blank">optimizing for ad-hoc workloads</a>, estimating the <a href="http://sqlblog.com/blogs/jonathan_kehayias/archive/2010/01/19/tuning-cost-threshold-of-parallelism-from-the-plan-cache.aspx" target="_blank">correct cost threshold for parallelism</a>, or <a href="https://www.sqlskills.com/blogs/jonathan/finding-what-queries-in-the-plan-cache-use-a-specific-index/" target="_blank">which queries are using a specific index</a>. Speaking of indexes…
<h3><strong>Review your index maintenance</strong></h3>
Assuming you are doing this already, but if not then now is the time to get started. You can use <a href="https://msdn.microsoft.com/en-us/library/ms187658.aspx" target="_blank">maintenance plans</a>, roll your own scripts, or <a href="https://ola.hallengren.com/" target="_blank">use scripts provided</a> by some <a href="http://minionware.net/" target="_blank">SQL Server MVPs</a>. Whatever method you choose, make certain you are <a href="https://msdn.microsoft.com/en-us/library/ms189858.aspx" target="_blank">rebuilding, reorganizing, and updating statistics</a> only when necessary. I’d even tell you to take time to <a href="http://www.sqlskills.com/blogs/kimberly/removing-duplicate-indexes/" target="_blank">review for duplicate indexes</a> and get those removed.

Index maintenance is crucial for query performance. Indexes help reduce the amount of data that searched and pulled back to complete a request. But there is another item that can reduce the size of the data searched and pulled through the network wires…
<h3><strong>Review your archiving strategy</strong></h3>
Chances are you don’t have any archiving strategy in place. I know because we are data hoarders by nature, and only now starting to <a href="https://www.youtube.com/watch?t=2&amp;v=GAXLHM-1Psk" target="_blank">realize the horrors of such things</a>. Archiving data implies less data, and less data means faster query performance. One way to get this done is to consider partitioning. (Yeah, yeah, I know I said no code changes; this is a schema change to help the logical distribution of data on physical disk. In other words, no changes to existing application code.)

Partitioning <a href="https://msdn.microsoft.com/en-us/library/ms190787.aspx" target="_blank">requires some work</a> on your end, and it will increase your administrative overhead. Your backup and recovery strategy must change to reflect the use of more files and filegroups. If this isn’t something you want to take on then instead you may instead want to consider…
<h3><strong>Enable page or row compression</strong></h3>
Another option for improving performance is data compression at the page or row level. The tradeoff for data compression is an increase in CPU usage. Make certain you perform testing to verify the benefits outweigh the extra cost. For tables that have a low amount of updates and a high amount of full scans then data compression is a decent option. Here is the <a href="https://technet.microsoft.com/en-us/library/dd894051(v=sql.100).aspx" target="_blank">SQL 2008 Best Practices whitepaper on data compression</a> which describes in detail the different types of workloads and estimated savings.

But, if you already know your workload to that level of detail, then maybe a better option for you might be…
<h3><strong>Change your storage configuration</strong></h3>
Often this is not an easy option, if at all. You can’t just wish for a piece of spinning rust on your SAN to go faster. But technology such as <a href="https://technet.microsoft.com/en-us/library/hh831739.aspx" target="_blank">Windows Storage Spaces</a> and <a href="https://www.vmware.com/products/virtual-san" target="_blank">VMWare’s VSAN</a> make it easy for administrators to alter storage configurations to improve performance. At VMWorld in San Francisco <a href="http://resources.solarwinds.com/using-vsan-to-maximize-database-performance/" target="_blank">I talked about how VSAN technology</a> is the magic pixie dust of software defined storage right now.

If you don’t have magic pixie dust then SSDs are an option, but changing storage configuration only makes sense if you know that disk is your bottleneck. Besides, you might be able to avoid reconfiguring storage by taking steps to distribute your I/O across many drives with…
<h3><strong>Use distinct storage devices for data, logs, and backups</strong></h3>
These days I see many storage admins configuring database servers to use one big RAID 10, or <a href="https://community.spiceworks.com/topic/262196-one-big-raid-10-the-new-standard-in-server-storage" target="_blank">OBR10</a> for short. For a majority of systems out there the use of OBR10 will suffice for performance. But there are times you will find you have a disk bottleneck as a result of all the activity hitting the array at

<a href="http://www.solarwinds.com/resources/infographics/8-tips-faster-sql-server-performance.aspx" target="_blank" rel="http://www.solarwinds.com/resources/infographics/8-tips-faster-sql-server-performance.aspx"><img class="alignright" src="http://cdn.swcdn.net:80/creative/v2.6/images/../infographics/8_tips_faster_sql_server_performance_8_5x11-1.png" alt="8 Tips for Faster SQL Server Performance: Without the Expense of Over-provisioning" width="270" height="1204" /></a>once. Your first step is then to separate out the database data, log, and backup files onto distinct drives. Database backups should be off the server. Put your database transaction log files onto a different physical array. Doing so will reduce your chance for data loss. After all, if everything is on one array, then when that array fails <a href="https://support.microsoft.com/en-us/kb/2033523" target="_blank">you will have lost everything</a>.

Another option is to break out tempdb onto distinct array as well. In fact, tempdb deserves its own section here…
<h3><strong>Optimize tempdb for performance</strong></h3>
Of course this is only worth the effort <a href="http://www.sqlskills.com/blogs/paul/the-accidental-dba-day-27-of-30-troubleshooting-tempdb-contention/" target="_blank">if tempdb is found to be the bottleneck</a>. Since tempdb is a shared resource amongst all the databases on the instance it can be a source of contention. That is why we have lots of information on <a href="https://technet.microsoft.com/en-us/library/ms175527(v=sql.105).aspx" target="_blank">how to optimize tempdb for performance</a> as well as <a href="https://support.microsoft.com/en-us/kb/2154845" target="_blank">trace flags</a>.

We operate in a world of shared resources, so finding tempdb being a shared resource is not a surprise. Storage, for example, is a shared resource. So are the series of tubes that makes up your network. And if the database server is virtualized (as it should be these days) then you are already living in a completely shared environment. So why not try…
<h3><strong>Increase the amount of physical RAM available</strong></h3>
Of course, this only makes sense if you are having a memory issue. Increasing the amount of RAM is easy for a virtual machine when compared to having to swap out a physical chip. OK, swapping out a chip isn’t that hard either, but you have to buy one, then get up to get the mail, and then bring it to the data center, and…you get the idea.

When adding memory to your VM one thing to be mindful about is if your <a href="http://www.davidklee.net/2013/12/02/sql-server-virtual-machine-vnuma-sizing/" target="_blank">host is using vNUMA</a>. If so, then it could be the case that adding more memory may result in performance issues for some systems. So, be mindful about this and know what to look for (link).

Memory is an easy thing to add to any VM. Know what else is easy to add on to a VM?
<h3><strong>Increase the number of CPU cores</strong></h3>
Again, this is only going to help if you have identified that CPU is the bottleneck. You may want to consider swapping out the CPUs on the host itself if you can get a boost in performance speeds. But adding physical hardware such as a CPU, same as with adding memory, may take too long to physically complete. That’s why VMs are great, as you can make modifications in a short amount of time.

Since we are talking about CPUs I would also mention to examine the Windows power plan settings, this is a <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1018206" target="_blank">known issue for database servers</a>. But even with virtualized servers resources such as CPU and memory are not infinite…
<h3><strong>Reconfigure VM allocations</strong></h3>
Many performance issues on virtualized database servers are the result of the host being over-allocated. Over-allocation by itself is not bad. But over-allocation leads to over-commit, and over-commit is when you see performance hits. You should be conservative with your initial allocation of vCPU resources when rolling out VMs on a host. Aim for a 1.5:1 ratio of vCPU to logical cores and adjust upwards from there always paying attention to overall host CPU utilization. For RAM you should stay below 80% total allocation, as that allows room for growth and migrations as needed.

You should also take a look at how your network is configured. Your environment should be <a href="https://technet.microsoft.com/en-us/library/ee619734(v=ws.10).aspx" target="_blank">configured for multi-pathing</a>. Also, know your current <a href="http://blogs.msdn.com/b/joesack/archive/2009/01/28/sql-server-and-hba-queue-depth-mashup.aspx" target="_blank">HBA queue depth</a>, and <a href="http://sqlblogcasts.com/blogs/christian/archive/2009/01/12/tuning-your-san-too-much-hba-queue-depth.aspx" target="_blank">what values you want</a>.
<h3><strong>Summary</strong></h3>
We’ve all had times where we’ve been asked to fix performance issues without changing code. The items listed above are options for you to examine and explore in your effort to improve performance before changing code. Of course it helps if you have an effective <a href="http://www.solarwinds.com/products/#database management" target="_blank">database performance monitoring solution</a> in place to help you make sense of your environment. You need to have performance metrics and baselines in place before you start turning any "nerd knobs", otherwise you won't know if you are have a positive impact on performance no matter which option you choose.

With the right tools in place collecting performance metrics you can then understand which resource is the bottleneck (CPU, memory, disk, network). Then you can try one or more of the options above. And then you can add up the amount of money you saved on new hardware and put that on your performance review.