---
layout: post
title: Azure Cosmos DB Costs vs Dynamo DB and Neptune
date: '2018-03-21 13:53:11 +0000'
categories:
- AWS
- Azure
- MSSQL
- SQL MVP
tags:
- AWS
- Azure
- Cosmos DB
- DynamoDB
- Neptune
---

Building on yesterday's post, <a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">Azure vs. AWS Data Services Comparison</a>, today I want to write about the <a href="https://azure.microsoft.com/en-us/services/cosmos-db/?v=17.45b" target="_blank" rel="noopener">Azure Cosmos DB</a> costs vs <a href="https://aws.amazon.com/dynamodb/details/" target="_blank" rel="noopener">DynamoDB</a> and <a href="https://docs.aws.amazon.com/neptune/latest/userguide/intro.html" target="_blank" rel="noopener">Neptune</a>. I'm going to give an example today comparing only the NoSQL services offered by Azure and AWS.

For Azure, the NoSQL service offered is Azure Cosmos DB. Cosmos DB is the place for all your key-value, document, and graph database needs. (Cosmos DB is what we would have if your cable company started offering databases. Phone, television, and internet all bundled together for one low price sounds good, but key-value, document, and graph for one price and SHUT UP AND TAKE MY MONEY). On the AWS side, we have DynamoDB for key-value and document, and Neptune for graph.

For the purpose of this post, I am going to try to price the simplest of deployments in an effort to match services. In other words, I'm not going to dive into multi-region or geo-replicated databases today. I am going to assume that we have a requirement of 50GB of storage for three database services: key-value, document, and graph. I will keep the reads and writes to be the same, and do my best to keep everything equal.

Let's break this down. First up, Cosmos DB pricing.

&nbsp;
<h2>Azure Cosmos DB Pricing</h2>
The Azure pricing page seems simple enough. You pay for your storage and for these things called request units per second, or RU/s. The FAQ section of the Cosmos DB page <a href="https://azure.microsoft.com/en-us/pricing/details/cosmos-db/" target="_blank" rel="noopener">explains in simple terms what RU/s means</a>. However, <a href="https://docs.microsoft.com/en-us/azure/cosmos-db/request-units" target="_blank" rel="noopener">this page is far better</a> for referencing what RU/s means, as well as understanding that <em>size matters</em>. That page also breaks down how you pay less for reading data from Cosmos DB than you do for writing data. I'm going to use one of the 4kb size examples and 500 reads and 500 writes, giving us a total of 4,150 RU/s. We will use that along with a modest 50GB of storage. The pricing calculator looks like this:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/azure_cosmos_db_pricing.jpg"><img class="aligncenter wp-image-18816 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/03/azure_cosmos_db_pricing-600x311.jpg" alt="Azure Cosmos DB pricing" width="600" height="311" /></a>

&nbsp;

Not shown in that image is the fact that support is included, along with 99.99% availability for local region databases (99.999% for multi-region databases). Also worth noting is that Cosmos DB has an SLA of 10ms for reads and 15ms for writes. If Azure cannot give meet that SLA you will receive a credit on your next billing statement.

Let's move on to AWS. For that, we need to look at two services: DynamoDB and Neptune.

&nbsp;
<h2>Amazon DynamoDB Pricing</h2>
For DynamoDB the pricing calculator requires a few more inputs. SImilar to Cosmos DB, we need to know the storage and the expected reads and writes. But we also need to know details about the expected throughput, the consistency model (apparently you pay 2x more for 'strong' consistency in DynamoDB), and we need to know how many requests for something called <a href="https://aws.amazon.com/about-aws/whats-new/2014/11/10/introducing-dynamodb-streams/" target="_blank" rel="noopener">DynamoDB Streams</a>. That link suggests that I would use DynamoDB streams to implement my own form of replication across AWS zones. So, we won't include that in our pricing today. Here's what it looks like:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_dynamo_db_pricing.jpg"><img class="aligncenter size-large wp-image-18817" src="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_dynamo_db_pricing-534x600.jpg" alt="AWS DynamoDB pricing" width="534" height="600" /></a>

&nbsp;

One thing to note here is that the consistency model is a factor for price. For Cosmos DB, there is no difference in price based on consistency models. I chose 'strong' consistency here and we should assume I would be deploying a Cosmos DB with strong consistency as well. Also, warrants mentioning: DynamoDB Streams is in Preview, and the first 2.5 million requests are free. Lastly, I split out the read/write throughput to be an 80/20 split.

Oh, and we are still missing one thing; the ability to use graph.

&nbsp;
<h2>Amazon Neptune Pricing</h2>
Enter Neptune, the AWS graph database service. First, I want you to know that as of this post (March 2018), Neptune is in Preview. You won't find it on the calculator page. Instead, you have to go to the <a href="https://aws.amazon.com/neptune/pricing/" target="_blank" rel="noopener">pricing page for Neptune</a> and manually figure out your costs.

This alone makes it very difficult to compare services between Azure and AWS. For the Cosmos DB example above, I don't need to worry about what service I am using, I just pay one price.

From the Neptune pricing page, it would appear the billing will involve the size of the instance, storage, I/O, and data transfer. For our purposes here, let's assume we have modest needs, and that 25% of the Cosmos DB workload is graph related. So, that's 10 GB storage and 830 RU/s. We will calculate this cost for Neptune.

I will take the lowest end memory-optimized instance (db.r4.large), and allocate 10GB storage. For the total requests, we need to do some math. The Cosmos DB example above was 4200 RU/s, for one month (730 hours). To get the equivalent number of requests for Neptune, we will take 20% of 4200, or 840 requests/second. That would be 220.7 million requests/month. The last piece of information we need is data transfer. Let's assume 20% of the DynamoDB transfer rate, so 8GB out and 2 GB in.

The total for Neptune would be:

- The db.r4.large instance is $255.50/month
- The 10 Gb storage is $1/month
- The 220.7 million requests are $44.14/month
- The data transfer rate is $0.72/month

That's a total of $301.36/month for our graph needs.

But now we need to adjust DynamoDB, reducing it by 20%. Doing that and we have:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_dynamo_db_pricing_again.jpg"><img class="aligncenter size-large wp-image-18818" src="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_dynamo_db_pricing_again-539x600.jpg" alt="AWS DynamoDB pricing" width="539" height="600" /></a>

&nbsp;

Adding this up, we now have $790.60 for DynamoDb and $301.36 for Neptune, for a total of $1,091.96.

The Cosmos DB costs are $257.78. And you get all three services. One bill versus two.

&nbsp;
<h2>Summary</h2>
I've tried here to break down the costs for these three services in an effort to help you make an apples-to-apples comparison. Some things were left out such as specific region costs, failover, availability, backups, etc. I've tried to keep things as simple as possible to give you an idea of costs and services provided.

It's hard to compare cloud services, but not impossible. Feel free to use this method for any of the other services I talked about yesterday. As I mentioned in that post, it is easier to evaluate services when you examine costs versus trying to examine the resource limits the services provide.

This research also makes me wonder why AWS decided to deploy Neptune instead of extending DynamoDB. With that in mind, it would not surprise me to wake up one day to find Neptune absorbs DynamoDB. After all, Cosmos DB absorbed DocumentDB last year. If Neptune became the only offering, it would make this example above a bit easier to complete. And I'd have to <a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWSvAzure.jpg?x74410" target="_blank" rel="noopener">update my cheat sheet</a>.

I'm OK with that.