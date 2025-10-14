---
layout: post
title: Get All Endpoints for VMs in an Azure Subscription
date: '2015-05-12 08:32:52 +0000'
categories:
- MSSQL
- SQL Azure
- SQL MVP
- Virtualization
tags:
- Azure
- Powershell
- SQL Azure
---

I wrote a post recently about <a href="https://thomaslarock.com/2015/04/troubleshooting-azure-connectivity-ports-and-endpoints/" target="_blank">troubleshooting connectivity for endpoints on Microsoft Azure VMs</a>. The day the post went out I was greeted with this tweet:
<blockquote class="twitter-tweet" lang="en" data-cards="hidden">
<p dir="ltr" lang="en"><a href="http://t.co/Ww3MyYjwPu">http://t.co/Ww3MyYjwPu</a> right on time context post for me <a href="https://twitter.com/SQLRockstar">@SQLRockstar</a> tx sir. Need to see on ports for my <a href="https://twitter.com/hashtag/linux?src=hash">#linux</a> vms with <a href="https://twitter.com/hashtag/mysql?src=hash">#mysql</a> running :)</p>
— Shyam Viking (@myluvsql) <a href="https://twitter.com/myluvsql/status/593816027445665792">April 30, 2015</a></blockquote>
<script src="//platform.twitter.com/widgets.js" async="" charset="utf-8"></script>So then I did what I usually do: I let my mouth (in this case, fingers) get ahead of my brain. Here was an opportunity for me to do more work! I answered the tweet with:

<blockquote class="twitter-tweet" lang="en">
<a href="https://twitter.com/SQLRockstar">@SQLRockstar</a> yes sir that's one other thing I would have wanted to do through the script. — Shyam Viking (@myluvsql) <a href="https://twitter.com/myluvsql/status/593818667411902464">April 30, 2015</a>
</blockquote>

<script src="//platform.twitter.com/widgets.js" async="" charset="utf-8"></script>

Feeling like my Powershell script wasn't getting the job done here I decided to pull together the code necessary to get all endpoints for VMs in an Azure subscription. So that's what we have here. You’re welcome. As always, here is the usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

You can also download a copy of the Powershell script <a href="http://1drv.ms/1JEhB91" target="_blank">here</a>.
<pre lang="powershell">&lt;############################################## File: GetAllEndpoints.ps1 Author: Thomas LaRock, https://thomaslarock.com/contact-me/ https://thomaslarock.com/2015/05/get-all-endpoints-for-vms-in-an-azure-subscription Summary: This script will loop through all the virtual machines in an Azure subscription and report on the assigned endpoints. Date: May 11th, 2015 You may alter this code for your own purposes. You may republish altered code as long as you give due credit. THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. ##############################################&gt;

&lt;# We are going to loop through all VM's in this subscription. However, if you want to filter for a subset, perhaps by name, you could use something like: #$VMlist = Get-AzureVM | Where-Object { ($_.Name -ilike “something”) } But we don't want to filter for our example, so we just grab all VMs and build an array #&gt;

$VMlist = Get-AzureVM

&lt;# We will now loop through each VM in the array #&gt;

foreach ($VMServiceName in $VMlist) {

    $obj = Get-AzureVM -ServiceName $VMServiceName.ServiceName -Name $VMServiceName.Name | Get-AzureEndpoint 

    $Output = New-Object PSObject 
    $Output | Add-Member VMName $VMServiceName.Name    
    $Output | Add-Member EndpointNames $obj.Name   
    $Output | Add-Member Endpoints $obj.LocalPort

    Write-Output $Output 
    }

</pre>
The Powershell script will output the details to the command window. Feel free to format the output as you see fit, I can imagine some might want to output to a text file. Of course, with Powershell you could output to Excel and create a donut chart if you wanted.

Enjoy!