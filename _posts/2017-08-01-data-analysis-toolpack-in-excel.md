---
layout: post
title: Data Analysis ToolPack in Excel
date: '2017-08-01 13:02:34 +0000'
categories:
- Data Analytics
- SQL MVP
tags:
- Data
- data analytics
- data science
- excel
---

As you may have heard, last week I <a href="https://thomaslarock.com/2017/07/why-im-learning-data-science/" target="_blank" rel="noopener">finished the capstone project for the data science course</a> offered through Microsoft Academy. I learned a lot of things while taking the course. Some of these things are probably not new to you. For example, I didn't know you could select a bunch of rows and columns in Excel this quickly:

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/excel.gif"><img class="aligncenter size-large wp-image-17977" src="https://thomaslarock.com/wp-content/uploads/2017/08/excel-600x360.gif" alt="" width="600" height="360" /></a>

Sure, that's old news for many of you. But I don't work in Excel enough to have the need to know such shortcuts. And when you start working with thousands of rows and hundreds of columns, tricks like that become useful.

Here's another trick I learned: Excel has a Data Analysis pack available as an Excel add-in.

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/data_pack.jpg"><img class="aligncenter size-large wp-image-17978" src="https://thomaslarock.com/wp-content/uploads/2017/08/data_pack-600x360.jpg" alt="" width="600" height="360" /></a>

The Data Analysis toolpack has a lot of useful statistical functions. The first one I used in the course was the descriptive statistics. All we need to do is point it at some data:

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/data_pack_options.jpg"><img class="aligncenter size-full wp-image-17979" src="https://thomaslarock.com/wp-content/uploads/2017/08/data_pack_options.jpg" alt="" width="515" height="374" /></a>

&nbsp;

Click OK and observed the statistical goodness:

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/descriptive_stats.jpg"><img class="aligncenter size-full wp-image-17980" src="https://thomaslarock.com/wp-content/uploads/2017/08/descriptive_stats.jpg" alt="" width="326" height="494" /></a>

Here I was, calculating these numbers the old-fashioned way. Now I know how to get the same results in far less time.

What's more, this underscores why Excel is the go-to tool for millions of business pros each day. If I wanted to get these same results inside of SQL Server, I would need to write T-SQL to get the job done. It wouldn't be hard for me to do that, but I've been writing database queries for some time now. For business pros, they don't care to spend time writing T-SQL, they just want to use Excel to do some basic math and statistics. And I can't blame them, either, since Excel also allows for things like this:

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/histogram.jpg"><img class="aligncenter size-large wp-image-17981" src="https://thomaslarock.com/wp-content/uploads/2017/08/histogram-600x403.jpg" alt="" width="600" height="403" /></a>

Yes, it's a simple histogram. You know how to create simple histograms in SSMS using T-SQL? You don't, that's how. (OK, you can, but it's not as easy as Excel).

There's lots of little things like this I learned during the 10-course program. I didn't keep a list, but wish I had. I will keep posting and sharing as I remember. Let's just say that I the course was eye-opening for me in terms of what Excel and PowerBI can do for data professionals. It also helped me understand that the future for data professionals isn't in query tuning, but in data analysis.