---
layout: post
title: Schema Compare for SQL Server
date: '2018-02-14 13:32:09 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- data migration
- Microsoft SQL Server
- schema compare
---

SQL Server Management Studio (SSMS) does not offer the ability to do a schema compare between two databases. Therefore, you have two options to do a schema compare for SQL Server databases. The first is to use Visual Studio. The other is to use a 3rd party tool. However, there are two issues with either of those options that affect a lot of data professionals and DBAs:

1 - You aren't allowed to install tools to your work machine.
2 - You don't get any budget to purchase tools.

Today I'm going to show how to do a schema compare using only SSMS, dacpac files, and the FC (File Compare) command available in Windows. As always, you're welcome.

&nbsp;
<h2>Create a DACPAC</h2>
First, create a dacpac for each database. I am going to use AdventureWorks2008 and AdventureWorks2012 as my examples for this post. You create a dacpac by right-clicking on the database name in SSMS, selecting Tasks, then 'Extract Data-tier Application...' No, I don't know why they couldn't name it something easier, like 'Create DACPAC'. But I digress. Here's what it looks like:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/create_dacpac.jpg"><img class="aligncenter wp-image-18674 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/02/create_dacpac-600x573.jpg" alt="create dacpac" width="600" height="573" /></a>

&nbsp;

Click through the wizard, pick a location to save the dacpac files, and wait for it to finish.

The dacpac files aren't useful in their current format at the moment. We will fix that next.

&nbsp;
<h2>How To Crack Open DACPAC Files Using This One Weird Trick</h2>
&nbsp;

[video width="800" height="502" mp4="https://thomaslarock.com/wp-content/uploads/2018/02/rename_dacpac.mp4"][/video]

&nbsp;

That's right, all you need to do is rename the files from .dacpac to .zip, then extract the files. It's that simple. Once you do you will find a handful of files. We are going to focus on the model.xml today. I encourage you to poke around the origin.xml file to see the goodness inside there.

&nbsp;
<h2>Open a Command Prompt</h2>
Yes, I said a command prompt. I know this is possible with PowerShell. More on that later.

Windows comes with the FC command, available from the command line. Open a command line and run 'help FC' to see the list of available switches.

<img class="aligncenter size-large wp-image-18680" src="https://thomaslarock.com/wp-content/uploads/2018/02/help_FC-600x481.jpg" alt="help fc.exe" width="600" height="481" />

&nbsp;

We will use the /L and /N switches and compare the two schemas, outputting to a file.
<pre lang="cmd">FC /L /N AdventureWorks2008\model.xml AdventureWorks2012\model.xml > output.txt</pre>
The compare produces an output file that looks like this:

<a href="https://thomaslarock.com/wp-content/uploads/2018/02/output_results.jpg"><img class="aligncenter size-large wp-image-18681" src="https://thomaslarock.com/wp-content/uploads/2018/02/output_results-600x161.jpg" alt="" width="600" height="161" /></a>

A quick check confirms that the PK name for the HumanResources.Employee table did change between the 2008 and 2012 versions of AdventureWorks.

&nbsp;
<h2>Summary</h2>
If you need to do a schema compare but are limited in your ability to purchase or install tools, the FC command is a brilliant option you have available in Windows.

If you are a PowerShell aficionado then you don't need me to tell you that the Compare-Object and Get-Content cmdlets can get the same job done. I will leave you with two thoughts on that subject. First, the FC command is a lot less typing, and I'm lazy. Second, PowerShell isn't the answer here, and neither is a command line. The real answer is to use Visual Studio to do the job right.