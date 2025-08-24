---
layout: post
title: The Server Draft
date: '2016-04-28 13:13:25 +0000'
categories:
- Database Design
- MSSQL
- SQL Server Performance
tags:
- CPU
- disk
- memory
- network
- server
- Things I Write While High on Bacon
- Things Only I Find Amusing
---

<a href="https://thomaslarock.com/wp-content/uploads/2016/04/draft_server.jpg"><img class="alignleft wp-image-17364 size-medium" src="https://thomaslarock.com/wp-content/uploads/2016/04/draft_server-420x315.jpg" alt="This is still a better pick than Ryan Leaf." width="420" height="315" /></a>Years ago <a href="http://www.nba.com/celtics/history/red-auerbach" target="_blank">Red Auerbach</a> was asked which player he would draft first, <a href="http://www.biography.com/people/bill-russell-9467384" target="_blank">Bill Russell</a> or <a href="http://www.nba.com/celtics/history/legends/larry-bird" target="_blank">Larry Bird</a>. Red thought it over and decided that Russell was the better choice because "he would get you the ball". Then, after thinking a bit more about this decision, <a href="http://espn.go.com/sportsnation/boston/halloffame/jersey?id=6857227" target="_blank">Red added "then I'd trade for Bird"</a>.

Tonight is the <a href="http://www.nfl.com/draft/2016" target="_blank">NFL draft</a>. There has been a lot of data analysis over the last few months, even years, regarding the selections that will be made tonight. For teams on top of the NFL, tonight is their night to make an effort to pick players that help them to stay on top. For the teams on the bottom (hello <a href="http://www.clevelandbrowns.com/" target="_blank">Cleveland</a>!) tonight is a night for them to rebuild everything.

And that brings me to the thought I had today regarding drafts, and rebuilding.

If you were given the chance to build the ultimate server, what would you draft first? I don't care if you want to run Linux, Unix, or Windows, every server and O/S has the same constraints: network, memory, disk, and CPU.

So, which one would you draft first?

I know lots of data experts who make a living off of configuring disk and storage networks. They will tell you that the secret to performance is getting the fastest disks possible. These people are the <a href="http://espn.go.com/nfl/story/_/id/14462075/chip-kelly-released-philadelphia-eagles" target="_blank">Chip Kelly</a> of server performance. Every <a href="http://www.philadelphiaeagles.com/" target="_blank">Eagles</a> fan is nodding their head, and sobbing, right now.

I know folks that will throw RAM at every performance issue. They go out of their way to say that the secret to good performance is to load everything into memory as quickly as possible so that queries will run faster. These people are the <a href="http://www.rollingstone.com/culture/lists/the-15-worst-owners-in-sports-20141125/jerry-jones-dallas-cowboys-20141124" target="_blank">Jerry Jones</a> of server performance, people who throw money at a problem and never seem to buy their way to a proper solution.

Then there are those that insist everything depends upon the best and newest CPUs available. These people are the <a href="http://www.businessinsider.com/the-14-worst-business-practices-of-redskins-owner-daniel-snyder-2010-11" target="_blank">Dan Snyder</a> of server performance, always moving on to something they think is better than where they were but ultimately not going anywhere.

If I was tasked with drafting the parts for building the best server possible, my first pick would be used for the network. None of the above matter if you can't move the data through the pipe. This is why the <a href="http://www.patriots.com/" target="_blank">New England Patriots</a> with <a href="http://www.biography.com/people/bill-belichick-20967651" target="_blank">Bill Belichick</a> are the best team in the NFL (<a href="https://twitter.com/hashtag/freebrady" target="_blank">#FreeBrady</a>). They know how to assemble the pieces, and in the correct order.

Here's my server draft ranking, assuming money is not a factor:

1. Network
2. Disk
3. Memory
4. CPU

For a database server I may swap disk and memory but I'd want to know more about the specifics of the workload. And I haven't even brought into this discussion the financial aspects here. Same as with the NFL, you may find yourself going after hardware based as much on finance as performance.

What would be your server draft order? I'm thinking I should revisit this post in a few months and break it down a bit more, adding in specific hardware components and prices.