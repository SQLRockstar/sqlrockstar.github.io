---
layout: post
title: Data Migration Assistant Error During Assessment of SQL Server 2017
date: '2018-01-09 10:59:52 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server 2016
- SQL Server 2017
tags:
- Data Migration Assistant
- SQL Server 2016
- sql server 2017
---

The Data Migration Assistant (DMA) offers you the ability to perform a feature assessment against your SQL Server database. Built as the successor for the SQL Server Upgrade Advisor, the DMA is a valuable tool for migration projects. I've written before <a href="https://thomaslarock.com/sql-server-upgrades/" target="_blank" rel="noopener">about upgrades</a> and the <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-pre-upgrade-tasks/" target="_blank" rel="noopener">use of DMA as part of your pre-upgrade checklist</a>. I'm a big fan of the tool, if you can't tell.

The DMA will assist with upgrades and migrations to newer versions of SQL Server. The DMA will not work if you try to assess a source database against an older target version. For example, I cannot use SQL Server 2017 database as a source with SQL Server 2016 as a target. If you try that you will get an error such as the following:
<blockquote>The database 'AdventureWorks2016CTP3' from server 'PORC\SQL2016' cannot be assessed because its version is greater than the selected target.</blockquote>
That's the error I saw with an assessment of a source SQL 2016 database against a SQL Server 2014 target. It looks like this:

&nbsp;

<img class="aligncenter size-large wp-image-18502" src="https://thomaslarock.com/wp-content/uploads/2018/01/DMA_error-600x361.jpg" alt="Data Migration Assistant Error" width="600" height="361" />

&nbsp;
<h2>Use Visual Studio to Assess a SQL Server Database</h2>
If you need to perform an assessment of a database against a prior version, you would use Visual Studio. However, this is not an apples-to-apples assessment. The DMA is going to help guide you on feature recommendations for the new version of SQL Server. When you use Visual Studio you are going to find features that need to be removed. Visual Studio wants to make your project compatible with the target. DMA wants to help you understand the features you may be missing.

I'll say that again: <strong>Visual Studio will tell you what features to remove. DMA will tell you what features you might want to add.</strong>

To get started you first need to <a href="https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt" target="_blank" rel="noopener">install the SQL Server Data Tools</a> extension. Then, create a database project. After creating the project, set the target to the desired version of SQL Server. In this case, I will again use a source database from SQL Server 2016, and set the target to be SQL Server 2014:

&nbsp;

<img class="aligncenter size-large wp-image-18505" src="https://thomaslarock.com/wp-content/uploads/2018/01/vs_prior_version_check-600x246.jpg" alt="visual studio database project sql server prior version target" width="600" height="246" />

&nbsp;

Next, save the project, then do a build and note if any errors appear. In this example, I have a few things to fix before I would be able to deploy the schema in this project to the SQL Server 2014 target:

&nbsp;

<img class="aligncenter size-large wp-image-18506" src="https://thomaslarock.com/wp-content/uploads/2018/01/vs_build_errors-600x203.jpg" alt="visual studio build errors sql migration prior version" width="600" height="203" />

&nbsp;

So, we are able to perform an assessment against a prior version. Just remember that Visual Studio is not going to recommend features in the same manner as DMA. They are two different tools with two different goals here.

There is one thing worth noting here with regards to the use of Visual Studio in this manner. This is the process you would follow should you ever need to migrate a database to a prior version of SQL Server. You would use Visual Studio to find any issues, fix those issues, deploy the schema, then migrate the data.