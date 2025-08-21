---
layout: post
title: Pingdom Made Me Stop Using Disqus for Blog Comments
date: '2018-06-12 11:22:14 +0000'
categories:
- Blogging
tags:
- disqus
- pingdom
---

Last week <a href="https://hbr.org/2018/06/why-microsoft-is-willing-to-pay-so-much-for-github" target="_blank" rel="noopener">Microsoft bought GitHub</a> and there was a flood of "the sky is falling" from the anti-Microsoft trolls as well as the typical knee-jerk reactionary type folks we find in the tech industry. It reminded me of the time <a href="https://www.solarwinds.com/company/press-releases/solarwinds-acquires-pingdom" target="_blank" rel="noopener">four years ago when SolarWinds bought Pingdom</a>. The day the deal went down I read comments from current users saying they would start looking for a new service. We hadn't even touched anything and people were in a panic.

So, after the events last week, it got me thinking how I have not written many (or any?) posts about available free tools such as Pingdom. So, here's one for today. I will use the <a href="https://tools.pingdom.com/#!/eyMvfE/https://thomaslarock.com/2018/06/hey-cortana/" target="_blank" rel="noopener">free website performance tool from Pingdom</a> to do performance testing against this blog. I'll run a quick test against my "<a href="https://thomaslarock.com/2018/06/hey-cortana/" target="_blank" rel="noopener">Hey Cortana</a>" post from last week, with Disqus enabled at first then disabled.

Here's the result with Disqus enabled:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_enabled.jpg"><img class="aligncenter size-large wp-image-19177" src="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_enabled-600x195.jpg" alt="Pingdom Disqus enabled" width="600" height="195" /></a>

&nbsp;

13 seconds to load the page? That seems like a bit of a drag to anyone trying to read my post. I know I wouldn't wait around that long for a page to load (and from my page stats, I can tell you don't either).

Further down the Pingdom test results page, I find details on the number of requests and content size broken down by domain:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_enabled_by_domain.jpg"><img class="aligncenter size-large wp-image-19178" src="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_enabled_by_domain-600x227.jpg" alt="Pingdom Disqus enabled by domain" width="600" height="227" /></a>

&nbsp;

I see 14 requests from Disqus, with a sum total of 413.27KB. Roughly one-third of the entire 1.2MB page size, just from Disqus.

Now, let's have a look at the same page, but this time with Disqus disabled:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_disabled.jpg"><img class="aligncenter size-large wp-image-19179" src="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_disabled-600x193.jpg" alt="Pingdom Disqus disabled" width="600" height="193" /></a>

&nbsp;

The page size is half as much as before, and the load time is about 90% faster. The total number of requests went from 156 down to 52, a nice decrease.

Let's look at the content and requests by domain:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_disabled_by_domain.jpg"><img class="aligncenter size-large wp-image-19180" src="https://thomaslarock.com/wp-content/uploads/2018/06/pingdom_disqus_disabled_by_domain-600x222.jpg" alt="Pingdom Disqus disabled by domain" width="600" height="222" /></a>

&nbsp;

The Disqus requests are gone. As a result, this blog will perform better for my readers.

Disqus no longer serves any purpose for me or my readers. As a result, I have removed it from this blog. Thanks to Pingdom I was able to identify this easy change to improve the performance of my blog. I have some additional cleanup to do for this blog. I will continue to use Pingdom to help me navigate the location of performance tuning opportunities.

If you are so inclined I would advocate that you try Pingdom for your own blogs and websites.