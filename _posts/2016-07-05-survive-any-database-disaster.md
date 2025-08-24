---
layout: post
title: How To Survive A Database Disaster
date: '2016-07-05 14:54:22 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- backups
- database
- disaster
- ETR
- recovery
- RPO
- RTO
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/07/keep-calm-man-fire.jpg"><img class="aligncenter size-medium wp-image-17431" src="https://thomaslarock.com/wp-content/uploads/2016/07/keep-calm-man-fire-224x315.jpg" alt="keep-calm-man-fire" width="224" height="315" /></a>

A database disaster is going to happen to everyone at some point. If you haven't had one yet, just give it time.

I am here today to share my FOOLPROOF method that allows you and your business to SURVIVE any database disaster:

<strong>Have backups</strong>.

This isn't rocket surgery folks. The key to surviving any database disaster is having a good backup available and ready. No backups means you can't recover. At all. Like, ever.

I see stories every day about companies (or even regular people) that <a href="http://stackoverflow.com/questions/14675969/recover-database-with-no-backups" target="_blank">don't have backups of critical systems and files</a>. I want everyone to understand that if your data is important then <a href="http://www.hanselman.com/blog/TheComputerBackupRuleOfThree.aspx">you should have three copies</a>.

I also see and hear people confuse the terminologies "high availability" with "disaster recovery". Two different terms, with very different meanings. One will help you recover from a disaster, the other will not. Guess which one?

Let's take a minute to review some definitions:
<h2>Database Disaster Terminologies You Need To Know</h2>
<b>HA </b>– Stands for High Availability. The word you want to think about here is this: uptime. It’s that simple. If your servers have a high uptime percentage (<a href="http://www.continuitycentral.com/feature0267.htm">five-nines</a>) then they are highly available.

<b>DR </b>– Stands for Disaster Recovery. The word you want to think about here is this: recovery. It’s that simple. If you are able to recover your data then you have the makings of a DR plan.

Now, here is the very important piece of information that you must know: <strong>HA IS NOT THE SAME AS DR</strong>. For the developers that might stumble upon this blog I would explain it like this: HA &lt;&gt; DR

You might be surprised that people confuse these two terms, or heard folks try to classify issues as “events” versus a “disaster”. To me it does not matter if one server or one hundred servers are wiped out, a disaster is a disaster.

<strong>RPO</strong> - Stands for Recovery Point Objective and is the point in time to which you can recover data as part of an overall business continuity plan. In other words, it is the acceptable amount of data loss. For example, if your RPO is 15 minutes then you are going to take a backup every 15 minutes (or less). But your business may not be able to restart at that point and carry on. <a href="http://www.continuitycentral.com/feature0374.htm" target="_blank">Read this article</a> for more examples of how you set an appropriate RPO based upon the nature of the system. You can't set an arbitrary number such as "15 minutes" and expect it has meaning without knowing the underlying system.

<strong>RTO</strong> - Stands for Recovery Time Objective and this is the amount of time it will take for you to recover data before the business is severely impacted. Taking log backups every minute may help satisfy your RPO objective, but if it takes hours to recover a 5TB database because you have to apply all those log backups then you are not helping your business continuity plans.

Every business continuity and recovery plan should include both a recovery point objective (RPO) and a recovery time objective (RTO).

<strong>ETR</strong> - This stands for the Estimated Time to Restore. I see ETR and RTO being interchangeable at times but I think of them as two different things. ETR changes as your data grows in size and complexity and therefore ETR is the reality upon which the RTO should be based. It's also good to check often and make certain the ETR for your database is less than the RTO. If it is not, then you can start making necessary changes before disaster strikes.
<h2>Do You Know Your DR Plan?</h2>
For most folks the DR plan is simple: recover the server from a server tape backup (or snapshot), then restore the databases from backup files. Some sys admins will tell you that they have replication deployed as a DR solution. So I like to play a game called “what if?”

If your shop is using SAN replication and claim it is their DR solution, ask some simple questions such as: “<em>What if a corruption happens at Site A and is replicated immediately to Site B</em>?”

And see where the answers to that question lead you. (HINT: it will lead you to your current DR solution (if you have one) which is most likely recovering from tape, which will show you are only as good as your last tape backup.)

Here's another question that is overlooked: What if your RPO and RTO agreements are no longer (or never were) compatible?

For example, your RPO could be stated as "We need to be put back to a point in time no more than 15 minutes prior to the disaster", and your RTO could be 15 minutes as well. So if it takes you 15 minutes in recovery time to be at a point 15 minutes prior to the disaster then you are going to have 30 minutes of total downtime.

Think about what you current RPO and RTO are right now (assuming they exist) and how long ago were they agreed upon. When was the last time you tested to make certain those agreements were still compatible?
<h2>Check That Your RPO and RTO Still Make Sense</h2>
You must make certain that you are meeting your RTO for the given RPO and that you are at an acceptable re-starting point for business to continue. Chances are the RPO and RTO agreed to initially are no longer viable as the size of the data has grown over the years.

The reality of being down for 30 minutes and not the expected 15 minutes causes folks to start thinking about alternatives such as HA in an effort to augment their DR situation. Having HA augment your DR solution is good. Having HA replace your DR is not. This is where the trouble begins.

And the prices rise considerably as you try to narrow the RPO and RTO gaps. As you approach zero downtime, and no data loss, your costs skyrocket. While the Cloud and Hybrid IT makes for more options the fact remains that there is a price to pay for uptime.

And that is why companies often decide that (some) downtime is acceptable. But not having backups, or a DR solution in place?

That is never acceptable.

If you want to survive any database disaster then you need to start with having your backups in place.