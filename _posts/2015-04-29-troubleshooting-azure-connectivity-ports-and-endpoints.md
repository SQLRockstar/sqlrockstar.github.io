---
layout: post
title: 'Troubleshooting Azure Connectivity: Ports and Endpoints'
date: '2015-04-29 14:17:35 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
- Virtualization
tags:
- Azure
- Powershell
---

It was a simple enough question, or so I thought. One I felt should be either a simple “yes” or “no”.

“Do we block remote desktop connections here?”

Sure enough, I got back the quick and simple answer I expected, along with a question for myself.

“Nope. We don’t block any RDP sessions. Maybe you configured your server wrong?”

I was in the SolarWinds Austin office trying to connect to one of my virtual machines running inside of Microsoft Azure. The remote desktop (RDP) session had worked fine from my home for weeks, and again from the hotel the night before. But now it didn’t work.

Knowing how to diagnose an issue is a skill you acquire with experience. I thought about all the possible ways this connection could be failing and the only difference I could find was the network. But here I was, being told that nothing was blocked, despite the evidence to the contrary.

Being the good DBA that I am I double-checked my work. I looked at the current port settings for this server in the Azure Portal. These ports are randomly assigned when the VM is created. For remote sessions the private port is 3389, but the public port was set to 54630:

<a href="https://thomaslarock.com/wp-content/uploads/2015/04/endpoints.png"><img class="aligncenter size-medium wp-image-12039" src="https://thomaslarock.com/wp-content/uploads/2015/04/endpoints-560x169.png" alt="endpoints" width="560" height="169" /></a>

And I checked the port number being used in my RDP connection:

<a href="https://thomaslarock.com/wp-content/uploads/2015/04/rdp.png"><img class="aligncenter size-medium wp-image-12040" src="https://thomaslarock.com/wp-content/uploads/2015/04/rdp-560x198.png" alt="rdp" width="560" height="198" /></a>

But the result stayed the same. After a minute or so I would get this message:

<a href="https://thomaslarock.com/wp-content/uploads/2015/04/blocked.png"><img class="aligncenter size-medium wp-image-12041" src="https://thomaslarock.com/wp-content/uploads/2015/04/blocked-560x190.png" alt="blocked" width="560" height="190" /></a>

This appears to be a generic error message. There are no details, no links to documentation on how to troubleshoot possible connectivity errors. This error message is less than helpful. We are left to fend for ourselves at this point.

Instead of giving up I put my troubleshooting skills to work by breaking down each sentence.

<strong>“This computer can’t connect to the remote computer.”</strong>

Well, OK. But that doesn’t tell me if the issue is with me, is with the remote computer, or with something in between. We are using a cloud service (Azure) so it is always possible that communication failures may happen. I move on to look at the second sentence.

<strong>“Try connecting again.”</strong>

Definition of insanity: doing the same thing over and over and expecting a different result. Right now this error message is Groundhog Day for cloud admins. I move on to the last sentence.

<strong>“If the problem continues, contact the owner of the remote computer or your network administrator.”</strong>

Well, I’m the owner of this remote computer, and I already know I won’t be of much use to me. Unless you consider Microsoft to be the owner. And, in a way, they are the owner, but I don’t have the number for the data center handy.

But what about that network administrator? That’s a good, and as it turns out only, clue here. Could it be that there is, indeed, an issue blocking the port despite my being told that was not the case?

I went back to my colleague to ask more questions about the network. (That’s my way of politely writing “I went back to my colleague to blame the network”.) And this time I was greeted with the most brilliant of replies:

“We don’t block any ports here. Show me the error message.”

OK, maybe I call that brilliant because I’ve written before about <a href="https://thomaslarock.com/2007/12/show-me-the-error/" target="_blank">showing me the error message</a>. A picture is worth a thousand support tickets, so we went to my machine, I launched my RDP session, and it failed. The response at that point was this:

“Oh, why are you using <em>that</em> port? I doubt we are allowing non-default ports. Just use the default 3389 and see if that works.”

I was happy, confused, and frustrated all at the same time. Yeah, I was a typical user, the one with a case of <a href="http://www.internetslang.com/PEBKAC-meaning-definition.asp" target="_blank">PEBKAC</a>.

“But you just said you weren’t blocking any-“

“And <strong>you</strong> said RDP wasn’t working. You never said you were using a different port. RDP works fine with the default port of 3389. So try 3389 and let’s see what happens.”

So, back to the Azure portal I went, updating the public port to be 3389, matching the private port. And then, trying RDP again, we see success:

<a href="https://thomaslarock.com/wp-content/uploads/2015/04/success.png"><img class="aligncenter size-medium wp-image-12042" src="https://thomaslarock.com/wp-content/uploads/2015/04/success-371x315.png" alt="success" width="371" height="315" /></a>

Which then led to this exchange:

“I thought you said we didn’t block any ports!”

“What I meant was we don’t block the <em><u>correct</u></em> ports. Use the correct ports and you’ll be fine.”
<h3>This, dear reader, is what you call <em>experience</em>.</h3>
I’ve lost time before due to a firewall of one kind or another. My favorite all-time firewall issue was at TechEd in New Orleans in 2013 when the convention center was blocking port 1433. Ask Grant Fritchey (<a href="http://scarydba.wordpress.com/" target="_blank">blog</a> | <a href="http://twitter.com/gfritchey" target="_blank">@gfritchey</a>) or me about that someday. Good times.

A few months from that trip to Austin I <a href="https://sqlbits.com/" target="_blank">found myself at SQLBits</a>, delivering a <a href="https://sqlbits.com/information/Event14/Designing_For_Performance_Myths_and_Misunderstandings/TrainingDetails.aspx" target="_blank">precon with Karen López</a> (<a href="http://blog.infoadvisors.com/" target="_blank">blog</a> | <a href="http://twitter.com/datachick" target="_blank">@datachick</a>). We’ve built out some VMs in Azure so that our attendees can put their hands on something because that’s what makes for a <a href="https://thomaslarock.com/2011/11/what-is-training/" target="_blank">proper training experience</a>.

Everything worked fine from the hotel the day before. Our scripts built and configured all the VMs in a matter of minutes. We could RDP to the machines without any trouble. Everything was working as expected.

Until it wasn’t.

When we got to the event the next day we were no longer able to RDP to our Azure VMs.

I was concerned I had somehow made a mistake with the port numbers. I set about double-checking them when an attendee approached me and suggested we should check the ports again. I was confused at first (probably because he was speaking British) but then I immediately understood what was being suggested: the conference center was blocking the non-default ports! Same as with Austin, if we switched to 3389, then RDP would work as expected.

So we set about manually updating each VM through the portal. And as I was updating each one it occurred to me that I should have a script for this in the future, should I find myself needing to quickly make changes to the RDP ports (any endpoints, really) on many VMs at the same time.

So, here is the script I cobbled together after SQLBits to help me for next time. You’re welcome. As always, here is the usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

You can also download a copy of the script <a href="http://1drv.ms/1EDCZbn" target="_blank">here</a>.
<pre lang="Powershell"><##############################################
    File: AlterEndpoints.ps1             
    Author: Thomas LaRock, https://thomaslarock.com/contact-me/
        https://thomaslarock.com/2015/04/troubleshooting-azure-connectivity-ports-and-endpoints        

    Summary: This script will loop through all the virtual machines
              in an Azure subscription. You can modify the script below
              to add, modify, or remove endpoints as needed.    

    Date: April 28th, 2015

    You may alter this code for your own purposes. You may republish
    altered code as long as you give due credit.

    THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
    OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT
    LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR
    FITNESS FOR A PARTICULAR PURPOSE.
##############################################>

<# We are going to loop through all VM's in this subscription. However, if you want to filter for a subset, perhaps by name, you could use something like: #$VMlist = Get-AzureVM | Where-Object { ($_.Name -ilike "something") } But we don't want to filter for our example, so we just grab all VMs and build an array #>

$VMlist = Get-AzureVM

<# We will now loop through each VM in the array #>

foreach ($VMServiceName in $VMlist) {

    Get-AzureVM -ServiceName $VMServiceName.ServiceName –Name $VMServiceName.Name | Set-AzureEndpoint -Name "Remote Desktop" -PublicPort 3389 -LocalPort 3389 -Protocol "tcp" | Update-AzureVM
 
    }

</pre>
If you wanted to add an endpoint to all your VMs that's easy, you just use the following syntax:
<pre lang="Powershell">Get-AzureVM -ServiceName $VMServiceName.ServiceName –Name $VMServiceName.Name | Add-AzureEndpoint -Name "Remote Desktop" -Protocol "tcp" -PublicPort 3389 -LocalPort 3389 | Update-AzureVM
</pre>
If you wanted to remove an endpoint on all your VMs that's easy too, you just use the following syntax:
<pre lang="Powershell">Get-AzureVM –ServiceName $VMServiceName.ServiceName –Name $VMServiceName.Name | Remove-AzureEndpoint –Name "Remote Desktop" | Update-AzureVM
</pre>
I even have a version of this script that can remove all endpoints from all VMs, but I won't post it here because I’d be concerned someone ran that unwittingly. I would rather not be the enabler for someone bringing down hundreds of servers. But Denny Cherry (<a href="http://itknowledgeexchange.techtarget.com/sql-server/" target="_blank">blog</a> | <a href="http://twitter.com/mrdenny" target="_blank">@mrdenny</a>) needed it one night so I put it together for him, and I know others may want it as well. If you want a copy of the code snippet, just <a href="https://thomaslarock.com/contact-me/" target="_blank">drop me an email</a> and I’ll send it to you.

Lesson here is that when working remotely you need to consider things like firewalls and blocked ports and be ready to quickly troubleshoot, diagnose, and remedy Azure connectivity issues.

And always blame the network.