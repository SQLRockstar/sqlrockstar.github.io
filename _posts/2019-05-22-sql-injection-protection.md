---
layout: post
title: SQL Injection Protection
date: '2019-05-22 10:52:56 +0000'
categories:
- AWS
- Azure
- Data Security and Privacy
- Database Design
- MSSQL
- SQL MVP
tags:
- security
- sql injection
---

SQL injection is a common form of data theft. I am hopeful we can make SQL injection protection more common.

The <a href="https://www2.trustwave.com/rs/815-RFM-693/images/Trustwave_2018-GSR_20180329_Interactive.pdf" target="_blank" rel="noopener noreferrer">2018 TrustWave Global Security Report</a> listed SQL Injection as the second most common technique for web attacks, trailing only cross-site scripting (XSS) attacks. This is a 38% increase from the previous year. That same report also shows SQL Injection ranked fifth on a list of vulnerabilities that can be identified through simple penetration testing.

You may look at the increase and think “whoa, attacks are increasing”. But I believe that what we are seeing is a rising awareness in security. No longer the stepchild, security is a first-class citizen in application design and deployment today. As companies focus on security, they deploy tools and systems to help identify exploits, leading to more reporting of attacks.

SQL Injection is preventable. That’s the purpose of this post today, to help you understand what SQL Injection is, how to identify when it is happening, and how to prevent it from being an issue.

&nbsp;
<h2>SQL Injection Explained</h2>
SQL injection is the method where an adversary appends a SQL statement to the input field inside a web page or application, thereby sending their own custom request to a database. That request could be to read data, or download the entire database, or even delete all data completely.

The most common example for SQL injection attacks are found inside username and password input boxes on a web page. This login design is standard for allowing users to access a website. Unfortunately, many websites do not take precautions to block SQL injection on these input fields, leading to SQL injection attacks.

Let’s look at a sample website built for the fictional Contoso Clinic. The source code for this can be found at <a href="https://github.com/Microsoft/azure-sql-security-sample" target="_blank" rel="noopener noreferrer">https://github.com/Microsoft/azure-sql-security-sample</a>.

On the Patients page you will find an input field at the top, next to a ‘Search’ button, and next to that a hyperlink for ‘SQLi Hints’.

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2019/05/contoso.jpg"><img class="aligncenter size-large wp-image-19531" src="https://thomaslarock.com/wp-content/uploads/2019/05/contoso-600x124.jpg" alt="contoso clinic sql injectoin example" width="600" height="124" /></a>

&nbsp;

Clicking on the SQLi Hints link will display some sample text to put into the search field.

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2019/05/sql-injection-example.jpg"><img class="aligncenter size-large wp-image-19532" src="https://thomaslarock.com/wp-content/uploads/2019/05/sql-injection-example-600x64.jpg" alt="sql injection example" width="600" height="64" /></a>

&nbsp;

I’m going to take the first statement and put it into the search field. Here is the result:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2019/05/sql-injection-error.jpg"><img class="aligncenter size-large wp-image-19533" src="https://thomaslarock.com/wp-content/uploads/2019/05/sql-injection-error-600x111.jpg" alt="sql-injection-error" width="600" height="111" /></a>

&nbsp;

This is a common attack vector, as the adversary can use this method to determine what version of SQL Server is running. This is also a nice reminder to not allow your website to return such error details to the end user. More on that later.

Let’s talk a bit about how SQL injection works under the covers.

&nbsp;
<h2>How SQL Injection works</h2>
The vulnerability in my sample website is the result of this piece of code:
<pre lang="tsql">return View(db.Patients.SqlQuery
("SELECT * FROM dbo.Patients
WHERE [FirstName] LIKE '%" + search + "%'
OR [LastName] LIKE '%" + search + "%'
OR [StreetAddress] LIKE '%" + search + "%'
OR [City] LIKE '%" + search + "%'
OR [State] LIKE '%" + search + "%'").ToList());</pre>
This is a common piece of code used by many websites. It is building a dynamic SQL statement based upon the input fields on the page. If I were to search the Patients page for ‘Rock’, the SQL statement sent to the database would then become:
<pre lang="tsql">SELECT * FROM dbo.Patients
WHERE [FirstName] LIKE '%Rock%'
OR [LastName] LIKE '%Rock%'
OR [StreetAddress] LIKE '%Rock%'
OR [City] LIKE '%Rock%'
OR [State] LIKE '%Rock%'</pre>
In the list of SQLi hints on that page you will notice that each example starts with a single quote, followed by a SQL statement, and at the end is a comment block (the two dashes). For the example I chose above, the resulting statement is as follows:
<pre lang="tsql">SELECT * FROM dbo.Patients
WHERE [FirstName] LIKE '%' OR CAST(@@version as int) = 1 --%'
OR [LastName] LIKE '%' OR CAST(@@version as int) = 1 --%'
OR [StreetAddress] LIKE '%' OR CAST(@@version as int) = 1 --%'
OR [City] LIKE '%' OR CAST(@@version as int) = 1 --%'
OR [State] LIKE '%' OR CAST(@@version as int) = 1 --%'</pre>
This results in the conversion error shown above. This also means that I can do interesting searches to return information about the database. Or I could do malicious things, like drop tables.

Chance are you have code like this, somewhere, right now. Let’s look at how to find out what your current code looks like.

&nbsp;
<h2>SQL Injection Discovery</h2>
Discovering SQL injection is not trivial. You must examine your code to determine if it is vulnerable. You must also know if someone is actively trying SQL injection attacks against your website. Trying to roll your own solution can take considerable time and effort.

There are two tools I can recommend you use to help discover SQL injection.

&nbsp;
<h3>Test Websites with sqlmap</h3>
One method is to use <a href="http://sqlmap.org/" target="_blank" rel="noopener noreferrer">sqlmap</a>, an open-source penetration testing project that will test websites for SQL injection vulnerabilities. This is a great way to uncover vulnerabilities in your code. However, sqlmap will not tell you if someone is actively using SQL injection against your website. You will need to use something else for alerts.

&nbsp;
<h3>Azure Threat Detection</h3>
If you are using Azure SQL Database, then you have the option to enable <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-threat-detection" target="_blank" rel="noopener noreferrer">Azure Threat Detection</a>. This feature will discover code vulnerabilities as well as alert you to attacks. It also checks for anomalous client login, data exfiltration, and if a harmful application is trying to access your database.

(For fairness, I should mention that <a href="https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-sql-conditions.html" target="_blank" rel="noopener noreferrer">AWS WAF allows for SQL injection detection</a>, but their process is a bit more manual that Azure).

If you try to roll your own discovery, you will want to focus on finding queries that have caused errors. Syntax errors, missing objects, permission errors, and UNION ALL errors are the most common. You can find a list of the common SQL Server error message numbers <a href="https://www.red-gate.com/hub/product-learning/sql-monitor/detect-sql-injection-attacks-using-extended-events-sql-monitor" target="_blank" rel="noopener noreferrer">here</a>.

It warrants mentioning that not all SQL injection attacks are discoverable. But when it comes to security, you will never eliminate all risk, you take steps to lower your risk. SQL injection discovery is one way to lower your risk.

&nbsp;
<h2>SQL Injection Protection</h2>
Detection of SQL Injection vulnerabilities and attacks are only part of the solution. In an ideal world, your application code would not allow for SQL Injection. Here’s a handful of ways you can lower your risk of SQL injection attacks.

&nbsp;
<h3>Parameterize Your Queries</h3>
Also known as ‘prepared statements’, this is a good way to prevent SQL injection attacks against the database. For SQL Server, prepared statements are typically done using the <a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql" target="_blank" rel="noopener noreferrer">sp_executesql()</a> system stored procedure.

Prepared statements should not allow an attacker to change the nature of the SQL statement by injecting additional code into the input field. I said “should”, because it is possible to write prepared statements in a way that would still be vulnerable to SQL injection. You must (1) know what you are doing and (2) learn to sanitize your inputs.

Traditionally, one argument against the use of prepared statements centers on performance. It is possible that a prepared statement may not perform as well as the original dynamic SQL statement. <em>However, if you are reading this and believe performance is more important than security, you should reconsider your career in IT before someone does that for you</em>.

&nbsp;
<h3>Use Stored Procedures</h3>
Another method available are stored procedures. Stored procedures offer additional layers of security that prepared statements may not allow. While prepared statements require permissions on the underlying tables, stored procedures can execute against objects without the user having similar direct access.

Like prepared statements, stored procedures are not exempt from SQL injection. It is quite possible you could put vulnerable code into a stored procedure. You must take care to compose your stored procedures properly, making use of parameters. You should also consider validating the input parameters being passed to the procedure, either on the client side or in the procedure itself.

&nbsp;
<h3>Use EXECUTE AS</h3>
You could use a security method such as <a href="https://docs.microsoft.com/en-us/sql/t-sql/statements/execute-as-transact-sql" target="_blank" rel="noopener noreferrer">EXECUTE AS</a> to switch the context of the user as you make a request to the database. As mentioned above, stored procedures somewhat act in this manner by default. But EXECUTE AS can be used directly for requests such as prepared statements or ad-hoc queries.

&nbsp;
<h3>Remove Extended Stored Procedures</h3>
Disabling the use of extended stored procedures is a good way to limit your risk with SQL injection. Not because you won’t be vulnerable, but because you limit the surface area for the attacker. By <a href="https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server" target="_blank" rel="noopener noreferrer">disabling these system procedures</a> you limit a common way that an attacker can get details about your database system.

&nbsp;
<h3>Sanitize Error Messages</h3>
You should never reveal error messages to the end user. Trap all errors and redirect to a log for review later. The less error information you bubble up, the better.

&nbsp;
<h3>Use Firewalls</h3>
Whitelisting of IP addresses is a good way to limit activity from anomalous users. Use of VPNs and VNETs to segment traffic can also reduce your risk.

&nbsp;
<h2>Summary</h2>
The #hardtruth here is that every database is susceptible to SQL injection attacks. No one platform is more at risk than any other. The weak link here is the code being written on top of the database. Most code development does not emphasize security enough, leaving themselves open to attacks.

When you combine poor database security techniques along with poor code, you get the recipe for SQL Injection.

&nbsp;
<h2>REFERENCES</h2>
<a href="https://www2.trustwave.com/rs/815-RFM-693/images/Trustwave_2018-GSR_20180329_Interactive.pdf" target="_blank" rel="noopener noreferrer">2018 TrustWave Global Security Report</a>
<a href="https://github.com/Microsoft/azure-sql-security-sample" target="_blank" rel="noopener noreferrer">Contoso Clinic Demo Application</a>
<a href="http://sqlmap.org/" target="_blank" rel="noopener noreferrer">sqlmap: Automatic SQL injection and database takeover tool</a>
<a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-threat-detection" target="_blank" rel="noopener noreferrer">Azure SQL Database threat detection</a>
<a href="https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-sql-conditions.html" target="_blank" rel="noopener noreferrer">Working with SQL Injection Match Conditions</a>
<a href="https://www.red-gate.com/hub/product-learning/sql-monitor/detect-sql-injection-attacks-using-extended-events-sql-monitor" target="_blank" rel="noopener noreferrer">How to Detect SQL Injection Attacks</a>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql" target="_blank" rel="noopener noreferrer">sp_executesql (Transact-SQL)</a>
<a href="https://docs.microsoft.com/en-us/sql/t-sql/statements/execute-as-transact-sql" target="_blank" rel="noopener noreferrer">EXECUTE AS (Transact-SQL)</a>
<a href="https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server " target="_blank" rel="noopener noreferrer">Server Configuration Options (SQL Server)</a>