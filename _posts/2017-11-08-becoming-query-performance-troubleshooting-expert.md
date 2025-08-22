---
layout: post
title: Becoming a Query Performance Troubleshooting Expert
date: '2017-11-08 13:30:35 +0000'
categories:
- MSSQL
- PASS
- Professional Development
- SQL MVP
- SQL Server Performance
tags:
- MSSQL
- performance
- performance tuning
- sql server
- Troubleshooting
---

Every DBA wants to become an expert in query performance troubleshooting.

Not every DBA is willing to put in the time and effort it takes to become an expert.

The #hardtruth here is that to become an expert in anything you need a combination of two factors: experience and knowledge. You don't become an expert overnight, or by going to any one conference, or by attending any particular class.

Today I'm here to share some knowledge to help get you started on the path to expert query performance troubleshooting. The first step is to watch this video from the PASS Summit in 2010. Yes, that's right, it's from <span style="text-decoration: underline;">seven years ago</span>. The video is 77 minutes long, make certain to set aside enough time:

<iframe src="https://www.youtube.com/embed/Nbxg5crWq38" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

One of the main takeaways from this video I want you to have is the fact that troubleshooting performance is not always rocket surgery. I'm a huge fan of using "buckets" to help troubleshoot issues. It's one of the reasons I fell in love with wait events about 2006.

In the video, these are the first buckets discussed: <em>Are <strong>all</strong> queries affected, or just a <strong>subset</strong> of queries affected?</em>

If all queries are having performance issues then you will want to examine settings that affect the entire instance, such as memory settings, or perhaps issues with NUMA nodes. You will want to do this first before trying to tune any one particular query.

In comparison, if a subset of queries (or users, or a particular application) then you will want to focus your efforts on those queries first. Otherwise, you are wasting time trying to fix one query without addressing the root cause of the performance issue affecting all queries.

The ability to diagnose "all versus some" in the first five minutes of triage during a production down situation will get you to a root cause faster. Thinking in buckets will allow for you to build an action plan to bring performance back to acceptable limits.
<h2>Summary</h2>
We all start out with zero knowledge.

Sure, the video is old. And yes, the tools available now are better. But the methods have not changed much. Have a baseline. Know what is good. Use buckets.

Also, this video has less than 3,000 views. Let's get this video in front of the people gravitating to SQL Server and want to become an expert.