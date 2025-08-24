---
layout: post
title: The Future of Monitoring
date: '2016-09-07 16:34:40 +0000'
categories:
- Cloud Computing
- Musings
- SQL MVP
tags:
- machine learning
- monitoring
- Predictive analytics
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/09/human-robot.jpg"><img class="size-medium wp-image-17488 alignleft" src="https://thomaslarock.com/wp-content/uploads/2016/09/human-robot-140x315.jpg" alt="The future of monitoring" width="140" height="315" /></a>The past two years I have noticed a development trend for monitoring tools. Vendors are starting to market their tools as using <a href="http://www.predictiveanalyticstoday.com/what-is-predictive-analytics/" target="_blank">predictive analytics</a> in order to make our workdays a bit easier. Many of these predictive analytic monitoring designs are based upon machine learning algorithms that have become readily accessible. <a href="http://whatis.techtarget.com/definition/machine-learning" target="_blank">Machine learning</a> (ML) is a great tool, it can offer amazing insights into large data sets fairly quickly, giving system administrators valuable information.

While that sounds fantastic to everyone (including me!), I am here to remind you that machine learning, by itself, has a slight flaw.

Machine learning is only as good as the data that it can consume. That data is a finite set, bounded by the human(s) that have been tasked with curation and cleansing of the data. Therefore, predictive analytic monitoring tools are only as good as the data they can access. That means that as an administrator I will still be blind to the things that are unknown, because ML has no way of knowing anything outside of the data it is fed.

Predictive analytic monitoring tools that rely on ML are going to be wonderful at helping administrators adjust their environments for optimal performance. ML is going to help system administrators manage workloads and squeeze every ounce of performance out of the available hardware. This is great stuff, and I'm looking forward to using these tools as they become available. But I also understand that these tools are not going to help predict when a developer is going to decide that today is the day they want to alter that index in the data warehouse and fill up the transaction log, or when an architect decides that they can store 30TB of data on a network share, or when everyone in the office decides that today is the day to play <a href="http://www.pokemongo.com/" target="_blank">Pokemon Go</a> and use up all the network bandwidth. As long as humans are part of the equation, the idea behind predictive analytic tools will remain slightly flawed.

It's this simple: machine learning won't fix stupid. This new wave of monitoring tools will help reduce sys admin headaches but what we really want is for our tools to reduce the amount of time we spend being reactive.

Enter <a href="http://searchcio.techtarget.com/definition/AI" target="_blank">Artificial Intelligence</a> (AI). What AI promises to do for us is to do the thinking that ML cannot. AI will make an effort to fill in the gaps in logic, make guesses, and eventually learn from its own mistakes. Think about <a href="http://www.ibm.com/watson/" target="_blank">IBM Watson</a> and now imagine Watson was the AI on top of your ML monitoring tool.

That's the future of monitoring.

It's a future where we use data to help predict future events and use AI to make the decisions that ML cannot.

It's a future where we let the machines talk to each other and not let humans near them (and we all know at least one person that we don't want touching our servers, ever.)

We are a long way from automating ourselves out of existence in the IT industry. And yet I feel that day will come sooner than we know. As we adopt Hybrid IT to be a standard for enterprise shops we start letting go of the traditional monitoring, alerting, and administrative tasks. Managing more with less is becoming easier. Backups, HA, DR...all done automatically for us through software defined policies and scripts we never see.

The new wave of predictive analytic monitoring tools is coming, and it's the first step towards building the monitoring systems of the future.

But the future will arrive only when AI is here. Until then, as long as there is a developer out there looking to fill up a transaction log drive, humans will be needed.