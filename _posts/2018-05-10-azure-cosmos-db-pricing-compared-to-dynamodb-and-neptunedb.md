---
layout: post
title: Azure Cosmos DB Pricing Compared to DynamoDB and NeptuneDB
date: '2018-05-10 15:29:15 +0000'
categories:
- AWS
- Azure
- SQL Azure
- SQL MVP
tags:
- AWS
- Azure
- cosmosdb
- DynamoDB
- neptunedb
---

This week at the Microsoft Build conference a <a href="https://searchcloudcomputing.techtarget.com/news/252440845/Azure-Cosmos-DB-flexes-joints-for-multiple-data-stores" target="_blank" rel="noopener">new provisioning option for Cosmos DB was announced</a>. The new option, to provision throughput for a set of containers, is a wonderful new feature. However, this meant I needed to take some time to understand Azure Cosmos DB pricing compared to DynamoDB and NeptuneDB.

This new provisioning feature for Cosmos DB offers more granularity than previously. Now, we are allowed to provision a set of containers, say with 50,000 RU/s to be shared. Then, you can create collections to have a piece of the 50,000  instead of needed to create new Cosmos DB for your applications that have different throughput needs.

The 50,000 number isn't something I pulled out of thin air. It is the minimum number you are allowed to use. A quick look at the <a href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank" rel="noopener">pricing calculator</a> show us the cost, at a minimum, for this new feature:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/azure-cosmosdb-pricing.jpg"><img class="aligncenter size-large wp-image-19084" src="https://thomaslarock.com/wp-content/uploads/2018/05/azure-cosmosdb-pricing-600x313.jpg" alt="Azure CosmosDB Pricing" width="600" height="313" /></a>

&nbsp;

At $3k a month, this new provisioning option seems expensive. The minimum for CosmosDB is 400 RU/s, and that's only about $30/month to get started. This 50k minimum and $3k/month costs have been discussed a bit online, mostly by people complaining that the cost is too much. My first thought to seeing such complaints was "this isn't the right solution for you", followed by "how much would a similar offering from AWS cost?"

That's what I want to do here today. Let's break this down.

&nbsp;
<h2>Pricing Specifications</h2>
We need to set the stage for our comparison. Here's the <a href="https://docs.microsoft.com/en-us/azure/cosmos-db/request-units" target="_blank" rel="noopener">reference</a> I will use as a starting point:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/azure-cosmosdb-pricing-RU-example.jpg"><img class="aligncenter size-large wp-image-19085" src="https://thomaslarock.com/wp-content/uploads/2018/05/azure-cosmosdb-pricing-RU-example-600x236.jpg" alt="Azure CosmosDB Pricing" width="600" height="236" /></a>

&nbsp;

That table shows us some examples of throughput capacity. It breaks down item size along with reads and writes. This shows us the total number of RU/s needed.

The fifth line is the one we will use as our base. We are going to assume an item size of 64kb, and a 5:1 ratio of reads to writes. At a 50,000 RU/s minimum for the new provisioning option, that implies we should have about 2500 reads and 500 writes per second. We will also use 100GB as our storage requirement.

Lastly, we will split the workload in Cosmos DB to be 50-50 between graph and non-graph. The reason for this is because AWS doesn't have an all-in-one service like Cosmos DB. We will need to compare to AWS DynamoDB and AWS NeptuneDB.

&nbsp;
<h2>Amazon DynamoDB Pricing</h2>
I am going to configure the AWS monthly calculator for 50Gb of storage, and we will assume that 40GB is egress, and 10Gb is ingress. We will set the item size to be 64k, the reads/sec to 1250, and the writes/sec to 250. The Cosmos DB numbers were set to a consistency state of "session", which is in the middle between strong and eventual. Since AWS doesn't offer this level, I will go with eventual consistency, which <a href="https://calculator.s3.amazonaws.com/index.html" target="_blank" rel="noopener">lowers the price overall</a>:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/aws-dynamo-db-pricing.jpg"><img class="aligncenter size-large wp-image-19089" src="https://thomaslarock.com/wp-content/uploads/2018/05/aws-dynamo-db-pricing-600x437.jpg" alt="AWS DynamoDB Pricing" width="600" height="437" /></a>

&nbsp;

So, that would cost over $9k, and wouldn't include our graph database needs. So, let's get that number next.

&nbsp;
<h2>Amazon NeptuneDB Pricing</h2>
The AWS monthly calculator does not have NeptuneDB as an option yet. I am guessing this is because NeptuneDB is still in preview. So we need to do this by hand.

From the <a href="https://aws.amazon.com/neptune/pricing/" target="_blank" rel="noopener">Neptune pricing page</a>, it the billing involves the size of the instance, storage, I/O, and data transfer. For our purposes, we will use the lower end instance (db.r3.large). We will use 50GB for storage. We will use 40GB egress and 10GB ingress. For the requests, we need to do some math. We need to calculate the total number of requests per month in Cosmos DB. We need to do this in order to convert into the pricing metric for NeptuneDB. Half the Cosmos DB workload would be 25k RU/s, and that works out to be (25000 * 720 * 3600) 64,800,000,000 requests a month. NeptuneDB charges $0.20 per million, so that works out to be (64800000000 / 1000000 * $0.20) = $12,960.

So, the total for NeptuneDB would be:

– The db.r3.large instance is $252/month
– The 50 Gb storage is $5/month
– The 64,800 million requests are $12,960/month
– The data transfer rate is $3.60/month

That's a total of $13220.60, just for NeptuneDB. And that makes the AWS offering(s) a total of $22636.43/month.

Just a tad more expensive than the CosmosDB monthly price.

&nbsp;
<h2>Summary</h2>
The new provisioning option for Cosmos DB allows for greater flexibility in how to manage workloads for your specific containers. Previously you would have had to provision new Cosmos DB instances in order to meet your RU/s requirements. Allowing for customers to group a set of containers and share throughput is a wonderful new feature.

But this feature has a minimum requirement of 50,000 RU/s, which has a price tag of $3k/month. That is likely going to price some people out for now. I can see a scenario where Microsoft reduces the 50k minimum. <a href="https://azure.microsoft.com/en-us/blog/azure-cosmosdb-entry-point-for-unlimited-containers-is-now-60-cheaper-and-other-improvements/" target="_blank" rel="noopener">They've reduced costs before</a>, doing so again would not be unprecedented.

And when you compare the throughput evenly across AWS DynamoDB and NeptuneDB, $3k is a bargain. This becomes more apparent when you consider additional things such as performance, recovery, availability, and multi-master.