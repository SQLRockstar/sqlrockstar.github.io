---
layout: post
title: Installing SQL Server vNext on Red Hat Enterprise Linux in Azure
date: '2016-11-18 11:49:57 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
tags:
- Linux
- Red Hat Enterprise
- sql server
- SSMS
- v.Next
- VS Code
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/watching.jpg"><img class="aligncenter wp-image-17553 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/11/watching-560x312.jpg" alt="Installing SQL Server vNext on Red Hat Enterprise Linux in Azure" width="560" height="312" /></a>This past Wednesday at <a href="https://connectevent.microsoft.com/" target="_blank">Microsoft Connect();</a> Scott Guthrie <a href="https://channel9.msdn.com/Events/Connect/2016/Keynotes-Scott-Guthrie-and-Scott-Hanselman" target="_blank">announced</a> the public preview of SQL Server on Linux. I was fortunate enough to have access to the early bits of SQL Server on Linux during the private preview phase, and was also given a tour of SQL Server vNext during the <a href="https://thomaslarock.com/2016/11/2016-microsoft-mvp-summit-preview/" target="_blank">Microsoft MVP Summit</a> last week. Today I wanted to help walk you through how to be up and running with SQL Server on Linux so that you can kick the tires on this version yourself.

First off, let me share with you a quick picture of how all the pieces fit:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/Cxd1t3WWQAAK96_.jpg"><img class="size-medium wp-image-17542 aligncenter" src="https://thomaslarock.com/wp-content/uploads/2016/11/Cxd1t3WWQAAK96_-560x315.jpg" alt="SQL Server on Linux" width="560" height="315" /></a>

SQL Server runs on Linux by using what is called the Platform Abstraction Layer (SQLPAL). Inside of SQLPAL is a new version of the SQLOS (named SQLOS v2), and this allows for SQL Server to run in the user process space. So if you get things up and running and are poking around to see how SQL Server is running in the Linux kernel, you are going to be disappointed. Or happy. Or meh. One of those. Anyway, I wanted to mention this and share the slide because I've seen the question more than a few times.

Now, to use SQL Server on Linux you will need a few things:

1. <strong>A linux box</strong>. If you have your own Linux server then <a href="https://www.microsoft.com/en-us/sql-server/sql-server-vnext-including-Linux#resources" target="_blank">download the v.Next bits here</a>. Have fun with that because I'm lazy and will use an Azure VM instead.
2. <strong>A way to connect</strong> to the SQL Server instance, such as the latest version of <a href="https://msdn.microsoft.com/en-us/library/mt238290.aspx" target="_blank">SQL Server Management Studio (SSMS v17.0 RC1)</a>, or perhaps <a href="https://code.visualstudio.com/download" target="_blank">Visual Studio Code</a>.
3. <strong>No fear of a command line</strong>. Maybe practice with some <a href="https://powershell.org/" target="_blank">PowerShell</a> or <a href="https://thomaslarock.com/2013/03/administering-sql-server-running-on-server-core/" target="_blank">Server Core</a> to get your feet wet first.

And that's it, really. Let's get started.

&nbsp;
<h2>Creating SQL Server v.Next on Red Hat Enterprise Linux in Azure</h2>
Well, first things first, if you don't have an Microsoft Azure account, <a href="https://account.windowsazure.com/Home/Index" target="_blank">go get one</a>. Once you do then you will want to create a VM using the image that is already available. A quick search of 'sql linux' should return the following:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/2016-11-17_12-37-45.png"><img class="aligncenter wp-image-17543 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/2016-11-17_12-37-45-600x133.png" alt="SQL Server vNext on Red Hat Enterprise Linux in Azure" width="600" height="133" /></a>

I will create a VM named 'sqlonlinux', set the size to be A3, and be up and running in less than five minutes. Here's what the confirmation page looks like before I click OK:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/2016-11-17_13-13-57.png"><img class="aligncenter wp-image-17544 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/11/2016-11-17_13-13-57.png" alt="SQL Server vNext on Linux Azure confirmation" width="414" height="469" /></a>

It was that simple. Mostly.

&nbsp;
<h2>Installing SQL Server vNext on Red Hat Enterprise Linux in Azure</h2>
OK, we have our Linux server, and I will assume you have either SSMS v17.0 RC1 (or some other client like VS Code) installed and working properly. We are ready to connect to the instance of SQL Server, right?

<strong>Wrong</strong>!

We need to complete the installation of SQL Server on the Linux server. That's right, the current Azure image of Red Hat Enterprise Linux doesn't come with SQL Server already running. So that means we need to put our hands on a command line.

I am going to open up Terminal on my iMac and use SSH to connect to the Linux server (yeah, that's right, I'm doing all of my work with SQL Server using my iMac and somewhere Steve Jobs is smiling, I know it):
<pre lang="bash">ssh sqlonlinux.cloudapp.net</pre>
Followed by the install command (the SQL Server bits are in the /opt/mssql/bin directory, and don't forget sqlservr is missing the second 'e'):
<pre lang="bash">sudo ../../opt/mssql/bin/sqlservr-setup</pre>
<a href="https://thomaslarock.com/wp-content/uploads/2016/11/ssh-sql-server-vnext-linux.png"><img class="aligncenter wp-image-17545 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/ssh-sql-server-vnext-linux-600x357.png" alt="SSH SQL Server vNext Linux" width="600" height="357" /></a>

We will accept the license terms, set a strong 'sa' password, and let the install complete. You should then see something like this:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/complete.png"><img class="aligncenter wp-image-17546 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/complete-600x471.png" alt="SQL Server vNext on Linux install complete" width="600" height="471" /></a>

Notice how we were prompted to start the service (well, it's really a process, but whatevs) and also prompted to enable SQL Server to start upon a reboot. That's a nice touch for folks that may not be Linux admins and aren't aware that installing programs on Linux often requires 87 steps to make certain everything is up and running. I will then verify that the process is running:
<pre lang="bash">ps aux | grep sql</pre>
<a href="https://thomaslarock.com/wp-content/uploads/2016/11/grep.png"><img class="aligncenter wp-image-17547 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/grep-600x78.png" alt="SQL Server vNext on Linux grep ps" width="600" height="78" /></a>

&nbsp;
<h2>Connecting to SQL Server vNext on Red Hat Enterprise Linux in Azure</h2>
With the instance running I can now use whatever client tool I choose and connect...

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/error.png"><img class="aligncenter wp-image-17548 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/error-600x214.png" alt="SQL Server vNext on Linux Azure connection error" width="600" height="214" /></a>

Oops. Looks like we got an error:
<pre lang="tsql"><span style="color: #ff0000;">A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. 
Verify that the instance name is correct and that SQL Server is configured to allow remote connections. 
(provider: Named Pipes Provider, error: 40 - Could not open a connection to SQL Server) (.Net SqlClient Data Provider)</span></pre>
That's because there's just <em>one more thing</em> that we need to do here. We need to open up and endpoint for this VM in the Azure portal.

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/endpoint.png"><img class="aligncenter wp-image-17549 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/11/endpoint.png" alt="SQL Server vNext on Linux Azure endpoint" width="583" height="262" /></a>

I’ve also chosen some bad things here. I would advise you don’t name your endpoint ‘MSSQL’, and you probably want a public port that isn’t 1433. But this is a trivial example I am doing for you (<strong>don’t do this for production, please</strong>). Also worth noting is that I could have configured the endpoint during the creation of the VM (by default we are given one for SSH as shown here):

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/create-endpoint.png"><img class="aligncenter wp-image-17550 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/11/create-endpoint.png" alt="SQL Server vNext on Linux Azure create endpoint" width="307" height="417" /></a>

Typically on a Windows VM here is another step to take and that is <a href="http://logicalread.solarwinds.com/connect-windows-azure-vm-using-ssms-tl01/#.WC41vqIrIvo" target="_blank">allowing the port to connect through the Windows Firewall rules</a>. I will leave it as an exercise for the reader as to why we don't need to worry about the Windows Firewall for our Linux server.

Once the endpoint is saved and applied to the VM we should be able to connect without any issue. This is what I get when I connect through Visual Studio Code:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/vs-code.png"><img class="aligncenter wp-image-17551 size-large" src="https://thomaslarock.com/wp-content/uploads/2016/11/vs-code-600x58.png" alt="SQL Server vNext Linux Azure connect VS code" width="600" height="58" /></a>

And this is what it looks like when I connect with SSMS:

<a href="https://thomaslarock.com/wp-content/uploads/2016/11/ssms.png"><img class="aligncenter wp-image-17552 size-full" src="https://thomaslarock.com/wp-content/uploads/2016/11/ssms.png" alt="SQL Server vNext Linux Azure connect SSMS" width="356" height="657" /></a>

A few things worth noting in that image. First, the SQL Agent is shown as 'disabled', but there is no SQL Agent service for you to enable. Another thing is that Polybase is not available, and neither are Availability Groups. Here's a <a href="https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes" target="_blank">link to the current release notes that talks about the features that are not supported</a>. But what I think is most important to notice is this:
<h1 style="text-align: center;">WE ARE RUNNING SQL SERVER ON FRAKKIN' LINUX!</h1>
&nbsp;
<h2>Summary</h2>
To me, the whole premise of SQL Server on Linux went from zero to <a href="https://www.youtube.com/watch?v=ygE01sOhzz0" target="_blank">Ludicrous Speed</a> in just a few months in 2016. I'm not sure what more to say than that. I've shown you how easy it is to get started using it for yourself. Here are some useful links for you:

<a href="https://docs.microsoft.com/en-us/sql/linux/" target="_blank">The (current) complete documentation for SQL Server on Linux</a>
<a href="https://vlabs.holsystems.com/vlabs/technet?eng=VLabs&amp;auth=none&amp;src=vlabs&amp;altadd=true&amp;labid=29101&amp;lod=true" target="_blank">Here's a lab for SQL admins to learn about Linux</a>
<a href="https://vlabs.holsystems.com/vlabs/technet?eng=VLabs&amp;auth=none&amp;src=vlabs&amp;altadd=true&amp;labid=29103&amp;lod=true" target="_blank">Here's a lab for Linux admins to know more about SQL</a>

I will do my best to update this page as more SQL-Server-on-Linux goodness is announced. Until then, have fun exploring SQL Server on Linux!