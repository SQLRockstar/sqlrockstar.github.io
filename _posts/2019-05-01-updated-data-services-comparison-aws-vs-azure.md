---
layout: post
title: 'Updated Data Services Comparison: AWS vs. Azure'
date: '2019-05-01 11:59:25 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- SQL MVP
tags:
- aurora
- AWS
- Azure
- Cosmos DB
- data services
- RDS
- SQL Database
---

Last year I wrote a post <a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener noreferrer">comparing the data services offered by both AWS and Microsoft Azure</a>. Well, there's been some changes since, so it was time to provide an updated graphic and links.

Since both Microsoft Azure and Amazon Web Services offer many data services, I thought it worth the time to create a graphic to help everyone understand the services a bit more. Essentially, I wanted to build a cheat sheet for any data services comparison (click to embiggen):

<a href="https://thomaslarock.com/wp-content/uploads/2019/05/DataServices.jpg"><img class="aligncenter size-large wp-image-19510" src="https://thomaslarock.com/wp-content/uploads/2019/05/DataServices-600x174.jpg" alt="data services comparison aws versus azure" width="600" height="174" /></a>

You might notice that there is no Data Warehouse category. That category is located in the Analytics and Big Data comparison chart which I will share in a future post.

It is my hope that this post will be a starting guide for you when you need to research cloud data services. I'm not going to do a feature comparison here because these systems evolve so quickly I'd spend all day updating the info. Instead, you get links to the documentation for everything and you can do your own comparisons as needed. I hope to have future posts that help break down features and costs, but for now let's keep it simple.

&nbsp;
<h2>Relational</h2>
Azure offerings: <a href="https://docs.microsoft.com/en-us/azure/sql-database/" target="_blank" rel="noopener noreferrer">SQL Database</a>, <a href="https://docs.microsoft.com/en-us/azure/mysql/" target="_blank" rel="noopener noreferrer">Database for MySQL</a>, <a href="https://azure.microsoft.com/en-us/services/postgresql/" target="_blank" rel="noopener noreferrer">Database for PostgreSQL</a>, <a href="https://docs.microsoft.com/en-us/azure/mariadb/" target="_blank" rel="noopener noreferrer">Database for MariaDB</a>

AWS offerings: <a href="https://aws.amazon.com/rds/details/" target="_blank" rel="noopener noreferrer">RDS</a>, <a href="https://aws.amazon.com/rds/aurora/details/" target="_blank" rel="noopener noreferrer">Aurora</a>

RDS is an umbrella term, as it is six engines in total, and it includes <a href="https://aws.amazon.com/rds/aurora/details/">Amazon Aurora</a>, <a href="https://aws.amazon.com/rds/mysql/details/">MySQL</a>, <a href="https://aws.amazon.com/rds/mariadb/details/">MariaDB</a>, <a href="https://aws.amazon.com/rds/oracle/details/">Oracle</a>, <a href="https://aws.amazon.com/rds/sqlserver/details/">Microsoft SQL Server</a>, and <a href="https://aws.amazon.com/rds/postgresql/details/">PostgreSQL</a>. I've listed Aurora as a distinct offering because it is the high-end service dedicated to MySQL and PostgreSQL. Since Azure also offers those distinct services it made sense to break Aurora out from RDS. (Or, to put it another way, if I didn't call out Aurora here you'd finish this post and say 'what about Aurora', and now you don't have to ask that question.)

&nbsp;
<h2>NoSQL - Key/Value</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener noreferrer">Cosmos DB</a>, <a href="https://azure.microsoft.com/en-us/services/storage/tables/" target="_blank" rel="noopener noreferrer">Table Storage</a>

AWS offerings: <a href="https://aws.amazon.com/dynamodb/details/" target="_blank" rel="noopener noreferrer">DynamoDB</a>, <a href="https://aws.amazon.com/simpledb/details/" target="_blank" rel="noopener noreferrer">SimpleDB</a>

Cosmos DB is the major NoSQL player for Azure, as it does everything (key/value, document, graph) except relational. DynamoDB is a workhorse for AWS. SimpleDB is still around, but there are rumors it will be going away. This might be due to the fact that you cannot <a href="https://us-west-2.console.aws.amazon.com/console" target="_blank" rel="noopener noreferrer">create a SimpleDB service using the AWS Console</a>. So, short story, look for this category to be just Cosmos DB and DynamoDB in the future.

&nbsp;
<h2>NoSQL - Document</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener noreferrer">Cosmos DB</a>

AWS offerings: <a href="https://aws.amazon.com/documentdb/" target="_blank" rel="noopener noreferrer">DocumentDB</a>

Azure used to offer DocumentDB, but that platform was sunset <a href="https://azure.microsoft.com/en-us/blog/azure-cosmos-db-microsofts-globally-distributed-multi-model-database-service/" target="_blank" rel="noopener noreferrer">when Cosmos DB came alive</a>. AWS <a href="https://www.infoq.com/news/2019/01/aws-documentdb-mongodb" target="_blank" rel="noopener noreferrer">recently launched</a> DocumentDB with MongoDB compatibility in what some people see as a <a href="https://www.itpro.co.uk/open-source/32703/aws-launches-documentdb-in-a-blow-to-open-source" target="_blank" rel="noopener noreferrer">major blow to open source</a>.

&nbsp;
<h2>NoSQL - Graph</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener noreferrer">Cosmos DB</a>

AWS offerings: <a href="https://docs.aws.amazon.com/neptune/latest/userguide/intro.html" target="_blank" rel="noopener noreferrer">Neptune</a>

As of May 2019, Neptune is in Preview, so the documentation is likely to change in the coming <del>weeks</del> <del>months</del> years (well, that's my assumption, <a href="https://aws.amazon.com/blogs/aws/amazon-neptune-a-fully-managed-graph-database-service/" target="_blank" rel="noopener noreferrer">because Neptune has been in Preview since November 2018</a>.) Cosmos DB uses a Gremlin API for graph purposes.

&nbsp;
<h2>In-Memory</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/cache/" target="_blank" rel="noopener noreferrer">Cache for Redis</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/elasticache/" target="_blank" rel="noopener noreferrer">ElastiCache</a>

Both of these services are built upon Redis, so the real question here is if you want to use Redis-as-a-service from a 3rd party provider as opposed to just using it Redis itself.

&nbsp;
<h2>Time Series</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/time-series-insights/" target="_blank" rel="noopener noreferrer">Time Series Insights</a>

AWS offerings: <a href="https://aws.amazon.com/timestream/" target="_blank" rel="noopener noreferrer">Timestream</a>

If you are in need of a time series database for your IoT collections, then both Azure and AWS have a service to offer. Azure Time Series Insights was launched in early 2017, and AWS announced Timestream in late 2018. In other words, the world of data services is moving fast, and the two major cloud providers are able to roll out services to meet growing demand.

&nbsp;
<h2>Ledger</h2>
Azure offerings: [<a href="https://wompwompwomp.com/" target="_blank" rel="noopener noreferrer">Sad Trombone</a>]

AWS offerings: <a href="https://aws.amazon.com/qldb/" target="_blank" rel="noopener noreferrer">Quantum ledger Database</a>

Setting aside the silliness of using the buzzword 'Quantum' in the name of this product, AWS does have a ledger database service available. As of May 2019, Azure does not offer a similar service.

&nbsp;
<h2>Pricing</h2>
Azure Pricing calculator: <a href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank" rel="noopener noreferrer">https://azure.microsoft.com/en-us/pricing/calculator/</a>

AWS Pricing Calculator: <a href="https://calculator.aws" target="_blank" rel="noopener noreferrer">https://calculator.aws</a>

I like using pricing as a way to start any initial comparison between data services. These calculators will help you focus on the important details. Not just costs, but how the technology works. For example, Azure SQL Database focuses on the concept of a DTU, which has no meaning in AWS. Using the calculators forces you to learn the differences between the two systems. It's a great starting point.

That being said, trying to compare the data services offered by AWS and Azure can be frustrating. Part of me thinks this is done on purpose by both companies in an effort to win our favor without giving away more information than is necessary. This is a common practice, and I'm not bashing either company for doing what has been done for centuries. I'm here to help others figure out how to make the right choice for their needs. At the end of the day, I believe both Amazon and Microsoft want the same thing: happy customers.

By starting at the pricing pages I can then dive into the specific costs, and use that as a first level comparison between the services. If you start by looking at resource limits and maximums you will spend a lot of time trying to compare apples to oranges. Just focus on costs, those resources, throughput, and DR. That should be a good start to help you determine the cost, benefit, and risk of each service.

&nbsp;
<h2>Summary</h2>
I hope you find this page useful for referencing the many data service offerings from both Microsoft Azure and Amazon Web Services. I will do my best to update this page as necessary, and offer more details and use cases as I am able.