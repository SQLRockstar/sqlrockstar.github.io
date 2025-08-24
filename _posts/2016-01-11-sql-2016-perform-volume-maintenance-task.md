---
layout: post
title: SQL 2016 Perform Volume Maintenance Task
date: '2016-01-11 13:40:57 +0000'
categories:
- MSSQL
- SQL MVP
- SQL Server Performance
tags:
- ".NET 3.5 SP1"
- installation
- lock pages in memory
- microsoft
- perform volume maintenance
- sql server
- startup parameters
- trace flags
---

Last week while building out some labs for my upcoming session at <a href="http://www.sqlsaturday.com/461/Sessions/Details.aspx?sid=40468" target="_blank">SQL Saturday Austin</a>, I noticed this screen during the installation of SQL Server 2016 CTP3 (the green markers are mine, obviously):

<a href="https://thomaslarock.com/wp-content/uploads/2016/01/server_config_perform_volume.jpg" rel="attachment wp-att-17261"><img class="aligncenter size-large wp-image-17261" src="https://thomaslarock.com/wp-content/uploads/2016/01/server_config_perform_volume-600x453.jpg" alt="server_config_perform_volume" width="600" height="453" /></a>

Seeing this got me all kinds of excited! Enabling '<a href="https://msdn.microsoft.com/en-us/library/ms175935.aspx" target="_blank">perform volume maintenance</a>' is one of the post-install tasks that we often include when installing SQL Server. Now we don't have to go back and manually add this permission when the install is completed, it will be done for us during the installation. This is a welcome addition to the install for SQL Server 2016 that I had not seen mentioned previously (you can find <a href="https://www.google.com/search?q=sql+2016+tempdb+install&amp;oq=sql+2016+tempdb+install" target="_blank">lots of posts about the new tempdb options</a>, for example).

Seeing this also got me thinking about other features I'd like to see added to the install process before SQL 2016 goes RTM.
<blockquote>
<h6><strong>Lock Pages in Memory</strong></h6>
</blockquote>
I'd love to see a similar checkbox for the 'lock pages in memory' permission here as well. In fact, I'm a bit surprised it isn't listed already, since both items are security related. I've no idea if LPIM not being included was intentional or an oversight, but it would be great to see this as an option someday.
<blockquote>
<h6><strong>Trace flags and startup paramaters</strong></h6>
</blockquote>
I'd love to see the install process allow for us to include any and all trace flags and startup parameters we night want included. This is another post-install task that can be streamlined by adding it to the installation process itself. Perhaps even a link to a page on MSDN that includes the common trace flags and startup parameters, their use cases, etc.
<blockquote>
<h6><strong>.NET 3.5 SP1 installed</strong></h6>
</blockquote>
For the record I'd like to point out that .NET 3.5 was released in 2007. For whatever reason(s), installations of SQL Server 2016 *still* require you to install .NET 3.5 SP1 on the server before the install is allowed to start. The installer recognizes if this feature has not been added to the server, so why can't the installer simply perform the install for us as needed? Instead, we are forced to go to Server Manager and perform this task ourselves manually. This bothers me so much I <a href="https://connect.microsoft.com/SQLServer/feedback/details/2231048" target="_blank">created a Connect item to have it fixed</a>. Feel free to upvote as desired.