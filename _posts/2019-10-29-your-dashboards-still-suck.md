---
layout: post
title: Your Dashboards Still Suck
date: '2019-10-29 11:51:52 +0000'
categories:
- Data Analytics
- MSSQL
- SQL MVP
tags:
- data analytics
---

<p>I've already written a post about how <a aria-label="dashboards are a horrible way to communicate (opens in a new tab)" rel="noreferrer noopener" href="https://thomaslarock.com/2018/03/we-need-to-talk-about-dashboards/" target="_blank">dashboards are a horrible way to communicate</a>. I'm here today to remind you that your dashboards still suck. Let's start with the most recent example.</p>



<div class="wp-block-image"><figure class="aligncenter"><img src="https://i1.wp.com/thomaslarock.com/wp-content/uploads/2019/10/gas.jpg?fit=600%2C302&amp;ssl=1" alt="" class="wp-image-19660"/></figure></div>



<p>This image is a useless piece of information. I'm certain somewhere there is a developer proud of how they took a donut chart and made it prettier. And I would agree it is pretty...it's pretty useless.</p>



<p>Let's break it down.</p>



<p>This graphic doesn't tell me anything about the amount of fuel, in gallons (or liters for my non-US readers). And that's really the most important piece of information. A close second is displaying the range (number of miles/km remaining before empty). Telling me I have 35% fuel remaining has no value unless you know (1) how much fuel is left or (2) how far you can travel before empty.</p>



<p>This is why your dashboards still suck. Right now, you've built something, some chart, and the chart is hiding data behind an aggregate, a summation, or a percentage. And I bet it is leading to bad business decisions. </p>



<p>When I pull up to the pump the question I have is "how many gallons can I put in my Jeep", not "how much percentage". (As an aside, Jeep does not provide me the size of my tank in the operating manual. I needed to <a aria-label="Google that information (opens in a new tab)" rel="noreferrer noopener" href="https://www.autoblog.com/buy/2019-Jeep-Wrangler+Unlimited-Sahara__4dr_4x4/specs/" target="_blank">Google that information</a>, it's 21.5 gallons). If the app can tell me I am at 35% full, they can also tell me I have 7.525 gallons remaining, or that I need 13.975 gallons to fill my tank.</p>



<div class="wp-block-image"><figure class="aligncenter"><a href="https://thomaslarock.com/wp-content/uploads/2019/10/image-2.png" target="_blank" rel="noreferrer noopener"><img src="https://thomaslarock.com/wp-content/uploads/2019/10/image-2-600x452.png" alt="You can only see 35% of my new Jeep. " class="wp-image-19659"/></a><figcaption>You can only see 35% of my new Jeep. </figcaption></figure></div>



<p>Stop building images that take good data and make it useless. </p>



<p>You're better than this. </p>