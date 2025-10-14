---
layout: post
title: The DBA Plate for 2016
date: '2015-11-25 12:09:52 +0000'
categories:
- MSSQL
- Professional Development
- SQL MVP
- SQL Server Performance
tags:
- backups
- DBA Plate
- maintenance
- monitoring
- performance tuning
- Professional Development
- training
---

Four years ago I wrote about the DBA Plate, which was a reference to the <a href="http://www.choosemyplate.gov/" target="_blank">food plate</a> that replaced the food pyramid right about the time the <a href="http://www.huffingtonpost.com/kristin-wartman/pizza-is-a-vegetable_b_1101433.html" target="_blank">U.S. Congress declared pizza to be a vegetable</a>. I had every intention of keeping the plate updated annually but never got around to doing so because reasons. Well, today is the day. You're welcome.

Let's have a quick review of the driving force behind the need for a DBA Plate:

<span style="color: #ff0000;"><em>Many people have no idea what a DBA does for daily work.</em></span>

[And most of the time these people are also put in charge of DBAs. No, I'm not bitter.]

Sadly, most new DBAs also have no idea what they are supposed to be doing. Often they have no mentor to help them along the way. This is especially true in Microsoft shops, where the installation and use of SQL Server is so easy that many forget the fact that you need someone to administer what has been installed.

Most people learn better through visualizations so that's why I created the DBA Plate:

<a href="https://thomaslarock.com/wp-content/uploads/2015/11/The-DBA-Plate-rz.jpeg"><img class="aligncenter size-full wp-image-17176" src="https://thomaslarock.com/wp-content/uploads/2015/11/The-DBA-Plate-rz.jpeg" alt="The DBA Plate rz" width="512" height="384" /></a>

Everything is there, really. Backups should be the biggest part of your plate, followed by maintenance. Monitoring and tuning come next, and you should have a side plate of training as well. I hope this clears up everything. What's that? You need more details? OK then, how about this...
<h2>Backup</h2>
The number one responsibility for any DBA is the ability to recover. If you cannot recover you need to find a different career. And that word ("recover") can mean a lot of different things. It could be your ability to recover as the result of a large scale disaster. It could be your ability to recover the piece of data that was updated inside of one row, in one table, in one database, in some obscure instance of SQL hundreds of miles away. And it could also be everything in between those two events.

And you can't do any of that without having backups in place, having them running in a consistent manner, the ability to check that they are running, and even <a href="http://www.simple-talk.com/sql/database-administration/statistical-sampling-for-verifying-database-backups/" target="_blank">testing that they are valid by doing some periodic restores</a>.
<h2>Maintain</h2>
This part of your plate is for things like the rebuild/reorganizing of indexes, or the updating of statistics. Essentially, anything that helps to maintain the current performance levels for your end users are what I consider to be "maintenance". However there is also administrative maintenance, such as the removal of logins that are no longer used, or running DBCC CHECKDB. If you are looking for some help on getting started with maintenance I would point you to <a href="https://ola.hallengren.com/" target="_blank">Ola Hallengren's scripts</a> as well as <a href="http://minionware.net/" target="_blank">Jen and Sean McCown's Minionware</a>.
<h2>Monitor</h2>
This part of your plate is for the items you want to be alerted and take action upon. For example, running low on disk space, or seeing a spike in CPU utilization, or having one of your SQL Agent jobs fail. As a DBA we are keen to collect all sorts of details about our instances and databases because we never know which particular piece of data is going to help us diagnose and resolve an issue. But you should <a href="http://www.solarwinds.com/database-management-software.aspx" target="_blank">only collect the pieces of information that help you to take action</a>. If you try to monitor everything possible then you may find that the biggest performance impact on your system is yourself! With SQL Server 2016 coming around the corner you should also look at the <a href="https://msdn.microsoft.com/en-us/library/dn817826.aspx" target="_blank">SQL Server Query Store</a>, as that looks to be a promising solution. And Query Store is also available in Azure SQL Database, serving as the backbone for the <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-query-performance/" target="_blank">Query Performance Insights offering</a>.
<h2>Tune</h2>
This part of your plate is when you roll up your sleeves and make adjustments to your instances in some way. Tuning could be the rewriting of T-SQL statements, it could be adding memory to a server, or it could be altering the configuration settings between a virtual host and guest. In essence, anything that goes beyond the traditional maintenance tasks is what I would consider to be tuning. There are lots of tools and scripts available online to assist you with performance tuning, but of course <a href="http://www.solarwinds.com/database-management-software.aspx" target="_blank">I have my favorite</a>.
<h2>Train</h2>
This is the little side plate to everything else that you do. Think of it like having a few strips of bacon with your meal. You need to be constantly keeping up to date with the latest trends in technology. Most of this training is a lot of self-help, but you can also attend events such as SQL Saturdays or the PASS Summit. Just make certain that you reinforce whatever you have been taught by taking the time to <a href="https://thomaslarock.com/2011/11/what-is-training/" target="_blank">lay your hands on the product or piece of functionality</a>.

For 2016 I would suggest that you get some training in one or more of the following areas:

<strong>Microsoft Azure</strong> - Get familiar with what Azure can offer and start thinking about how you can transition from DBA to Cloud DBA in the next 2-3 years. Hybrid IT is a thing, and the traditioonal tasks for DBAs will change. Start getting used to the shiny new things Azure offers.

<strong>Data analytics</strong> - No, I'm not saying you need to drop everything and call yourself a data scientist. What I am saying is that you should become familiar with the industry trend towards data analytics so that you can help architect and build proper solutions with your end users. <a href="https://msdn.microsoft.com/en-us/library/mt604845.aspx" target="_blank">SQL Server 2016 will come with R Services embedded</a>, that alone should be a big hint.

<strong>Speaking</strong> - Hard skills have a salary cap. Soft skills do not. You should find ways to get better at making presentations. Being able to communicate effectively and work well within a team is a good way to keep being employed. Go and find a local user group or <a href="http://www.sqlsaturday.com/" target="_blank">SQL Saturday</a> and submit a topic. Organizers are always looking for speakers.

Happy Thanksgiving.