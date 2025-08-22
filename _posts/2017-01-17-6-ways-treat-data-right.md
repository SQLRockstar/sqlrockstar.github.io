---
layout: post
title: 6 Ways To Treat Your Data Right
date: '2017-01-17 12:45:55 +0000'
categories:
- Data Security and Privacy
- MSSQL
- SQL MVP
tags:
- backups
- Data
- encryption
- privacy
- recovery
- security
---

<a href="https://thomaslarock.com/wp-content/uploads/2015/07/lost_data_h.jpg"><img class="aligncenter wp-image-16953 size-medium" src="https://thomaslarock.com/wp-content/uploads/2015/07/lost_data_h-473x315.jpg" alt="6 Ways To Treat Your Data Right" width="473" height="315" /></a>Data is the most critical asset that you, or any company, owns. Without data, your company would cease to exist. All that hardware you bought? Yeah, that's just there to help data get from one place to another faster. It's all about the data, so you'd better treat it right.

I've said this before but it bears repeating: You get paid for performance, but you keep your job with recovery.

Not everyone understands just how important data is until it is gone. When disaster strikes, and you can't recover, you are likely to be shown the door...if your company still exists at all.

Here are six ways that you can treat your data right.
<h2>Establish Objectives</h2>
Establish a <a href="http://whatis.techtarget.com/definition/recovery-point-objective-RPO" target="_blank">Recovery Point Objective</a> (RPO) that determines how much data loss is acceptable. Understanding acceptable risk levels can help establish a baseline understanding of where you should focus their recovery efforts.

Then, work on a <a href="http://whatis.techtarget.com/definition/recovery-time-objective-RTO" target="_blank">Recovery Time Objective</a> (RTO) that shows how long you can afford to be without access to the data as it is being restored. Is a two-day restore period acceptable, or does it have to be 15 minutes?

Once you nail down those RPO and RTO objectives, I suggest you consider defining an alt-RPO and alt-RTO objectives. These are your alternatives for when you need to pull the plug on recovery and reboot everything. Like what <a href="https://thwack.solarwinds.com/community/solarwinds-community/geek-speak_tht/blog/2016/08/10/lessons-learned-from-the-delta-outage" target="_blank">Delta did last year</a> when they found out recovery was going to take longer than expected. Rather than wait for an unknown amount of time, they took the alternative method and knew they would be back up and running in a few hours.

Finally, remember that “high availability” and “disaster recovery” are different. Data isn't the only thing that gets replicated, so do errors and corruption. Having two (or more) copies of errors and corruption won't help the buisness fix those issues. So you better have a plan in place to recover when this happens (because <em>it will happen</em>).
<h2>Understand that snapshots are not backups</h2>
There’s a surprising amount of confusion about the differences between database backups, server tape backups, and snapshots. For instance, many people have a misperception that a storage area network (SAN) snapshot is a backup, when it’s really only a <a href="http://searchdatabackup.techtarget.com/definition/storage-snapshot" target="_blank">set of data reference markers</a>. Remember that a true backup, either on- or off-site, is one in which data is securely stored in the event it needs to be recovered.

Consider the <a href="http://www.hanselman.com/blog/TheComputerBackupRuleOfThree.aspx" target="_blank">backup rule of three</a>, which dictates that you should save three copies of everything, in two different formats, and with one off-site backup. Yes, I'm that paranoid when it comes to my data.
<h2>Make certain the backups are working</h2>
Although many DBAs will undoubtedly insist that their backups are working, the only way to know for sure is to test the backups by doing a restore. This will provide assurance that backups are running and not failing. Oh, and it wouldn't hurt to know if the <a href="http://www.sqlservercentral.com/articles/Administration/areyourdatabasebackupscurrentandavailable/2309/" target="_blank">backup files are still available</a>.
<h2>Use encryption</h2>
Instead of spending time trying to determine if a piece of data should be classified as "sensitive" and therefore needs to be encrypted, you should treat all your data as sensitive. At a minimum data-at-rest on the server should always be encrypted. Also, you should default to using backup encryption for the database backup file(s). You can either encrypt the database backup file or encrypt the entire database using <a href="https://msdn.microsoft.com/en-us/library/bb934049.aspx" target="_blank">Transparent Data Encryption</a> (TDE). That way, if someone takes a backup, they won’t be able to access the information without a key.

You should also note that some storage arrays, like Pure Storage, <a href="http://blog.purestorage.com/at-rest-encryption-of-sql-server-databases-on-pure-storage-flasharrays/" target="_blank">perform encryption for you already</a>. This means you could rely on their encryption and not deploy a feature such as TDE. The point here is that as a DBA you should take steps to ensure that if a device is lost or stolen, the data stored on the device remains inaccessible to users without proper keys.
<h2>Monitor and collect data</h2>
Real-time data collection (RTC) and real-time monitoring (RTM) should be used together to protect data. Combined with network performance monitoring and other analysis software, RTM and RTC can improve performance, reduce outages, and maintain network and data availability.

With RTC, administrators can capture events as they come in, allowing them to establish a real-time collection of information they can then store to do proper data forensics. This will make it easier to track down the cause of an intrusion, which can be detected through monitoring.

RTM, database analysis, and log and event management can help you understand if something is failing. They’ll be able to identify potential threats through things like unusual queries or suspected anomalies. They can compare the queries to their RTC historical information to gauge whether or not the requests represent potential intrusions.
<h2>Test, test, test</h2>
This is assuming you have already tested backups, but let’s make it a little more interesting. Let’s say a DBA is managing an environment with 3,000 databases. It’s impossible to restore them every night; there’s simply not enough space or time.

In this case, DBAs should take a random sampling of their databases to test. Shoot for a sample size representing at least 95 percent of the 3,000 databases in deployment, while leaving a small margin of error (much like a political poll). From this information DBAs can gain confidence that they will be able to recover any database they administer, even if that database is in a large pool. If you’re interested in learning more, check out this <a href="https://www.simple-talk.com/sql/database-administration/statistical-sampling-for-verifying-database-backups/">post</a>, which gets into further detail on database sampling.
<h2>Summary</h2>
Data lasts longer than code, treat it right.

Don’t treat it like it’s anything but the most critical asset you or your company owns. Make sure no one is leaving server tapes lying around cubicles, practice the backup rule of three, and, above all, develop a sound data recovery plan and make certain that it works.