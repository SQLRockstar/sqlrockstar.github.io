---
layout: post
title: SQL Profiler Will Never Die
date: '2017-05-09 16:43:49 +0000'
categories:
- Data Analytics
- MSSQL
- SQL MVP
tags:
- sampling
- selection bias
- SQL Profiler
---

For many SQL Server professionals, emotions run deep for <a href="https://docs.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler" target="_blank" rel="noopener noreferrer">SQL Profiler</a>. Ask five SQL Server professionals their thoughts about SQL Profiler versus Extended Events and you'll get seven different opinions. If you are looking for some fun, and happen to be in a group of SQL Server professionals, just ask them if they prefer SQL Profiler or Extended Events. Then grab some popcorn while you watch the show.

Knowing this, last Friday I decided to have a bit of fun and put up a Twitter poll, asking my #SQLFamily to pick their team:

https://twitter.com/SQLRockstar/status/860480504390451204

I gave three options, including a #TeamWhatever for those people that either don't care, or will use whatever option is best for them at the time. You can see the results. Out of 176 total votes, #TeamExtendedEvents won 40% of the vote.

So, what does this mean? Absolutely nothing!
<h2>Your Bias is Showing</h2>
<a href="https://thomaslarock.com/2017/05/book-review-the-death-of-expertise/" target="_blank" rel="noopener noreferrer">In yesterday's post I mentioned two forms of bias</a>, cognitive and confirmation. There are many forms of bias when it comes to surveys and sampling. In most cases bias is unintentional, often the result of a sampling procedure not being well thought out. The Twitter poll gives me an opportunity to point out why such things as Twitter polls and blog surveys are poor sampling methods.

There are a handful of reasons why I said the results of the Twitter poll I ran last Friday have no value. The biggest reason has to do with selection bias. Here are some examples.

<strong>The poll didn't give everyone a chance to respond</strong>. This is a selection bias known as under coverage. Not every SQL Server professional is on Twitter. You cannot consider the 176 respondents a valid random sample of all SQL Server professionals.

<strong>The poll was available for 24 hours</strong>. Even for a SQL Server professional on Twitter, they likely missed the poll altogether. This is  known as nonresponsive bias. There are many SQL Server professionals that would vote for #TeamProfiler if they were Twitter users *and* known about the poll.

<strong>Polls such as this draw responses due to strong opinions</strong>. This is called voluntary response bias. You might have seen me tweeting about #TeamProfiler and decided "WTH is he doing?" and decided to vote for the wrong option.

If there is one thing to take away from this post it is that Twitter polls are a poor excuse for a survey. The next time someone hands you the results of a survey you will be able to determine if any bias has affected the results. Otherwise you are going to draw the wrong conclusion from the data that was collected.
<h2>What's the Deal With SQL Profiler?</h2>
Nothing, really. It's old...I mean experienced...having been around since SQL Server 7. SQL Profiler has been deprecated, which means that it is scheduled to be removed in a future version of SQL Server. However, at Microsoft Amp last month Scott Guthrie announced that <a href="https://channel9.msdn.com/Events/Data-Science/Microsoft-Data-Amp-2017/Keynote" target="_blank" rel="noopener noreferrer">SQL Profiler would be available for Azure SQL Database</a> (about 20 minutes into the keynote). So, I wouldn't expect Profiler to go away anytime soon.

<a href="https://docs.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events" target="_blank" rel="noopener noreferrer">Extended Events</a> were created in SQL Server 2008, along with SQL Server Audit. My understanding at the time was that these two features were to replace the use of SQL trace (which is what Profiler uses). Adoption for Extended Events has been, well, slow. Which means we've had nine years (and 4 releases of SQL Server) of discussion about which tool to use.

Here's a hint: use what works. I don't think Profiler will ever die. And neither will #TeamProfiler.

<strong>BLOG POST BONUS QUIZ</strong>: Here's a <a href="https://www.g2crowd.com/grid_report/documents/business-intelligence-platforms-implementation-index-fall-2016?tab=tab-id-185246--&amp;tab-nested=tab-185193-5048" target="_blank" rel="noopener noreferrer">survey of BI reporting tools</a>. Yes, it is clearly a marketing piece disguised as valid data. <a href="https://thomaslarock.com/2012/02/the-internet-where-facts-go-to-die/" target="_blank" rel="noopener noreferrer">We've seen such things before</a>. But there are other reasons why this survey is suspect, let me know if you can spot a few of the reasons.