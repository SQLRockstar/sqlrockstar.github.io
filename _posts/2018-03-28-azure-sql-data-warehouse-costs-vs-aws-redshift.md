---
layout: post
title: Azure SQL Data Warehouse Costs vs AWS Redshift
date: '2018-03-28 14:39:07 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- MSSQL
- SQL MVP
tags:
- AWS
- AWS Redshift
- Azure
- SQL Data Warehouse
---

Today I wanted to detail <a href="https://azure.microsoft.com/en-us/services/sql-data-warehouse/" target="_blank" rel="noopener">Azure SQL Data Warehouse</a> costs vs <a href="https://aws.amazon.com/documentation/redshift/" target="_blank" rel="noopener">AWS Redshift</a>. This post is meant to follow up on two earlier posts (<a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">Azure vs. AWS Data Services Comparison</a> and <a href="https://thomaslarock.com/2018/03/azure-vs-aws-analytics-and-big-data-services-comparison/" target="_blank" rel="noopener">Azure vs AWS Analytics and Big Data Services Comparison</a>), where I outlined the different services offered. In both of those posts, you will notice that Aure SQL Data Warehouse and AWS Redshift were mentioned. Today I'm going to do a quick price comparison between the two services.

I am going to do my best to arrive at a conclusion that has equal sized servers. The reason for this is because I need to start somewhere, and I want to show the differences in how the costs are broken down. Feel free to experiment with the pricing calculators on your own and do similar pricing comparisons.

Let's break this down. First up, Azure SQL Data Warehouse costs.

&nbsp;
<h2>Azure SQL Data Warehouse Costs</h2>
Here is the <a href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank" rel="noopener">Azure pricing calculator</a> for Azure SQL Data Warehouse:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/Azure_SQL_DW_costs.jpg"><img class="aligncenter size-large wp-image-18857" src="https://thomaslarock.com/wp-content/uploads/2018/03/Azure_SQL_DW_costs-600x313.jpg" alt="Azure SQL Data Warehouse Costs" width="600" height="313" /></a>

&nbsp;

A few things to note here. First, the option for Performance Tier. Here we get to choose Elasticity or Compute (still in Preview). I've chosen Compute for this example because reasons.

Next, we see the choice of cDWU blocks. DWU is short for Data Warehouse Unit, <a href="https://docs.microsoft.com/en-us/azure/sql-data-warehouse/what-is-a-data-warehouse-unit-dwu-cdwu" target="_blank" rel="noopener">and you can read about those here</a>. The thing you want to remember about a DWU is that it is how we <a href="https://docs.microsoft.com/en-us/azure/sql-data-warehouse/performance-tiers" target="_blank" rel="noopener">measure the number of compute nodes for your SQL Data Warehouse</a>. SQL DW uses 60 distribution streams, and the DWU decides how many compute nodes there are. For 1000 cDWU we have 2 nodes. This is important later.

Lastly, we have to select how much storage we need. I will select 2TB of storage because that will be closer to the size of the single node we use in AWS.

So, the total on this page for a SQL Data Warehouse, optimized for compute, 100% utilized for 1 month, at the lowest cDWU allowed (1000 minimum), and 2TB of storage is $5789.14.

Let's look at the AWS Redshift costs next.

&nbsp;
<h2>AWS Redshift Costs</h2>
Here is the <a href="http://calculator.s3.amazonaws.com/index.html" target="_blank" rel="noopener">AWS pricing calculator</a> for Redshift:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_Redshift_costs.jpg"><img class="aligncenter size-full wp-image-18858" src="https://thomaslarock.com/wp-content/uploads/2018/03/AWS_Redshift_costs.jpg" alt="AWS Redshift Costs" width="570" height="394" /></a>

&nbsp;

It's just one line, you pick the size of the node you want. There's no description for the different nodes, but <a href="https://aws.amazon.com/redshift/faqs/" target="_blank" rel="noopener">this page helped me understand</a> that "ds" means "Dense Storage", and "dc" means "Dense Compute". So, I chose the dc2.8xlarge, which gives me 2.56TB of SSD storage. And I need two of these nodes, because our Azure SQL Data Warehouse has two compute nodes. Our total cost here is $7729.92.

&nbsp;
<h2>Just to Make Things More Complex</h2>
The AWS Redshift pricing makes no mention of a DWU unit in any way. <a href="https://aws.amazon.com/redshift/pricing/" target="_blank" rel="noopener">This page helps me see there is a 7/5Gb/sec I/O rate</a>. Azure SQL Data Warehouse does not offer a similar metric for the hardware they are using. Well, I guess they *do*, and it's called a DWU. But since a DWU is a combination of CPU, memory, and I/O, it's up to you to figure out what resource is most important based on your workload. In other words, you can't just spin up one of each and compare performance without knowing what resource your workload will need the most.

Another point of interest here: no mention of failover or backups on the pricing pages for either Redshift or SQL Data Warehouse. But <a href="https://azure.microsoft.com/en-us/pricing/details/sql-data-warehouse/compute/" target="_blank" rel="noopener">on this page for SQL Data Warehouse</a> you will find that geo-replication costs you $0.12/Gb/Month. Redshift talks about giving you <a href="https://aws.amazon.com/redshift/pricing/" target="_blank" rel="noopener">backup storage equal to the size of your warehouse each month for free</a>. SQL DW rolls backup (snapshot) costs into the storage costs you set on the pricing page.

Oh, one more thing: egress. Neither service makes much effort to talk about egress charges on their pricing calculators. You can find the details if you hunt for them. At first, I thought this was odd. But now I understand that there may not be egress from these data warehouse services. It is likely you would move data from the warehouse to another service inside that same cloud. From there you would perform analytics or run reports, and that is where you would see egress charges.

&nbsp;
<h2>Summary</h2>
I've tried to outline the high-level differences in pricing between these two data warehouse services. I did not explore all regions, or failovers, availability, etc. I've tried to keep things as simple as possible to give you an idea of costs and services provided.

It's hard to compare cloud services, but not impossible. I find it is easier to evaluate services when you examine costs versus trying to examine the resource limits the services provide.