---
layout: post
title: Data Migration Assistant Custom Configuration
date: '2018-02-06 12:35:50 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server 2016
- SQL Server 2017
tags:
- Data Migration Assistant
- sql server
---

The Data Migration Assistant (DMA) is a great tool made available by Microsoft. Successor to the SQL Server Upgrade Advisor, the DMA will perform an assessment of your database against a target version. The DMA can also perform the migration of both schema and data, if desired.

The other day I wanted to run DMA from a command line. When I went to the install directory I noticed that there were some .config files available:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config.jpg"><img class="aligncenter wp-image-18619 size-medium" src="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config-560x220.jpg" alt="Data Migration Assistant configuration file" width="560" height="220" /></a>

&nbsp;

Yes, *very* interested. So, I did what anyone else would do, I opened the file to have a look. The file was set to use Visual Studio Code by default, so opening the file was easily done. Once opened I found what I expected, an XML file with configuration settings for DMA.

I scrolled through the file, looking for interesting pieces of information. I could write a whole series of posts on what that file contains, but today I will keep it short. We will focus on one item: stretch database recommendations.

The file contains this line:
<div>
<pre>&lt;!-- Tables are eligible to stretch only if the number of rows 
is equal or greater than the recommendedNumberOfRows treshold --&gt; 

&lt;stretchDBAdvisor useSimulator="false" timeBetweenIssues="0.00:00:00.10" 
timeBetweenTables="0:00:00:00.10" recommendedNumberOfRows="100000" /&gt;
</pre>
</div>
So, the DMA will recommend a table as a candidate for stretch database if the number of rows is equal to or greater than 100,000. We could debate all day if that number is the correct number, but the DMA needs to have a starting point. 100,000 isn't a bad place to start. But here's where things get interesting.

If your shop has specific requirements, you can edit these config files to match your requirements. For example, maybe you want a minimum number of rows to be 1,000,000. You can edit the config file and run your assessment. Let's take a look.

Check out what the an assessment looks like against a copy of GalacticWorks with a target of SQL 2017:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config_default_stretch.jpg"><img class="aligncenter wp-image-18620 size-medium" src="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config_default_stretch-544x315.jpg" alt="Data Migration Assistant default stretch configuration" width="544" height="315" /></a>

&nbsp;

You can see that we have 2 results returned, and I highlighted the row count and size of the table. Now, we will modify the config file. I will make the default row number to be 10,000, because I want to show you that the number of recommendations will increase. So, same source database, the only change being made here is the configuration of DMA. Here's what the assessment looks like after the change:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config_modified_stretch.jpg"><img class="aligncenter wp-image-18621 size-medium" src="https://thomaslarock.com/wp-content/uploads/2018/02/DMA_config_modified_stretch-516x315.jpg" alt="Data Migration Assistant modified configuration for stretch" width="516" height="315" /></a>

&nbsp;

Notice that the first image returns a total of 2 objects, one "High value" and one "Medium value" as candidates for stretch. After modifying the config file we get see a total of 19 objects. I have highlighted the 2MB sized Sales.Customer table and the 19,820 rows it contains.

This is just an example to show that modifying the config file changed how the DMA worked. I am not recommending that you stretch such small tables. I just wanted to show you a quick test. Here's a handful of other items inside the config file that may be of interest to you:

- BCP argument defaults (both BCP in and out)
- Database collation settings
- Scripting options

Go <a href="https://www.microsoft.com/en-us/download/details.aspx?id=53595" target="_blank" rel="noopener">download the Data Migration Assistant</a> and have a look for yourself.

&nbsp;
<h2>Summary</h2>
The Data Migration Assistant is a great tool to help you evaluate and migrate your database to newer versions of SQL Server, including Azure SQL Database. The DMA is also customizable to a certain degree, and can be run from a command line. With a handful of lines in PowerShell you could run assessments against a large number of databases in a short period of time.

(If you liked this post, you'll love <a href="https://sqlkonferenz.de/agenda.aspx" target="_blank" rel="noopener">our session at SQL Konferenz</a> later this month. We are going to walk you through the entire migration process, helping you to understand how to avoid the common pitfalls that affect many migration projects.)