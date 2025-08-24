---
layout: post
title: SQL Server Linked Server Connection Test
date: '2016-03-01 11:39:51 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- connection
- linked server
- sql server
---

Database servers have a lot of moving parts, as do the applications built on top of any database platform. That's why when it comes time to rebuild a server, or migrate systems to use new servers, it can be difficult to get everything correctly configured the first time through.

As time passes and systems pass from one administer to another details of the installations can be lost. No matter how great your documentation and change control process might be there always seems to be something that gets forgotten. Things like specific trace flags, or a specific permissions granted, or a specific SSIS package.

And then there are linked servers, the equivalent of hotel wifi for SQL Server. You know they are there, and they should just work to bring you data as needed, but you don't think about them until they stop working.

The last thing you want to do after a disaster is to hand over a server to your end users that is not ready.
<h2>How To Test Linked Server Connections</h2>
It's easy enough to verify that a linked server connection is working after such events, you just need to navigate and right-click:

<a href="https://thomaslarock.com/wp-content/uploads/2016/03/linked_server_test_connection.jpg" rel="attachment wp-att-17309"><img class="aligncenter size-full wp-image-17309" src="https://thomaslarock.com/wp-content/uploads/2016/03/linked_server_test_connection.jpg" alt="Linked server connection test" width="369" height="460" /></a>

Of course, this process is not optimal if you have dozens of linked servers defined. It is not uncommon as servers get older to have more than a handful of linked servers. And these linked servers could point to a variety of sources, requiring a variety of specific drivers to be loaded onto your instance. Do you know all the drivers that are installed on your servers right now? Probably not.

Having a script to quickly check each definition would sure be nice, right?
<h2>Script To Test Linked Server Connections</h2>
Here's a script for you to use to test your linked server connections. As always, the usual disclaimer:

<span style="color: #ff0000;"><strong><em>Script disclaimer, for people who need to be told this sort of thing:</em></strong></span>

<strong>DISCLAIMER</strong>: <em><span style="color: #008000;">Do not run code you find on the internet in your production environment without testing it first. Do not use this code if your vision becomes blurred. Seek medical attention if this code runs longer than four hours. On rare occasions, this code has been known to cause one or more of the following: nausea, headaches, high blood pressure, popcorn cravings, and the impulse to reformat tabs into spaces. If this code causes your servers to smoke, seek shelter. Do not taunt this code.</span></em>

You can also download a copy of the script <a href="http://1drv.ms/1RDFmjs" target="_blank" rel="noopener">here</a>.
<pre lang="powershell"><# /*============================================= File: SQL_Server_linked_server_connection_check.ps1 Authors: Thomas LaRock, https://thomaslarock.com/contact-me/ Original blog post at https://thomaslarock.com/2016/03/sql-server-linked-server-connection-test Summary: This script will test the connection for each linked server defined. This script will accept an input of a server name. If no name is passed, the script will default to the current computer name. This script will output to a file, you should set the $OutputFile variable to whatever you want. REMARKS: None. Date: February 29th, 2016 SQL Server Versions: SQL2012, SQL2014, SQL2016 You may alter this code for your own purposes. You may republish altered code as long as you give due credit. THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. =============================================*/ #>

<# Input a server name. #>
param(
[Parameter(Mandatory = $false)]
[String]
$ServerName
)

<# Load the assemblies. #>
[system.reflection.assembly]::LoadWithPartialName("Microsoft.SqlServer.Smo")|Out-Null
[system.reflection.assembly]::LoadWithPartialName("Microsoft.SqlServer.SqlWmiManagement")|Out-Null

<# If no server name is passed, we will set to the current server name. #>
if ($ServerName.Length -eq 0)
{
$ServerName = $env:COMPUTERNAME
}

<# Set the output file path, and initialize. #>
$OutputFile = "C:\Users\Administrator\Documents\linked_server_output.txt"
"$(Get-Date) Starting Linked Server connection test for server $ServerName." | Out-File $OutputFile 

<# Create new objects for managed computer and SQL server instances. We use ServerInstances to get friendly names for installed instances, and we get a list of services to skip those not currentoy running. #>
$mc = new-object Microsoft.SqlServer.Management.Smo.Wmi.ManagedComputer $ServerName
$Instances = $mc.ServerInstances
$Services = $mc.Services

<# Begin outer loop for each SQL instance installed. #>
foreach($Instance in $Instances)
{
$Servername = $Instance.Parent.Name

<# Begin inner loop, for all services installed. #>
 foreach ($ServiceName in $Services)
 {
  <# We are filtering for services that are running. #>
  if ($ServiceName.ServiceState -eq "Running") 
  {
   <# Using wildcard search to find services that are like the instance name. #>
   if ($ServiceName.Name -like ("*" + $Instance.Name + "*"))
   {
   <# Build string for sql server name. If -ne, assume named instance. #>
    if ($Instance.Name -ne "MSSQLSERVER")
    {
    <# Build connection name. #>
    $ServerName = $ServerName + "\" + $Instance.name 
    }

    <# Build SQL Server object. #>
    $Server = New-Object Microsoft.SqlServer.Management.Smo.Server($ServerName)
   
    <# Attempt to connect to this instance by returning the Version property. #>
    try   
    {
     $Server.Version | Out-Null
     "$(Get-Date) $ServerName connection attempt." | Out-File $OutputFile -Append

     <# If connection above is successful, get array of linked servers. #>
     $LSNames = $Server.LinkedServers
     "$(Get-Date) $ServerName connection success." | Out-File $OutputFile -Append
   
     <# If no linked servers defined. #>  
     if ($LSNames.Count -eq 0) 
     {
     "$(Get-Date) $ServerName no linked servers found." | Out-File $OutputFile -Append
     }

     <# For each linked server test the connection. #>
     foreach ($LSname in $LSnames)
     { 
      if ($LSname -ne $null)
      {
       try
       {
        $LSname.testconnection()                     
        $Connectivity = $true
        "$(Get-Date) $ServerName $LSname connection success." | Out-File $OutputFile -Append
       } 
       catch 
       {    
       $Connectivity = $false
       "$(Get-Date) $ServerName $LSname connection failure." | Out-File $OutputFile -Append
       }
      }
     }
    }
    catch [System.Exception] 
    {
    "$(Get-Date) $ServerName Server connection failed." | Out-File $OutputFile -Append
    }
   }
  }
 }
}
</pre>
Another use for this script would be for routine checks to make sure that your linked servers are still valid, or remove any that are no longer working. I believe it is better to only have linked servers defined that are necessary, rather than continue to carry forward a host of linked server definitions that are no longer valid.