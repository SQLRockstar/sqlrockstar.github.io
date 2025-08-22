---
layout: post
title: 'Upgrading to SQL Server 2016: Upgrade tasks'
date: '2017-04-25 13:49:57 +0000'
categories:
- Featured
- MSSQL
- SQL MCM
- SQL MVP
- SQL Server Performance
tags:
- migrating
- migration
- mistakes
- sp_refreshview
- sql server
- SQL Server 2016
- upgrade
- upgrading
---

<a href="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016.jpg"><img class="aligncenter wp-image-17808 size-medium" src="https://thomaslarock.com/wp-content/uploads/2017/04/Upgrading-to-SQL-Server-2016-560x297.jpg" alt="Upgrading SQL Server 2016" width="560" height="297" /></a>

In the <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-pre-upgrade-tasks/" target="_blank" rel="noopener noreferrer">last post</a>, I mentioned that when upgrading SQL Server 2016 you have two options: in-place or side-by-side. With in-place upgrades, there is no need to worry about the transferring of data to a new server. Side-by-side upgrades require you to move data from one server to another. For data migrations there are four main options for you to consider:

• Backup and restore. Good option for smaller systems and if you want piecemeal migrations. You may also consider detach and attach here.
• Pre-staging the data using full, differential, and transaction log backups to minimize the data transfer. Log shipping is also a consideration.
• Database mirroring. This allows for easy migration of data from the old system to the new.
• Availability Groups. More complex than database mirroring because multiple databases can be involved.

The concept of rolling upgrades was also mentioned in the last post. This is when you use a high-availability feature such as mirroring, clustering, or Availability Groups. The idea is that you can upgrade a secondary node, failover, and continue upgrading all nodes in this manner until you upgrade the primary node, and then fail back if needed.

Let’s look at the steps involved for each.
<h2>Steps for an In-Place Upgrade</h2>
In-place upgrades are the easiest to perform, but the most difficult to rollback. The steps involved for in-place upgrades are as follows:
<p style="padding-left: 30px;">1. Verify that backups exist for all databases (user and system). If you have a database that is not in SIMPLE recovery mode, make certain a transaction log backup exists. Verify that these backups can be restored.
2. Review the list of prerequisites for SQL Server 2016, and install whatever necessary.
3. Run the SQL Server 2016 installation media.
4. Perform your post-upgrade tasks.
5. Test, test, and test that everything is working as expected.</p>

<h2>Steps for a Side-by-side Upgrade</h2>
Side-by-side upgrades have more steps and are more complex. They also give you more flexibility for rolling back, because you are not touching the original system while it is still in use.

The steps involved in a side-by-side upgrade are similar for both an existing or new database server. The only difference is that for a new server you will need to install SQL Server. Here are the steps:
<p style="padding-left: 30px;">1. Verify that backups exist for all databases (user and system). If you have a database that is not in SIMPLE recovery mode, make certain a transaction log backup exists. Verify that these backups are able to be restored.
2. Script out any necessary system objects.
3. Script out any necessary SSIS packages (either from MSDB or as flat files).
4. For a new instance on a new server:
(a.) Review the list of prerequisites for SQL Server 2016, and install whatever prerequisites necessary.
(b.) Install the desired version and edition of SQL Server 2016.
5. Use script(s) from old server to create necessary system objects on the new server.
6. Migrate SSIS packages to MSDB (or as flat files, if applicable).
7. Select database(s) to migrate, take offline.
8. Migrate database to new instance. Repeat for each database.
9. Perform your post-upgrade tasks.
10. Test, test, and test that everything is working as expected.</p>

<h2>Steps for a Rolling Upgrade</h2>
Rolling upgrades can reduce downtime during upgrades. Database mirroring is my preferred method for doing rolling SQL Server upgrades. But we could also use log shipping or Availability Groups, the choice of which feature you want is up to you. Make sure you have a solid rollback plan for whichever feature you are using.

The steps involved for rolling upgrades are as follows:
<p style="padding-left: 30px;">1. Choose your high-availability method (log-shipping, mirroring, Availability Groups).
2. Choose one of the following:
(a.) Upgrade one of the secondary nodes following the in-place upgrade instructions above.
(b.) Install SQL Server 2016 on a new server (and add it as a node if applicable)
(c.) Use script(s) from primary node to create necessary system objects on the new server.
3. Failover to the secondary node.
4. Perform any post-upgrade tasks.
5. Test, test, and test that everything is working as expected.
6. Repeat the upgrade for any remaining secondary nodes.
7. Perform any post-upgrade tasks.
8. Test, test, and test that everything is working as expected for each node.
9. Repeat the upgrade for the primary node.
10. Perform any post-upgrade tasks.
11. Test, test, and test that everything is working as expected for the primary node.</p>
With rolling upgrades, you don’t have to fail back to the original server (the primary node). It is fine to configure database mirroring for the single purpose of a rolling upgrade. After you have failed over to the secondary you then break the mirror and remove the server from your inventory. This is the same result as a side-by-side migration but with less downtime than doing the traditional method of backup/restore or detach/attach. And for very large databases (VLDBs) this concept is crucial because restoring can be a cumbersome task.

Finally, it is important to note that data movement in a rolling upgrade is in one direction only. As a result, you can migrate from an older version to a newer version of SQL Server, not the other way around. If you are doing a rolling upgrade and you move your data to an upgraded node, you can’t go back without recovering from backups on the original server. You will see error messages indicating this issue. Recognize that SQL is telling you that you cannot migrate down to an earlier version.
<h2>Summary</h2>
For help with the migration of system objects, have a look at the <a href="https://dbatools.io/" target="_blank" rel="noopener noreferrer">DBAtools.io project</a>. The DBAtools.io project has a lot of PowerShell cmdlets available to assist you with migrating objects and data.

In the <a href="https://thomaslarock.com/2017/04/upgrading-sql-server-2016-post-upgrade-tasks/" target="_blank" rel="noopener noreferrer">next post</a>, we will look at the tasks necessary after the upgrade is complete.

Don't forget that you can also <a href="http://go.solarwinds.com/2016DPA_SQL_Server_Upgrade_whitepaper?CMP=OTC-WP-SQLRSR-CF_WW_X_NP_X_CQ_EN_DPAGEN_SW-DPA-20170419_TLWHP_X_X-X" target="_blank" rel="noopener noreferrer">download and read the upgrade whitepaper</a> I wrote for SolarWinds. It contains additional information as well as a set of tips and reference links that I believe you will find useful.