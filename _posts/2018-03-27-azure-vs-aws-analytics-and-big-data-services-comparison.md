---
layout: post
title: Azure vs. AWS Analytics and Big Data Services Comparison
date: '2018-03-27 11:43:57 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- MSSQL
- SQL MVP
---

Last week I <a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">wrote a post that helped visualize the different data services</a> offered by Microsoft Azure and Amazon AWS. This week I'm writing about the Azure vs. AWS Analytics and big data services comparison. This comparison took a bit longer because there are more services offered here than data services. Making the chart was also challenging. Because both Microsoft and Azure offer so many wonderful analytics and big data services, it was hard to fit them all on one page.

Just like last week I made a cheat sheet to help make sense of all the services offered. It is my hope that this post will be a starting guide for you when you need to research these analytic services. I have included relevant links for each service, along with some commentary, in the text of this post below. I’ve done my best to align the services, but there is some overlap between offerings. (Click image to embiggen)

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/03/AWSvAzureBigDataServices.jpg"><img class="aligncenter size-large wp-image-18852" src="https://thomaslarock.com/wp-content/uploads/2018/03/AWSvAzureBigDataServices-600x168.jpg" alt="Azure vs AWS analytics and big data services comparison" width="600" height="168" /></a>

&nbsp;

OK, let’s break these down into their respective groups. I’m not going to do a feature comparison here because these systems evolve so quickly I’d spend all day updating the info. Instead, you get links to the documentation for everything and you can do your own comparisons as needed. I will make an effort to update the page as frequently as I am able.

&nbsp;
<h2>Data Warehouse</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/sql-data-warehouse/" target="_blank" rel="noopener">SQL Data Warehouse</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/redshift/" target="_blank" rel="noopener">Redshift</a>

It feels like these two services have been around forever. That’s because, in internet years, they have. Redshift goes back to 2012, and SQL DW goes back to 2009. That’s a lot of time for both Azure and AWS to learn about data warehousing as a service.

&nbsp;
<h2>Data Processing</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/hdinsight/" target="_blank" rel="noopener">HDInsight</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/emr/" target="_blank" rel="noopener">Elastic MapReduce</a>

Both services are built upon Hadoop, and both are built to hook into other platforms such as Spark, Storm, and Kafka.

&nbsp;
<h2>Data Orchestration</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/data-factory/" target="_blank" rel="noopener">Data Factory</a>, <a href="https://azure.microsoft.com/en-us/services/data-catalog/" target="_blank" rel="noopener">Data Catalog</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/data-pipeline/" target="_blank" rel="noopener">Data Pipeline</a>, <a href="https://aws.amazon.com/glue/details/" target="_blank" rel="noopener">AWS Glue</a>

These are true enterprise-class ETL services, complete with the ability to build a data catalog. Once you try these services you will never BCP data again.

&nbsp;
<h2>Data Analytics</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/stream-analytics/" target="_blank" rel="noopener">Stream Analytics</a>, <a href="https://azure.microsoft.com/en-us/services/data-lake-analytics/" target="_blank" rel="noopener">Data Lake Analytics</a>, <a href="https://azure.microsoft.com/en-us/services/data-lake-store/" target="_blank" rel="noopener">Data Lake Store</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/kinesis/" target="_blank" rel="noopener">Kinesis Analytics</a>

Last week I talked about how Cosmos DB was all-in-one billing for your NoSQL needs. Well, here is the AWS version, as their Kinesis is one service whereas for Azure you need three. I didn't list <a href="https://azure.microsoft.com/en-us/services/event-hubs/" target="_blank" rel="noopener">Event Hubs</a> here for Azure, but if you want to stream data you are likely going to need that service as well. (In other words, "Analytics" is an umbrella term, and is one of the most difficult things to compare between Azure and AWS).

&nbsp;
<h2>Data Visualization</h2>
Azure offerings: <a href="https://powerbi.microsoft.com/en-us/" target="_blank" rel="noopener">PowerBI</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/quicksight/" target="_blank" rel="noopener">QuickSight</a>

I saw some demos of QuickSight while at AWS re:Invent last fall, and it looks promising. It also looks to be slightly behind PowerBI at this point. Of course, we all know most people are still using Tableau, but that is a post for a different day.

&nbsp;
<h2>Search</h2>
Azure offerings: <a href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps?page=1&amp;search=Elasticsearch" target="_blank" rel="noopener">Elasticsearch</a>, <a href="https://azure.microsoft.com/en-us/services/search/" target="_blank" rel="noopener">Azure Search</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/elasticsearch-service/" target="_blank" rel="noopener">Elastisearch</a>, <a href="https://aws.amazon.com/cloudsearch/" target="_blank" rel="noopener">CloudSearch</a>

Elastisearch for both is just a hook to the Elastisearch open source platform. For Azure, you have to get that from their marketplace (that's what I link to because I can't find it anywhere else). One of the biggest differences I know between the services is the number of languages supported. AWS CloudSearch claims to support 34, and Azure Search claims to support 56.

&nbsp;
<h2>Machine Learning</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/machine-learning-studio/" target="_blank" rel="noopener">Machine Learning Studio</a>, <a href="https://azure.microsoft.com/en-us/services/machine-learning-services/" target="_blank" rel="noopener">Machine Learning Workbench</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/sagemaker/" target="_blank" rel="noopener">SageMaker</a>, <a href="https://aws.amazon.com/documentation/deeplens/" target="_blank" rel="noopener">DeepLens</a>

DeepLens isn't available yet, but I've got one on pre-order as an attendee gift from re:Invent last year. I enjoyed using Azure Machine Learning Studio during my data science certification journey last year. I'm currently using it for my big data certification, too. If I get a chance I will try SageMaker and do a comparison post in the future.

&nbsp;
<h2>Data Discovery</h2>
Azure offerings: <a href="https://azure.microsoft.com/en-us/services/data-catalog/" target="_blank" rel="noopener">Data Catalog</a>, <a href="https://azure.microsoft.com/en-us/services/data-lake-analytics/" target="_blank" rel="noopener">Data Lake Analytics</a>

AWS offerings: <a href="https://aws.amazon.com/documentation/athena/" target="_blank" rel="noopener">Athena</a>

Imagine a library without a card catalog and you need to find one book. That's what your data looks like right now. I know you won't believe this, but not all data is tracked or classified in any meaningful way. That's why services like Athena and Data Catalog exist.

&nbsp;
<h2>Pricing</h2>
Azure Pricing calculator: <a href="https://azure.microsoft.com/en-us/pricing/calculator/" target="_blank" rel="noopener">https://azure.microsoft.com/en-us/pricing/calculator/</a>

AWS Pricing Calculator: <a href="https://calculator.s3.amazonaws.com/index.html" target="_blank" rel="noopener">https://calculator.s3.amazonaws.com/index.html</a>

Same as last week, you will find it difficult to do an apples-to-apples comparison between services. Your best bet is to start at the pricing pages for each and work your way from there.

&nbsp;
<h2>Summary</h2>
I hope you find this page (<a href="https://thomaslarock.com/2018/03/azure-versus-aws-data-services-comparison/" target="_blank" rel="noopener">and this one</a>) useful for referencing the many analytic and big data service offerings from both Microsoft Azure and Amazon Web Services. I will do my best to update this page as necessary, and offer more details and use cases as I am able.

&nbsp;