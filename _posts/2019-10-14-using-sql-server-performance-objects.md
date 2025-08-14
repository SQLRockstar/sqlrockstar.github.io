---
layout: post
title: Using SQL Server Performance Objects
date: '2019-10-14 12:28:59 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- perfmon
- sql server
---

<p>SQL Server performance objects are found inside the Performance Monitor tool, also known as perfmon. If you are using Performance Monitor for gathering resource metrics for SQL Server then you are familiar with a screen such as this one:</p>



<figure class="wp-block-image"><a href="https://thomaslarock.com/wp-content/uploads/2019/10/image.png"><img src="https://i2.wp.com/thomaslarock.com/wp-content/uploads/2019/10/image.png?fit=600%2C554&amp;ssl=1" alt="SQL Server Performance Monitor Counters" class="wp-image-19650"/></a></figure>



<p>You can see I have navigated to the SQL Server Plan Cache counter, selected Cache Hit Ratio, and an instance of Extended Stored Procedures. You will also note in the lower left I have enabled "Show description". This results in the text at the bottom, "Ratio between cache hits and lookups". </p>



<p>That text is referring to the counter itself, and not to the instance. If I toggle to another instance, such as SQL plans, the text doesn't change. I have an idea what SQL plans means, but I'm also smart enough to know I don't know everything. So, where would one find information about the instances?</p>



<p>Those details can be found here: <a aria-label="Use SQL Server Objects (opens in a new tab)" href="https://docs.microsoft.com/en-us/sql/relational-databases/performance-monitor/use-sql-server-objects?view=sql-server-2017#SQLServerPOs" target="_blank" rel="noreferrer noopener">Use SQL Server Objects</a>. From there we can go to the <a aria-label="SQL Server, Plan Cache Object (opens in a new tab)" href="https://docs.microsoft.com/en-us/sql/relational-databases/performance-monitor/sql-server-plan-cache-object?view=sql-server-2017" target="_blank" rel="noreferrer noopener">SQL Server, Plan Cache Object</a> page, where we will find the following details:</p>



<figure class="wp-block-image"><a href="https://thomaslarock.com/wp-content/uploads/2019/10/image-1.png"><img src="https://i2.wp.com/thomaslarock.com/wp-content/uploads/2019/10/image-1.png?fit=600%2C95&amp;ssl=1" alt="SQL Server Performance Counters Plan Cache SQL Plans" class="wp-image-19651"/></a></figure>



<p>That's a lot more detail than I was expecting! Now I know exactly what this counter will consider to be a plan. These details provide more context to the metric, helping users understand what they are measuring. </p>



<p>Having SQL Server performance objects documented is important, and you should review them. Otherwise you run a risk of collecting the wrong metrics.</p>