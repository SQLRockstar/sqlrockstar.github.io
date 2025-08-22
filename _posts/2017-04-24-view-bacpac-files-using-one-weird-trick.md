---
layout: post
title: View BACPAC Files Using This One Weird Trick
date: '2017-04-24 15:50:58 +0000'
categories:
- Database Design
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server Performance
tags:
- BACPAC
- DACPAC
- SQL
- Things I Write While High on Bacon
- ZIP
---

I've talked before about examining the contents of a <a href="https://docs.microsoft.com/en-us/sql/relational-databases/data-tier-applications/data-tier-applications" target="_blank" rel="noopener noreferrer">DACPAC</a> using the built in 'Unpack...' command as shown here:

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/unpack.jpg"><img class="aligncenter wp-image-17784 size-medium" src="https://thomaslarock.com/wp-content/uploads/2017/04/unpack-260x315.jpg" alt="unpack DACPAC" width="260" height="315" /></a>

Unpacking the DACPAC will allow for me to see the contents:

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/dacpac.jpg"><img class="aligncenter size-medium wp-image-17790" src="https://thomaslarock.com/wp-content/uploads/2017/04/dacpac-560x137.jpg" alt="unpack DACPAC" width="560" height="137" /></a>

Until recently I did not think it possible to view the contents of a <a href="https://docs.microsoft.com/en-us/sql/relational-databases/data-tier-applications/data-tier-applications" target="_blank" rel="noopener noreferrer">BACPAC</a> file. Last month <a href="http://sqlbits.com/information/event16/The_DBA_of_the_Future_Hands-on_with_Automation/trainingdetails.aspx" target="_blank" rel="noopener noreferrer">at SQL Bits</a> an attendee reminded me about this one weird trick to view the contents of a BACPAC file. The trick is like how you <a href="https://msdn.microsoft.com/en-us/library/aa982683(v=office.12).aspx" target="_blank" rel="noopener noreferrer">examine the XML inside of office documents</a>, we add the .ZIP extension! First, make a copy of the BACPAC file and rename (in case we need a backup):

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/bacpac-zip.jpg"><img class="aligncenter size-medium wp-image-17785" src="https://thomaslarock.com/wp-content/uploads/2017/04/bacpac-zip-560x292.jpg" alt="change BACPAC to ZIP file" width="560" height="292" /></a>

I will click 'yes', and then I can examine what is inside:

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/bacpac.jpg"><img class="aligncenter size-medium wp-image-17786" src="https://thomaslarock.com/wp-content/uploads/2017/04/bacpac-560x240.jpg" alt="BACPAC file open" width="560" height="240" /></a>

I can navigate inside the data folder and find all the tables included in the BACPAC. <span data-offset-key="5kql6-0-0">The <a href="https://docs.microsoft.com/en-us/sql/relational-databases/replication/snapshot-replication">snapshot replication BCP process</a> creates the tables within the BACPAC. </span>The easiest way to import the data is to use SSMS and import the BACPAC file as a whole. But, if I wanted to get a subset of the tables I can use the BULK INSERT command like this:
<pre lang="tsql">BULK INSERT dbo.DatabaseLog
    FROM 'some-filepath-name-here\TableData-000-00000.BCP'
    WITH (DATAFILETYPE = 'native');</pre>
This will allow for me to only insert the tables I want.

I could also automate a process to move data between different databases and systems. SQL Server Replication would be great for this, but replication may not always be the answer. For example, sometimes you need to move data between versions and editions of SQL Server. And then there is the fact that not all data resides in SQL Server (gasp!), so you may need to use some BCP to get the job done.
<div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="ce16o-0-0"><span data-offset-key="ce16o-0-0">DACPAC and BACPAC are great for moving data between systems. They allow for more flexibility than database backups. But, database backups allow for transactional consistency. Choose the data migration method that is right for you.</span></div>