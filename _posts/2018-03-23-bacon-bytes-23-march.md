---
layout: post
title: Bacon Bytes for 23-March
date: '2018-03-23 10:14:58 +0000'
categories:
- Bacon Bytes
- Data Security and Privacy
tags:
- bacon bytes
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/bacon_bytes.jpeg"><img class="aligncenter size-large wp-image-18830" src="https://thomaslarock.com/wp-content/uploads/2018/03/bacon_bytes-600x600.jpeg" alt="bacon bytes" width="600" height="600" /></a>

I'm starting something new, a weekly series to recap recent events from the world of technology, business, and data. Probably some sports and entertainment at times, too. Basically, anything I want, because it's my blog.

When I decided to do this I had one simple rule: the word bacon had to be in the title. After that, anything goes.

So, welcome to the inaugural edition of Bacon Bytes. Let's get this started.

The <a href="https://www.engadget.com/2018/03/23/atlanta-government-computers-hit-by-ransomware/" target="_blank" rel="noopener">city of Atlanta has been struck by ransomware</a>, which always serves as a reminder to me to take backups of everything I own. What I find frustrating about this story is the ransomware used has been around since 2015. And it targeted government and healthcare systems. So, Atlanta has had three years to patch their systems. It's hard to feel sorry for them. The ransom is $51k, which sounds like it is cheaper than if they did try to patch, which means someone in the COO office will put together a PowerPoint deck explaining how the attack actually saved them money.

Something I've been meaning to write about for a while now, but haven't done yet, is how <a href="https://www.mysanantonio.com/real-estate/article/Microsoft-buys-80-million-data-center-on-far-12330383.php" target="_blank" rel="noopener">Microsoft is strategically buying existing data centers and migrating them to Azure</a>. This is the ultimate in "lift and shift", folks. It's also brilliant. Instead of building data centers from scratch, Microsoft can simply convert existing ones to be Azure. The company (in this case Chevron) becomes an Azure customer, Microsoft gets a new data center in the region and increases capacity at a fraction of the cost otherwise. So, the next time you think you can't lift and shift one of your production systems you should think about how Microsoft is able to lift and shift an entire company.

On a related note, let's talk about failovers. There's a <a href="https://medium.com/netflix-techblog/project-nimble-region-evacuation-reimagined-d0d0568254d4" target="_blank" rel="noopener">great article out there on Project Nimble</a> and how Netflix decreased a region failover from an hour to less than 10 minutes. Granted, you may not have the engineering resources and infrastructure that Netflix does. But the post should help you understand how to diagnose your current failover strategy and look to streamline. FOlks, we are all data hoarders. We only accumulate more data, we never archive or delete anything. That means our time to failover and failback increases just a little bit with each passing day. Do yourself a favor and take the time to examine your failover process now. You don't want to get to a point where you are "too big to failover".

<a href="https://www.howtogeek.com/346783/how-to-stop-facebook-giving-your-data-to-third-parties/" target="_blank" rel="noopener">How to Stop Facebook Giving Your Data to Third Parties</a>. Stop using Facebook, problem solved. If you think for a moment that Facebook cares about your security and privacy then you are a fool. Platforms such as Facebook are free because *you* are the product. And if you want to be scared out of your pants, <a href="https://www.howtogeek.com/346197/ever-wonder-how-much-facebook-knows-about-you-here%E2%80%99s-how-to-see/" target="_blank" rel="noopener">go read this and learn how much Facebook knows about you</a>.

I've been a fan of autonomous cars for years now. Well, to be fair, I want flying cars, but I digress. The past few years we've seen a lot of progress with self-driving cars. Unfortunately this past week an <a href="https://www.mbtmag.com/news/2018/03/experts-uber-self-driving-system-should-have-spotted-woman" target="_blank" rel="noopener">Uber self-driving car killed a pedestrian</a>. From where I sit, I want (and expect) the software to have better reactions than humans. Self-driving cars promised to reduce traffic-related deaths. Warrants mentioning here that as a result of this one accident, Uber suspended all self-driving tests for a thorough investigation. That's likely the first responsible thing Uber has done since, well, ever.

If you ever had doubt about Wall Street understanding technology, check out this piece on the <a href="http://www.businessinsider.com/dropbox-ipo-stock-price-2018-3" target="_blank" rel="noopener">Dropbox IPO happening today</a>. Here are the three main takeaways: Dropbox admits they may never make a profit, they admit they could suffer security breaches, and they are going to be worth $9 billion dollars. Imagine how much money they could make if they could protect our data and turn a profit!

Slack is now making it <a href="http://www.dailymail.co.uk/sciencetech/article-5531583/Slack-releases-new-policy-lets-bosses-read-employees-messages.html" target="_blank" rel="noopener">easier for your boss to read your private messages</a>. As if I needed yet another reason to <a href="https://thomaslarock.com/2018/03/why-im-leaving-slack-communities/" target="_blank" rel="noopener">dislike Slack</a>, this updated policy serves as a reminder to us all that anything we do that is digital is tracked and recorded for all time.

See you next week.