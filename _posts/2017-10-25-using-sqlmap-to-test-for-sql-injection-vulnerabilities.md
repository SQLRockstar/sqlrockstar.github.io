---
layout: post
title: Using sqlmap to Test For SQL Injection Vulnerabilities
date: '2017-10-25 09:06:44 +0000'
categories:
- Data Security and Privacy
- MSSQL
- PASS
- SQL Azure
- SQL MVP
tags:
- sql injection
- sqlmap
---

You may have noticed my recent articles have had a security focus. I wrote one about <a href="https://thomaslarock.com/2017/10/audit-sql-server-jobs/" target="_blank" rel="noopener">using SQL Server Audit to track changes made to jobs inside of SQL Agent</a>. And another on the <a href="https://thomaslarock.com/2017/10/sql-vulnerability-assessment/" target="_blank" rel="noopener">SQL Vulnerability Assessment feature in Azure</a>. Today I'm going to write a bit about a third tool, <a href="http://sqlmap.org/" target="_blank" rel="noopener">sqlmap</a>, an open-source penetration testing project that will help test websites for SQL injection vulnerabilities.

The sqlmap tool is quite versatile. Here's just a brief list of capabilities listed on the homepage that caught my attention immediately:

- Support for MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, IBM DB2, SQLite, Firebird, Sybase, SAP MaxDB, HSQLDB and Informix database management systems.
- Support for six SQL injection techniques: boolean-based blind, time-based blind, error-based, UNION query-based, stacked queries and out-of-band.
- Ability to directly connect to the database without passing via a SQL injection, by providing DBMS credentials, IP address, port and database name.
- Support to enumerate users, password hashes, privileges, roles, databases, tables and columns.
- Support to dump database tables entirely, a range of entries or specific columns as per user's choice. The user can also choose to dump only a range of characters from each column's entry.
- Support to search for specific database names, specific tables across all databases or specific columns across all databases' tables. This is useful, for instance, to identify tables containing custom application credentials where relevant columns' names contain string like name and pass.

You can read the full list of features here: <a href="https://github.com/sqlmapproject/sqlmap/wiki/Features" target="_blank" rel="noopener">https://github.com/sqlmapproject/sqlmap/wiki/Features</a>. Also, you can download <a href="http://sqlmap.org/" target="_blank" rel="noopener">sqlmap from the homepage</a>, or you can <a href="https://github.com/sqlmapproject/sqlmap" target="_blank" rel="noopener">clone sqlmap from Git</a>.

But before you can get started with sqlmap you need to have Python installed. You do that <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">by going here</a>. Note that sqlmap requires Python versions later than 2.6 and before 3.0, so be mindful which version you choose on the downloads page.

Once you have both python and sqlmap installed you are ready to run sqlmap from the command line. Oh, I guess I should have warned you first abut that part. If you are the type of person that doesn't like to work with a command line, then sqlmap isn't the tool for you.

I've created a demo website at <a href="https://azure-sql-security-sample4e2b.azurewebsites.net/" target="_blank" rel="noopener">https://azure-sql-security-sample4e2b.azurewebsites.net/</a>, this is the website I will be using next week for my demos during my SQL Server Audit session at the PASS Summit. Feel free to poke around there while it is still available and try your hand at some SQL injection. Or, if you prefer, use sqlmap instead. (Seriously, go to the website and try your hand at SQL injection, that's what it's for. You can build your own following the directions here: <a href="https://github.com/Microsoft/azure-sql-security-sample" target="_blank" rel="noopener">https://github.com/Microsoft/azure-sql-security-sample</a>)

For this blog post I will open a PowerShell window from the sqlmap install directory and run the following command:

C:\Python27\python.exe .\sqlmap.py --batch --flush-session -u https://azure-sql-security-sample4e2b.azurewebsites.net/Patients --forms --os=windows --dbms=mssql --exclude-sysdbs -T creditcards --dump --technique=UE

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sqlmap.jpg"><img class="aligncenter size-large wp-image-18097" src="https://thomaslarock.com/wp-content/uploads/2017/10/sqlmap-600x266.jpg" alt="" width="600" height="266" /></a>

You can see in the command I used a handful of the options that sqlmap has to offer. However, if you want to do the shotgun approach you can let sqlmap test against all possible attack vectors by simply pointing it at a website like this

C:\Python27\python.exe .\sqlmap.py --batch --flush-session -u https://azure-sql-security-sample4e2b.azurewebsites.net/Patients --forms --dump

It goes without saying that by hitting the entire website in this manner, sqlmap will take longer to complete. Here's a quick look at how the results come back to the screen for the first example where we focused on just one table:

[video width="1080" height="720" mp4="https://thomaslarock.com/wp-content/uploads/2017/10/sqlmap.mp4"][/video]

&nbsp;

Here's a look at the output files obtained from scanning the entire website:

<a href="https://thomaslarock.com/wp-content/uploads/2017/10/sqlmap_csv.jpg"><img class="aligncenter size-large wp-image-18100" src="https://thomaslarock.com/wp-content/uploads/2017/10/sqlmap_csv-600x247.jpg" alt="sqlmap csv" width="600" height="247" /></a>
<h2>Summary</h2>
The sqlmap tool makes testing websites easy. It's also a great example of a community project. It's good to see someone helping to make the internet a little more secure, one scan at a time.

I would suggest you try using sqlmap against your own websites and blogs. Don't use sqlmap against websites you don't own. And don't use sqlmap against the websites you find on <a href="https://www.shodan.io/" target="_blank" rel="noopener">shodan.io</a>, either. You're just asking for trouble if you do.