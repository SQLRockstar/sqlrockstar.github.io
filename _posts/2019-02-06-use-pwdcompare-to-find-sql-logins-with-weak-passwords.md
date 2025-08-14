---
layout: post
title: Use PWDCOMPARE() to Find SQL Logins With Weak Passwords
date: '2019-02-06 09:55:15 +0000'
categories:
- Data Security and Privacy
- Database Design
- MSSQL
- SQL MVP
- SQL Server 2017
tags:
- data privacy
- data security
---

Not a day, week, or month goes by without news of <a href="https://www.bing.com/news/search?q=data+breach" target="_blank" rel="noopener">yet another data breach</a>.

And the breaches aren't the result of some type of <a href="https://www.youtube.com/watch?v=ar0xLps7WSY" target="_blank" rel="noopener">Mission Impossible heist</a>. No, it's often an <a href="https://threatpost.com/experts-warn-too-often-aws-s3-buckets-are-misconfigured-leak-data/126826/" target="_blank" rel="noopener">unprotected S3 bucket</a>, maybe some <a href="https://threatpost.com/sql-injection-attack-is-tied-to-election-commission-breach/122571/" target="_blank" rel="noopener">SQL Injection</a>, or <a href="https://www.hipaajournal.com/july-2018-healthcare-data-breach-report/" target="_blank" rel="noopener">files left behind when relocating to a new office</a>. Silly, fundamental mistakes made by people that should know better.

After decades of reviewing data breaches I have arrived at the following conclusion:
<blockquote>
<h2>Data security is hard because people are dumb.</h2>
</blockquote>
Don't just take my word for it though. Do a quick search for "common password list" and you'll see examples of passwords scraped from breaches. These are passwords often used by default to secure systems and data.

Chances are, these passwords are in your environment, right now.

Here's what you can do to protect your data.

&nbsp;
<h2>Use PWDCOMPARE() to Find SQL Logins With Weak Passwords</h2>
SQL Server ships with an internal system function, <a href="https://docs.microsoft.com/en-us/sql/t-sql/functions/pwdcompare-transact-sql?view=sql-server-2017" target="_blank" rel="noopener">PWDCOMPARE()</a>, that we can use to find SQL logins with weak passwords. We can combine this function, along with a list of weak passwords, and some PowerShell to do a quick check.

First, let's build a list. I'll store mine as a text file and it looks like this:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2019/02/password_list.jpg"><img class="aligncenter size-large wp-image-19474" src="https://thomaslarock.com/wp-content/uploads/2019/02/password_list-206x600.jpg" alt="use PWDCOMPARE() to find sql logins with weak passwords" width="206" height="600" /></a>

&nbsp;

I can import that file as an array into PowerShell with one line of code:
<pre lang="powershell">$pwdList = Get-Content .\password_list.txt</pre>
And with just a few lines of code, we can build a query and execute against our instance of SQL Server:
<pre lang="powershell">foreach ($password in $pwdList) {
$SQLText = "SELECT name FROM sys.sql_logins WHERE PWDCOMPARE('$password', password_hash) = 1;"
Invoke-Sqlcmd -Query $SQLText -ServerInstance $SQLServer
}</pre>
And we find that the ITSupport login has a weak password:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2019/02/password_check_result.jpg"><img class="aligncenter size-large wp-image-19476" src="https://thomaslarock.com/wp-content/uploads/2019/02/password_check_result-600x182.jpg" alt="weak password check result" width="600" height="182" /></a>

&nbsp;

As <a href="https://www.youtube.com/watch?v=U7XVcqZodAM" target="_blank" rel="noopener">Dark Helmet once said</a>, "Now you see that evil will always triumph, because good is dumb."

&nbsp;
<h2>Preventing Weak Passwords for SQL Logins</h2>
One of the easiest things you can do is to <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017" target="_blank" rel="noopener">enable the CHECK_POLICY for SQL logins</a>. By default, enabling the CHECK_POLICY option will also force the password expiration by enabling the CHECK_EXPIRATION flag. In other words, you can have passwords for SQL logins expire as if they were windows logins, and you can enforce complex passwords.

However, even with those checks enabled, I would advise you still do a manual check for weak passwords. Do not assume that by enabling the password policy checks that you are secure. In fact, you should do the opposite. You should take a stance of <em>assume compromise</em>. This is a <a href="https://www.cyberscoop.com/nist-cybersecurity-guide-legacy-systems-ron-ross/" target="_blank" rel="noopener">fundamental aspect of modern Cybersecurity practices</a>.

As a side note, I also want to point out that Troy Hunt has collected the passwords from many data breaches, and <a href="https://haveibeenpwned.com/Passwords" target="_blank" rel="noopener">he has made the passwords searchable</a>. Do yourself a favor and take some of the passwords you've used throughout the web and see if they have been exposed at some point.
<h2></h2>
<h2>Summary</h2>
SQL Server offers system functions to help you search for weak passwords, as well as policies to enforce complex passwords and password expiration. You should adopt a stance of "assume compromise" and be proactive about checking the passwords in your environment to make certain they are not considered weak.

[<em>Hey there, dear reader, if you liked this post about passwords and data security, then you might also like the full day training session I am delivering with Karen Lopez in two weeks at <a href="https://sqlkonferenz.de/agenda.aspx" target="_blank" rel="noopener">SQL Konferenz</a>. The title is Advanced Data Protection: Security and Privacy in SQL Server, and you'll learn more about how to protect your data at rest, in use, and in motion</em>.]

&nbsp;