---
layout: post
title: SQL Slammer Is Back. Here's What You Need to Know
date: '2017-02-20 08:23:01 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
tags:
- data privacy
- data security
- sql slammer
---

<a href="https://thomaslarock.com/wp-content/uploads/2014/03/data_theft_rz.jpg"><img class="alignleft wp-image-11298 size-full" src="https://thomaslarock.com/wp-content/uploads/2014/03/data_theft_rz.jpg" alt="SQL Slammer is back. Here's what you need to know." width="215" height="201" /></a>You shouldn't be running unpatched versions of SQL 2000. That's what you need to know.

First reported back in 2002, the SQL Slammer virus caught fire in January of 2003, and spread worldwide. It wasn't much more than a nuisance—it propagated itself and brought networks to a crawl. The worm could have done much more damage, considering that many of those same instances had blank 'sa' passwords (by default!).

But all of that is in the past. Here's what you need to know about SQL Slammer today.

First, this worm infects unpatched SQL 2000 and MSDE instances only. About a month ago, I would have thought that the number of such installs would be quite small. But the recent uptick in Slammer tells me that there are enough of these systems to make Slammer one of the top malware detected at the end of 2016. And a quick search at Shodan shows thousands of public-facing database servers available. And if you want to have some real fun at Shodan®, Ian Trump (<a href="http://www.huffingtonpost.com/author/mike-stahl-722">blog</a> | <a href="https://twitter.com/phat_hobbit">@phat_hobbit</a>) has a <a href="https://twitter.com/phat_hobbit/status/829883612292083714">suggestion for you</a>.

Second, old worms never die; they get saved and re-used every now and then by attackers. Some software vendors get a bit lazy, maybe even have some hubris in thinking they don't need to protect themselves from old attack vectors. Attackers know that vendors are lazy, so they will try old exploits to see what they can find. Right now, they are finding a bunch of unsecured instances of SQL 2000. This does beg the question: "why?" Perhaps they are poking around to distract us from something else. Or maybe they are delivering a modified payload we don't know about yet. With so many legacy systems out there, it's hard to tell what is the real target.

Third, it's quite possible we are seeing IoT devices (or vending machines, POS devices, or remote kiosks in industries like healthcare), which are running older versions of MSDE. If a vendor thought "hey, I can use this old version of MSDE for free" and shipped a few thousand units in the past year, we now see the Slammer attack uptick. This may not be a targeted attack... yet. But it is a possible attack vector by now.
<h2>4 Things You Can Do to Stop SQL Slammer</h2>
Here's what you can do right now.

1. <strong>Stop using old software</strong>. Yes, I know that the software works. And it's cheap. It's also less secure than you might think. Slammer is just one of the known holes. Imagine the number of holes we haven't learned about yet.

2. <strong>Patch the software you do have</strong>. I know companies like to hold off on patching systems for a period of time. Microsoft<span style="color: #303030; font-size: 10.5pt; font-family: Calibri;"><sup>®</sup></span> issued a patch for Slammer a full six months before the attacks really started. There's no excuse for any company to have waited so long to apply the patch.

3. <strong><a href="https://technet.microsoft.com/library/security/ms02-039" target="_blank">Read this security bulletin</a></strong>. It's old, but it provides details on the Slammer worm, how it works, and what it can do to your systems.

4. <strong>Review your use of firewalls, ACLs, and <a href="https://thomaslarock.com/2016/12/using-non-default-ports-for-sql-server/" target="_blank">default ports</a></strong>. Do everything you can do to limit your exposure. Even if you can't upgrade to newer versions of SQL, or patch the one you have, you can use other methods to reduce your risk of a breach.

Lastly, I will leave you with this thought from Ian in an email exchange we had regarding this post:

<em>"It’s no coincidence this attack is taking place, as there recently was exploit code for a Windows<span style="color: #303030; font-size: 10.5pt; font-family: Calibri;"><sup>®</sup></span> SMB attack; perhaps the return of “The Slammer” is a great way to identify at-risk, legacy systems, which a myriad of unpatched Windows<span style="color: #303030; font-size: 10.5pt; font-family: Calibri;"><sup><em>®</em></sup></span> exploits exist for. It’s unlikely you are running SQL 2000 on Windows<span style="color: #303030; font-size: 10.5pt; font-family: Calibri;"><sup><em>®</em></sup></span> Server 2016—great way to get a nice list of targets if the spread of “The Slammer” has a command and control element identifying who’s been infected."</em>

There's a lot of bad actors out there. Don't think your public-facing database server isn't at risk. Any piece of information you provide to a hacker allows them to learn ways to attack someone else.

We are all in this together.