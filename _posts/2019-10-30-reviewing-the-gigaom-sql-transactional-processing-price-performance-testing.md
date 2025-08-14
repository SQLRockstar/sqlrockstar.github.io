---
layout: post
title: Reviewing the GigaOM SQL Transactional Processing Price-Performance Testing
date: '2019-10-30 14:47:35 +0000'
categories:
- AWS
- Azure
- MSSQL
- SQL Azure
- SQL Server Performance
tags:
- AWS
- Azure
- benchmark
- sql server performance
---

<p>Earlier this month Microsoft and GigaOM announced a <a rel="noreferrer noopener" aria-label="new benchmark study (opens in a new tab)" href="https://azure.microsoft.com/en-us/resources/sql-transactional-processing-price-performance-testing/" target="_blank">new benchmark study</a> comparing AWS RDS to Azure SQL Database. This study was authored by the same people that wrote the previous GigaOM <a rel="noreferrer noopener" aria-label="data warehouse benchmark (opens in a new tab)" href="https://gigaom.com/report/data-warehouse-cloud-benchmark/" target="_blank">data warehouse benchmark</a> last year. I enjoyed the data warehouse study. I found it to be fair and thorough enough to help the reader understand how to conduct their own benchmark testing. I was eager to read the new SQL Transactional Processing Price-Performance Testing study.</p>



<p>I found this latest effort to be a good start, but it fell short of the effort the authors put forth in their previous benchmark for data warehousing.</p>



<p>Before I go any further, I want to thank the authors for putting together their results. I recognize that these are humans, working hard, putting forth their best efforts at being fair and thorough. Comparing cloud services is not an easy task. I found this latest effort to be good, but not great. If they were students of mine I would grade this latest paper from them a solid B-. </p>



<p>Let's break it down.</p>



<h2>The Good Stuff</h2>



<p>First, the good stuff. I love how they drove everything towards a formula, price/performance, where performance is tracked in transactions per second. The downside to price/performance is that not every workload is focused on transactions per second. Still, I'd like to see this formula adopted as a standard way of comparing services. </p>



<p>In the past I've focused only on total price as shown by the online pricing calculators. This is because (1) you aren't supposed to publish benchmarks without permission from the company (Microsoft, AWS) and (2) I can't bankroll this level of test AND maintain my scotch and bacon addictions. By using price/performance you level the playing field somewhat. A service may cost more, but if it runs your query in half the time, the cost may be worth it. </p>



<p>I also liked the choice of using TPC-E as their test, I believe that to be a fair way to compare how the services will handle a workload. And I liked how they explained the difficulties in comparing services and the associated hardware. That's something I've <a rel="noreferrer noopener" aria-label="written about previously (opens in a new tab)" href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank">written about previously</a>. <a rel="noreferrer noopener" aria-label="Many (opens in a new tab)" href="https://thomaslarock.com/2019/05/updated-data-services-comparison-aws-vs-azure/" target="_blank">Many</a> <a rel="noreferrer noopener" aria-label="times (opens in a new tab)" href="https://thomaslarock.com/2018/03/azure-vs-aws-analytics-and-big-data-services-comparison/" target="_blank">times</a>, <a rel="noreferrer noopener" aria-label="really (opens in a new tab)" href="https://thomaslarock.com/2018/03/azure-sql-data-warehouse-costs-vs-aws-redshift/" target="_blank">really</a>.</p>



<p>It is frustrating to compare the data services being offered between Azure and AWS. Part of me thinks this is done on purpose by both companies in an effort to win our favor without giving away more information than is necessary. This is a common practice, and I’m not bashing either company for doing what has been done for centuries. I’m here to help others figure out how to make the right choice for their needs. At the end of the day, I believe both Amazon and Microsoft want the same thing: happy customers.</p>



<p>But it is not in their best interest to make it easy for anyone to compare costs. This is how utilities operate. Make no mistake, AWS and Azure are the new electric company. </p>



<p>Now, for the items that I didn't like as much. I'll capture the quote from the article and explain my concern. </p>



<h2>The Not As Good Stuff</h2>



<p>"<strong>There are no exact matches in processors or memory</strong>." - This is a bit of nitpicking, but I took issue here with the use of the word "or". As someone who charges (and receives) top dollar for performing technical reviews of books, it bugged me. The authors are correct in saying that it is hard to find exact matches. However, I can certainly find a match for vCPU, but not for memory. <a rel="noreferrer noopener" aria-label="Azure publishes memory as weird increments (opens in a new tab)" href="https://azure.microsoft.com/en-us/pricing/details/sql-database/single/" target="_blank">Azure publishes memory as weird increments</a>, starting at 10.2 GB while <a rel="noreferrer noopener" aria-label="AWS shows traditional increments (opens in a new tab)" href="https://aws.amazon.com/ec2/instance-types/" target="_blank">AWS shows traditional increments</a> of 8, 16, etc. So, yeah, it's a nitpick. But it was this exact item what caught my eye and made me dig deeper to fact check everything. Warrants mentioning. </p>



<p>"<strong>Thus, R4 seemed a suitable instance class to use for AWS RDS</strong>." - The authors explain why they chose R4 (memory optimized instance) versus the M4 (general purpose). I have no issue with this except that neither M5 or R5 was considered. This study just came out, why were those instances not considered? And since the authors went out of their way to tell us what AWS says about the R4, let me tell you what AWS also says about the R5:</p>



<blockquote class="wp-block-quote"><p>"R5 instances deliver 5% additional memory per vCPU than R4 and the largest size provides 768 GiB of memory. In addition, R5 instances deliver a 10% price per GiB improvement and a ~20% increased CPU performance over R4."</p></blockquote>



<p>I can't think of any reason why the authors chose R4 here. But let's move past this, because now is time for the hard part: finding a suitable match for Azure SQL Database.</p>



<p>"<strong>On the Azure side, we expect customers to gravitate towards SQL Database Business Critical (BC) offerings</strong>...” - Well, Azure doesn't offer a memory optimized version of SQL Database, so I guess using BC is fine. But the question I have now is why not consider using Managed Instance? In the <a rel="noreferrer noopener" aria-label="data warehouse benchmark study (opens in a new tab)" href="https://gigaom.com/report/data-warehouse-cloud-benchmark/" target="_blank">data warehouse benchmark study</a> they tried a variety of sizes against the workload. This study focused ONLY on one size machine. This is part of the reason they got a B-, they weren't thorough enough for my liking. I'd send them back and tell them to run more tests against different sized machines and include Managed Instance. At the very least they could have made an effort to simply use general purpose, it would have been closer to an apples-to-apples comparison. </p>



<p>"<strong>Therefore, we chose the BC_Gen5_80 instance, which has more CPUs than R4.16xlarge, but less memory at 408 GB</strong>." - Yes, finding an exact match is difficult. Here's a breakdown of what they chose:</p>



<figure class="wp-block-image"><a href="https://thomaslarock.com/wp-content/uploads/2019/10/image-3.png" target="_blank" rel="noreferrer noopener"><img src="https://i0.wp.com/thomaslarock.com/wp-content/uploads/2019/10/image-3.png?fit=553%2C600&amp;ssl=1" alt="" class="wp-image-19665"/></a></figure>



<p>But this image shows AWS at 64,000 provisioned IOPS, and further in the study they say they tested against 32,000 provisioned IOPS. So, which is it? I've no idea. Neither do you. But I do know that provisioning 32,000  IOPS added about $6k to the monthly bill. </p>



<p>"...<strong>the monthly cost of Microsoft Azure comes to $40,043.71. The monthly cost for AWS comes to $65,239.43.</strong>" - Verified, I can get the same prices using the <a rel="noreferrer noopener" aria-label="AWS (opens in a new tab)" href="http://calculator.s3.amazonaws.com/index.html" target="_blank">AWS</a> and <a rel="noreferrer noopener" aria-label="Azure (opens in a new tab)" href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank">Azure</a> calculators. But the small detail that is glossed over here is single versus multi-zone. The AWS calculator is clear, if you deploy multi-zone, the price doubles. The Azure calculator doesn't have this option, it only exists when you create your SQL Database. I'd be shocked to find out that deploying multi-zone in Azure didn't bump the price as well. But the chart above clearly states "in a single availability zone". So, which is it? </p>



<p>I've no idea. Neither do you.</p>



<h2>Summary</h2>



<p>Some quick math tells me that if we drop the multi-zone from AWS RDS the price/performance result comes in at $1,269.85, slightly cheaper than the $1,410.04 for SQL Database. And this is why I like price/performance as a metric. A database service may have a slightly higher price, but offers greater throughput. </p>



<p>This was the exact conclusion from the data warehouse study, too. The cost for Azure SQL Data Warehouse was just a tad more than AWS Redshift, but the performance with Azure was better. I wanted to see a similar conclusion in this study. </p>



<p>Instead, we have a report with a handful of inaccuracies. Perhaps in an effort to rush to publish ahead of Ignite, they simply used a wrong graph, or missed doing one final round of edits. When you are doing this work it is easy to have such things fall through the cracks. </p>



<p>I'd love to see this study republished without these errors. I'd also love for AWS and Azure to find a way to make it easier to compare costs and services. </p>



<h2>REFERENCES:</h2>



<p><a rel="noreferrer noopener" href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank">Azure vs. AWS Data Services Comparison</a><br><a rel="noreferrer noopener" aria-label="Updated Data Services Comparison: AWS vs. Azure (opens in a new tab)" href="https://thomaslarock.com/2019/05/updated-data-services-comparison-aws-vs-azure/" target="_blank">Updated Data Services Comparison: AWS vs. Azure</a><br><a rel="noreferrer noopener" href="https://thomaslarock.com/2018/03/azure-vs-aws-analytics-and-big-data-services-comparison/" target="_blank">Azure vs AWS Analytics and Big Data Services Comparison</a><br><a rel="noreferrer noopener" aria-label="Updated Analytics and Big Data Comparison: AWS vs. Azure (opens in a new tab)" href="https://thomaslarock.com/2019/05/updated-analytics-and-big-data-comparison-aws-vs-azure/" target="_blank">Updated Analytics and Big Data Comparison: AWS vs. Azure</a><br><a rel="noreferrer noopener" aria-label="Azure SQL Data Warehouse Costs vs AWS Redshift (opens in a new tab)" href="https://thomaslarock.com/2018/03/azure-sql-data-warehouse-costs-vs-aws-redshift/" target="_blank">Azure SQL Data Warehouse Costs vs AWS Redshift</a><br><a rel="noreferrer noopener" href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank">Azure pricing calculator</a><br><a rel="noreferrer noopener" href="http://calculator.s3.amazonaws.com/index.html" target="_blank">AWS pricing calculator</a><br><a rel="noreferrer noopener" aria-label="Amazon EC2 Instance Types (opens in a new tab)" href="https://aws.amazon.com/ec2/instance-types/" target="_blank">Amazon EC2 Instance Types</a><br><a rel="noreferrer noopener" aria-label="Sizes for Windows virtual machines in Azure (opens in a new tab)" href="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes" target="_blank">Sizes for Windows virtual machines in Azure</a><br><a rel="noreferrer noopener" aria-label="Azure SQL Database pricing (opens in a new tab)" href="https://azure.microsoft.com/en-us/pricing/details/sql-database/managed/" target="_blank">Azure SQL Database pricing</a><br><a rel="noreferrer noopener" aria-label="Data Warehouse in the Cloud Benchmark (opens in a new tab)" href="https://gigaom.com/report/data-warehouse-cloud-benchmark/" target="_blank">Data Warehouse in the Cloud Benchmark</a><br><a rel="noreferrer noopener" aria-label="SQL Transactional Processing Price-Performance Testing
 (opens in a new tab)" href="https://azure.microsoft.com/en-us/resources/sql-transactional-processing-price-performance-testing/" target="_blank">SQL Transactional Processing Price-Performance Testing<br></a></p>



<p></p>