---
layout: post
title: 'SQL Server 2016: What Time Is It?'
date: '2016-03-15 11:40:56 +0000'
categories:
- Database Design
- MSSQL
- SQL Azure
- SQL MVP
tags:
- datetime
- spacetime
- SQL Server 2016
- Things I Write While High on Bacon
- time zone
- UTC
---

<a href="https://thomaslarock.com/wp-content/uploads/2009/08/spacetime1.gif" rel="attachment wp-att-2648"><img class="alignleft size-full wp-image-2648" src="https://thomaslarock.com/wp-content/uploads/2009/08/spacetime1.gif" alt="spacetime" width="325" height="431" /></a>Last week Microsoft had their <a href="https://www.microsoft.com/en-us/server-cloud/data-driven.aspx" target="_blank">#datadriven event to kick off the launch of SQL Server 2016</a>. If you haven’t heard about the announcements such as "data is the new electricity" and <a href="https://blogs.microsoft.com/blog/2016/03/07/announcing-sql-server-on-linux/" target="_blank">SQL Server on Linux</a> then I can only imagine you are either (1) living in a shack in Montana or (2) not a Microsoft-centric person such as myself.

One item that was talked about as part of the launch event was how SQL Server has been used to <a href="https://blogs.technet.microsoft.com/dataplatforminsider/2016/03/10/mapping-the-universe-with-sql-server/" target="_blank">map the Universe</a>. This was, and is, one of the coolest things I have seen in a long time. Then again, I’m a <a href="https://thomaslarock.com/wp-content/uploads/2012/06/LaRockLaunch.jpg" target="_blank">bit of a space nerd</a>.

The fact that my astronomy background is now intersecting with my data career and SQL Server is making me as happy as a Korean schoolgirl learning about emoticons for the first time

?(*´?`*)?

When I heard that SQL Server was being used to store information on the Universe I started thinking about <a href="http://blog.infoadvisors.com/index.php/2014/04/01/sql-server-2014-new-datatype/" target="_blank">a post from Karen López</a> (<a href="http://blog.infoadvisors.com/" target="_blank">blog</a> | <a href="http://twitter.com/datachick" target="_blank">@datachick</a>) regarding a new datatype in SQL Server 2014: spacetime. (It’s an April Fool’s day post, folks).

Well, this past weekend the United States entered into Daylight Saving Time (DST). (Yes, I said ‘Saving’, <a href="http://www.timeanddate.com/time/dst/daylight-savings-time.html" target="_blank">because it’s time, not a bank</a>). For most of us in the data industry, the <a href="http://wedontneeddst.com/" target="_blank">concept of DST is something we can’t stand</a>. We would prefer to have everything stored in UTC time, to remove any ambiguity about the data that has been stored.
<h2>A Brief History of SQL Server Time</h2>
The launch of SQL Server 2005 gave us the ability to find the UTC date with the following function:
<pre lang="tsql">SELECT GETUTCDATE()</pre>
You would need to do some math between that result and the GETDATE() function in order to find your timezone offset, if you wanted. The purpose of such an exercise would be to display the time a GUI somewhere. The offset itself isn't as important as the displaying of the local time to the application user.

Unless, of course, your time zone changes a couple of times a year. Or if different countries switch at different times. <a href="http://www.timeanddate.com/time/dst/2016.html" target="_blank">Or never at all</a>. Such problems with knowing what “time” means to an end user lead to database designs that track two pieces of data: UTC and the local time of the server.

I don’t like storing the same piece of information twice. Neither should you.
<h2>SQL 2008 Solved Everything, Kinda</h2>
With SQL 2008 we got a new time function:
<pre lang="tsql">SELECT SYSDATETIMEOFFSET()</pre>
This was a nice step forward as it allowed for us to find the current time along with the current offset for the local machine in one easy step. Well, more than one step if we still wanted to know the exact UTC time. And you would either need to parse out the offset and store that, or just store the entire datetime offset itself and do the math later.

Oh, and did I mention that SYSDATETIMEOFFSET() is not DST aware. Well, it’s not.

So, in the end we would still be storing two dates (or more) because nobody ever can agree upon anything when it comes to date and time and GUIs and data storage.
<h2>SQL Server 2016: What Time Is It?</h2>
Today I found that SQL 2016 introduces a function to help alleviate the issues we have when it comes to finding the current time. No, it’s not spacetime (I wish), nor is it a stardate (how cool would that be?), it is the ability to transform a given time into your local time by using the <a href="https://msdn.microsoft.com/en-IN/library/mt612795.aspx" target="_blank">AT TIME ZONE</a> function.

[ASIDE: This is a feature that has existed in Azure SQL Database and is a GREAT example of how features from Azure are making their way into the boxed product. More on that in a future post, I promise.]

The syntax is simple enough:
<pre lang="tsql">SELECT CONVERT(datetime, '03/14/2016 01:01:00')
 AT TIME ZONE 'Eastern Standard Time'</pre>
Of course you will need to know what is allowed for you to use for the time zone name. Fortunately for us, this list is stored in the registry of the server. In other words, you can use whatever timezones are installed on the server. For a complete list you can query the <a href="https://msdn.microsoft.com/en-us/library/mt612790.aspx" target="_blank">sys.time_zone_info DMV</a>:
<pre lang="tsql">SELECT *
 FROM sys.time_zone_info</pre>
Running that statement returns 109 rows on my SQL 2016 CTP3 instance, including such time zone classic names we all know and love such as “UTC -11” and “Ulaanbaatar Standard Time”, which I think might be <a href="http://starwars.wikia.com/wiki/Jakku" target="_blank">near Jakku</a>.

The real beauty of the sys.time_zone_info DMV is that it has columns for the offset as well as a column named is_currently_dst to indicate if that region is currently following the idea a <a href="http://www.timeanddate.com/time/dst/history.html" target="_blank">bunch of Canadians in 1908</a> came up with after a hard night of drinking <a href="http://www.drinkspirits.com/canadian-whisky/crown-royal-maple-finished-canadian-whisky/" target="_blank">maple-flavored whiskey</a> and <del>wanted</del> needed an extra hour of sleep. OK, that last part is a guess, but probably closer to the truth than anyone wants to admit.

The sys.time_zone_info DMV now allows for us to avoid building out our own calendar tables in order to store dates and times for our end users. A simple CTE can be used to replace what used to be a lot more code:
<pre lang="tsql">;WITH time_CTE (tz_name, is_currently_dst)
 AS
 (SELECT name, is_currently_dst
 FROM sys.time_zone_info)
  
 SELECT SYSUTCDATETIME()
 AT TIME ZONE tz_name as [Time]
 , tz_name
 , is_currently_dst
 FROM time_CTE</pre>
All in all, I’d rather we work on getting <a href="http://trekguide.com/Stardates.htm" target="_blank">stardates</a> into SQL Server vNext. But this new function seems useful, too.