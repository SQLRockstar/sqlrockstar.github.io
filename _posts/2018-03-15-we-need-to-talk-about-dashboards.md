---
layout: post
title: We Need To Talk About Dashboards
date: '2018-03-15 14:45:15 +0000'
categories:
- Data Analytics
- MSSQL
- SQL MVP
tags:
- dashboards
- Data
- data analytics
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/piechart.png"><img class="aligncenter size-large wp-image-18783" src="https://thomaslarock.com/wp-content/uploads/2018/03/piechart-600x477.png" alt="we need to talk about dashboards" width="600" height="477" /></a>

Hey everyone, gather 'round. We need to talk about dashboards.

For C-level executives, dashboard reports are essential. Executives don’t have time to review details for every decision they make, they just want to consume a report that has red, yellow, and green to help them make decisions for the day. But the need for such dashboards is also true for the cubicle-dwelling system administrators. They also need dashboards to help them understand where to focus their efforts daily in order to keep operations running.

I'm here today to tell you that your dashboards are a failure.

&nbsp;
<h2>Why Dashboards Fail</h2>
More than 90% of the data in the world has been created in the past two years.

Don’t take my word for it, though. I’m just citing a statement made <a href="https://www.sciencedaily.com/releases/2013/05/130522085217.htm">in this article</a>. Published more than four years ago, that article is the cited source in presentations on how data continues to grow at an exponential rate.

I believe we continue to create, and curate, data at an accelerated pace with each passing year. Today we have access to more data than ever before. Everyone I meet will say they manage more data today than a year ago.

The data explosion has given rise to a never-ending marketing lexicon. The first one I remember being used widely was <a href="http://searchsqlserver.techtarget.com/definition/data-warehouse">data warehouse</a>. That was soon followed by a <a href="http://searchsqlserver.techtarget.com/definition/data-mart">data mart</a>. Today we also have a <a href="https://azure.microsoft.com/en-us/services/data-factory/">data factory</a> and a <a href="http://searchaws.techtarget.com/definition/data-lake">data lake</a>, which is a nice feature to have next to our <a href="https://blogs.technet.microsoft.com/dataplatforminsider/2017/09/25/microsoft-for-the-modern-data-estate/">data estate</a>, built with <a href="https://azure.microsoft.com/en-us/services/databricks/" target="_blank" rel="noopener">data bricks</a>.

With so much data available, information is cheap. Today it is easy to get data about anything. We are drowning in data, inundated with metrics with every step of our day.

The trouble with such easy access to data is this: <strong>When information is so cheap, attention becomes expensive</strong>.

&nbsp;
<h2>I'm Looking Through You</h2>
Here's an experiment for you to try. Watch this video and count the number of passes between the people in white shirts:

https://www.youtube.com/watch?v=vJG698U2Mvo

It's an old study, and you may have seen it before. If you haven't seen it before let me know if you are surprised by the results.

This is part of the problem with dashboards: they are being read by humans. And humans, as it turns out, can have difficulty determining what is important. The experiment helps to show how there is an area of our visual cortex that determines what is important and filters out everything else. In other words, we gain a lot of data when we focus our attention, but we can miss a gorilla staring back at us.

Focusing is a great thing for us humans, and this experiment helps to show why multi-tasking is something we shouldn't be doing. Dashboards are meant to provide that focus. We don't want to spend the time examining all the data streams.

&nbsp;
<h2>Spot the Difference</h2>
Here's another experiment for you. <a href="https://www.popsci.com/spot-difference-between-similar-pictures" target="_blank" rel="noopener">Remember those "spot the difference" games? Here’s why your brain is so bad at them</a>.

When we look at a dashboard we don't take in everything that we see. Our brains don't bother logging details about something that is not important. Just like the gorilla. Of course, once we see it, we don't forget it.

Dashboards that contain an overload of information require more focus, which means less information is being consumed. This is not the desired outcome.

&nbsp;
<h2>Dashboards are a Horrible Way to Communicate</h2>
The trouble with such dashboards is that they are a horrible way to communicate.

Dashboards need data in order to exist. Good dashboards are able to communicate the story the data is trying to tell. But the data contains the details necessary for that story, <strong>and those details are often left behind</strong>. Summaries, aggregations, and averages blur the details from our view. Offering users the ability to drill-through to get the details is a workaround, but the whole point of a dashboard is to avoid having to review the details. Remember, it is better for us humans to be able to focus.

A common example I often use to explain when dashboards aren’t useful involves disk space usage. Let’s say that a disk is at 90% of capacity, and the dashboard shows a big red circle for this metric. The trouble now is that you are missing important details. A 1TB disk at 90% is a different situation than a 10TB disk at 90% full. You also need to know how full the disk was yesterday, what the growth trend has been over time, and at what point the disk is completely full.

While those details might help you figure out what steps to take next, they do little for your end user. This dashboard reporting a disk at 90% has little meaning to the end user that only wants to be able to get their work done for the day.

&nbsp;
<h2>Summary</h2>
Dashboards are not new, they’ve been around for years. It’s the ease in which they are created and consumed that has driven demand. You get a dashboard, and you get a dashboard, and everyone gets a dashboard. The phrase “pin it to your dashboard” has become common for users of tools such as <a href="https://powerbi.microsoft.com/en-us/">PowerBI</a>.

But with so much data coming across our desk each day we need the data to communicate with everyone in a way they can understand.

<strong>Saying your disk is 90% full is not nearly as effective as saying that you only have space for three more Netflix movie downloads</strong>. That’s a story that anyone can understand. Even simple things like bar charts do a better job communicating the story that data is trying to tell. And I have yet to meet a manager that doesn’t understand a bar chart.

Those of us that work in IT are always asking for more. We want more space, more memory, more CPU, more bandwidth.

It’s time we also ask for more ways for our data to tell a story that everyone can understand.

And don't get me started on pie charts.