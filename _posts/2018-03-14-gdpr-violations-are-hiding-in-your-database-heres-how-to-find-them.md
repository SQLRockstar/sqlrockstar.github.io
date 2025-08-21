---
layout: post
title: GDPR Violations Are Hiding In Your Database - Here's How To Find Them
date: '2018-03-14 19:36:36 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
- SQL Server 2017
tags:
- data privacy
- data security
- GDPR
- microsoft
- sql server 2017
---

Today I was attending the Microsoft Virtual Security Summit, and they posted this poll:

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/GDPR.jpg"><img class="aligncenter wp-image-18771 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/03/GDPR-600x433.jpg" alt="GDPR Violations Are Hiding In Your Database - Here's How To Find Them" width="600" height="433" /></a>

As you can see, 22% of the respondents believe that their organization is not impacted by the GDPR.

I think that many of that 22% have their head in the sand, <a href="https://thomaslarock.com/2018/01/a-few-words-about-gdpr-data-privacy-and-this-blog/" target="_blank" rel="noopener">something I've written about before</a>. I've seen an uptick in conversations around GDPR recently. They go like this: "Hey, we just heard about GDPR, can you help us figure out what we need to do to be compliant?"

The short answer is "maybe". But with only two months before GDPR takes effect, it is unlikely you are going to catch everything. And it is going to be even harder to find data if you don't know where to look. That's why I am writing this today. Because GDPR violations are hiding in your database, and here's how to find them.

And even if the GDPR doesn't apply to you, this post will help you find Personally Identifiable Information (PII) that might be overlooked. I bet even the 22% above are concerned about PII data leaking out.

&nbsp;
<h2>Data Discovery and Classification</h2>
The first step is to start building a process for data discovery and classification. I've written before about the <a href="https://thomaslarock.com/2018/02/sql-data-discovery-and-classification/" target="_blank" rel="noopener">tools Microsoft is making available to help</a>, as well as the limitations these tools have right now. With GDPR coming there is no better time to get started. But get started, you must. The sooner, the better, as you are likely to discover thousands of columns that need classification, masking, and/or encryption.

&nbsp;
<h2>The Two Datatypes You Must Check</h2>
There's a couple of column data types that aren't getting enough attention for GDPR and/or PII. They are the <a href="https://docs.microsoft.com/en-us/sql/relational-databases/xml/xml-data-type-and-columns-sql-server" target="_blank" rel="noopener">XML</a> and <a href="https://docs.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql" target="_blank" rel="noopener">NVARCHAR(MAX)</a> columns. These columns can be catch-alls for data, and likely contain details that may fall under the scope of GDPR. They are not being flagged by the Data Discovery and Classification tool by default. That's because the tools look at column names, and not the data inside of the columns. You need to be aware of this gap and include a manual check for these columns, to be safe.

&nbsp;
<h2>How to Find XML Columns in SQL Server</h2>
Finding these columns inside your database is easy enough. Here's some sample code to help get you started.
<pre lang="tsql">SELECT SCHEMA_NAME(so.schema_id) AS [Schema],
OBJECT_NAME(sc.object_id) AS [Table],
sc.name AS [Column],
'SELECT ' + sc.name + ' FROM ' +
SCHEMA_NAME(so.schema_id) + '.' + 
OBJECT_NAME(sc.object_id) AS [SelectStmt]
FROM sys.columns sc
INNER JOIN sys.objects so ON sc.object_id = so.object_id
WHERE sc.max_length = -1 --varchar(max), nvarchar(max), varbinary(max), or xml 
AND so.type = 'U' --user table
</pre>
This code snippet will help you find any columns in your database that are varchar(max), nvarchar(max), varbinary(max), or xml. The code is limited to only user tables. The code returns schema, table, and column names and builds a SELECT statement for you to run, if desired.

Feel free to take it and modify as you see fit.

When I run it against my version of GalacticWorks it returns 14 columns:

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/GDPR_columns.jpg"><img class="aligncenter size-large wp-image-18776" src="https://thomaslarock.com/wp-content/uploads/2018/03/GDPR_columns-600x302.jpg" alt="hidden columns with GDPR violations" width="600" height="302" /></a>

Once we have our list we can get started on examining the data to determine if they contain any PII data and likely GDPR violations you didn't know about.

&nbsp;
<h2>Parsing the Data</h2>
When it comes to parsing this data we have two main options: T-SQL and PowerShell. However, neither of those will help you with the varbinary(max) columns. For those columns you will need to export the data and view with any tool that can open an image. I included varbinary(max) in the result set because images can contain PII data and therefore you should be ware and classify those columns accordingly.

For the varchar(max and nvarchar(max) columns you can use T-SQL to easily search for strings. Here is but one example:
<pre lang="tsql">SELECT DocumentSummary 
FROM Production.Document
WHERE DocumentSummary LIKE '%SearchForSomething%'
</pre>
For the xml columns you can also use T-SQL, here's how you can do that:
<pre lang="tsql">SELECT * 
FROM  
(SELECT cast (Diagram as nvarchar(max)) [XmlText]
 FROM Production.Illustration) a 
WHERE [XmlText] LIKE '%SearchForSomething%'
</pre>
Yes, I could also use XQuery here, but to be honest XQuery is not the right solution anyway. No, if I was building this out for an enterprise I would use PowerShell to get this done. With PowerShell I could have a list of keywords to check as well as a list of regex strings to look for patterns (credit card number formats, social insurance number formats, etc.) PowerShell would make this task a lot easier than T-SQL. And PowerShell would let me scale beyond just the one instance of SQL Server, too.

&nbsp;
<h2>Summary</h2>
Life is dirty. So is your data. And that dirt is hiding everywhere. Don't be foolish to think you don't have PII data stuffed into a column somewhere. Don't think that because you are located in the US that the GDPR won't apply to you. Get in front of this situation now, before May arrives.

Take the time to do some data discovery. It will be worth your time.