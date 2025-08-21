---
layout: post
title: How to Check if Your Database Server Is Protected Against Meltdown and Spectre
date: '2018-01-09 14:29:50 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MCM
- SQL MVP
- SQL Server 2016
- SQL Server 2017
- SQL Server Performance
tags:
- meltdown
- microsoft
- security
- spectre
- sql server
---

Last week <a href="https://thomaslarock.com/2018/01/sql-server-guidance-protect-meltdown-spectre-attacks/" target="_blank" rel="noopener">I wrote about the Meltdown and Spectre vulnerabilities</a>. Today I want to show you how to check if your database server is protected against Meltdown and Spectre.

Since last week I've seen a lot of scare tactics and knee-jerk reactions to Meltdown and Spectre. My post last week was meant to help keep everybody calm. I want you to understand that there *could* be a performance hit, but you won't know unless you test. If you are afraid to test then you have more issues than just a chipset flaw. I also wanted you to understand the level of risk for your server to be compromised. Chances are it's a small risk, so you might be able to avoid patching right away.

But you should patch anyway. There are few reasons why you would not want, or be able, to patch. And in those cases you will want to take extra measures to ensure your server will not be compromised.

As it turns out the word "patching" is overloaded with meaning. This is leading to confusion with users thinking they are protected, but they have not installed the correct patches.

To be fully protected from Meltdown and Spectre you need to install a patch from the manufacturer of your PC or server <span style="text-decoration: underline;">in addition to</span> the software patches for your OS. You need both, just having one won't be enough. And you are only going to get the microcode update form the manufacturer website at this time. You will need to install this update manually, outside of Windows Update. <a href="https://support.microsoft.com/en-us/help/4073757/protect-your-devices-against-spectre-meltdown" target="_blank" rel="noopener">Microsoft has made this very clear, that you need distinct updates</a>.

&nbsp;
<h2>How to Check if Your Database Server Is Protected Against Meltdown and Spectre</h2>
Microsoft has made available a <a href="https://support.microsoft.com/en-gb/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in" target="_blank" rel="noopener">Powershell script to use to check if your system is protected</a>. That KB article also tells you that you need two distinct updates. I can't stress that point enough here: you need two updates.

Let's get started with the Powershell script. We will right-click on the Windows menu (I'm on my Surface here) and launch Powershell as an Administrator:

<img class="aligncenter wp-image-18528 size-medium" src="https://thomaslarock.com/wp-content/uploads/2018/01/launch_powershell_admin-251x315.jpg" alt="How to Check if Your Database Server Is Protected Against Meltdown and Spectre" width="251" height="315" />

Next, we need to install the module. We can do that with the following command:
<pre lang="Powershell">Install-Module SpeculationControl</pre>
<img class="aligncenter size-large wp-image-18529" src="https://thomaslarock.com/wp-content/uploads/2018/01/install-module-speculationcontrol-600x293.jpg" alt="install-module-speculationcontrol" width="600" height="293" />

I had to click 'Y' to trust the repository, you will likely need to do the same. Next, we need to make sure our execution policy is configured. So, let's run the following command:
<pre lang="Powershell">Set-ExecutionPolicy RemoteSigned -Scope Currentuser</pre>
Now, we should be able to import the module, then run the command:
<pre lang="Powershell">Import-Module SpeculationControl
Get-SpeculationControlSettings</pre>
And this was my result:

<img class="aligncenter size-large wp-image-18530" src="https://thomaslarock.com/wp-content/uploads/2018/01/Get-SpeculationControlSettings-600x535.jpg" alt="Get-SpeculationControlSettings" width="600" height="535" />

As you can see, I have the Windows update, but not the hardware update. Looks like I have some work to do to be protected.

&nbsp;
<h2>How to Get the Patches</h2>
Here's the current list of places you need to check for patching against Meltdown and Spectre.
<h3>For Windows:</h3>
Here is the Windows KB article: <a href="https://support.microsoft.com/en-us/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution" target="_blank" rel="noopener">https://support.microsoft.com/en-us/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution</a>

The Windows Update patches can be found at Settings &gt; Update &amp; security &gt; Windows Update. Click “Check for updates” to install any available updates.

For Red Hat Linux:

Red Hat has a <a href="https://access.redhat.com/security/vulnerabilities/speculativeexecution" target="_blank" rel="noopener">page dedicated to the issue, complete with a long list of patches available</a>. If you are running something other than RHEL, you should be able to find a patch from wherever you got your distribution from.
<h3>For SQL Server:</h3>
Here is the SQL Server KB article: <a href="https://support.microsoft.com/en-us/help/4073225/guidance-for-sql-server" target="_blank" rel="noopener">https://support.microsoft.com/en-us/help/4073225/guidance-for-sql-server</a>

That KB article lists all the available patches for the affected and supported versions of SQL Server. I'd rather you reference that KB article than a long list of patches here.
<h3>For CPUs:</h3>
The hardware updates should be located on the website of the manufacturer. For example, here is the <a href="http://www.dell.com/support/contents/us/en/04/article/product-support/self-support-knowledgebase/software-and-downloads/support-for-meltdown-and-spectre" target="_blank" rel="noopener">page for Dell</a>, and <a href="http://h22208.www2.hpe.com/eginfolib/securityalerts/SCAM/Side_Channel_Analysis_Method.html" target="_blank" rel="noopener">for HP</a>. You can find a comprehensive list of manufacturers at <a href="https://meltdownattack.com/" target="_blank" rel="noopener">https://meltdownattack.com/</a>

Lastly, you will want to patch your browsers, too. If there is one thing we can all learn from Meltdown and Spectre it is this: keep your software up to date.