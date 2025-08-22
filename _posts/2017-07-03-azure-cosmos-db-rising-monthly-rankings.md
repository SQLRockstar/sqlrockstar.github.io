---
layout: post
title: Azure Cosmos DB Rising in Latest DB-Engines Monthly Rankings
date: '2017-07-03 12:04:31 +0000'
categories:
- Cloud Computing
- MSSQL
- SQL Azure
- SQL MVP
tags:
- Azure
- Cosmos DB
- database
- microsoft
- rankings
---

&nbsp;

The latest DB-Engines Database Rankings are available, and it shows that <a href="https://db-engines.com/en/ranking" target="_blank" rel="noopener">Microsoft continues to gain ground on Oracle/MySQL</a>:<a href="https://thomaslarock.com/wp-content/uploads/2017/07/db-engines.jpg"><img class="aligncenter size-large wp-image-17943" src="https://thomaslarock.com/wp-content/uploads/2017/07/db-engines-600x355.jpg" alt="" width="600" height="355" /></a>

I've been following the DB-Engines ranking for a few years and would encourage you to do the same. The rankings are not an exact science. You can <a href="https://db-engines.com/en/ranking_definition" target="_blank" rel="noopener">read for yourself how they are calculated</a>. One thing to note here is the selection bias in how they collect their data. The rankings show a clear preference for systems that have a lot of engagement online. It doesn't talk about revenue, the number of installations, or if the engagement online is negative or positive.

That means a system like DB2 or even the artist formerly known as Sybase doesn't have as much engagement online as MySQL. DB2 and SAP are ranked lower than the newer, hipster data platforms. But if you were to find a way to factor in things like revenue or licensing you might find those systems ranked a bit higher. Still, despite all of that, I do find some value in the overall trends.

It might also be interesting to note the number of exposed database platforms on the internet. A <a href="https://www.shodan.io/search?query=database" target="_blank" rel="noopener">quick search of Shodan</a> would show that PostgreSQL leads the way with Mongo DB being a distant second place:<a href="https://thomaslarock.com/wp-content/uploads/2017/07/shodan.jpg"><img class="aligncenter size-large wp-image-17944" src="https://thomaslarock.com/wp-content/uploads/2017/07/shodan-323x600.jpg" alt="" width="323" height="600" /></a>

I do wish the rankings would include the popularity of a system installed in an unsecured manner by default. But I digress...

One of the things I like most at the DB-Engines report is that it lists both relational (RDBMS) and non-relational (NoSQL) platforms. Even better, it offers a breakdown of all the systems, allowing for us to see the variety in the NoSQL world – document, graph, key-value, time series, object oriented, etc. This helps point out the deep variety of data platforms that exist for users. This also explains why it can be frustrating for a company to decide on one platform (say, SQL Server) only to find that a year later they need a piece of functionality that is best served by something else (say, a document store).

This also explains why we have systems listed as “multi-store”, such as Azure Cosmos Database. I’ve briefly <a href="http://mailchi.mp/47efba65c1f1/what-dbas-need-to-know-from-the-microsoft-build-announcements" target="_blank" rel="noopener">written about Cosmos DB</a> and I’ll share more thoughts on Cosmos DB in <a href="https://thomaslarock.com/is-not-null-newsletter/" target="_blank" rel="noopener">my next newsletter</a>. But for now, I wanted to show you that the DB-Engines rankings also offer a trend page. Here is the latest trend for multi-store systems:<a href="https://thomaslarock.com/wp-content/uploads/2017/07/db-engines-trend.jpg"><img class="aligncenter size-large wp-image-17945" src="https://thomaslarock.com/wp-content/uploads/2017/07/db-engines-trend-600x477.jpg" alt="" width="600" height="477" /></a>

Notice the recent spike for Azure Cosmos DB correlates nicely to the official launch announcement this past April. This is due to the rankings weighted towards product mentions online. But Cosmos DB (nee DocumentDB) has been rising for a while now. Cosmos DB is the 2nd ranked multi-store system. I would wager it will be the top system by the end of the year. Maybe even the end of Q3.

Bookmark the DB-Engine page for reference. It’s not perfect, but it is a nice guide as to how database systems are trending in the market.