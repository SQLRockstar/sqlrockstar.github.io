---
layout: post
title: Why I’m Not Worried About Skynet
date: '2018-11-19 14:40:06 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- SQL MVP
---

I’m 98% confident if you ask three data scientists to define Artificial Intelligence (AI), you will get five different answers.

The field of AI research dates to the mid-1950s, and even earlier when you consider the work of Alan Turing in the 1940s. So, the phrase “AI” has lasted for 60+ years, or roughly the amount of time since the last Cleveland Browns championship.

My preference for a definition to AI is this one, from Elaine Rich in the early 1990s:

“The study of how to make computers do things which, at the moment, people do better.”

But there is also this quote from Alan Turing, in his effort to describe computer intelligence:

“A computer would deserve to be called intelligent if it could deceive a human into believing it was human.”

Here's my take.
<h1>Defining Artificial Intelligence</h1>
When I try to define AI, I combine the two thoughts:

“Anything written by a human that allows a machine to do human tasks.”

This, in turn, allows humans to find more tasks for machines to do on our behalf. Because we’re driven to be lazy.

Think about the decades spent finding ways to build better programs, and the automation of traditional human tasks. We built <a href="https://www.acieta.com/why-robotic-automation/robotic-solutions-industry/automotive-applications/" target="_blank" rel="noopener">robots to build cars</a>, <a href="http://store.irobot.com/default/robot-vacuum-roomba/" target="_blank" rel="noopener">vacuum our house</a>, and even <a href="https://www.dailymail.co.uk/sciencetech/article-4291376/Meet-Flippy-robot-cooks-perfect-burger.html" target="_blank" rel="noopener">flip burgers</a>.

It the world of IT, alerting is one example of where automation has shined. We started building actions, or triggers, to fire in response to alert conditions. We added triggers until we reached a point where human intervention was necessary. And then we would spend time trying to figure out a way to remove the need for a person.

This means if you ever wrote a piece of code with IF-THEN-ELSE logic, you’ve written AI. Any computer program that follows rule-based algorithms is AI. If you ever built code that has replaced a human task, then yes, you built AI.

But for many in the field of AI research, AI means more than simple code logic. It also means things like image recognition, text analysis, or a fancy “Bacon/Not-Bacon” app on your phone. AI also means talking robots, speech translations, and predicting loan default rates.

AI means so many different things to different people because AI is a <strong>very</strong> broad field. The field contains both Machine Learning and Deep Learning, as shown in this diagram:

<a href="https://thomaslarock.com/wp-content/uploads/2018/11/ai-venn.jpg"><img class="aligncenter size-large wp-image-19398" src="https://thomaslarock.com/wp-content/uploads/2018/11/ai-venn-600x338.jpg" alt="why i'm not worried about skynet" width="600" height="338" /></a>

That’s why you can find one person who thinks of AI as image classification, but another person who thinks AI is as simple as a rules-based recommendation engine. So, let’s talk about those subsets of AI called Machine Learning and Deep Learning.
<h1>Machine Learning for Mortals</h1>
Machine Learning (ML) is a subset of AI. ML offers the ability for a program to apply statistical techniques to a dataset and arrive at a determination. We call this determination a <em>prediction</em>, and yes, this is where the field of predictive analytics resides.

The process is simple enough: you collect data, you clean data, you classify your data, you do some math, you build a model. This model is necessary to make predictions upon similar sets of data. This is how Netflix knows what movie you want to watch next, or how Amazon knows what additional products you would want to add to your cart.

But ML requires a human to provide the input. It’s a human task to define the features used in building the model. Humans are the ones to collect and clean the data used to build the model. As you can imagine, humans desire to shed themselves of some tasks that are better suited for machines, like determining if an image is a <a href="https://medium.freecodecamp.org/chihuahua-or-muffin-my-search-for-the-best-computer-vision-api-cbda4d6b425d" target="_blank" rel="noopener">chihuahua or a muffin</a>.

Enter the field of Deep Learning.
<h1>Deep Learning Demystified</h1>
The first rule of Deep Learning (DL) is this: You don’t need a human to input a set of features. DL will identify features from large sets of data (think hundreds of thousands of images) and build a model without the need for any human intervention <em>thankyouverymuch</em>. Well, sure, <strong>some</strong> intervention is needed. After all, it’s a human that will need to collect the data, in the example above some pictures of chihuahuas, and tell the DL algorithm what each picture represents.

But that’s about all the human needs to do for DL. Through the use of <a href="https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8" target="_blank" rel="noopener">Convoluted Neural Networks</a>, DL will take the data (an image, for example), break it down into layers, do some math, and iterate through the data over and over to arrive at a predictive model. Humans will adjust the iterations in an effort to tune the model and achieve a high rate of accuracy. But DL is doing all the heavy lifting.

DL is how we handle image classifications, handwriting recognition, and speech translations. Tasks once suited for humans are now reduced to a bunch of filters and epochs.
<h1>Summary</h1>
Before I let you go, I want to mention one thing to you: beware companies that market their tools as being “predictive” when they aren’t using traditional ML methods. Sure, you can make a prediction based upon a set of rules; that’s how <a href="http://www-03.ibm.com/ibm/history/ibm100/us/en/icons/deepblue/" target="_blank" rel="noopener">Deep Blue</a> worked. But I prefer tools that use statistical techniques to arrive at a conclusion.

It’s not that these companies are knowingly lying, it’s just that they may not know the difference. After all, the definitions for AI are muddy at best, so it is easy to understand the confusion. Use this post as a guide to ask some probing questions.

As an IT pro, you should consider use cases for ML in your daily routine. The best example I can give is the use of linear regression for capacity planning. But ML would also help to analyze logs for better threat detection. One caveat though: if the model doesn’t include the right data due to a specific event not observed, then the model may not work as expected.

That’s when you realize that the machines are only as perfect as the humans that program them.

And this is why I’m not worried about <a href="http://terminator.wikia.com/wiki/Skynet" target="_blank" rel="noopener">Skynet</a>.