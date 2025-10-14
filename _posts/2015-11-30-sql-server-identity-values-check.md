---
layout: post
title: SQL Server Identity Values Check
date: '2015-11-30 10:09:16 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- identity values
- sql server
---

When I am delivering my session "<a href="http://www.sqlsaturday.com/423/Sessions/Details.aspx?sid=36725" target="_blank">Database Design: Size DOES Matter</a>" at events around the world I will ask about the use of SQL Server identity values. My question comes in two parts, the first being "Do you use identity values" followed by "do you know how many you have left"?

Many people answer yes to the first part. Very few have any idea about the second part.

So, that's the reason for this post today.
<h2>What is an identity column?</h2>
Identity columns are defined on a table so that the database engine will provide an incremental value automatically when a new row is inserted into the table. Only one identity column can be <a href="https://msdn.microsoft.com/en-us/library/ms174979.aspx" target="_blank">created per table</a>, and they are not guaranteed to be unique. You enforce uniqueness for an identity column when you define it as the only column in a unique index or in a unique constraint (which, in SQL Server, creates a unique index).

Identity columns are often great choices for primary keys because they are narrow and ever increasing (this matters most for clustered primary keys). For many OLTP systems in SQL Server this is often ideal and what I would prefer over another common primary key choice of GUIDs. Identity columns are defined with two parameters, the seed value and the increment. If not specified these values default to (1,1). This is often a problem in many designs because by choosing (1,1) you are cutting your possible values in half (because numeric datatypes have a range from negative to positive, i.e., smallint goes from -32768 to 32767).

That means you can run out in half the amount of time.
<h2>What happens when you run out of values?</h2>
When the engine runs out of values all inserts to the table will stop with this error message:

<span style="color: #ff0000;">Server: Msg 8115, Level 16, State 1, Line 1</span>
<span style="color: #ff0000;"> Arithmetic overflow error converting IDENTITY to data type smallint. Arithmetic overflow occurred.</span>

This is a bad thing, and forces people to reseed the identity, often choosing the negative values as a stop-gap until they can rebuild the table with a larger datatype such as integer or bigint. I find it amusing that the seed value of 1 was chosen to avoid using negative values but since using negative values is how people end up digging themselves out of a hole eventually anyway why not just use them from the start? I'm guessing some folks enjoy being called at 3AM.

<a href="https://thomaslarock.com/wp-content/uploads/2015/11/SQL_server_identity_value_check.jpg"><img class="aligncenter size-full wp-image-17198" src="https://thomaslarock.com/wp-content/uploads/2015/11/SQL_server_identity_value_check.jpg" alt="SQL_server_identity_value_check" width="614" height="461" /></a>

Oh well, that's why I like to keep track of such things. I want to know how many identity values I have left, if they started at the smallest possible value, if they are incrementing by more than 1, etc.
<h2>How you can keep track of identity values?</h2>
By using our script!

Earlier this year Karen Lopez prompted me to write some code to help answer a few basic questions about identity values. She and I worked on this over the past few months, trying to find time in between our busy travel schedules. Over time the questions got more complex (such as "what happens if an identity column is part of more than one index?") and we kept moving forward until we got to the version of the script we are sharing today.

A few remarks about the script:

<strong>If an identity column has not been used</strong> (i.e., no rows inserted yet) then it will not appear in the result set. I decided to avoid the extra math involved for NULL values because <a href="https://thomaslarock.com/2014/09/isnull-title-null-is-an-unknown-not-empty/" target="_blank">you know how much I hate those things</a>. Karen disagrees, of course, and will tell you the story about how her father has no middle name. But I digress.

Also, the script should <strong>return one row for each identity value for which uniqueness is being enforced</strong>. In other words, since it is valid for multiple unique indexes to be created with only the identity column as a member, the script should return one row for each. I mentioned earlier that a column only has one identity value allowed, but that identity can be in multiple indexes and constraints. If you have an identity column that is a single column in more than one index, we thought you should know this.

<strong>We assume a rate of one insert per second </strong>when calculating the date you will run out. Feel free to adjust as needed. We used that because we thought we should use something. Also, the DATEADD function we use only allows for integer values so we can't tell you how many seconds into the future it is for bigint values. It's a lot, though.

<strong>We show you if the identity column is unique</strong> with the Is_Unique column. Not all identity columns are unique. If they are, then the values you see for this column should be PK (primary key), UQ (unique constraint), or Index (unique index). In each case, the identity column should be the only column in the index. Since uniqueness is not guaranteed by default, if you find your identity columns are not unique then you should check with your business end-users and make certain if uniqueness is a requirement or not.

<strong>We show you how many inserts were possible</strong>, as well as remaining. This helps you decide if your original seed value was perhaps not the best choice.

OK, enough remarks for now, on to the script. As always, here is the usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

<del>You can also download a copy of the script here.</del>

UPDATED: As <a href="https://thomaslarock.com/2016/12/sql-server-identity-values-check-github/" target="_blank">noted in this post</a>, the script can now be <a href="https://github.com/SQLRockstar/BlogScripts/blob/master/SQL_Server_identity_values_check.sql" target="_blank">found over at GitHub</a>, please pull the latest version from there, thanks!
<pre lang="tsql">/*=============================================
  File: SQL_Server_identity_values_check.sql

  Authors: Thomas LaRock, https://thomaslarock.com/contact-me/ 
	    Karen Lopez, http://www.datamodel.com/index.php/category/blog/ 

  Original blog post at https://thomaslarock.com/2015/11/sql-server-identity-values-check

  Summary: 
  
	This script will return the following items:
		1. Schema_Name - The name of the schema for which the identity object belongs
		2. Table_Name - The name of the table for which the identity object belongs
		3. Column_Name - The name of the column for which the identity object belongs
		4. Row_Count - The current number of rows in the table, as found in sys.dm_db_partition_stats
		5. Total_Possible_Inserts - The number of inserts theoretically possible for the chosen identity datatype,
			(i.e., if we had started at the min/max value and incremented by a value of +/- 1)
		6. Inserts_Remaining - The number of inserts remaining given the last value and increment 
		7. Inserts_Possible - The number of total inserts possible given the defined seed and increment
		8. Current_Inserts_Used_Pct - The percentage of inserts used, 
		    calculated based upon Inserts_Remaining and Inserts_Possible (i.e., 1 - (IR/IP))
		9. Date_You_Will_Run_Out - The estimated date you will run out, based upon ONE INSERT PER SECOND and added to GETDATE()
		10. Is_Unique - If the identity column has been defined as unique. Possible values are:
			PK - Uniqueness through primary key definition
			UQ - Uniqueness through a unique constraint definition
			INDEX - Uniqueness through the creation of a unique index (and we filter for indexes with only the identity column)
			NONE - No uniqueness defined
		11. Increment_Value - The current increment value
		12. Last_Value - The last value inserted
		13. Min_Value - The minimum value for the chosen identity datatype
		14. Max_Value - The maximum value for the chosen identity datatype
		15. Seed_Value - The chosen seed value

  REMARKS: 
 
	If an identity column has not been used (i.e., no rows inserted yet) then it will not appear in the result set.
	You can see this in the code below, the section:

	WHERE Last_Value IS NOT NULL

	is where we are filtering for identity columns that have a last known value. 
	
	Also, the script should return one row for each identity value for which uniqueness is being enforced. In other words,
	since it is valid for multiple unique indexes with only the identity column as a member, the script should return
	one row for each. 

  Date: November 30th, 2015

  SQL Server Versions: SQL2008, SQL2008R2, SQL2012, SQL2014

  You may alter this code for your own purposes. You may republish
  altered code as long as you give due credit. 

  THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
  OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT
  LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR
  FITNESS FOR A PARTICULAR PURPOSE.

=============================================*/


/*=============================================
 Drop/create our temp table
=============================================*/
IF EXISTS (SELECT * FROM tempdb.dbo.sysobjects 
	WHERE id = OBJECT_ID(N'tempdb.dbo.#tmp_IdentValues')
	AND type IN (N'U'))
	DROP TABLE #tmp_IdentValues
GO

CREATE TABLE #tmp_IdentValues
	(Schema_Name sysname,
	Table_Name sysname,
	Column_Name sysname,
	Index_ID int,
	Seed_Value DECIMAL(38,0),
	Increment_Value DECIMAL(38,0),
	Last_Value DECIMAL(38,0),
	Data_Type sysname,
	Min_Value DECIMAL(38,0),
	Max_Value DECIMAL(38,0),
	Row_Count bigint,
	Is_Unique CHAR(5),
	Count tinyint)
GO

/*=============================================
 Insert into #tmp_IdentValues 
=============================================*/
INSERT INTO #tmp_IdentValues
select OBJECT_SCHEMA_NAME(si.object_id), OBJECT_NAME(si.object_id)
	, si.name
	, six.index_id
	, CONVERT(DECIMAL(38,0),si.seed_value)
	, CONVERT(DECIMAL(38,0),si.increment_value)
	, CONVERT(DECIMAL(38,0),si.last_value)
	, TYPE_NAME(si.system_type_id)
	, CASE WHEN TYPE_NAME(si.system_type_id) = 'tinyint' THEN 0
	  WHEN TYPE_NAME(si.system_type_id) = 'smallint' THEN -32768
	  WHEN TYPE_NAME(si.system_type_id) = 'int' THEN -2147483648
	  WHEN TYPE_NAME(si.system_type_id) = 'bigint' THEN -9223372036854775808
	  WHEN TYPE_NAME(si.system_type_id) = 'decimal' THEN -9999999999999999999999999999999
	  WHEN TYPE_NAME(si.system_type_id) = 'numeric' THEN -9999999999999999999999999999999
	  END
	, CASE WHEN TYPE_NAME(si.system_type_id) = 'tinyint' THEN 255
	  WHEN TYPE_NAME(si.system_type_id) = 'smallint' THEN 32767
	  WHEN TYPE_NAME(si.system_type_id) = 'int' THEN 2147483647
	  WHEN TYPE_NAME(si.system_type_id) = 'bigint' THEN 9223372036854775807
	  WHEN TYPE_NAME(si.system_type_id) = 'decimal' THEN 9999999999999999999999999999999
	  WHEN TYPE_NAME(si.system_type_id) = 'numeric' THEN 9999999999999999999999999999999
	  END 
	, sp.row_count
	, CASE WHEN kc.type IS NULL THEN --If NULL, then we don't have a key constraint, so check for unique index
			CASE WHEN six.is_unique = 0 THEN 'NONE' --If = 0, then we don't have a unique index 
			ELSE 'INDEX'
			END
	  ELSE kc.type 
	  END AS [uniquiness]
	 , COUNT(*) OVER(PARTITION BY OBJECT_SCHEMA_NAME(si.object_id), OBJECT_NAME(si.object_id), si.name) as [Count]
FROM sys.identity_columns si
INNER JOIN sys.tables st ON si.object_id = st.object_id
LEFT OUTER JOIN sys.indexes six ON si.object_id = six.object_id
LEFT OUTER JOIN sys.index_columns sic ON si.object_id = sic.object_id
	AND six.index_id = sic.index_id
LEFT OUTER JOIN sys.key_constraints kc ON kc.parent_object_id = si.object_id AND kc.unique_index_id = six.index_id
INNER JOIN sys.dm_db_partition_stats sp ON sp.object_id = si.object_id
	AND sp.index_id = six.index_id
GROUP BY OBJECT_SCHEMA_NAME(si.object_id), OBJECT_NAME(si.object_id)
	, si.name
	, six.index_id
	, CONVERT(DECIMAL(38,0),si.seed_value)
	, CONVERT(DECIMAL(38,0),si.increment_value)
	, CONVERT(DECIMAL(38,0),si.last_value)
	, TYPE_NAME(si.system_type_id)
	, six.name
	, six.is_unique
	, kc.type
	, sp.row_count 
HAVING COUNT(*) &lt; 2 --we are only interested in unique indexes with one column order by 1,2 /*============================================= Select from #tmp_IdentValues =============================================*/ SELECT Schema_Name , Table_Name , Column_Name , Row_Count , FLOOR((Max_Value - Min_Value)/ABS(Increment_Value)) AS [Total_Possible_Inserts] , FLOOR(CASE WHEN (Increment_Value &gt; 0) 
	  THEN (Max_Value-Last_Value)/Increment_Value
	  ELSE (Min_Value-Last_Value)/Increment_Value
	  END) AS [Inserts_Remaining] 
	, FLOOR(CASE WHEN (Increment_Value &gt; 0) 
	  THEN (Max_Value-Seed_Value + 1.0)/Increment_Value
	  ELSE (Min_Value-Seed_Value + 1.0)/Increment_Value
	  END) AS [Inserts_Possible] 
	, CAST(
		CASE WHEN (Increment_Value &gt; 0) 
		THEN (100)*(1.0-(CAST(Max_Value-Last_Value AS FLOAT)/CAST(Max_Value-Seed_Value + 1.0 AS FLOAT)))
		ELSE (100)*(1.0-(CAST(Min_Value-Last_Value AS FLOAT)/CAST(Min_Value-Seed_Value + 1.0 AS FLOAT)))
		END AS DECIMAL(10,8))
		AS [Current_Inserts_Used_Pct] 
	, CASE WHEN (Increment_Value &gt; 0) THEN
				CASE WHEN FLOOR((Max_Value - Last_Value)/Increment_Value) &lt;= 2147483647 
				THEN CONVERT(DATE, DATEADD(ss, FLOOR((Max_Value - Last_Value)/Increment_Value), GETDATE()), 103)
				ELSE '1/1/1900' 
				END
		ELSE 
				CASE WHEN FLOOR((Min_Value - Last_Value)/Increment_Value) &lt;= 2147483647 
				THEN CONVERT(DATE, DATEADD(ss, FLOOR((Min_Value - Last_Value)/Increment_Value), GETDATE()), 103)
				ELSE '1/1/1900' 
				END
		END AS [Date_You_Will_Run_Out] 
	, Is_Unique 
	, Increment_Value   
	, Last_Value  
	, Min_Value  
	, Max_Value  
	, Seed_Value  
FROM #tmp_IdentValues
WHERE Last_Value IS NOT NULL  --only want to include identity columns that have been used
AND (Is_Unique &lt;&gt; 'NONE' AND INDEX_COL(Schema_Name+'.'+ Table_Name, Index_ID, 1) = Column_Name
	OR
	Count = 1
	) 
GROUP BY Schema_Name, Table_Name, Column_Name, Index_ID, Row_Count, Is_Unique, Increment_Value, Last_Value, Min_Value, Max_Value, Seed_Value 
ORDER BY Current_Inserts_Used_Pct DESC
</pre>
Many thanks to Karen for her patience in helping with this script. I would have never written it without her prompting or her telling me to "try harder" with each version. Data architects seem to have a knack for asking about absurd edge cases normal people never think about happening, like not having a middle name.