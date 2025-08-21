---
layout: post
title: No, You Don’t Need a Blockchain
date: '2018-11-01 14:11:57 +0000'
categories:
- Cloud Computing
- Data Security and Privacy
- Database Design
- SQL Azure
- SQL MVP
tags:
- blockchain
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/10/IMG_0323.jpg"><img class="aligncenter wp-image-19379 size-large" title="No, you don't need a blockchain" src="https://thomaslarock.com/wp-content/uploads/2018/10/IMG_0323-600x338.jpg" alt="No, you don't need a blockchain" width="600" height="338" /></a>

The hype around blockchain technology is reaching a fever pitch these days. Visit any tech conference and you’ll find more than a handful of vendors offering blockchain. This includes Microsoft, IBM, and AWS. Each of those companies offers a public blockchain as a service.

Blockchain is also the driving force behind cryptocurrencies, <a href="https://www.vice.com/en_us/article/5gq3ga/bitcoin-testimonials-black-market-dispatches">allowing Bitcoin owners to purchase drugs on the internet without the hassle of showing their identity</a>. So, if that sounds like you, then yes, you should consider using blockchain. A private one, too.

Or, if you’re running a large logistics company with one or more supply chains made up of many different vendors, and need to identify, track, trace, or source the items in the supply chain, then blockchain may be the solution for you as well.

Not every company has such needs. In fact, there’s a good chance you are being persuaded to use blockchain as a solution to a current logistics problem. It wouldn’t be the first time someone has tried to sell you a piece of technology software you don’t need.

Before we can answer the question if you need a blockchain, let’s take a step back and make certain we understand blockchain technology, what it solves, and the issues involved.
<h1>What is a blockchain?</h1>
The simplest explanation is a blockchain serves as a ledger. This ledger is a long series of transactions. And it uses cryptography to verify each transaction in the chain. Put another way, think of a very long sequence of small files. Each file based upon a hash value of the previous file, combined with new bits of data, and the answer to a math problem.

Put another way, blockchain is a database—one that is never backed up, grows forever, and takes minutes or hours to update a record. Sounds amazing!
<h1>What does blockchain solve?</h1>
Proponents of blockchain believe it solves the issue of data validation and trust. For systems needing to verify transactions between two parties, you would consider blockchain. Supply chain logistics is one problem people believe solved by blockchain technology. Food sourcing and traceability are good examples.

Other examples include <a href="https://www.insurancejournal.com/news/national/2018/09/27/502246.htm">Walmart requiring food suppliers to use a blockchain provided by IBM starting in 2019</a>. Another is Albert Heijn using blockchain technology along with the use of QR codes to <a href="https://thenextweb.com/hardfork/2018/09/21/albert-heijn-juicy-blockchain/">solve issues with orange juice</a>. Don’t get me started on <a href="https://amzn.to/2NXkX0h">the use of QR codes</a>; we can save it for a future post.
<h1>The problem with blockchain</h1>
Blockchain should make your system more trustworthy, but it does the opposite.

Blockchain pushes the burden of trust onto individuals adding transactions to the blockchain. This is how all distributed systems work. The burden of trust goes from a central entity to all participants. And this is the inherent problem with blockchain.

[Warrants mentioning - many cryptocurrencies rely on trusted third parties to handle payouts. So, they use blockchain to generate coins, but don’t use blockchain to handle payouts. Because of the issues involved around trust. Let that sink in for a moment.]

Here’s another issue with blockchain: data entry. In 2006, Walmart launched a system to help track bananas and mangoes from field to store, only to abandon the system a few years later. The reason? Because it was difficult to get everyone to enter their data. Even when data is entered, <strong>blockchain will not do anything to validate that the data is correct</strong>. Blockchain will validate the transaction took place but does nothing to validate the actions of the entities involved. For example, a farmer could spray pesticides on oranges but still call it organic. It’s no different than how I refuse to put my correct cell phone number into any form on the internet.

In other words, <strong>blockchain, like any other database, is only as good as the data entered</strong>. Each point in the ledger is a point of failure. Your orange, or your ground beef, may be locally sourced, but that doesn’t mean it’s safe. Blockchain could show the point of contamination, but it won’t stop it from happening.
<h1>Do you need a blockchain?</h1>
Maybe. All we need to do is ask ourselves a few questions.

<strong>Do you need a [new] database</strong>? If you need a new database, then you might need a blockchain. If an existing database or database technology would solve your issue, then no, you don’t.

Let’s assume you need a database. The next question: <strong>Do you have multiple entities needing to update the database</strong>? If no, then you don’t need a blockchain.

OK, let’s assume we need a new database and we have many entities needing to write to the database. <strong>Are all the entities involved known, and trust each other</strong>? If the answer is yes, then you don’t need a blockchain. If the entities have a third party everyone can trust, then you also don’t need a blockchain. A blockchain should remove the use of a third party.

OK, let’s assume we know we need a database, with multiple entities updating it, all trusting each other. The final question: <strong>Do you need this database distributed in a peer-to-peer network</strong>? If the answer is no, then you don’t need a blockchain.

If you have different answers, then a private or public blockchain may be the right solution for you.
<h1>Summary</h1>
No, you don’t need a blockchain.

Unless you do need one, but that’s not likely.

And it won’t solve basic issues of data validation and trust between entities. If we can trust each other, then we would be able to trust a central clearinghouse, too.

Don't buy a blockchain solution unless you know for certain you need one.

[<em>This article first appeared on <a href="https://orangematter.solarwinds.com/no-you-dont-need-a-blockchain/" target="_blank" rel="noopener">Orange Matter</a>. Head over there and check out the great content</em>.]

<a href="https://thomaslarock.com/wp-content/uploads/2018/11/CHANGE-MY-MIND.jpg"><img class="aligncenter size-full wp-image-19383" src="https://thomaslarock.com/wp-content/uploads/2018/11/CHANGE-MY-MIND.jpg" alt="" width="412" height="418" /></a>