---
layout: post
title: 'Designing a Database: 7 Things You Don''t Want To Do'
date: '2018-08-21 12:17:39 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- data quality
- database
- design
---

<a href="https://thomaslarock.com/wp-content/uploads/2013/01/corner.jpg"><img class="aligncenter wp-image-10036 size-full" src="https://thomaslarock.com/wp-content/uploads/2013/01/corner.jpg" alt="Designing a database" width="301" height="399" /></a>

Your database design is awful.

The reason nobody has told you this yet is for one of two reasons: ignorance or apathy. They either don't know it's bad, or they don't care.

Well *I* care about bad designs, as I typically bear the burden of having to make queries run fast and overcome the limits of the bad design. As a data professional for the past 15 years I have seen (and built) my share of database designs. Some are good, some are OK, but most make me want to stab someone with a paper clip shiv.

When I come across a design that is sub-optimal it makes me ask myself "what did this data do to deserve to be treated so poorly?" Data lasts longer than code and it should be treated accordingly.

In my continuing quest to help you respect your databases, I’d like to start today with pointing out where you are doing it wrong. You’ll thank me later.

Here are the seven things you don't want to do when designing a database.
<h2>Do It Yourself</h2>
Like dentistry, database design is something that is best left to a professional and not something you should do for yourself. I don't care if you are able to get one of those probes with a fancy mirror on the end, you should stop shoving sharp things in your mouth.

Just because you can do something doesn't mean you should. If you haven't designed a database before then don't make a mission-critical system your first project. Go out and hire an expert to help guide you.

I think this Dilbert sums it up rather nicely:

<a href="http://dilbert.com/dyn/str_strip/000000000/00000000/0000000/000000/20000/1000/100/21168/21168.strip.gif"><img class="alignleft size-full wp-image-10032" style="margin-right: 1000px;" src="https://thomaslarock.com/wp-content/uploads/2013/01/21168.strip_.gif" alt="21168.strip" width="640" height="194" /></a>
<h2></h2>
<h2>Have No Performance Expectations (or *no* expectations)</h2>
I've been involved in more than one project where there were no performance expectations at all. Well, not until we went live in production and it was "too slow". Without having ever defined an acceptable level of performance it was rather difficult to unwind a few months worth of work in order to get performance to an acceptable level. The end result was that we got a system deployed but nobody was happy with the process.

If you have not set any performance expectations then you should expect some headaches during the early stages of deployment. Likewise, if you have wild expectations for performance you should expect some disappointments especially if you haven't done any stress testing. Chances are the test system with ten rows of data is not a good indication of how the millions of rows in production will behave.

&nbsp;
<h2>Going Big, Just In Case</h2>
I often see data types being chosen as if they don't matter. But the truth is (despite everything you were told in college) <i>size matters</i>. If you know that the only possible values for a certain column are between 0 and 100,000 then you don't need to slap a BIGINT data type for that column when a INT would do just fine. Why does this matter? The BIGINT data type requires 8 bytes of storage, and the INT requires only 4 bytes of storage. That means for each row of data you could be wasting 4 bytes. Doesn't sound like much, right?

OK then, let's consider that your table has two million rows. Multiply those rows by 4 bytes and you have 8 million bytes, or roughly 7.8MB of wasted space. I know it doesn't sound like a lot, does it? Well, it adds up, and quickly. I've only shown you one example for just one column, but how about your date columns? if you don't have a need for calendar dates prior to the year 1900 or after the year 2079 then SMALLDATETIME is likely to work just fine for you. Oh, and let's not forget that these columns can be indexed, and those indexes will also be unnecessarily wider as well.

Choosing the right data type matters, for all sorts of reasons. Take the time and make an effort to get it right at the start.
<h2></h2>
<h2>Not Examining Foreign Keys As Part Of Your Indexing Strategy</h2>
I am assuming, of course, that you even have foreign keys defined. I've seen *many* databases that have little to no primary keys, foreign keys, or even any indexes defined. No, I don't know who would do such a thing either. But they're out there, and sooner or later you will find them, too.

Assuming you have FKs defined then you should be evaluating to see if it would make sense to add indexes to match those FK definitions. In some case, it will. In other cases, it won't. But you should make certain that this type of review is part of your overall design process.

In fact, that reminds me of another thing you don't want to be doing when designing a database...

&nbsp;
<h2>Indexing Every Column, or Indexing No Columns</h2>
Assuming you have set some realistic performance benchmarks then you are likely going to want to consider building some indexes. If you don't have any indexes defined then you are likely not concerned about performance at all anyway.

What I see most of the time are databases with too many indexes defined. This is usually the result of someone using an index tuning advisor tool but it can often be the case where it is due to someone reading a blog post that says "indexes are what you need" and they go about creating a dozen indexes in an effort to get one query to run faster.

While an index is wonderful to help you read data faster it adds overhead for every DUI statement (Delete, Update, Insert). Adding an index to every column in a table is likely to be a nightmare for any process that has data coming in to that table.
<h2></h2>
<h2>Forgetting About Data Quality</h2>
As a DBA I understood my role to be focused on recovery. If the system went down I needed to be able to recover the data, and fast. That was my primary focus. Database designers don't have to worry about the recovery of data (because that's my job) and instead they focus on the integrity of the data.

If you are designing a database then you need to make certain you have accounted for data quality. You simply cannot expect someone else to do that for you. Imagine if the DBA was expecting someone else to take care of recovering the data? Unfortunately I have worked with many systems that have had outages due to what was lovingly called "garbage in, garbage out". If you have built a system that relies on perfect data I am here to tell you that your system is going to fail one day, likely very soon.

There are many ways for you to enforce some type of data integrity. Normalization is one way. Another way is to deploy a service such as <a href="http://msdn.microsoft.com/en-us/library/ff877917.aspx">Data Quality Service</a>. This allows for you to enforce rules and constraints that help guarantee a certain level of data quality.
<h2></h2>
<h2>No Data Retention Or Archiving Strategy</h2>
I'm willing to bet that you have data older than seven years sitting on your disks right now. Seven years seems to be that mythical line in the sand that everyone says they need, no matter what the system. If you ask someone how long they need to keep records for any system the answer almost always comes back "seven years", even if the real answer is closer to seven weeks.

As a result systems get built with only one thing in mind: storing and preserving it in tables for all time. It is rare for someone to stand up and say "hey, maybe we could agree that data older than a year can be archived." Inevitably someone will respond with "that's fine, but if I need to run a report for the previous year you had better be able to get my data back within the hour."

If you are designing a database you need to spend the time finding out exactly how much data will be retained. Knowing that information is going to help you project performance expectations as you store more and more data.

That's my list of how I see good database ideas become bad database designs. If you find yourself doing any one of those seven things it is likely that over time your database design will become further and further away from ideal. Simply avoiding these seven things would keep your database from performance degradation over time.