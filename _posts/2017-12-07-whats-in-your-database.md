---
layout: post
title: What's In Your Database?
date: '2017-12-07 08:38:31 +0000'
categories:
- Data Security and Privacy
- Database Design
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server Performance
- Virtualization
tags:
- AWS
- Data
- data security
- microsoft
- MSSQL. data privacy
---

<img class="aligncenter size-large wp-image-18212" src="https://thomaslarock.com/wp-content/uploads/2017/12/wallet_encrypt_rz-600x450.jpeg" alt="what's in your wallet" width="600" height="450" />Recently, while settling in to watch television with my family, we were treated to an amusing advertisement for a credit card company. This particular commercial showed men dressed as Vikings asking questions about the contents of my wallet. My son laughed then turned to me and asked the obvious question, "Papa, what's in your wallet?"

"Nothing," was my answer, and it's true. Ever since direct deposit became a thing I find I never have any cash in my wallet, even while traveling. My wallet has a handful of credit cards, insurance cards, and a picture of my daughter taken when she was a few hours old.

As I thought about the minimal contents of my wallet, and the things inside I had forgotten, I began to ponder about data, databases, and data security. I know everyone collects and stores data without truly understanding its importance or value. We have all seen data forgotten, neglected, and misused.

I think we should all take time to ask ourselves the simple question, "What's in your database?"
<h2>What's In Your Database?</h2>
Data is the obvious answer, of course. But there are many different types of data inside of a database, some more sensitive than others. I'm not just talking about data types like INT or VARCHAR. No, I'm talking about data that can be <a href="http://www.gsa.gov/portal/content/104256" target="_blank" rel="noopener">classified as personally identifiable information</a> (PII). This is data that contains a unique identifier from which the identity of a specific person is obtained.

PII data has existed for centuries (thank you, US Census!), albeit not in digital form. To some degree, awareness of this data's value has increased. This is evident in the number of security measures offered and deployed by many companies as they try to protect their data and databases, such as encryption, access controls, permissions, password policies, and securing backups.

But has awareness of its value increased enough? No, I don't think so; and this will become even truer as the Internet of Things (IoT) begins to take hold. The evidence is that despite all of the security measures companies have adopted to protect their data and databases, we <a href="http://www.databreachtoday.com/lost-server-what-went-wrong-a-7560" target="_blank" rel="noopener">still</a> <a href="http://www.databreachtoday.com/hsbc-turkey-confirms-card-breach-a-7558" target="_blank" rel="noopener">have</a> <a href="http://www.databreachtoday.com/chase-breach-what-we-know-so-far-a-7521" target="_blank" rel="noopener">data</a> <a href="http://www.databreachtoday.com/malware-examining-home-depot-breach-a-7339" target="_blank" rel="noopener">breaches</a>.

Why does this continue to happen?

As I said, I suspect it is because people don't understand the true value and importance of their data and databases. A database isn't just a container for your data. <strong><em>A database contains the most precious business asset any company can have</em></strong>. If you don't have data, you don't have a business.
<h2>Security is a Shared Responsibility</h2>
I've written before about how <a href="https://thomaslarock.com/2017/05/security-shared-responsibility/" target="_blank" rel="noopener">security is a shared responsibility</a>. Last week at AWs re:Invent I was ecstatic to see and hear AWS CTO Werner Vogels spend a dedicated amount of time <a href="https://youtu.be/nFKVzEAm-ts?t=45m37s" target="_blank" rel="noopener">during his keynote</a> to talk directly about data security (about 45:38 in here:)

<iframe src="https://www.youtube.com/embed/nFKVzEAm-ts?rel=0" width="500" height="281" frameborder="0" allowfullscreen="allowfullscreen"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start">?</span></iframe>

"Protecting your customer should be your number one priority". Preach.

And yet, data breaches will continue until we are able to create a deep appreciation for business data. We need to guard business data as closely as our own wallets.

AWS knows this, and that's why they've started rolling out enhanced security features. They needed to do this to keep pace with what Microsoft has been doing for years already. Check out the <a href="https://azure.microsoft.com/en-us/overview/trusted-cloud/" target="_blank" rel="noopener">long list of security features in Azure</a>, many of which were rolled out ahead of similar AWS offerings.

Good security comes from good people. Humans are the weakest link in the data chain. In fact, humans have been known to give away their passwords in exchange for a <a href="http://www.theregister.co.uk/2003/04/18/office_workers_give_away_passwords/" target="_blank" rel="noopener">cheap pen</a> or a <a href="http://news.bbc.co.uk/2/hi/technology/3639679.stm" target="_blank" rel="noopener">chocolate bar</a>.

We must do better.
<h2>Dance like no one is watching, encrypt like everyone is</h2>
If someone told you that you might lose your wallet, you'd go out of your way to keep it secure. You should have the same mindset with your data. If concerned about losing your wallet, you'd move it to a front pocket, keep your hand on it, or minimize the contents inside so that if it were lost or stolen you are able to recover quickly. For data, this means making certain you have effective monitoring, logging, and auditing tools in place, as well as effective security measures such as encrypting data at rest, in use, and in flight.

And if you lost your wallet you wouldn't wait months to tell someone. You'd act quickly. The same should go for your data. The moment you discover a breach you need to disclose the breach to minimize damage and losses.

Only by truly understanding and appreciating the value of our data and databases and motivating everyone to take these steps will we see the necessary diligence needed to protect data from theft. Maybe we need our own commercial with IT professionals dressed as Vikings. That might help get the point across.