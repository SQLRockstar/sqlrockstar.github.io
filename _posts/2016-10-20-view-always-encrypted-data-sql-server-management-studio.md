---
layout: post
title: How To View Always Encrypted Data in SQL Server Management Studio
date: '2016-10-20 12:50:53 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- Always Encrypted
- SQL Server 2016
---

One of the shiny new features in SQL Server 2016 is <a href="https://msdn.microsoft.com/en-us/library/mt163865.aspx" target="_blank">Always Encrypted</a>. I think Always Encrypted is a great addition to SQL Server (and <a href="https://azure.microsoft.com/en-us/documentation/articles/sql-database-always-encrypted/" target="_blank">Azure SQL Database</a>) and a step in the right direction for data security. The last data security feature added to SQL Server was <a href="https://msdn.microsoft.com/en-us/library/bb934049.aspx" target="_blank">Transparent Data Encryption (TDE)</a> and that was just about ten years ago. So, we were due for some new features.

Configuring a column for encryption is easy enough (providing it meets the <a href="https://msdn.microsoft.com/en-us/library/mt163865.aspx" target="_blank">long list of supported columns listed here</a>), and here's an example of what the result looks like:<a href="https://thomaslarock.com/wp-content/uploads/2016/10/encrypt.jpg">
</a>

<a href="https://thomaslarock.com/wp-content/uploads/2016/10/encrypt.png"><img class="aligncenter wp-image-17507 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/encrypt-600x312.png" alt="always encrypted" width="600" height="312" /></a>
<p style="text-align: left;">The NationalIDNumber is encrypted, and shows only the ciphertext in the results window inside SQL Server Management Studio (SSMS). Note that I am only seeing the ciphertext even though I am logged in as a member of the system administrators role. The reason for this is because I need to connect to the database server with the 'Column Encryption Setting = Enabled' parameter.</p>
<p style="text-align: left;">Well, that's easy enough to do, I can just change the connection and select the 'Options' in the lower right:<a href="https://thomaslarock.com/wp-content/uploads/2016/10/conn1.jpg">
</a></p>
<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2016/10/conn1.png"><img class="aligncenter wp-image-17509 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/conn1-600x395.png" alt="always encrypted" width="600" height="395" /></a></p>
<p style="text-align: left;">Doing so will reveal a new screen with three tabs. Click on the 'Additional Connection Parameters' and type in the parameter:</p>
<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2016/10/conn2.png"><img class="aligncenter wp-image-17510 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/conn2-550x600.png" alt="always encrypted connection" width="550" height="600" /></a></p>
<p style="text-align: left;">And, if we run the query again, we see the unencrypted data:</p>
<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2016/10/plaintext.png"><img class="aligncenter wp-image-17511 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/plaintext-600x371.png" alt="always encrypted" width="600" height="371" /></a></p>
<p style="text-align: left;">The reason I can see this data is because the column master key exists on the database server. You can see the one that was created by me for this example:</p>
<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2016/10/master-key.png"><img class="aligncenter wp-image-17512 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/master-key-600x231.png" alt="always encrypted" width="600" height="231" /></a></p>
<p style="text-align: left;">That certificate wasn't there before. And, it's worth noting that the name says 'Always Encrypted'. If an attacker got access to the server they *may* be able to search for that string and try to export the certificates. But I don't want to you to think that this is likely, because if a person really wants access to the data they are going to get it from Jim down the hall who is only to happy to run reports for people when asked. But I digress...</p>
<p style="text-align: left;">The real point here is that without that master column key, I will not be able to see the data. This is how Always Encrypted works. You export the column master key certificate to the client(s) and then the client connects using the connection string parameter and you are done (assuming the necessary database permissions to query the data).</p>
<p style="text-align: left;">But look at what happens when I query the AdventureWorks2016CTP3.Sales.CustomerPII table using the same connection:</p>
<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2016/10/error.png"><img class="aligncenter wp-image-17513 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/10/error-600x342.png" alt="always encrypted" width="600" height="342" /></a></p>
<p style="text-align: left;">I get the following error message:</p>

<pre><span style="color: #ff0000;">Msg 0, Level 11, State 0, Line 0</span>
<span style="color: #ff0000;">Failed to decrypt column 'SSN'.</span>
<span style="color: #ff0000;">Msg 0, Level 11, State 0, Line 0</span>
<span style="color: #ff0000;">Failed to decrypt a column encryption key using key store provider: 'MSSQL_CERTIFICATE_STORE'. 
The last 10 bytes of the encrypted column encryption key are: 'F7-B0-8B-E6-79-EA-D4-E5-7A-D7'.</span>
<span style="color: #ff0000;">Msg 0, Level 11, State 0, Line 0</span>
<span style="color: #ff0000;">Certificate with thumbprint '8C5AE6DCC176752931B33BFE03B7E4EA3A73572C' not found in 
certificate store 'My' in certificate location 'CurrentUser'. Verify the certificate path 
in the column master key definition in the database is correct, and the certificate has 
been imported correctly into the certificate location/store.</span>
<span style="color: #ff0000;">Parameter name: masterKeyPath</span></pre>
I don't have the column master key for this data, so I won't be able to view it. Ever.

I can't decrypt it either, also because I don't have the column master key.

And unless the person at Microsoft that deployed AdventureWorks2016CTP3 gives me the key, I never will.

So, I'd say that 'Always Encrypted' is a perfect description for this new feature in SQL Server 2016. Unlike TDE which will <a href="https://thomaslarock.com/2016/02/migrating-data-from-a-tde-enabled-sql-server-database-without-a-key/" target="_blank">allow for me to migrate encrypted data without having the key</a>, Always Encrypted won't allow anyone to see the data without having the certificate installed.