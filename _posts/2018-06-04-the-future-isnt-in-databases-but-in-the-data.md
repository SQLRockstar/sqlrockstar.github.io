---
layout: post
title: The Future Isn’t In Databases, But In the Data
date: '2018-06-04 09:53:32 +0000'
categories:
- AWS
- Azure
- Data Analytics
- SQL Azure
- SQL MVP
tags:
- big data
- data analytics
- data science
---

<a href="https://www.theguardian.com/news/datablog/2012/mar/02/data-scientist" target="_blank" rel="noopener"><img class="aligncenter wp-image-19139 size-full" src="https://thomaslarock.com/wp-content/uploads/2018/06/data-science.jpg" alt="the future isn't in databases, it's in the data" width="460" height="276" /></a>

In the past year, you may have heard me mention my certificates from the Microsoft Professional Program. <a href="https://thomaslarock.com/2017/07/why-im-learning-data-science/" target="_blank" rel="noopener">One certificate was in Data Science</a>, the <a href="https://thomaslarock.com/2018/04/big-data-certification/" target="_blank" rel="noopener">other in Big Data</a>. I’m currently working on a third certificate, this one in Artificial Intelligence.

You might be wondering why a database guy would be spending so much time on data science, analytics, and AI. Well, I’ll tell you.

The future isn’t in databases, but in the data.

Let me explain why.

&nbsp;
<h2>Databases Are Cheap and Plentiful</h2>
Take a look at the latest <a href="https://db-engines.com/en/ranking">DB-Engines rankings</a>. You will find there are 343 distinct database systems listed, <a href="https://db-engines.com/en/ranking_categories" target="_blank" rel="noopener">138 of those are relational databases</a>. And I’m not sure it is a complete list, either. But it should help make my point: you have no idea which one of 343 database systems is the <span style="text-decoration: underline;"><em>right one</em></span>. It could be none of them. It could be all of them.

Sure, you can narrow the list of options by looking at categories. You may know you want a relational, or a key-value pair, or even a graph database. Each category will have multiple options, and it will be up to you to decide which one is the right one.

Decisions are made to go with whatever is easiest. And “easiest” doesn’t always mean “best.” It just means you’ve made a decision allowing the project to move forward.

Here’s the fact I want you to understand: <strong>Data doesn’t care where or how it is stored</strong>. Neither do the people curating the data. Nobody ever stops and says “wait, I can’t use that, it’s stored in JSON.” If they want (or need) the data, they will take it, no matter what format it is stored in to start.

And the people curating the data don’t care about endless debates on MAXDOP and NUMA and page splits. They just want their processing to work.

And then there is this #hardtruth - It’s often easier to throw hardware at a problem than to talk to the DBA.

&nbsp;
<h2>Technology Trends Over the Past Ten Years</h2>
Here's a handful of technology trends over the past ten years. These trends are the main technology drivers for the rise of data analytics during this timeframe.

<strong>Business Intelligence software</strong> – The ability to analyze and report on data has become easier with each passing year. The Undisputed King of all business analytics, Excel, is still going strong. Tableau shows no signs of slowing down. PowerBI has burst onto the scene in just the past few years. Data analytics is embedded into just about everything. You can even run R and Python through SQL Server.

<strong>Real-time analytics</strong> – Software such as Hadoop, Spark, and Kafka allow for real-time analytic processing. This has allowed companies to gather quality insights into data at a faster rate than ever before. What used to take weeks or months can now be done in minutes.

<strong>Data-driven decisions</strong> – Companies can use real-time analytics and enhanced BI reporting to build a data-driven culture. We can move away from “hey, I think I’m right, and I found data to prove me right” to a world of “hey, the data says we should make a change, so let’s make the change and not worry about who was right or wrong.” In other words, we can remove the human factor from decision making, and let the data help guide our decisions instead.

<strong>Cloud computing</strong> – It’s easy to leverage cloud providers such as Microsoft Azure and Amazon Web Services to allocate hardware resources for our data analytic needs. Data warehousing can be achieved on a global scale, with low latency and massive computing power. What once cost millions of dollars to implement can be done for a few hundred dollars and some PowerShell scripts.

&nbsp;
<h2>Technology Trends Over the Next Ten Years</h2>
Now, let’s look at a handful of current trends. These trends will affect the data industry for the next ten years.

<strong>Predictive analytics</strong> – Artificial intelligence, machine learning, and deep learning are just starting to become mainstream. AWS is releasing <a href="https://amzn.to/2Je1HbJ">DeepLens</a> this year. Azure Machine Learning makes it easy to deploy predictive web services. <a href="https://docs.microsoft.com/en-us/azure/machine-learning/service/quickstart-installation" target="_blank" rel="noopener">Azure Machine Learning Workbench</a> lets you build your own facial recognition program in just a few clicks. It’s never been easier to develop and deploy predictive analytic solutions.

<strong>DBA as a service</strong> – Every company making database software (Microsoft, AWS, Google, Oracle, etc.) is actively building automation for common DBA tasks. Performance tuning and monitoring, disaster recovery, high availability, low latency, auto-scaling based upon historical workloads, the lists go on. The current DBA role, where lonely people work in a basement rebuilding indexes, is ending, one page at a time.

<strong>Serverless functions</strong> – Serverless functions are also hip these days. Services such as <a href="https://ifttt.com/">IFTTT</a> make it easy for a user to configure an automated response to whatever trigger they define. <a href="https://azure.microsoft.com/en-us/services/functions/" target="_blank" rel="noopener">Azure Functions</a> and <a href="https://aws.amazon.com/lambda/" target="_blank" rel="noopener">AWS Lambda</a> are where the hipster programmers hang out, building automated processes to help administrators do more with less.

<strong>More chatbots</strong> – We are starting to see a rise in the number of chatbots available. It won’t be long before you are having a conversation with a chatbot playing the role of a DBA. The only way you’ll know it is a chatbot and not a DBA is because it will be a pleasant conversation for a change. Chatbots are going to put a conversation on top of the automation of the systems underneath. As new people enter the workforce, interaction with chatbots will be seen as the norm.

&nbsp;
<h2>Summary</h2>
There is a dearth of people able to analyze data today.

Data analytics is the biggest growth opportunity I see for the next ten years. The industry needs people to help collect, curate, and analyze data.

We also need people to build data visualizations. Something more than an unreadable pie chart. But I will save that rant for a different post.

We are always going to need an administrator to help keep the lights on. But as time goes on we will need fewer administrators. This is why I’m advocating a shift for data professionals to start learning more about data analytics.

Well, I’m not just advocating it, I’m doing it.