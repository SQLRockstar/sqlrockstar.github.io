---
layout: post
title: Advanced Accidental Database Design
date: '2016-04-05 17:00:46 +0000'
categories:
- Database Design
- MSSQL
- SQL Server Performance
- Travel
tags:
- Database Design
- sql server
- sqlbits
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/04/CoddIsMyCopilot.jpg" rel="attachment wp-att-17340"><img class="alignleft wp-image-17340 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/04/CoddIsMyCopilot-315x315.jpg" alt="Advanced Accidental Database Design" width="315" height="315" /></a>I see the phrase 'accidental administrator' and even 'accidental architect' often in our industry. At some point in our career we get put in charge of things we don't own at first much in the same way as when your neighbor goes on vacation and asks you to look after their cats.

This is very true for many database administrators out there. Nobody goes to school to be a DBA. We fall into the role by accident because (1) we think the job is cool or (2) we think we can do the job better than anyone else, or a combination of both.

But after a few weeks, once we've created a table, or altered a column, or reset a password we are then seen as someone that can design an entire database for a project. We sit in meetings, we take notes, and we go back to our desks to do as we're told and we don't often think about the ramifications of the design choices that we are implementing.

And that means this: <strong>Over 90% of the databases out there right now have been designed by an accidental administrator*</strong>, if they are being designed at all.

When the SQLBits call for speakers went out I immediately wrote an email to Karen López (<a href="http://blog.infoadvisors.com/" target="_blank">blog</a> | <a href="http://twitter.com/datachick" target="_blank">@datachick</a>) and asked her if she would do another training day with me, this time focused on database design for accidental administrators. And thus the session '<a href="http://sqlbits.com/information/Event15/Advanced_Accidental_Database_Design_for_SQL_Server_2016/TrainingDetails.aspx" target="_blank">Advanced Accidental Database Design</a>' was born.

Similar to last year, the day will include lecture style format as well as interactive discussions and exercises. We will break the attendees out into teams and have them perform lab exercises using Azure VMs with SQL Server installed. This isn’t your average "Here's how to create a table, now go build a database" course. Our goal is to cover new features in SQL Server 2016 that are relevant to modern enterprise development practices. We’ll talk about some of the pain points designers feel as well as the costs, benefits, and risks associated with design choices.

Discussion topics will include:

• Advanced database design process
• Advanced Data Types (XML, JSON, Geospatial)
• Files/Filegroups/Partitioning/Archiving/Stretching
• Security/Encryption/Data masking/Audit
• Advanced Table design Topics (Temporal/Hekaton/Compression)
• Other Advanced Topics

Attendees will leave our session with an understanding of new features in SQL Server 2016, advanced database design process for modern enterprise development projects, and how to decide which design choice is the right decision choice for your needs.

If you have the opportunity to <a href="https://www.regonline.com/Register/Checkin.aspx?EventID=1778751" target="_blank">go to SQLBits</a> and attend a training day we'd love to see you.

If you aren't able to attend SQLBits but still want a taste of our session you are in luck, we've got you covered there, too. <strong>Next week (12th April, 2016) we will be doing a webinar for <a href="http://www.solarwinds.com/" target="_blank">SolarWinds</a></strong>, <a href="http://launch.solarwinds.com/Webinar_20160412_EN_TL.html" target="_blank">Advanced Accidental Database Design</a>, taking place at 9AM ET (<a href="http://www.timeanddate.com/worldclock/converter.html" target="_blank">13:00 UTC</a>).

Join us for the webinar and get a taste of what it would be like to be stuck in a room with us for a full day!

*-I've no idea what the real number is, and <a href="http://dilbert.com/strip/2008-05-08" target="_blank">neither do you</a>.