---
layout: post
title: 'HOW TO: Change the Compatibility Level of an Azure SQL Database'
date: '2016-01-04 12:35:22 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
- SQL Server Performance
tags:
- Azure
- cardinality
- compatibility mode
- database
- microsoft
- MSSQL
- SQL
- sql server
---

I love how Azure SQL Database keeps <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-v12-whats-new/" target="_blank">adding new features on a frequent basis</a>. And while they maintain a good list of new features being added, every now and then something slips under the radar for me. Here's an example of something I came across for Azure SQL Database V12 that I don't see documented anywhere (yet):

<em><strong>You can change the compatibility level of an Azure SQL Database.</strong></em>

It's true! I know!

OK, so I'm a little excited about this one. See, I've been giving this talk on cardinality for the <a href="https://channel9.msdn.com/Events/TechEd/NorthAmerica/2014/DBI-B331#fbid=" target="_blank">past couple of years now</a>, so this is a hidden gem to me. When I found out this was possible I took out my demo scripts to see if changing the compatibility level would have any effect.

First, let's see what the compatibility mode looks like when we connect to our Azure SQL Database:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/azure_db_properties_mask.jpg" target="_blank" rel="attachment wp-att-17245"><img class="aligncenter wp-image-17245 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/01/azure_db_properties_mask-600x539.jpg" alt="azure_db_properties_mask" width="600" height="539" /></a>

There are a few things to note in the above image. First, I am connected to my Azure SQL database named AdventureWorks2014_v12. This is so I don’t lose track of the database I am connected to when testing. Second, the compatibility level for my v12 Azure SQL Database is set to 120. Lastly, the compatibility level dropdown is disabled because I cannot change the compatibility mode for an Azure SQL Database from within SQL Server Management Studio (I am using the SQL 2014 bits for SSMS here).

Using the scripts from my session I create a table of 65,536 rows using the following:
<pre lang="tsql">CREATE TABLE dbo.CETest
(
	ID int not null,
	ADate date not null,
	Placeholder char(10)
);

;WITH N1(C) AS (SELECT 0 UNION all SELECT 0) -- 2 rows
,N2(C) AS (SELECT 0 from N1 AS T1 cross join N1 AS T2) -- 4 rows
,N3(C) AS (SELECT 0 from N2 AS T1 cross join N2 AS T2) -- 16 rows
,N4(C) AS (SELECT 0 from N3 AS T1 cross join N3 AS T2) -- 256 rows
,N5(C) AS (SELECT 0 from N4 AS T1 cross join N4 AS T2) -- 65,536 rows
,IDs(ID) AS (SELECT row_number() OVER (ORDER BY (SELECT NULL)) FROM N5)
	INSERT INTO dbo.CETest(ID,ADate)
		SELECT ID,dateadd(day,abs(checksum(newid())) % 365,'2013-06-01') 
		FROM IDs;

CREATE UNIQUE CLUSTERED INDEX IDX_CETest_ID
ON dbo.CETest(ID);

CREATE NONCLUSTERED INDEX IDX_CETest_ADate
ON dbo.CETest(ADate);
</pre>
As in my session, I will now add an additional 10% to the table so as to not trigger an automatic updating of statistics:
<pre lang="tsql">;WITH N1(C) AS (SELECT 0 UNION all SELECT 0) -- 2 rows
,N2(C) AS (SELECT 0 FROM N1 AS T1 cross join N1 AS T2) -- 4 rows
,N3(C) AS (SELECT 0 FROM N2 AS T1 cross join N2 AS T2) -- 16 rows
,N4(C) AS (SELECT 0 FROM N3 AS T1 cross join N3 AS T2) -- 256 rows
,N5(C) AS (SELECT 0 FROM N4 AS T1 cross join N4 AS T2) -- 65,536 rows
,IDs(ID) AS (SELECT row_number() OVER (ORDER BY (SELECT NULL)) FROM N5)
	INSERT INTO dbo.CETest(ID,ADate)
		SELECT ID + 65536,dateadd(day,abs(checksum(newid())) % 365,'2013-06-01') 
		FROM IDs
		WHERE ID <= 6554;
</pre>
OK, everything is set for us to test, so we run the following query (for this query we are choosing a date that is not a boundary point in the histogram):
<pre lang="tsql">select ID, ADate, Placeholder
from dbo.CETest with (index=IDX_CETest_ADate)
where ADate = '2013-06-13'
</pre>
Which gives us the following result (your estimates are likely to be different than what is shown here, for this point the DBCC SHOW_STATISTICS gives me an estimate of 169 rows):

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/first_test.png" rel="attachment wp-att-17248"><img class="aligncenter wp-image-17248 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/01/first_test.png" alt="first_test" width="490" height="361" /></a>

OK, that’s good. For a value not a boundary point in the histogram the new cardinality estimator (CE) takes into account the extra 10% of rows. This is as expected for the new CE, as the legacy CE would have returned an estimate of 169.

So, now lets run the statement but revert to the old CE <a href="https://support.microsoft.com/en-us/kb/2801413" target="_blank">using a query hint</a>:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/first_revert.png" rel="attachment wp-att-17249"><img class="aligncenter size-full wp-image-17249" src="https://thomaslarock.com/wp-content/uploads/2016/01/first_revert.png" alt="first_revert" width="438" height="205" /></a>

So, Azure SQL Database doesn't like the OPTION (QUERYTRACEON 9481) query hint. But that's OK, because we have another option when trying to test, we can set the compatibility mode for the entire Azure SQL Database.
<pre lang="tsql">ALTER DATABASE [AdventureWorks2014_v12] SET COMPATIBILITY_LEVEL = 110
GO
</pre>
This seems to work (at the very least it did not generate an error):

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/alter_database.png" rel="attachment wp-att-17250"><img class="aligncenter size-full wp-image-17250" src="https://thomaslarock.com/wp-content/uploads/2016/01/alter_database.png" alt="alter_database" width="546" height="121" /></a>

Now, let's rerun that first statement:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/second_test.png" rel="attachment wp-att-17251"><img class="aligncenter size-full wp-image-17251" src="https://thomaslarock.com/wp-content/uploads/2016/01/second_test.png" alt="second_test" width="487" height="328" /></a>

Success! I am able to test this query using the legacy cardinality estimator (CE)! Note that *all* queries will be using the legacy CE at this point, this is an all-or-nothing option here because the query hint is not supported at this time. Still, it's good to know that we can test estimates and query performance by comparing legacy CE versus the new CE.

And, just for good measure, we now see this:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/azure_db_properties_after_mask.jpg" rel="attachment wp-att-17252"><img class="aligncenter wp-image-17252 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/01/azure_db_properties_after_mask-600x539.jpg" alt="azure_db_properties_after_mask" width="600" height="539" /></a>

SSMS displays the compatibility mode as 110. I've tried looking for this information in the Azure portal but was not able to find it. If anyone does know where this is displayed in the portal please leave a comment.

Lastly, just for fun, I tried to set the compatibility mode to 80:

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/compatibility_80_Error.png" rel="attachment wp-att-17253"><img class="aligncenter size-full wp-image-17253" src="https://thomaslarock.com/wp-content/uploads/2016/01/compatibility_80_Error.png" alt="compatibility_80_Error" width="568" height="135" /></a>

130! That's SQL Server 2016! When I set the compatibility mode to 130 the SSMS properties displayed the dropdown as blank (or, perhaps, NULL). So, my guess is that while 130 is a valid option, there is still something missing under the hood to make v12 fully SQL 2016 right now. But I suspect that will change soon enough.

Now, a quick reminder, what we did here affects all queries. So, while changing the compatibility mode for your Azure SQL Database might not be wise to do, it's is at least an option. And something is always better than nothing.

But it would be great to have the QUERYTRACEON options available, someday.