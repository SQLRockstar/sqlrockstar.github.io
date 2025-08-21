---
layout: post
title: Fact Checking Some Statements from the AWS re:Invent Keynote
date: '2018-12-17 17:01:10 +0000'
categories:
- AWS
- Azure
- SQL MVP
tags:
- AWS
- Azure
- data service
- reInvent
---

During his keynote at AWS re:Invent, Andy Jassy made some statements that seemed…questionable. Well, questionable to me, at least. Not surprising, the questionable statements focused on databases, data services, and storage.

If you are interested in watching the keynote for yourself, you can see it here: <a href="https://youtu.be/ZOIkOnW640A" target="_blank" rel="noreferrer noopener">https://youtu.be/ZOIkOnW640A</a>

[embed]https://youtu.be/ZOIkOnW640A[/embed]

The keynote is 2 hours and 44 minutes. It’s not action packed, so I recommend you adjust the speed to 1.5x. Doing that will save you an hour of viewing time. YouTube offers a transcript as well, making it easy to grab the quotes.

Now, I’m not writing this post to make Jassy or AWS look like fools in any way. The keynote is long, filled with a lot of wonderful information. AWS is doing wonderful things with databases and data services. I’m a fan of all things data.

What I have here today are a handful of statements, out of a very long keynote. I found these statements to be unfair. As someone who works in marketing, I know how keynotes work. But as a data professional, and <a href="https://mvp.microsoft.com/en-us/PublicProfile/4025219" target="_blank" rel="noreferrer noopener">Azure fanbois</a>, I don't like seeing bad information presented as truth.

Thus, today's post is my effort to fact-check the statements that irked me the most.

You're welcome.

Let’s get started.

&nbsp;
<h2>AWS has 11 relational and non-relational databases. Which is much more than you'll find anywhere else, nobody has close to half of that.</h2>
Well, AWS has 13 databases now, because later in the keynote Jassy announced <a href="https://aws.amazon.com/timestream/" target="_blank" rel="noreferrer noopener">Timestream</a> and <a href="https://aws.amazon.com/qldb/" target="_blank" rel="noreferrer noopener">QLDB</a>. But let’s focus on the original 11, and the statement that “nobody has close to half that”.

The 11 databases that Jassy refers to are <a href="https://youtu.be/ZOIkOnW640A?t=671" target="_blank" rel="noreferrer noopener">listed on the screen behind him</a> are as follows: RDS (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server), Aurora (MySQL, PostgreSQL), DynamoDB, ElastiCache (Memcached, Redis), and Neptune.

That’s a confusing list to me, because it does not include SimpleDB, or Redshift. And Aurora is counted twice, but Aurora is really just RDS but at a higher performance tier. I don’t see how Jassy can count Aurora as something different, but he’s probably using SKU math that folks with MBAs like to use.

So, let’s count up the databases available in Azure today. And to keep it fair, I will also go by SKU, and leave off the Azure SQL Data Warehouse service.

<a href="https://azure.microsoft.com/en-us/services/sql-database/" target="_blank" rel="noreferrer noopener">Azure SQL Database</a>
<a href="https://azure.microsoft.com/en-us/services/mysql/" target="_blank" rel="noreferrer noopener">Azure Database for MySQL</a>
<a href="https://azure.microsoft.com/en-us/services/postgresql/" target="_blank" rel="noreferrer noopener">Azure Database for PostgreSQL</a>
<a href="https://azure.microsoft.com/en-us/services/mariadb/" target="_blank" rel="noreferrer noopener">Azure Database for MariaDB</a>
<a href="https://azure.microsoft.com/en-us/services/cosmos-db/" target="_blank" rel="noreferrer noopener">Azure Cosmos DB</a>
<a href="https://azure.microsoft.com/en-us/services/cache/" target="_blank" rel="noreferrer noopener">Azure Cache for Redis</a>

So, that’s six. Last I checked, 6 is more than half of 11. But we are not done yet.

Cosmos DB is really three engines, and the AWS equivalent to Cosmos DB are two engines: (Dynamo, Neptune). <a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">I wrote about this earlier in 2018, for reference</a>. So, Azure offers you one SKU, and AWS offers you two. But if we break Cosmos DB out, then Azure has 8 database services. And 8 is also more than half of 11.

More to the point, what does it matter if AWS has two databases (Dynamo, Neptune) and Azure only has Cosmos DB? I fail to understand why the number of databases offered is as important as the functionality that those services offer. At the end of the day, functionality is what should matter most for those “builders” that AWS is coveting.

I get that counting the number of databases is a convenient metric. It’s also useless.

Ok, let’s move on to the next.

&nbsp;
<h2>In AWS, it's the only place where you have a database migration service that allows you to switch from SQL to NoSQL or actually be able to migrate your data warehouse.</h2>
Well, Jassy certainly makes it sound easy to switch between relational and non-relational. Just a few clicks, export tables to JSON, and you are done, right? Maybe....maybe not.

The <a href="https://aws.amazon.com/dms/">AWS Data Migration Service (DMS) documentation</a> doesn’t talk about this “SQL toNoSQL” functionality. I did, however, <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html">find this other documentation that states you can use DynamoDB as a target for DMS, and have a relational database as a source</a>. And then <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html">this page</a> describes that you can use DMS to extract your database to S3 buckets, which are then imported into Redshift.

So, yeah, his statement is true. He just doesn’t talk about the nightmare of deconstructing your relational database prior to the migration. Note he didn’t use the phrase “only” here, as Azure offers a robust Data Migration Service, along with a <a href="https://datamigration.microsoft.com/">playbook for data migrations</a> that includes sources such as Cassandra and Access (sources not offered by AWS, by the way).

&nbsp;
<h2>AWS has 11 different ways to get your data into the cloud depending on the nature of your data and your application. Nobody else has a little bit more than half of that.</h2>
This is the list of data transfer services on stage when <a href="https://youtu.be/ZOIkOnW640A?t=1854" target="_blank" rel="noreferrer noopener">Jassy makes this statement</a>:

<a href="https://aws.amazon.com/directconnect/" target="_blank" rel="noopener">AWS Direct Connect</a>
<a href="https://aws.amazon.com/snowball/" target="_blank" rel="noopener">AWS Snowball</a>
<a href="https://aws.amazon.com/snowball-edge/" target="_blank" rel="noopener">AWS Snowball Edge</a>
<a href="https://aws.amazon.com/snowmobile/" target="_blank" rel="noopener">AWS Snowmobile</a>
<a href="https://aws.amazon.com/storagegateway/" target="_blank" rel="noopener">AWS Storage Gateway</a>
<a href="https://aws.amazon.com/kinesis/data-firehose/" target="_blank" rel="noopener">Amazon Kinesis Firehose</a>
<a href="https://aws.amazon.com/kinesis/data-streams/" target="_blank" rel="noopener">Amazon Kinesis Data Streams</a>
<a href="https://aws.amazon.com/kinesis/video-streams/" target="_blank" rel="noopener">Amazon Kinesis Video Streams</a>
<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html" target="_blank" rel="noopener">Amazon S3 Transfer Acceleration</a>
<a href="https://aws.amazon.com/datasync/" target="_blank" rel="noopener">AWS DataSync</a>
<a href="https://aws.amazon.com/sftp/" target="_blank" rel="noopener">AWS Transfer for SFTP</a>

My first issue here is counting Kinesis three times. That seems to be a bit of a stretch, but OK. Oh, and Kinesis is listed under “Analytics”, not with the migration products. Warrants mentioning.

Now, let’s consider similar offerings from Azure. I’ll use the same method of accounting that AWS did for that slide.

<a href="https://azure.microsoft.com/en-us/services/storage/databox/" target="_blank" rel="noopener">Azure Data Box</a>
<a href="https://azure.microsoft.com/en-us/services/storage/databox/" target="_blank" rel="noopener">Azure Data Box Disk</a>
<a href="https://azure.microsoft.com/en-us/services/storage/databox/" target="_blank" rel="noopener">Azure Data Box Heavy</a>
<a href="https://azure.microsoft.com/en-us/services/data-factory/" target="_blank" rel="noopener">Azure Data Factory</a>
<a href="https://azure.microsoft.com/en-us/services/event-hubs/" target="_blank" rel="noopener">Azure Event Hubs</a>
<a href="https://azure.microsoft.com/en-us/services/sql-server-stretch-database/" target="_blank" rel="noopener">SQL Server Stretch Database</a>
<a href="https://azure.microsoft.com/en-us/services/storsimple/" target="_blank" rel="noopener">Azure StorSimple</a>
<a href="https://azure.microsoft.com/en-us/services/vpn-gateway/" target="_blank" rel="noopener">Azure VPN Gateway</a>

That’s 8, and 8 is more than half of 11.

&nbsp;
<h2>Amazon Neptune which we launched here a year ago and it's off to really a raring start.</h2>
<a href="https://db-engines.com/en/ranking">Amazon Neptune is currently ranked #129 on the DB-Engines rankings</a>. Not exactly a fiery meteor cutting a path to the top of the leaderboard. But watch out Db4o, Neptune has you in their sights!

&nbsp;
<h2>S3 is the most secure object store. It's the only object store that allows you to audit any access to an object.</h2>
I don’t know what Jassy means by “most secure”. And the phrase “audit” can mean many different things. But Azure offers a lot of <a href="https://azure.microsoft.com/en-us/services/security-center/">security features</a> as well as <a href="https://docs.microsoft.com/en-us/azure/security/azure-log-audit">logging</a>.

&nbsp;
<h2>S3 is the only object store that allows you to do cross region replication.</h2>
This is false. <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction#replication">Azure Storage has offered this feature for years</a>. No, I don’t know why or how a statement this false was allowed in the keynote. It’s disappointing.

&nbsp;
<h2>The world of databases in the Old Guard commercial grade databases has been a miserable world for the last couple decades.</h2>
I won’t argue otherwise, but I would say that it’s not just the world of databases.

Warrants mentioning that those miserable databases are the exact ones that AWS wants to host for you. In other words, “commercial databases are miserable unless you are using them in our cloud”.

Seems legit.

&nbsp;
<h2>Summary</h2>
OK AWS, listen up. You've got a great set of services for data and databases. And a lot of stuff said in the keynote is true, too. For example, you have <a href="https://aws.amazon.com/ec2/instance-types/p3/" target="_blank" rel="noopener">the most powerful GPU offering on the market</a>. You are a leader in many areas of cloud computing.

You don't need to resort to these tactics, where you stretch the truth in order to make a point. Just focus on the awesome stuff you have. Talk about the wonderful support you offer your customers. Y<span style="display: inline !important; float: none; background-color: transparent; color: #666666; cursor: text; font-family: 'Open Sans',Arial,sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 500; letter-spacing: normal; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">ou're better than this. </span>

When I hear statements like the ones above, it makes me think twice about all of the messages that are coming out of AWS.

I know that these are a handful of statements in a long keynote. But I still believe this was a poor effort on your part. A simple 5 minutes of research to compare and contrast services would have fixed everything above.

Hugs.

(Please don't read this and decide to delay delivery of our Christmas gifts.)

&nbsp;
<h2>References</h2>
<a href="https://azure.microsoft.com/en-us/services/">https://azure.microsoft.com/en-us/services/</a>
<a href="https://aws.amazon.com/products/" target="_blank" rel="noopener">https://aws.amazon.com/products/</a>
<a href="https://db-engines.com/en/ranking" target="_blank" rel="noopener">https://db-engines.com/en/ranking</a>
<a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/</a>
<a href="https://thomaslarock.com/2018/03/azure-vs-aws-analytics-and-big-data-services-comparison/" target="_blank" rel="noopener">https://thomaslarock.com/2018/03/azure-vs-aws-analytics-and-big-data-services-comparison/</a>