---
layout: post
title: The Future For Database Transaction Units
date: '2017-06-05 11:44:05 +0000'
categories:
- Cloud Computing
- SQL Azure
- SQL MVP
- SQL Server Performance
tags:
- Azure
- DTUs
- MySQL
- PostgreSQL
---

It was over three years ago that Microsoft introduced the concept of Database Transaction Units (DTUs). To those of us familiar with SQL Server and SQL Database we all had one question: <a href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-what-is-a-dtu" target="_blank" rel="noopener noreferrer">what the hell is a DTU</a>?

The DTU would calculate the resources consumed and use that number to help guarantee performance for all customers. Exceed the DTU you pay for and you will get throttled. It does not matter what hardware resource your workload is consuming most. The end result is a DTU number that is used to compare to your service level.

For three years we have adjusted to the idea that DTUs are a thing. We even have taken the time to <a href="https://johnsterrett.com/2016/08/24/calculate-dtu-azure-sql-database/" target="_blank" rel="noopener noreferrer">write scripts so we could look at the DTU for specific queries</a>.

At <a href="https://techcrunch.com/2017/05/10/microsoft-launches-azure-database-for-mysql-and-postgressql/" target="_blank" rel="noopener noreferrer">Microsoft Build we heard about MySQL and PostgreSQL</a> coming to Azure. Earlier this week I noted the <a href="https://azure.microsoft.com/en-us/pricing/details/mysql/" target="_blank" rel="noopener noreferrer">billing for those services</a> and found something interesting: there is no DTU. They use Compute Units (CUs) combined with IOPS instead of DTUs.

But these are Platforms-as-a-Service, same as SQL Database. Why the difference in pricing? I tweeted about it and got a reply the next day:

https://twitter.com/JasonMA_MSFT/status/870665662653382656

I agree that using the combination of CUs and IOPS gives more flexibility for both customers and Microsoft.

So that leaves me with one question: Why are we still using DTUs? It would seem to me that the idea of a DTU, while once relevant, isn't anymore. And while DTUs are inside of the pricing for data products such as SQL Database and SQL Data Warehouse, I am uncertain that DTUs are as useful as CUs and IOPS. I like the current pricing model for MySQL and PostgreSQL. I'm hoping SQL Database start using CUs and IOPS for pricing soon.

I write this post with a smile, thinking about how fast things change in the Cloud-first world of tech these days. It's clear to me that if DTUs were the future then MySQL and PostgreSQL would have been using them. Since they are not, I suspect that DTUs will be going away. Customers care more about performance than billing. But it does not make sense to have complicated billing for customers using a mix of both platforms.