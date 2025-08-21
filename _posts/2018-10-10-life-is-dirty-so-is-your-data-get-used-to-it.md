---
layout: post
title: Life is dirty. So is your data. Get used to it.
date: '2018-10-10 14:31:34 +0000'
categories:
- Data Analytics
- Database Design
- MSSQL
- SQL MVP
tags:
- big data
- data cleaning
- dirty data
- PowerBI
---

<p>The internet provides everyone the ability to access data at any time, for any need. Unfortunately, it does not help guarantee that the data is valid, or clean.</p>



<p>In the past year I have earned certifications in three areas: <a href="https://thomaslarock.com/2017/07/why-im-learning-data-science/" target="_blank" rel="noopener noreferrer">Data Science</a>, <a href="https://thomaslarock.com/2018/04/big-data-certification/" target="_blank" rel="noopener noreferrer">Big Data</a>, and <a href="https://thomaslarock.com/2018/08/achievement-unlocked-certified-in-artificial-intelligence/" target="_blank" rel="noopener noreferrer">Artificial Intelligence</a>. Those studies have provided me the opportunity to explore the world of data that exists. For example, <a href="https://www.kaggle.com/" target="_blank" rel="noopener noreferrer">Kaggle</a> is a great source of data. They also offer competitions, if you are the type of person that <a href="https://www.kaggle.com/competitions" target="_blank" rel="noopener noreferrer">enjoys money</a>.</p>



<p>Today I want to spend time showing you an example of dirty data. Years ago, <a href="https://powerpivotpro.com/2011/10/friday-bonus-ufo-sightings-hallucinogen-use/" target="_blank" rel="noopener noreferrer">Rob Collie showed us that UFO pilots are attracted to LSD, but prefer ecstasy</a>. As a follow up, let's look at the National UFO Reporting Center Online Database. Or, as I like to call it, "what happens when you allow stoners to perform data entry".</p>



<p>Let's get started.</p>



<h2 id="h-dirty-data-example">Dirty Data Example</h2>



<p>The&nbsp;National UFO Reporting Center Online Database can be found at:&nbsp;<a href="http://www.nuforc.org/webreports.html" target="_blank" rel="noopener noreferrer">http://www.nuforc.org/webreports.html</a></p>



<p>Navigate to that page, and once there click on the&nbsp;‘Index by STATE’ link. Now notice at the top of the page there is a link for ‘UNSPECIFIED/INTERNATIONAL’.</p>



<p>OK, so let's pause here for a minute.&nbsp;Judging by the word STATE and the list of US states and Canadian provinces, I assume this database has a North American focus. But there are more than 8,000 sightings listed as 'UNSPECIFIED/INTERNATIONAL'. This doesn't seem right to me, and I am now curious to know where the majority of these sightings are taking place. So, let's download some data and get it into a map inside of PowerBI.</p>



<p>First, let's examine that data by clicking the link. I want to see what the data looks like, and here is what I find:</p>



<div class="wp-block-image"><figure class="aligncenter is-resized"><a href="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-ufo.jpg"><img src="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-ufo.jpg" alt="Dirty data UFO" class="wp-image-19351" width="525" height="254"/></a></figure></div>



<p>Then, using Excel we import the data, using the 'From Web' option in the Data tab:</p>



<div class="wp-block-image"><figure class="aligncenter is-resized"><a href="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-excel.jpg"><img src="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-excel-600x188.jpg" alt="Dirty data UFO excel" class="wp-image-19353" width="450" height="141"/></a></figure></div>



<p>This downloads the data into Excel, and I will save the data as a CSV file. I will then import the CSV file into PowerBI.&nbsp;After the data is loaded I will create a map:</p>



<div class="wp-block-image"><figure class="aligncenter is-resized"><a href="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-ufo-map.jpg"><img src="https://thomaslarock.com/wp-content/uploads/2018/10/dirty-data-ufo-map.jpg" alt="Dirty data UFO map PowerBI" class="wp-image-19354" width="600" height="394"/></a></figure></div>



<p>So far this has taken me less than 10 minutes to download roughly 8,000 rows, import those rows into PowerBI, generate this map, and see…I see…</p>



<p>Look at those bubbles inside the USA. I suppose those are "international" to someone not in the USA. But it is clear there is a disconnect in how this website is expecting data to be entered, and how the users are entering data. Alcohol is likely a factor, I'm certain. But it's clear to me that we have dirty data.</p>



<p>Just look at the first row. The entry says 'Kiev (Ukraine)'.&nbsp;That’s two different labels (City, Country) in one field (i.e., column). This could explain why the database classifies this entry as unspecified.</p>



<p>The PowerBI map made it easy for me to visualize the dirty data. But you won't be working with location data on every project. You'll need to find different ways to determine if your data is dirty.</p>



<p>[SPOILER ALERT]: All data is dirty.</p>



<h2 id="h-data-has-always-been-dirty">Data Has Always Been Dirty</h2>



<p>There's a <a href="https://www.youtube.com/playlist?list=PL2FF649D0C4407B30" target="_blank" rel="noopener noreferrer">series of videos from Dr. Richard Hammond</a>, taken from lectures in 1995. I believe these videos should be required viewing for every data professional. There's one video, in particular, that I'd suggest you watch, as it is related to the topic today. The video title is "<a href="https://www.youtube.com/watch?v=N-0kk-qDpuI" target="_blank" rel="noopener noreferrer">Unreliable Data</a>", and it is Dr. Hammond delivering a no-nonsense lecture recalling his experiences with data over many decades.</p>



<p>[Side note - this is a wonderful example of how you can deliver a great presentation without needing fancy slides, pictures of cats, or code demos.]</p>



<p>Dr. Hammond has some wonderful insights to share in the video. Have a look:</p>



[embed]https://www.youtube.com/watch?v=N-0kk-qDpuI[/embed]



<p>Watch and listen to the wisdom Dr. Hammond shares with the class. Here's the TL:DR summary for you:</p>



<blockquote class="wp-block-quote"><p><strong>There is never time to do it right, but somehow you think there will be time to fix it later</strong>.</p></blockquote>



<p>OK, so where does all this dirty data come from?</p>



<h2 id="h-the-origins-of-dirty-data">The Origins of Dirty Data</h2>



<p>The title of this post is&nbsp;a quote from my friend Oz du Soleil (<a href="http://ozdusoleil.com/" target="_blank" rel="noopener noreferrer">website</a> | <a href="https://twitter.com/ozexcel" target="_blank" rel="noopener noreferrer">@ozexcel</a>). It came up in conversation one night at the Microsoft MVP Summit many years ago. For a data professional like myself,&nbsp;it's one of those phrases that just sticks in your head and never leaves. Mostly because I spend lots of time cleaning data for various projects.</p>



<p>Your data gets dirty through a variety of ways. Here's but a few examples:</p>



<p><strong>Duplicate data</strong> - A single event is recorded and entered twice into your dataset.<br><strong>Missing data</strong> - Fields that should contain values, do not.<br><strong>Invalid data</strong> - Information not entered correctly, or not maintained.<br><strong>Bad data</strong> - Typos, Transpositions, variations in spelling, or formatting (say hello to unicode!)<br><strong>Inappropriate data&nbsp;</strong>- Data entered in the wrong field.</p>



<p>As Dr. Hammond suggests, it's difficult to determine if data is ever clean. Even scientific constants have a degree of accuracy. They are "good enough", but not perfect.</p>



<p>Data's ultimate purpose is to drive decisions.&nbsp;<em>Bad data means bad decisions</em>.</p>



<p>As a data professional it is up to us to help keep data "good enough" for use by others. We have to think of ourselves as data janitors.</p>



<p>But nobody goes to school to become a data janitor.&nbsp;Let's talk about options for cleaning dirty data.</p>



<h2 id="h-data-cleaning-techniques">Data Cleaning Techniques</h2>



<p>Here's a handful of techniques that you should consider when working with data. Remember, all data is dirty, you won't be able to make it perfect. Your focus should be making it "good enough" to pass along to the next person.</p>



<p>The first thing you should do when working with a dataset is to examine the data. Ask yourself "<strong>does this data make sense</strong>"? That's what we did in the example above. We looked at the first few rows of data and found that both the city and country listed inside of one column.</p>



<p>Then, before you do anything else, <strong>make a copy, or backup, of your data before you begin to make the smallest change</strong>. I cannot stress this enough.</p>



<p>OK, so we've examined the data to see if it makes sense, and we have a copy. Here's a few data cleaning techniques.</p>



<p><strong>Identify and remove duplicate data</strong> - Tools such as Excel and PowerBI make this easy. Of course, you'll need to know if the data is duplicated, or two independent observations. For relational databases we often use <a href="https://docs.microsoft.com/en-us/sql/relational-databases/tables/create-primary-keys?view=sql-server-2017" target="_blank" rel="noopener noreferrer">primary keys</a> as a way to enforce this uniqueness of the records. But such constraints aren't available for every system that is logging data.</p>



<p><strong>Remove data that doesn't fit</strong> - Data entered that doesn't help you answer the question you are asking.&nbsp;In our example, if I want North America sightings, I would remove all entries logged as outside North America.</p>



<p><strong>Identify and fix issues with spelling, etc.</strong> - There's lots of ways to manipulate strings to help get your data formatted and looking pretty. For example, you could use the TRIM function to remove spaces from the text in a column, then sort the data and look for things like capitalization and spelling. There's also regional terms, like calling a sugary beverage "pop" or "soda".</p>



<p><strong>Normalize data</strong> - Set a standard for the data. If the data is a number, make sure it is a number, not text. If it is categorical, make sure it has entries that apply for that category. Spelling, capitalization, etc., are all ways to set standards and normalize data to some degree.</p>



<p><strong>Remove outliers</strong> - But only when it makes sense to do so! If the outlier was due to poor collection, then it could be safe to remove. Dr. Hammond suggested that "for 90% of the time, the next independent measurement will be outside the 90% confidence interval". I trust his judgement here, so be mindful that outliers are innocent until proven guilty.</p>



<p><strong>Fix missing data</strong> - This gets...tricky. You have two options here. Either you remove the record, or you update the missing value. Yes, this is how we get faux null values.&nbsp;For categorical data I suggest you set the data to the word 'missing'. For numerical data, set the value to 0, or to the average of the field. I avoid using faux nulls for any data, unless it makes sense to note the absence of information collected. Your mileage may vary.</p>



<h2 id="h-summary">Summary</h2>



<p>Life is dirty. So's your data. Get used to it.</p>



<p>I encourage you to work with datasets, like the ones at Kaggle. Then walk through the techniques I discussed here. Ask yourself if the data makes sense. Think about what you might do to make the data cleaner, if necessary.</p>



<p>Get familiar with tools like Python, Excel, and PowerBI and how they can help you with data cleaning.</p>



<p>And remember that no matter how much you scrub that data, it will never be clean, but it will be good enough.</p>