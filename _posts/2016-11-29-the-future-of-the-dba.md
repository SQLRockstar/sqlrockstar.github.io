---
layout: post
title: The Future of the DBA
date: '2016-11-29 14:07:43 +0000'
categories:
- Cloud Computing
- MSSQL
- Professional Development
- SQL Azure
- SQL MVP
tags:
- career
- database
- DBA
---

<p style="text-align: left;"><a href="https://thomaslarock.com/wp-content/uploads/2014/01/azure_mech_rz.jpg"><img class="alignleft wp-image-11064 size-full" src="https://thomaslarock.com/wp-content/uploads/2014/01/azure_mech_rz.jpg" alt="The Future of the DBA" width="285" height="189" /></a><a href="https://thomaslarock.com/2012/07/which-data-professional-are-you/" target="_blank" rel="noopener">I've written before about how databases are like a car engine</a>, and DBAs are like a car mechanic. That's been the traditional view for production DBAs for, well, forever I think. And that analogy may have been true at one time, and may still be true for some DBAs.</p>
But the industry is changing. First we had virtualization, forcing DBAs to learn more about the world that exists outside of the database engine. Then we had cloud services forcing us to learn even more about the universe of data that is available to everyone, everywhere, at any time. Breadth is the new depth.

And with those changes, I no longer see DBAs as a car mechanic.

DBAs don't get to touch 3rd party apps, for example. A majority of data managed today by DBAs are 3rd party apps, often offered as a service.

DBAs sit and watch as the data hoarders continue to amass data <a href="http://whatis.techtarget.com/definition/ROT-redundant-outdated-trivial-information" target="_blank" rel="noopener">leading to ROT</a>. This ROT then forces database vendors to find new and interesting ways to make data go faster when the simple answer might be to get rid of the data you don't need anymore.

No, these days a DBA is no longer a car mechanic. Oh, we still have a cool collection of tools, and we know all about how the engines work, too. But we aren't allowed to touch the 3rd party apps. We are subject matter experts, but others do the lifting. We used to do backups and preventative maintenance, remember those days? Well, with <a href="https://msdn.microsoft.com/en-us/library/dn449496.aspx" target="_blank" rel="noopener">SQL Server Managed Backup</a> and <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-query-performance" target="_blank" rel="noopener">Azure Query Performance Insight</a> we aren't needed for those things anymore.

<span class="hardreadability"><span data-offset-key="aomvc-0-0">All the tasks traditional production DBAs have done for decades are being automated away</span></span><span data-offset-key="aomvc-1-0">. Right in front of our eyes.</span>

So, no, we aren't car mechanics. Not anymore.

These days a DBA is similar to an auto emission testing machine. We locate problems but notify someone else to take action.

Soon our salaries and tasks will be compared to PaaS costs. There won't be a need for paying to have a DBA on staff anymore. After all, we don't pay to have our mechanic live in our home, right? No, we take our car to the garage when needed. That's the model for databases in the future, too.

It's because <a href="https://thomaslarock.com/2014/01/access-trumps-ownership/" target="_blank" rel="noopener">access trumps ownership</a>. Companies don't care if they own databases as much as if they can access data. They don't need to own a DBA, either. They just need to access to a DBA from time to time.

The future of the DBA is in knowing how to build solutions, not tables and indexes. It is analyzing data, not how it is administered.

The future is in our hands, too. We get to decide what we want to learn today that will help us have a job tomorrow. Data science is one choice, but not the only choice. Another choice would be cloud architect, helping people build solutions by utilizing one or more cloud services.

Heck, maybe DBA will still be a choice in the future, but I can guarantee you that our days of rebuilding indexes are ending one page at a time.