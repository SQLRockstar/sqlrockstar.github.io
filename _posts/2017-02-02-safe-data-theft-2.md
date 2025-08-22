---
layout: post
title: How Safe Is Your Data From Theft?
date: '2017-02-02 22:16:38 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
tags:
- data privacy
- data security
- data theft
---

<a href="https://thomaslarock.com/wp-content/uploads/2013/02/dumpster.jpg"><img class="alignleft wp-image-10110 size-full" src="https://thomaslarock.com/wp-content/uploads/2013/02/dumpster.jpg" alt="data theft" width="279" height="181" /></a>This Tuesday will mark the 45th anniversary of the day that Jerry Neal Schneider became a household name.

Wait, you've never heard of him?

OK, let me recap events for those of you that may not be old enough to remember everything that led to Schneider's arrest on February 8th, 1972.

It all started with some dumpster diving. But Schneider wasn't looking for food. He was looking for spare parts. Schneider knew that the phone company would throw away used and broken equipment. So he would jump into a dumpster full of phone parts and scavenge for whatever he could find. If he could fix it up and sell it then all the better.

What he didn't count on finding was all that paper.

Alongside the used and broken equipment, the dumpsters contained old invoices. Schneider found them curious enough at first and started collecting them. He wanted to see if he could learn more about how the phone company processed equipment orders. Over time he did just that and soon he could call the telephone company and impersonate an employee. He would ask a few questions and obtain even more details on procedures. He even managed to get a tour of the warehouse by pretending to be a freelance journalist.

Then in June of 1971, he placed an order for $30,000 worth of equipment to be dropped off at a construction site. Jerry was right there to collect it and promptly sold it for a nice profit.

Because this crime involved computers to some degree (the invoices were computer printouts, and the ordering process was computerized) this crime was labeled a "<a href="http://www.haftofthespear.com/wp-content/uploads/2011/02/Becker_1980_Computer_crime_career_of_the_future.pdf" target="_blank">computer crime</a>". I say it is more of a <a href="http://www.pcworld.com/article/182180/top_5_social_engineering_exploit_techniques.html" target="_blank">social engineering crime</a> which is really just the modern way of saying "con-artist". At the time this crime was one of the largest computer crimes with Schneider having stolen about $900,000 worth of equipment.

How did he get caught? Business was so good for Jerry that he needed to take on a partner. When the partner found out the details of the business he demanded a hefty increase in his salary. Jerry refused, the partner went to the cops, and that was the end of it.
<h2>What Have We Learned?</h2>
It's been forty-five years since that happened. What have we learned in that time?

Not much, it seems.

First, <a href="https://www.interpol.int/Crime-areas/Financial-crime/Social-engineering-fraud/Types-of-social-engineering-fraud" target="_blank">social engineering hasn't gone away</a>. It never will, either. What comes and goes is the awareness to social engineering and what information you are sharing with close friends and family. During times of war (i.e. WWII) it was quite common to not say one word about what you were doing on a daily basis, not even to your family let alone strangers that struck up a conversation at a coffee shop.

Second, <a href="http://www.today.com/popculture/identity-theft-your-trash-their-treasure-wbna27011491" target="_blank">people still throw away pieces of paper with valuable information on them</a>. Chances are you receive credit card applications in the mail. These applications have some personal information about you. And instead of shredding them, you are probably just putting them in your trash. If you are not shredding those applications then don't be surprised if you find yourself the victim of identity theft one day.

Third, <a href="http://www.healthdatamanagement.com/news/hipaa-violations-stolen-usb-drive-costs-insurer-22m" target="_blank">employees take their work, and data, home with them all the time</a>. Often times they and up losing a laptop, perhaps even having it stolen, and BOOM! a few hundred thousand customers end up with a nice form letter from the company legal team informing them that there was a security breach.
<h2>When In Doubt, Don't</h2>
That quote is attributed to <a href="https://www.brainyquote.com/quotes/quotes/b/benjaminfr119121.html" target="_blank">Benjamin Franklin</a> and I believe it sums up just about everything when it comes to data security. If you ever have a doubt about your data being secure, stop. Get up off your arse and determine if a problem exists and then determine what you can do about it.

Here's a list of five things you can be doing today to help put your mind at ease. They aren't foolproof, but they are likely to help you help your company from being named in a lengthy lawsuit.

<strong>1. Encrypt The Data - </strong>You can use tools like <a href="https://technet.microsoft.com/en-us/itpro/windows/keep-secure/bitlocker-overview" target="_blank">BitLocker</a> to protect your disk drives and most database platforms offer some type of encryption protection such as <a href="http://msdn.microsoft.com/en-us/library/bb934049.aspx" target="_blank">Transparent Data Encryption (TDE)</a> or <a href="https://msdn.microsoft.com/en-us/library/mt163865.aspx" target="_blank">Always Encrypted</a>. Even storage companies such as <a href="http://blog.purestorage.com/at-rest-encryption-of-sql-server-databases-on-pure-storage-flasharrays/" target="_blank">Pure Storage offer encryption on their arrays</a> these days. If you aren't making the minimum effort to encrypt your data then you deserve your fate.

<strong>2. Most Email Is Not Secure - </strong>Do you send each and every email in an encrypted state? Are you comfortable with those reports being embedded in emails? No? Then stop sending them as attachments, and start sending just the link to the URL where the report resides on a network share or in a portal like Sharepoint.

<strong>3. Trust, But Verify - </strong>If you don't know a person then don't give them access to information no matter how nicely they ask. If someone persists on getting access then do a little legwork and verify that their request is valid. You owe it to your data to verify that the person is authorized to see the information they are asking about. The days of giving someone full access are over. Sure, I know sharing the data is the easiest thing to do, but it is not the right thing to do.

<strong>4. Save A Tree - </strong>Are you printing out your emails like it was 1999? Do you need to save a hard copy of everything just in case some men dressed in black show up and ask to see your files? <strong>Stop</strong>. Just stop it. And whatever documents you are printing out you should shred whenever you are done with them. Don't even think twice about this part, just shred.

<strong>5. Ask Yourself "What If?" - </strong>What if that piece of data got loose? What if someone outside the company was reading this old invoice? What's the worst that can happen? By asking yourself that question you are more than likely going to find yourself understanding that every piece of data needs to be treated as if it was the most important piece of data. Guard your data as if the future of your company depended on its privacy remaining intact.
<h2>Summary</h2>
<a href="http://blog.infoadvisors.com/index.php/2013/01/16/b-c-health-ministry-data-breach-affects-millions/" target="_blank">Every day</a> it seems a <a href="http://blog.infoadvisors.com/index.php/2013/01/13/global-payments-data-breach-tab-94-million-plus-more-in-2013/" target="_blank">new story</a> comes out regarding <a href="http://blog.infoadvisors.com/index.php/2013/01/09/health-data-breaches-insider-data-trading/" target="_blank">data theft</a>, <a href="http://blog.infoadvisors.com/index.php/2013/01/18/utah-health-department-yet-another-flashdrive-fail-yaff/" target="_blank">data security</a>, and <a href="http://blog.infoadvisors.com/index.php/2013/01/02/an-audible-data-privacy-breach/" target="_blank">data breaches</a>. It's like we are back in 1972 again, except without the <a href="https://www.pinterest.com/pin/373306256584746523/" target="_blank">bell-bottom jeans</a>. People seemed surprised that data theft continues to happen. I think part of the reason is because most security systems are designed and focused on preventing hackers from breaking in that they don't understand the real danger in <a href="http://blog.infoadvisors.com/index.php/2013/01/22/federal-department-bans-use-of-portable-devices-yaff/" target="_blank">allowing data to simply walk away</a> on something like a USB stick.

Or even an invoice.