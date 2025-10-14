---
layout: post
title: 'HOW TO: Recycle the SQL Server Analysis Services msmdsrv.log File'
date: '2015-01-14 15:39:37 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- errorlog
- msmdsrv
- Powershell
- SSAS
---

I found <a href="http://dba.stackexchange.com/questions/82624/huge-analysis-services-log-file-msmdsrv-log" target="_blank">this question over at DBA StackExchange</a> the other day and it left me shaking my head. How is it possible that there is no way to automatically recycle, or reset, the SQL Server Analysis Services (SSAS) error log in a similar manner to SQL Server? After all, it's <a href="http://www.sqlservercentral.com/articles/cyclingthoseerrorlogs/1118/" target="_blank">not like the technology doesn't exist</a> to solve this. More than likely it's just not a feature that anyone asked for, or anyone ever thought would be useful.

Until, that is, a log files grows out of control. I know that's certainly <a href="http://www.sqlservercentral.com/Forums/Topic625205-146-1.aspx" target="_blank">happened to me before</a>.

Where others see challenge, I see opportunity. I looked at this question as just that, an opportunity to get my hands on SSAS again as well as brush up on some Powershell.

The idea was simple enough. First, update the SSAS instance with a new filename. Then, restart the instance so that the new log file is used. You can see this in the server properties for SSAS:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/SSAS_Properties.png"><img class="aligncenter size-medium wp-image-11942" src="https://thomaslarock.com/wp-content/uploads/2015/01/SSAS_Properties-436x315.png" alt="SSAS_Properties" width="436" height="315" /></a>

You will want to enable the advanced properties checkbox (at the bottom) and then find the 'Log\File' property. You will notice that the column named 'Restart' has a value of 'yes' for this setting. If I make a change here and click OK I will be told that my changes require a restart. I could also choose to script this out in which case an <a href="http://technet.microsoft.com/en-us/library/ms186654(v=sql.110).aspx" target="_blank">XLMA script</a> will appear in a new window. And for a brief moment I thought that I might want to generate an XMLA script and use Powershell to just invoke that script each time, but then I regained my senses and knew that Powershell was better than that.

I stumbled a bit putting together my script so I decided to ask Laerte Junior (<a href="https://shellyourexperience.wordpress.com/" target="_blank">blog</a> | <a href="http://twitter.com/LaerteSQLDBA" target="_blank">@LaerteSQLDBA</a>) for some help. He got me back on track and this is what I have now. You can <a href="http://1drv.ms/1Ha50FP" target="_blank">download the script here</a> but before I forget, here’s my usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

OK, enough legalities, let's Powershell!
<pre lang="Powershell"><##############################################   
   File: ssas_cycle_errorlog.ps1     
   Author: Thomas LaRock, https://thomaslarock.com/contact-me/
   https://thomaslarock.com/2015/01/how-to-recycle-the-sql-server-analysis-services-msmdsrv-log-file/

   Summary: This script will connect to installed instances of SSAS
            that are running, will update the error log filename,
            and restart the SSAS instance.  

Here are the steps necessary to run this script:  

1. Run this script on demand  
2. Run this script as a Windows Scheduled Task  
3. Run this script as a SQL Agent Job (see script for section to uncomment)

   Date: January 12th, 2015

   SSAS Versions: SQL2008, SQL2008R2, SQL2012, SQL2014

   You may alter this code for your own purposes. You may republish
   altered code as long as you give due credit.

   THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
   OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT
   LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR
   FITNESS FOR A PARTICULAR PURPOSE.
##############################################>

[Reflection.Assembly]::LoadWithPartialName("Microsoft.AnalysisServices")

#Get a list of installed SSAS instances on this server that are running
#We need a service to be started in order to rename the log file
$SSASServices = Get-WmiObject -query "select * from win32_service where DisplayName LIKE 'SQL Server Analysis%' and State = 'Running'"

#for each installed instance, update the logfile name

ForEach ($sname in $SSASServices)

{
 # Connect to the SSAS server
 $SSASServer = New-Object Microsoft.AnalysisServices.Server
 $SSASServer.Connect($sname.SystemName)

 #gets current filename
 $SSASErrorFileName = ($SSASServer.Serverproperties | where-Object {$_.Name -eq "Log\File"}).Value

 #split out the .log extension
 $SSASErrorName=$SSASErrorFileName.Split(".")[0]

 #rename the errorlog, appending the current date
 $ErrorLogName = "msmdsrv_{0}.log" -f (Get-Date -Format 'MM_dd_yyy_hh_mm_ss')

 $SSASServer.ServerProperties['Log\File'].Value = $ErrorLogName
 $SSASServer.ServerProperties['Log\File'].PendingValue = $ErrorLogName
 $SSASServer.Update()

 Restart-Service $SSASServices.Name
}
</pre>
A few notes about this script.
<ol>
	<li>It is looking for all installed instances of SSAS on a server.</li>
	<li>It is checking to make certain the instances of SSAS are running.</li>
	<li>Because if the instance isn't running, we can't update the error log filename.</li>
	<li>I didn't try to start a stopped instance, as I assume there is a reason it is stopped and wouldn't want to automate such a thing.</li>
	<li>For each running instance of SSAS the script will update the error log to append a datetime to the name.</li>
	<li>The previous error log file will remain on the server.</li>
	<li>You might want to add in an additional check for file size, and have the log only rollover after it reaches a certain limit. I didn't do this.</li>
	<li>You might also want to add in a check for the number of log files generated, and clean them out after a period of time. I didn't do this, either.</li>
	<li>You're welcome.</li>
</ol>
Now, you will probably want to schedule this script to be run against your instance, except if you enjoy running scripts manually. Do whatever feels right for you.

The two easiest ways to schedule this script to be run are either through the use of the default windows Task Scheduler or through a SQL Agent job. You can find info on <a href="http://www.metalogix.com/help/Content%20Matrix%20Console/SharePoint%20Edition/002_HowTo/004_SharePointActions/012_SchedulingPowerShell.htm" target="_blank">running a Powershell script as a scheduled task here</a>, and you can find details on <a href="http://msdn.microsoft.com/en-us/library/hh213688.aspx" target="_blank">creating a SQL Agent job that runs a Powershell script here</a>.

One bit of warning for you is that you may need to make some permission modifications for this script to work from a SQL Agent job. The account running the SQL Agent service must have admin rights to the SSAS instance as well as rights to be able to stop and start the SSAS service.

I hope this script is useful for anyone that finds themselves in need of cycling the SSAS msmdsrv error log file. If there are any issues with the script let me know so I can make updates as necessary.