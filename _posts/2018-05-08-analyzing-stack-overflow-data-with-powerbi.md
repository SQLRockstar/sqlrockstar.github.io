---
layout: post
title: Analyzing Stack Overflow Data Directly and with PowerBI
date: '2018-05-08 13:24:51 +0000'
categories:
- Data Analytics
- MSSQL
- SQL MVP
- SQL Server 2017
tags:
- data analysis
- Stack Overflow
---

Last week, Stack Overflow acknowledge their culture issues <a href="https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/">with this post</a>. I’m glad to see them talking about these issues publicly, and they are actively looking to make things better. Admitting you have a problem is a good first step.

That post reminded me that I’ve been meaning to explore some Stack Overflow data. They make their databases public. You don’t need to download them, you can query the databases directly. Just head over to <a href="https://data.stackexchange.com/stackoverflow/query/new">https://data.stackexchange.com/stackoverflow/query/new</a> and get started. In the upper right you will see an icon that is also a drop-down menu:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-dropdown.jpg"><img class="aligncenter size-full wp-image-19031" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-dropdown.jpg" alt="Stack Overflow query database dropdown" width="328" height="98" /></a>

&nbsp;

I’m going to switch sites to the DBA Stack Exchange because that’s the one I’ve used the most and I thought it might be interesting to find myself in the results.

&nbsp;
<h2>Stack Overflow Users</h2>
First, let’s look at the users. I want to know just how many people are using the forum. A simple count will tell me how many users are in the system:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users.jpg"><img class="aligncenter size-full wp-image-19032" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users.jpg" alt="Stack Overflow count users" width="209" height="89" /></a>

&nbsp;

And the result:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-result.jpg"><img class="aligncenter size-full wp-image-19033" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-result.jpg" alt="Stack Overflow count users result" width="170" height="113" /></a>

&nbsp;

That’s a good number of users. The site is over 7 years old, so now I’m wondering about the rate at which new users have been signing up. We can get that info, here's one way:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-by-year.jpg"><img class="aligncenter size-large wp-image-19034" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-by-year-600x91.jpg" alt="Stack Overflow count users by year" width="600" height="91" /></a>

&nbsp;

And the result:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-by-year-result.jpg"><img class="aligncenter size-full wp-image-19035" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-users-by-year-result.jpg" alt="Stack Overflow count users by year result" width="174" height="313" /></a>

&nbsp;

It seems that 2017 had a dip in new users to the site, but 2017 was still the 2nd highest year. This dip in new users may have been something that Stack Overflow has noticed across all their websites. If fewer people are signing up, or being engaged, then it's time to talk about the reasons why people are staying away. A quick query against the main Stack Overflow database shows me that the number of users is increasing. So, the decline isn't being seen by every site. Or maybe they are attracting more of the <a href="https://www.urbandictionary.com/define.php?term=brogrammer" target="_blank" rel="noopener">brogrammers</a> that are contributing to the negative culture. I don't have enough data at this point to say one way or another.

OK, enough about the users, let's look at the posts.

&nbsp;
<h2>Stack Overflow Posts</h2>
Next, we will look at the Posts tables. This is the table that contains the actual questions and answers.

A simple count tells us that there are 154,806 posts. With only 122k users, that means a majority of users must be posting only once. Let’s look at the posts over time, same as we did for the users:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-year-result.jpg"><img class="aligncenter size-full wp-image-19036" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-year-result.jpg" alt="Stack Overflow count posts by year results" width="163" height="408" /></a>

&nbsp;

Wait, we have posts from 2008, but users only go back to 2011? Yep, because questions can be migrated from one Stack Overflow site to another, it’s possible for us to have questions with dates <em>from before the DBA Stack Exchange site even existed</em>.

[Welcome to the wonderful world of data analytics, where you spend 95% of your time as a Data Janitor, helping to clean up what needs cleaning and explaining weird stains on the carpet to visitors.]

So, if questions have been migrated, we don’t really know how many of the posts are from DBA SE users or not. Of course, it’s possible that a user of DBA SE had a question migrated from another site. But, hey, it’s close enough for me, because Data Janitor.

&nbsp;
<h2>Stack Overflow Posts from Unique Users</h2>
Next, we look at the number of posts grouped by the OwnerUserId:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid.jpg"><img class="aligncenter size-full wp-image-19037" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid.jpg" alt="Stack Overflow count posts by userid" width="354" height="115" /></a>

&nbsp;

I did the ORDER BY here so we could see the number of posts without an OwnerUserId. These are the posts migrated from other sites:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid-result.jpg"><img class="aligncenter wp-image-19038 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid-result.jpg" alt="Stack Overflow count posts by userid result" width="228" height="560" /></a>

&nbsp;

So, 2692 questions have been migrated. That’s a small fraction of the 154k total number. But what I found more interesting here was the total number of rows returned:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid-result-rowcount.jpg"><img class="aligncenter wp-image-19039 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-by-userid-result-rowcount.jpg" alt="Stack Overflow count posts by userid result rowcount" width="221" height="49" /></a>

&nbsp;

We have 122k users, but only 40k of them have written a post. What are the other 82k people doing?

Well, it’s possible that the other 82k have written a post and deleted it. Or, they haven’t written a post and have only left a comment. I’ll leave that analysis as an exercise for the reader. I have other questions I want to answer before I worry about those.

Here is a question I’ve thought about: How many users of DBA SE sign up, ask one question, and leave? We can filter the previous query:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-single-posts-by-userid.jpg"><img class="aligncenter wp-image-19040 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-single-posts-by-userid.jpg" alt="Stack Overflow count single posts by userid " width="332" height="95" /></a>

And the resulting rowcount:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-single-posts-by-userid-result-rowcount.jpg"><img class="aligncenter wp-image-19041 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-single-posts-by-userid-result-rowcount.jpg" alt="Stack Overflow count single posts by userid result rowcount" width="259" height="42" /></a>

&nbsp;

We have 26,801 users that have 1 post (or fewer). This means that we have just under 14k users asking two questions or more.

Suddenly, this website seems a whole lot smaller. I know that the Stack Overflow websites get a lot of views, there’s no question. But there are millions of database professionals. The answers at DBA SE are coming from a very small subset of database professionals.

&nbsp;
<h2>Stack Overflow Posts with Quick Answers</h2>
If you are like me, you’ve noticed questions posted at DBA SE by someone who is a new user, and there is a detailed answer in a matter of minutes. I’ve often wondered about this. I’m certain two users could collaborate the timing of the question and the answer. There are no rules against doing so.

I get a lot of questions emailed to me weekly from people all over the world. It would not be difficult to search DBA SE to see if the question is listed. If not, I could ask the person to ask the question, email me when it is posted, and I could then quickly post my answer for them to mark as correct.

Let’s see what the data has to say about this. First, how many users have been created and asked questions within the first 15 minutes:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-answered-quickly.jpg"><img class="aligncenter wp-image-19043 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-answered-quickly.jpg" alt="Stack Overflow count posts answered quickly" width="538" height="117" /></a>

There’s nothing odd about signing up and asking a question, that’s the whole point of the site. The number of users returned is 25,264. How many of these quick-questions users do we have over time:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-answered-quickly-by-year.jpg"><img class="aligncenter wp-image-19044 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-count-posts-answered-quickly-by-year.jpg" alt="Stack Overflow count posts answered quickly by year" width="175" height="409" /></a>

&nbsp;

It seems we hit a peak in 2015 and have had a decline in the number of users being created and asking a question within 15 minutes.

Now, I want to know how many of these posts had a *reply* within 15 minutes. I’m going to create a CTE to get this done and join back to the Posts table. I want to find all posts with a ParentId that is a post asked within 15 minutes of being created:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly.jpg"><img class="aligncenter wp-image-19045 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly.jpg" alt="Stack Overflow show posts answered quickly " width="565" height="291" /></a>

&nbsp;

That query will return 25,602 rows, but the result set contains all replies, not just answers. I'm curious to know how many questions are marked answered within 15 minutes. So, let’s make an adjustment. We will focus on the posts marked as an answer, and group by user id:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-count.jpg"><img class="aligncenter wp-image-19046 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-count.jpg" alt="Stack Overflow show posts answered quickly count" width="553" height="354" /></a>

And the results:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-counted-by-userid.jpg"><img class="aligncenter wp-image-19047 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-counted-by-userid.jpg" alt="Stack Overflow show posts answered quickly counted" width="172" height="560" /></a>

&nbsp;

That’s a lot of questions to have marked as an answer within 15 minutes of being posted. Of course, this is over 7 years. We could break it down a bit further if desired, and group into years to get a result that looks like this:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-counted-by-userid-year.jpg"><img class="aligncenter wp-image-19048 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-answered-quickly-counted-by-userid-year.jpg" alt="Stack Overflow show posts answered quickly counted by year" width="245" height="315" /></a>

&nbsp;

Looks to me like this user was simply active (*very* active) for a handful of years and has since tapered off.

&nbsp;
<h2>Stack Overflow Length of Answers</h2>
Asking a question and getting a quick reply seems to be common enough for the majority of users. However, there is one place where we might find an anomaly. If a person was to produce an answer of considerable length in a short amount of time, that might indicate that they were trying to game the system for points. The length of the posts is stored in characters with NVARCHAR(MAX). And the bulk of those characters are the result of code snippets, which are often cut and pasted. So, length by itself isn't an indication of something wrong. But the number of words *might* give a hint. This would be true if we were to find a pattern for one user providing many long-form answers to question posted just a few minutes prior.

So, let’s look for questions that have an accepted answer within 5 minutes and examine the length of the replies to see if there is anything unusual. I can’t view the whole text in the results window, but there is an option to download to CSV. So, I will download the results and use Excel to view the longest answer given within five minutes:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-long-answer.jpg"><img class="aligncenter size-large wp-image-19049" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-query-show-posts-long-answer-600x184.jpg" alt="" width="600" height="184" /></a>

&nbsp;

I could have written some T-SQL to parse our words by looking for spaces, and skipping over &lt;code&gt; blocks. But I used Excel here because (1) it's easier, and (2) I wanted you to be aware that the website allows for you to export to CSV.

The second result is an answer with some code and more than 2,300 words. That’s a lot of typing in less than 5 minutes. I believe this answer was prepared in advance.

Not that there’s anything wrong with that. I was just curious to know if such things were happening. To me, this shows that the user(s) involved are more interested in points, and strutting their knowledge, than in helping others.

That's their right. I'm not complaining, just observing what I see in the data.

&nbsp;
<h2>Importing Stack Overflow Data in PowerBI</h2>
I’ve spent this whole post showing you some queries that you can run against the Stack Overflow websites for yourself. There’s no need for any additional tools. If you want to do additional analysis, you will need to export the data. The issue you will find is that the database query interface provided by Stack Overflow limits you to only 50,000 rows of results.

There is an easy answer. You can download the Stack Exchange database for yourself. Go to <a href="https://archive.org/details/stackexchange">https://archive.org/details/stackexchange</a> and pick the repository you want. The full list can be found here <a href="https://archive.org/download/stackexchange">https://archive.org/download/stackexchange</a>.

I started by downloading the <a href="https://archive.org/download/stackexchange/dba.stackexchange.com.7z">https://archive.org/download/stackexchange/dba.stackexchange.com.7z</a> file. When I open it up it contains XML files, one for each table:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-data-into-power-bi.jpg"><img class="aligncenter size-full wp-image-19051" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-data-into-power-bi.jpg" alt="Stack Overflow data imported into PowerBI" width="201" height="241" /></a>

&nbsp;

I could try to import those into a database, but I won’t bother. My end goal is to get insights into the data. So, I’m going to load these files into PowerBI, because PowerBI desktop lets me import XML files.

Just go to ‘Get Data’, then ‘Other’, and you’ll find the XML option:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-import.jpg"><img class="aligncenter wp-image-19052 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-import-552x600.jpg" alt="Stack Overflow data imported into PowerBI" width="552" height="600" /></a>

&nbsp;

The downside to this is I must load the files one at a time. The upside is that PowerBI will detect relationships for me.

Once the data is loaded, I’m only a few clicks away from generating some graphs that provide some visualization to the results we’ve discovered above. For example, let’s look at user creation over time. Here I can see the number of new users each year along with a running total of the overall number of users:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-chart-users.jpg"><img class="aligncenter wp-image-19053 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-chart-users-600x414.jpg" alt="Stack Overflow PowerBI users over time" width="600" height="414" /></a>

&nbsp;

I can use PowerBI to analyze the entire dataset, looking for relationships that I didn’t know existed. Here’s another example, I can quickly see if there is a relationship between the length of the text and the score of a post:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-chart-scatter.jpg"><img class="aligncenter wp-image-19054 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/05/so-pbi-chart-scatter-600x351.jpg" alt="Stack Overflow PowerBI scatterplot" width="600" height="351" /></a>

&nbsp;

PowerBI makes exploring the Stack Overflow data easy. Use what works best for you. That's what I did for this post. I started it all by using PowerBI to explore the data. I recognize that not everyone uses PowerBI and I wanted to make sure you could get started on doing analysis with whatever tool you want. So I spent the first part here showing you how to query the database directly. I'm hoping to do some additional analysis over time on this data using PowerBI and share with you what interesting things I may find.

&nbsp;
<h2>Summary</h2>
Stack Overflow has publicly discussed that their websites may not have been the most welcoming. They make public their data on users and activity. I wanted to analyze the data to see if I could find examples of behavior that may be more focused on earning points than helping others. I think this gamification across the Stack Overflow sites is part of the issue they have currently. With gamification comes competition. And with competition, we get a culture that is not as welcoming as what Stack Overflow is stating they want to achieve.

If the gamification in Stack Overflow exists, there will always be people that want to earn as many points as possible. There’s nothing wrong with that. It’s what they need. It’s how they measure their self-worth. And for some, it is an opportunity to get some free marketing by posting links to products and blogs. But if the culture created by these few users are keeping others away, then we are missing out on better answers to our questions.

Future analysis should include reviewing the comments, perhaps some sentiment analysis. I will try to think of ways the Stack Overflow data may provide some insight into the user activities that are not welcoming to others.

&nbsp;
<h2>References</h2>
<a href="https://archive.org/details/stackexchange" target="_blank" rel="noopener">https://archive.org/details/stackexchange</a>

<a href="https://archive.org/download/stackexchange" target="_blank" rel="noopener">https://archive.org/download/stackexchange</a>

<a href="https://data.stackexchange.com/stackoverflow/queries" target="_blank" rel="noopener">https://data.stackexchange.com/stackoverflow/queries</a>

<a href="https://data.stackexchange.com/stackoverflow/query/new" target="_blank" rel="noopener">https://data.stackexchange.com/stackoverflow/query/new</a>

<a href="https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/" target="_blank" rel="noopener">https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/</a>

&nbsp;
<h2>Queries Used in this Post</h2>
<pre lang="tsql">--Total number of users
SELECT COUNT(*) FROM Users

--Total number of users, grouped by year
SELECT COUNT(Id) as [Total], DATEPART(yy,CreationDate) as [Year]
FROM Users
GROUP BY DATEPART(yy,CreationDate)

--Total number of posts
SELECT COUNT(*) FROM Posts

--Total number of posts, grouped by year
SELECT COUNT(Id) as [Total], DATEPART(yy,CreationDate) as [Year]
FROM Posts
GROUP BY DATEPART(yy,CreationDate)

--Total number of posts, grouped by userid
SELECT COUNT(p.Id), p.OwnerUserId
FROM Posts p
GROUP BY p.OwnerUserId
ORDER BY p.OwnerUserId

--Total number of users with more than one post
SELECT COUNT(p.Id), p.OwnerUserId
FROM Posts p
GROUP BY p.OwnerUserId
HAVING COUNT(p.Id) &lt;= 1

--user created and asks question in 15 minutes
SELECT COUNT(*)
FROM Users u
INNER JOIN Posts p ON u.Id = p.OwnerUserId
WHERE DATEDIFF(mi, u.CreationDate, p.CreationDate) &lt; 15

-- Total number of users created and posting within 15 minutes
SELECT COUNT(p.id), DATEPART(yy, p.CreationDate)
FROM Users u
INNER JOIN Posts p ON u.Id = p.OwnerUserId
WHERE DATEDIFF(mi, u.CreationDate, p.CreationDate) &lt; 15 
GROUP BY DATEPART(yy, p.CreationDate)

--Posts with replies within 15 minutes
WITH Posts_CTE (UserCreate, PostId, PostCreate, ParentId,
AcceptedAnswerId, OwnerUserId, DisplayName)
AS
(
SELECT u.CreationDate AS [UserCreate]
, p.id, p.CreationDate AS [PostCreate]
, p.ParentId, p.AcceptedAnswerId
, p.OwnerUserId, u.DisplayName
FROM Users u
INNER JOIN Posts p ON u.Id = p.OwnerUserId
)

SELECT *
FROM Posts_CTE pcte
INNER JOIN Posts p ON pcte.PostId = p.ParentId
WHERE DATEDIFF(mi, pcte.UserCreate, pcte.PostCreate) &lt; 15
</pre>