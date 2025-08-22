---
layout: post
title: SQL Server 2016 Updated Privacy Statement
date: '2017-04-13 12:50:56 +0000'
categories:
- Data Security and Privacy
- Featured
- MSSQL
- SQL Azure
- SQL MVP
tags:
- Data
- privacy
- sql server
- telemetry
---

Last week while at <a href="http://sqlbits.com/">SQLBits</a> I attended a session titled <a href="http://sqlbits.com/Sessions/Event16/SQL_Server_Azure_Engineering_Model">SQL Server/Azure Engineering Model</a> given by Conor Cunningham from Microsoft. During the talk, Conor announced that there was an update to the SQL Server 2016 privacy statement. Conor is hoping that this update will help clear up any confusion for customers.

Well, that’s what I want to do today as well. I want to help clear up any confusion around how SQL Server collects, stores, and uses your data. I have some thoughts I want to share regarding the updated statement as well as the End User License Agreement (EULA).

First, with this updated privacy statement, the SQL Server product team becomes the first team at Microsoft to publish detailed information about what data is being collected, when it is collected, why it is collected, how it is collected, where it is being stored, and for how long. This is an amazing show of transparency and I would expect other product teams at Microsoft to follow suit. (I am not, however, expecting other companies like Oracle to be excited about sharing the same details. But that’s a different blog post).

Second, the <a href="https://www.microsoft.com/EN-US/privacystatement/" target="_blank" rel="noopener">updated privacy statement</a> states that usage information is collected by default. In some cases, such as during the installation process, the collection is not something you can disable. In other cases, the data collection is something you can turn off, but only for paid versions of SQL Server. I have no issues with either of these items and here’s why:
<p style="padding-left: 30px;">1. Collecting usage information helps Microsoft make SQL Server better. This continuous feedback allows the SQL Server product team to have faster release cycles and to focus on the features that are being used or may need updating. This is why SQL Server is in the upper right <a href="https://mscorpmedia.azureedge.net/mscorpmedia/2016/03/Gartner-MQs.png">Gartner Magic Quadrant for Operational Management Database Systems</a>. This is a good thing, in my opinion, and therefore I’d like to see the continuous feedback continue (and not just for SQL Server, but for all Microsoft products).</p>
<p style="padding-left: 30px;">2. If you are using a free version of SQL Server then I believe it is reasonable to expect that Microsoft will want to collect information on how you are using the product. Just as Jackson Browne once told us, “nobody rides for free”. If you have a complaint about a free product then you can (1) pay for the product or (2) not use the product. The choice is yours.</p>
Lastly, the SQL Server 2016 EULA contains wording on what has been called “forced updates”. You should understand that these updates are not new. Here’s a screenshot from the SQL Server 2012 install screen:

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/sql-2012-eula.jpg"><img class="aligncenter size-large wp-image-17761" src="https://thomaslarock.com/wp-content/uploads/2017/04/sql-2012-eula-600x453.jpg" alt="SQL Server 2016 Updated Privacy Statement" width="600" height="453" /></a>

That’s right, these updates have been happening for some time now. <strong>These updates are not a new thing for SQL Server 2016</strong>. This is how enterprise class software works – it will update files from previous versions to ensure the latest version works as expected. Examples of items that would be automatically updated by the SQL Server 2016 installation are the client drivers and the .NET redistributables installed by previous versions.

Anyone that has worked with enterprise class software for more than a few years should understand how software updates work. The EULA is telling you that items shared across versions of SQL Server are subject to be updated, they are not strictly versioned per release.

If you don’t want these updates to happen then you should consider running distinct servers for each version of SQL Server.

I once knew a manager that installed SQL 2000 on a production server that was running Sybase ASE (yes, I’m old). It brought the Sybase instance to a stop, as well as the business. So, if you are the type of person that would install such things on top of one another, then yeah, I guess the idea of automatic updates would be a concern for you.

And that’s reason #374 why I advocate new machines for new installs. I think you should, too.
<h2><strong>Summary</strong></h2>
The internet has a lot of misinformation on a lot of topics. SQL Server 2016 data collection and privacy is one of those topics where I see confusion being spread. Take the time to review the details in the privacy statement and then decide if it is worth putting on that tinfoil hat. I suspect that once you go through the details you will find that the data collection is benign and necessary for the SQL Server product team to continue to make SQL Server the best-of-breed relational database management system.

<strong>P.S.</strong> None of the above matters if you don’t allow your server to connect to the internet. SQL Server cannot “phone home” without a dial tone folks. It takes just a few seconds to configure a firewall to block SQL Server from communicating to Redmond.

<strong>P.P.S.</strong> Don’t do that because by doing so you reduce the ability for the product team to make better versions of SQL Server. If you don’t want to opt-in, then consider paying for the software you are using. Or use something else.

<strong>P.P.P.S</strong>. Forget I said that. Use SQL Server. Read about the data collection yourself and make up your own mind. But lose the hat, it doesn’t look good on you anyway.