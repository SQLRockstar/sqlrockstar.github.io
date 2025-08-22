---
layout: post
title: Security is a Shared Responsibility
date: '2017-05-18 15:26:15 +0000'
categories:
- Data Security and Privacy
- MSSQL
- Professional Development
- SQL MVP
tags:
- data security
- privacy
- ransomware
---

<a href="https://thomaslarock.com/wp-content/uploads/2017/05/wannacry.jpg"><img class="aligncenter size-medium wp-image-17881" src="https://thomaslarock.com/wp-content/uploads/2017/05/wannacry-560x315.jpg" alt="" width="560" height="315" /></a>Last week the WannaCry ransomware made the rounds through Europe until it was inadvertently killed by a researcher. You can read more about what happened with the attack from Troy Hunt who <a href="https://www.troyhunt.com/everything-you-need-to-know-about-the-wannacrypt-ransomware/" target="_blank" rel="noopener noreferrer">provides a nice summary</a>.

For the past week, there has been a lot of finger-pointing about who was to blame for this. Some people point the finger at Microsoft. Others point the finger at businesses not being up to date on patches. And others blame the NSA for stockpiling a list of vulnerabilities that were then stolen. It seems everyone is to blame but the actual criminals.

Let's break it down.

<strong>Companies with unpatched systems</strong> - They get blamed for not keeping up to date with patches. This I could almost agree to, but we all know how patching works for most companies. Still, at least those companies are running the latest OS. Companies running older OS systems get blamed for not being current, of course. But <a href="https://twitter.com/shanselman/status/863638496430276608" target="_blank" rel="noopener noreferrer">there are good reasons why companies have older versions of Windows running</a>.

<strong>Microsoft</strong> - They get blamed by default as the makers of Windows. But once Microsoft knew the list from the NSA was public issued a patch for all supported OS versions. "Supported" is the key word here. It wasn't until after WannaCry hit that Microsoft issued patches for unsupported versions. They then <a href="https://blogs.microsoft.com/on-the-issues/2017/05/14/need-urgent-collective-action-keep-people-safe-online-lessons-last-weeks-cyberattack/#sm.001hgrr8y15wrdeky8b2m7jpmlusu" target="_blank" rel="noopener noreferrer">took to the web to hint that the NSA was more to blame</a>.

<strong>The NSA</strong> - They get blamed for stockpiling a list of vulnerabilities to use against systems. Being the NSA they didn't think that list would ever walk out the door at some point, but it did. Once it did they contacted the companies affected (such as Microsoft). But blaming the NSA for keeping such a list is rather silly. That's what they do for business. If the bank safety deposit boxes are robbed you don't blame the bank for keeping the boxes in the same room.

But none of the above are to blame.

The truth is that everyone is to blame. <strong>Security is a shared responsibility</strong>. We are all in this together.

The #hardtruth here is the <strong>current software business model is broken</strong>.

Today we buy software and we expect it to work. We expect the software maker to keep up to date with security and issue patches. But we don't always patch because we emphasize stability over security. And the software maker doesn't force us to stop using the old software. Unsupported means you pay more for support. That's why there are still instances of SQL 2000 out there. Companies know it is cheaper to pay for the support as needed than it is to upgrade to newer versions.
<h2>We need a new model</h2>
<strong>We need a model that makes security a priority</strong>.

If you buy an OS today, you are responsible for keeping it up to date with the latest patches. If you made the OS, you are responsible for issuing patches. You are also responsible for decommissioning older software. I'm not saying to mark it as 'unsupported', I'm saying to <a href="https://developer.microsoft.com/en-us/microsoft-edge/ie6countdown/" target="_blank" rel="noopener noreferrer">kill it same as with IE6</a>. That has to be part of the new model, that there is a kill switch at some point. If Microsoft could kill IE6 then they could kill SQL 6.5, too.

It's too convenient for companies to toss their hands in the air and find excuses to not upgrade. Stop blaming everyone but the criminals. You are the one taking the risk, not them.

No more excuses. If we want a more secure world then we need to make security a priority.