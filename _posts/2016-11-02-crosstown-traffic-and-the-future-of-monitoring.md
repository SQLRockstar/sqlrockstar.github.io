---
layout: post
title: Crosstown Traffic and the Future of Monitoring
date: '2016-11-02 18:52:28 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- bottlenecks
- monitoring
- resource
- sql server
---

[caption id="attachment_17523" align="aligncenter" width="479"]<a href="https://thomaslarock.com/wp-content/uploads/2016/11/Picture1.png"><img class="wp-image-17523 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/11/Picture1.png" alt="Cross town traffic and the future of monitoring" width="479" height="360" /></a> Crosstown traffic, all you do is slow me down. And I got better things on the other side of town.[/caption]

Rush hour traffic.

We have all, at one point in our lives, been stuck in car traffic. For many of us this happens during rush hour, that period of the day when the roads are jammed with people commuting to and from work.

When faced with the fact that you have to fight traffic as you go to and from work (assuming you cannot work from home) your choices are limited. You can choose to leave at a different time, or you could use a different route, or you could just accept the fact that your driving time was going to take longer.

It's just something we all accept.

Thinking of the road, and the cars, as resources for our consumption we can see things in a slightly different light. Let's consider the car to be our database, which would make the road our bottleneck in this example. Besides traffic, there are other things that can cause a bottleneck during our commute: weather, construction, accidents, etc.

When it comes to data, the are only five possible resource bottlenecks (disk, memory, cpu, network, locking/blocking). I don't include tempdb (or oracle temp tablespace) as a bottleneck because typically tempdb is a manifestation of one of the other issues. It doesn't matter to me if you want to include tempdb as a bottleneck or not, really, because here's the real secret:

When it comes to solving a database resource bottleneck you have 2 options: <strong><em>You can use less, or you can buy more.</em></strong>

That's it.

We really have the same two options for our commute, except the idea of buying our own road is not feasible (well, unless your name is <a href="https://www.massport.com/" target="_blank">MASSPORT</a>). We could try to change the mode of transportation for our commute, perhaps use a helicopter instead, but that is essentially the same as using less of the road. With resource bottlenecks that's really the only two options you have. Use less, or buy more.

For database resource bottlenecks the real trick can be (at times) trying to determine which bottleneck you have, and the true root cause of that bottleneck.

But this isn't rocket surgery. It is one of those five things, and you get those two solution options.
<h2>Solving Database Resource Bottlenecks Today</h2>
I use <a href="http://www.solarwinds.com/database-performance-analyzer-sql-server" target="_blank">wait events</a> to solve questions about database resource bottlenecks. They help me quickly identify the possible root causes for performance issues. Wait events are easy to track (and I can recommend a tool if you are looking for one) and give wonderful insight into the nature of the bottleneck.

Think of monitoring wait events as something similar to a traffic report. Sometimes it's nice to know that the 4 mile backup is caused by a car with a flat tire on the side of the road. It doesn't reduce your wait, but at least you know the cause and you can start to think about possible options such as taking the next exit.

Unfortunately, just diagnosing the root cause isn't always enough.

What you are likely to find is that your end user doesn't care about why traffic is bad, they either want the road to themselves or they want a new road.

By tomorrow, of course.
<h2>Solving Future Database Resource Bottlenecks</h2>
I mentioned the traffic report already. The traffic report is a common method for many commuters to know how to avoid bottlenecks. The traffic report is done in real-time, relaying information about what is happening now.

The future of monitoring is with predicative analytics. This would be the same as a traffic report that knows what is going to happen before it happens. Many companies are offering <a href="http://oriondemo.solarwinds.com/ui/recommendations/current" target="_blank">predictive analytics</a> as part of their monitoring tools. The technology is still new, so your experience may vary between vendors, but the next three to five years should see progress in this area until it becomes common.

The future of monitoring is not in the diagnosing of issues in real time, it is the prevention of issues before they happen.