---
layout: post
title: Azure vs. AWS Data Services Comparison
date: '2018-03-20 15:34:32 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- MSSQL
- SQL Azure
tags:
- Amazon
- AWS
- Azure
- microsoft
---

Both Microsoft Azure and Amazon Web Services offer a lot of data services. So many services that it can be hard to comprehend how the compare without a scorecard. So, that's what I did here, I put together a quick image to help you make sense of all the offerings current available (as of March, 2018). Essentially, I wanted to build a cheatsheet for Azure vs. AWS data services comparison purposes.

It is my hope that this post will be a starting guide for you when you need to research these services. I have included relevant links for each service, along with some commentary, in the text of this post below. I've done my best to align the services, but there is some overlap between offerings. Some offerings, like data warehousing and cache, are easy to discern.

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWSvAzure.jpg"><img class="aligncenter size-full wp-image-18807" src="https://thomaslarock.com/wp-content/uploads/2018/03/AWSvAzure.jpg" alt="Azure and Amazon AWS data services comparison" width="777" height="275" /></a>

&nbsp;

OK, let's break these down into groups. I'm not going to do a feature comparison here because these systems evolve so quickly I'd spend all day updating the info. Instead, you get links to the documentation for everything and you can do your own comparisons as needed.

&nbsp;
<h2>Relational</h2>
Azure offerings: <a href="https://docs.microsoft.com/en-us/azure/sql-database/" target="_blank" rel="noopener">SQL Database</a>, <a href="https://docs.microsoft.com/en-us/azure/mysql/" target="_blank" rel="noopener">Database for MySQL</a>, <a href="https://azure.microsoft.com/en-us/services/postgresql/" target="_blank" rel="noopener">Database for PostgreSQL</a>

AWS offerings: <a href="https://aws.amazon.com/rds/details/" target="_blank" rel="noopener">RDS</a>, <a href="https://aws.amazon.com/rds/aurora/details/" target="_blank" rel="noopener">Aurora</a>

RDS is an umbrella term, as it is six engines in total, and it includes <a href="https://aws.amazon.com/rds/aurora/details/">Amazon Aurora</a>, <a href="https://aws.amazon.com/rds/mysql/details/">MySQL</a>, <a href="https://aws.amazon.com/rds/mariadb/details/">MariaDB</a>, <a href="https://aws.amazon.com/rds/oracle/details/">Oracle</a>, <a href="https://aws.amazon.com/rds/sqlserver/details/">Microsoft SQL Server</a>, and <a href="https://aws.amazon.com/rds/postgresql/details/">PostgreSQL</a>. I've listed Aurora as a distinct offering because it is the high-end service dedicated to MySQL and PostgreSQL. Since Azure also offers those distinct services it made sense to break Aurora out from RDS. (Or, to put it another way, if I didn't call out Aurora here you'd finish this post and say 'what about Aurora', and now you don't have to ask that question.)

&nbsp;
<h2>NoSQL - Key/Value</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener">Cosmos DB</a>, <a href="https://azure.microsoft.com/en-us/services/storage/tables/" target="_blank" rel="noopener">Table Storage</a>

AWS offerings: <a href="https://aws.amazon.com/dynamodb/details/" target="_blank" rel="noopener">DynamoDB</a>, <a href="https://aws.amazon.com/simpledb/details/" target="_blank" rel="noopener">SimpleDB</a>

Cosmos DB is the major NoSQL player for Azure, as it does everything (key/value, document, graph) except relational.

&nbsp;
<h2>NoSQL - Document</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener">Cosmos DB</a>

AWS offerings: <a href="https://aws.amazon.com/dynamodb/details/" target="_blank" rel="noopener">DynamoDB</a>

Azure used to offer DocumentDB, but that platform was sunset <a href="https://azure.microsoft.com/en-us/blog/azure-cosmos-db-microsofts-globally-distributed-multi-model-database-service/" target="_blank" rel="noopener">when Cosmos DB came alive</a>.

&nbsp;
<h2>NoSQL - Graph</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener">Cosmos DB</a>

AWS offerings: <a href="https://docs.aws.amazon.com/neptune/latest/userguide/intro.html" target="_blank" rel="noopener">Neptune</a>

As of March 2018, Neptune is in Preview, so the documentation is likely to change in the coming weeks (well, that's my assumption, <a href="https://aws.amazon.com/blogs/aws/amazon-neptune-a-fully-managed-graph-database-service/" target="_blank" rel="noopener">because Neptune has been in Preview since November</a>.)

&nbsp;
<h2>Data Warehouse</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/sql-data-warehouse/" target="_blank" rel="noopener">SQL Data Warehouse</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/redshift/" target="_blank" rel="noopener">Redshift</a>

It feels like these two services have been around forever. That's because, in internet years, they have. Redshift goes back to 2012, and SQL DW goes back to 2009. That's a lot of time for both Azure and AWS to learn about data warehousing as a service.

&nbsp;
<h2>Cache</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cache/" target="_blank" rel="noopener">Redis Cache</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/elasticache/" target="_blank" rel="noopener">ElastiCache</a>

Both of these services are built upon Redis, so the real question here is if you want to use Redis-as-a-service from a 3rd party provider as opposed to just using it Redis itself.

&nbsp;
<h2>Pricing</h2>
Azure Pricing calculator: <a href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank" rel="noopener">https://azure.microsoft.com/en-us/pricing/calculator/</a>

AWS Pricing Calculator: <a href="https://calculator.s3.amazonaws.com/index.html" target="_blank" rel="noopener">https://calculator.s3.amazonaws.com/index.html</a>

The pricing calculators give you the best understanding of capacity. You could spend days trying to figure out the resource limits for each service listed on this page. But if you start with the calculator you get an idea of the most important thing, the cost of the service. Here's an example of what I mean. Let's look at something that should be an easy comparison: SQL Data Warehouse versus Redshift. I will compare a 100% utilized instance for each.

Here is the pricing summary for Azure SQL Data Warehouse, optimized for capacity, and with storage of 10 TB:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/azure_sql_dw_pricing.jpg"><img class="aligncenter size-large wp-image-18804" src="https://thomaslarock.com/wp-content/uploads/2018/03/azure_sql_dw_pricing-600x311.jpg" alt="Azure SQL Data Warehouse pricing" width="600" height="311" /></a>

&nbsp;

The calculator tells me the two most important things I need to know: That I pay for storage, and for <a href="https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-manage-compute-overview" target="_blank" rel="noopener">something called a DWU</a>. So, that's the stuff to research next.

For Redshift, we have this:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/aws_redshift_pricing.jpg"><img class="aligncenter size-large wp-image-18805" src="https://thomaslarock.com/wp-content/uploads/2018/03/aws_redshift_pricing-600x386.jpg" alt="AWS Redshift Pricing" width="600" height="386" /></a>

&nbsp;

AWS seems to be charging for compute power only and not for storage. Also, this is the cost for only one node, whereas SQL Data Warehouse will use more than one node to distribute the workload. And this doesn't help explain failovers, maintenance, disaster recovery, etc.

It can be frustrating to compare the data services being offered between Azure and AWS. Part of me thinks this is done on purpose by both companies in an effort to win our favor without giving away more information than is necessary. This is a common practice, and I'm not bashing either company for doing what has been done for centuries. I'm here to help others figure out how to make the right choice for their needs. At the end of the day, I believe both Amazon and Microsoft want the same thing: happy customers.

By starting at the pricing pages I can then dive into the specific costs, and use that as a first level comparison between the services. If you start by looking at resource limits and maximums you will spend a lot of time trying to compare apples to oranges. Just focus on costs, those resources, throughput, and DR. That should be a good start to help you determine the cost, benefit, and risk of each service.

[UPDATE: I did a quick comparison of <a href="https://thomaslarock.com/2018/03/azure-cosmos-db-costs-vs-dynamodb-and-neptune/" target="_blank" rel="noopener">Azure Cosmos DB costs vs DynamoDB and Neptune costs in this post</a>. You're welcome]

&nbsp;
<h2>Summary</h2>
I hope you find this page useful for referencing the many data service offerings from both Microsoft Azure and Amazon Web Services. I will do my best to update this page as necessary, and offer more details and use cases as I am able.