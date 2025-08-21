---
layout: post
title: When to Use Row or Page Compression in SQL Server
date: '2018-01-31 20:37:55 +0000'
categories:
- Database Design
- MSSQL
- SQL Server 2017
- SQL Server Performance
tags:
- Microsoft SQL Server
- page compression
- performance
- row compression
- sql server
---

Introduced with SQL Server 2008, <a href="https://technet.microsoft.com/en-us/library/dd894051(v=sql.100).aspx" target="_blank" rel="noopener noreferrer">page and row compression are turning ten years old this year</a>. In that time, the internet became littered with posts describing both features, how they work, the performance gains, etc.

Despite digesting all of that information, a colleague asked me a very simple question those posts did not answer:
<blockquote>"How do I know to use row or page compression in SQL Server?"</blockquote>
That's what this post is for, to help provide some clarity on row versus page compression. You're welcome.

&nbsp;
<h2>Types of Data Compression in SQL Server</h2>
Row and page compression are a dirty secret among many SQL consultants.&nbsp;I know more than one person who walked into a shop, enabled compression, showed a performance gain on a critical report, and walked out with a fat contract that same day. I'm not writing this post to out them or their secret. I'm writing to help you get a fat contract, or a fat bonus, by understanding compression a bit better.

Let's start with the basics.&nbsp;SQL Server 2017 has the follow compression features:

- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/data-compression/row-compression-implementation" target="_blank" rel="noopener noreferrer">Row Compression</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/data-compression/page-compression-implementation" target="_blank" rel="noopener noreferrer">Page Compression</a>
- <a href="https://docs.microsoft.com/en-us/sql/t-sql/functions/compress-transact-sql" target="_blank" rel="noopener noreferrer">COMPRESS function</a>
- <a href="https://docs.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression" target="_blank" rel="noopener noreferrer">Columnstore compression</a>

The COMPRESS function uses GZIP to store data in a compressed format. Columnstore indexes store compressed data by default, and also offer archival compression using XPRESS. We aren't going to talk about COMPRESS or Columnstore today. Instead, we will focus on row and page compression, because that's the question asked. But I thought you should know what types of data compression are available in SQL Server 2017.

&nbsp;
<h2>How They Work</h2>
The first thing to understand is that <strong>row compression is a subset of page compression</strong>. Put another way, you cannot have page compression without first having row compression performed. When you go to enable page compression the engine will do the following actions in this order:

- Row compression
- Prefix compression
- Dictionary compression

Row compression is <a href="https://technet.microsoft.com/en-us/library/cc280576(v=sql.110).aspx" target="_blank" rel="noopener noreferrer">defined here</a>. The simple explanation is that it take fixed-length columns and makes them variable length, adding additional bytes for the overhead of tracking the changes being made. The link provided has a table that references the savings for the datatypes used. It's interesting reading. And by "interesting" I mean "it won't matter for my summary later".

Prefix and dictionary compression come next, as part of page compression. You can read all the <a href="https://technet.microsoft.com/en-us/library/cc280464(v=sql.110).aspx" target="_blank" rel="noopener noreferrer">details here</a>. The simple explanation is that the process looks for repeated patterns. First it looks for repeated values by column (that's the prefix part), then it looks for patterns on the entire page (that's the dictionary part). The link provided has the details and is more interesting than the row compression article for reasons that will be apparent soon-ish, I promise.

&nbsp;
<h2>How to enable Row or Page Compression in SQL Server</h2>
Enabling row or page compression on a table is easy. (However, enabling row or page compression for a database is not easy, because you have to enable it for each object manually. For large schemas, this can be a PITA and make you wish for the days of Microsoft Access and the '<a href="https://support.microsoft.com/en-us/help/288631" target="_blank" rel="noopener noreferrer">Compact and Repair Database</a>' option. LOL, no, it doesn't. Nothing makes anyone wish for Access. #justsayin)

Let's set up a test table and enable compression. Here's the example I've been using in my session "<a href="https://live360events.com/Events/2012/Sessions/Thursday/SQTH3-Database-Design-Size-DOES-Matter.aspx" target="_blank" rel="noopener noreferrer">Database Design: Size DOES Matter!</a>" for years.&nbsp;In that session I use sys.messages to populate a table:
<pre lang="tsql">CREATE TABLE [dbo].[TestCompression](
	[m_id] [int]  NULL,
	[text] [nvarchar](3000) NULL
) ON [PRIMARY]

INSERT INTO [dbo].[TestCompression] 
	SELECT message_id, text from sys.messages
</pre>
After the table is created, we <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-estimate-data-compression-savings-transact-sql" target="_blank" rel="noopener noreferrer">estimate the space savings for row compression</a> like this:
<pre lang="tsql">EXEC sp_estimate_data_compression_savings 'dbo', 'TestCompression', NULL, NULL, 'ROW' ;  
GO 
</pre>
Here's my result set (click to embiggen):

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/01/compression_results.jpg"><img class="aligncenter wp-image-18609 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/01/compression_results-600x116.jpg" alt="When to Use Row or Page Compression in SQL Server" width="600" height="116"></a>

&nbsp;

The results show an expected gain of 54.8% (taking the column size_with_requested_compression_setting(KB) and dividing by the column size_with_current_compression_setting(KB), or 31880/58112).&nbsp;I will leave estimating the space savings for page compression as an exercise for the reader. Besides, I don't want to spoil the surprise ending.

One last item before we enable row compression for this table. I want to know how many logical reads it takes to return all the rows. I will use STATISTICSIO to get this information:
<pre lang="tsql">SET STATISTICS IO ON
SELECT m_id, text
FROM dbo.TestCompression
SET STATISTICS IO OFF
</pre>
This returns the following message (formatted to fit on this page):
<pre>(232056 rows affected)
Table 'TestCompression'. Scan count 1, logical reads 7226, 
physical reads 0, read-ahead reads 7172, lob logical reads 0, 
lob physical reads 0, lob read-ahead reads 0.
</pre>
We now enable row compression with the following statement:
<pre lang="tsql">ALTER TABLE dbo.TestCompression REBUILD PARTITION = ALL 
WITH  
(DATA_COMPRESSION = ROW) 
GO 
</pre>
And now rerun the SELECT, and we observe the following message returned with the results:
<pre>(232056 rows affected)
Table 'TestCompression'. Scan count 1, logical reads 3982, 
physical reads 0, read-ahead reads 7, lob logical reads 0, 
lob physical reads 0, lob read-ahead reads 0.
</pre>
So, we have 55% fewer logical reads (3982/7226). Similar to the expected savings estimate of 54.8% found earlier.

(I love it when I check my work and the answers match.)

&nbsp;
<h2>When to Use Row or Page Compression in SQL Server</h2>
OK, we've reviewed details on compression in SQL Server, let's answer the original question: "How do I know to use row or page compression in SQL Server?"

The MSDN article I referenced and linked to at the beginning of the article has a wonderful summary for this purpose. If you are too lazy to scroll up, <a href="https://technet.microsoft.com/en-us/library/dd894051(v=sql.100).aspx" target="_blank" rel="noopener noreferrer">I will link to it again for you here</a>. If you are too lazy to read the article, let me repeat the pertinent details for you now:
<p style="padding-left: 30px;"><em>A more detailed approach to deciding what to compress involves analyzing the workload characteristics for each table and index. It is based on the following two metrics:</em></p>
<p style="padding-left: 30px;"><em>U: The percentage of update operations on a specific table, index, or partition, relative to total operations on that object. The lower the value of U (that is, the table, index, or partition is infrequently updated), the better candidate it is for page compression.</em></p>
<p style="padding-left: 30px;"><em> S: The percentage of scan operations on a table, index, or partition, relative to total operations on that object. The higher the value of S (that is, the table, index, or partition is mostly scanned), the better candidate it is for page compression.</em></p>
That sounds great except we don't know the percentage of update and scan operations. Yet.

Lucky for us the whitepaper includes the T-SQL needed to determine such metrics. For the U-value, the percentage of updates, we are given this code:
<pre lang="tsql">/*
To compute U, use the statistics in the DMV sys.dm_db_index_operational_stats. 
U is the ratio (expressed in percent) of updates performed on a table or index
 to the sum of all operations (scans + DMLs + lookups) on that table or index. 
 The following query reports U for each table and index in the database. 
*/

SELECT o.name AS [Table_Name], x.name AS [Index_Name],
       i.partition_number AS [Partition],
       i.index_id AS [Index_ID], x.type_desc AS [Index_Type],
       i.leaf_update_count * 100.0 /
           (i.range_scan_count + i.leaf_insert_count
            + i.leaf_delete_count + i.leaf_update_count
            + i.leaf_page_merge_count + i.singleton_lookup_count
           ) AS [Percent_Update]
FROM sys.dm_db_index_operational_stats (db_id(), NULL, NULL, NULL) i
JOIN sys.objects o ON o.object_id = i.object_id
JOIN sys.indexes x ON x.object_id = i.object_id AND x.index_id = i.index_id
WHERE (i.range_scan_count + i.leaf_insert_count
       + i.leaf_delete_count + leaf_update_count
       + i.leaf_page_merge_count + i.singleton_lookup_count) != 0
AND objectproperty(i.object_id,'IsUserTable') = 1
ORDER BY [Percent_Update] ASC
</pre>
For S, the percentage of scans, we are given this code:
<pre lang="tsql">/*
To compute S, use the statistics in the DMV sys.dm_db_index_operational_stats. 
S is the ratio (expressed in percent) of scans performed on a table or index 
to the sum of all operations (scans + DMLs + lookups) on that table or index. 
In other words, S represents how heavily the table or index is scanned. 
The following query reports S for each table, index, and partition in the database.
*/

SELECT o.name AS [Table_Name], x.name AS [Index_Name],
       i.partition_number AS [Partition],
       i.index_id AS [Index_ID], x.type_desc AS [Index_Type],
       i.range_scan_count * 100.0 /
           (i.range_scan_count + i.leaf_insert_count
            + i.leaf_delete_count + i.leaf_update_count
            + i.leaf_page_merge_count + i.singleton_lookup_count
           ) AS [Percent_Scan]
FROM sys.dm_db_index_operational_stats (db_id(), NULL, NULL, NULL) i
JOIN sys.objects o ON o.object_id = i.object_id
JOIN sys.indexes x ON x.object_id = i.object_id AND x.index_id = i.index_id
WHERE (i.range_scan_count + i.leaf_insert_count
       + i.leaf_delete_count + leaf_update_count
       + i.leaf_page_merge_count + i.singleton_lookup_count) != 0
AND objectproperty(i.object_id,'IsUserTable') = 1
ORDER BY [Percent_Scan] DESC
</pre>
OK, let's put it all together.

&nbsp;
<h2>Summary</h2>
All of the above information can be found on hundreds of blog posts over the past ten years. Here's the part that I haven't found mentioned anywhere else:

<strong>When your table has few duplicate values, as our test table does here, row compression is the right answer no matter what your U-value or S-value</strong>. The reason for this is detailed above. Page compression looks for repeated patterns. Therefore, if your data does not have repeated patterns, you don't get much extra benefit from page compression. You will see extra CPU utilization, but probably not much of a performance gain to make it worthwhile. Our test table has few repeated patterns, therefore page compression is likely to be more overhead than what is needed.

(Of course you should test everything and not just listen to me ramble. Oh, and now would be a good time to do that exercise I left for you above.)

And that's the decision point I want you to take away from this post.<strong> When you need to decide to use either row or page compression look at the data and determine if it is likely to have repeated values or not</strong>. If yes, then it is a candidate for page compression provided the U and S-values are OK. If there are few repeated values, then row compression is likely to be sufficient.

(BONUS: I once wrote a post on how to <a href="https://thomaslarock.com/2014/05/size-matters-table-rows-and-database-data-pages/" target="_blank" rel="noopener noreferrer">find the objects in your database that store the fewest number of rows per page</a>. It may be relevant for your interests here, too. Have a look.)