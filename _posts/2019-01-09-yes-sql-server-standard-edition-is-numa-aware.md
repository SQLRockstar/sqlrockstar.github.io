---
layout: post
title: Yes, SQL Server Standard Edition is NUMA Aware
date: '2019-01-09 15:21:52 +0000'
categories:
- SQL MVP
- SQL Server 2016
- SQL Server 2017
- SQL Server Performance
tags:
- NUMA
- sql server 2017
---

<p>At VMworld in Barcelona this year there arose a question regarding SQL Server Standard edition and if it is NUMA aware. I was certain the answer was "yes", but it was pointed out to me that the documentation says otherwise. </p>



<p>Sure enough, here is the relevant piece of information from <a href="https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-2017">https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-2017</a>:</p>



<figure class="wp-block-image"><img src="https://thomaslarock.com/wp-content/uploads/2019/01/sql-standard-numa-aware-587x600.jpg" alt="SQL Server Standard NUMA aware" class="wp-image-19437"/></figure>



<p>This was a topic for discussion because I'm always reminding people about the benefits of being able to run a SQL Server workload inside of a single NUMA node when possible. So I was taken aback when people were pointing out that SQL Server Standard edition was not NUMA aware. </p>



<p>It didn't take long for me to find some relevant links about SQL Server and NUMA, because <a rel="noreferrer noopener" aria-label="I've got a list of posts regarding SQL Server 2016 (opens in a new tab)" href="https://thomaslarock.com/2016/06/sql-server-2016-just-runs-faster/" target="_blank">I've got a list of posts regarding SQL Server 2016</a>. At the bottom of that post is a link to this post by Bob Ward:</p>



<p><a rel="noreferrer noopener" href="https://blogs.msdn.microsoft.com/bobsql/2016/11/29/how-it-works-it-just-runs-faster-auto-soft-numa/" target="_blank">How It Works (It Just Runs Faster): Auto Soft NUMA</a></p>



<p>Bob clearly talks about SQL Server Standard edition and soft NUMA in the post. However, there is also a quote in there that is worth noting:</p>



<blockquote class="wp-block-quote"><p>"Standard Edition and CAL based licensing can restrict how many processors SQL Server can use."</p><cite>Bob Ward</cite></blockquote>



<p>And thus, we start to understand why the documentation suggests that SQL Server Standard edition is not NUMA aware. It's because Standard has limits on the amount of hardware available. </p>



<p>This is leading to confusion for SQL Server customers. It would be better for Microsoft to update the documentation to reflect that SQL Server Standard is NUMA aware. Perhaps add an additional footnote, as they have footnotes for other features in that same section. </p>



<p>I like that idea so much I decided to do my <a rel="noreferrer noopener" aria-label="first pull request for Microsoft documentation (opens in a new tab)" href="https://docs.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?view=sql-server-2017" target="_blank">first pull request for Microsoft documentation</a>. </p>



<figure class="wp-block-image"><img src="https://thomaslarock.com/wp-content/uploads/2019/01/sql-standard-numa-aware-pull-request-600x360.jpg" alt="SQL Server Standard NUMA aware pull request" class="wp-image-19438"/></figure>



<p>Here's hoping they like my suggestion enough to consider updating the documentation and remove the confusion for customers. </p>