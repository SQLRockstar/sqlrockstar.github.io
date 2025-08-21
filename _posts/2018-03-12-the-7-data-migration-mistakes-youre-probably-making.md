---
layout: post
title: The 7 Data Migration Mistakes You're Probably Making
date: '2018-03-12 11:07:35 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- Data
- data migration
- sql server
---

<a href="https://thomaslarock.com/wp-content/uploads/2013/02/datacenter1.jpg"><img class="aligncenter size-full wp-image-10176" src="https://thomaslarock.com/wp-content/uploads/2013/02/datacenter1.jpg" alt="" width="314" height="216" /></a>

We've all been there, sitting in our cubicle, trying to migrate data from one server to another. Most of the time everything works as expected. But sometimes data migrations don't work at all. That's because there is more to a data migration than just the data, or database. Being able to migrate schema and data between endpoints is but one part of an entire migration process.

Ask any data professional about mistakes they have witnessed on data migration projects and you'll get back a long list of items. I've put together the top 7 data migration mistakes (or missteps) I've witnessed through the years.

As always, you're welcome.

&nbsp;
<h2>Underestimating Time and Effort</h2>
Also filed under "failing to plan is planning to fail". Migration projects often involve a lot of different teams. Your project plan must account for the scope of applications and related objects involved. You might think "lift and shift" is an easy answer, but reality will tell you otherwise. With a plethora of upstream and downstream systems, coordinating all those different stakeholders will take time. And don't forget that moving the data itself takes time, too.

&nbsp;
<h2>Doing It All At Once</h2>
More than once I've seen migration projects stall because the teams tried to do too much at once. An example of this is a database migration and another team decides to deploy a bunch of code changes at the same time. This is often a disaster, as you can't unwind if the issue is with the code changes, the migration, the new hardware, etc.

&nbsp;
<h2>Migrating Junk Data</h2>
Migration projects are a great time to clean out your data closet and get rid of the data you don't need anymore. And by "get rid of", I mean "archive properly". Data lasts longer than code, treat it right. Don't just throw it away, or ignore it. But if you are doing a migration project take the time to evaluate the value of the data versus the volume you are migrating. Take the time to do some data quality checks and make certain it is correct prior to the migration.

&nbsp;
<h2>Not Understanding the Tools</h2>
There are a plethora of migration tools and techniques available these days. It is easy to be lulled into a false sense of security that your tools do everything you need. The most common issue is with dependencies. There are times when you think a migration is simple only to find that there is a dependent object you didn't think about, like a trigger. <a href="http://amzn.to/2FvJxwY" target="_blank" rel="noopener">I hate triggers</a>.

&nbsp;
<h2>Missing Performance Baselines</h2>
If you don't know how fast a query was prior to the migration, then you (and especially your users) have no idea how fast it should be after the migration is complete. Without a baseline, you are stuck guessing if there is a problem or not. This is one of the biggest hurdles to cloud migrations. You must have a performance expectation for when the migration is complete. And you set that expectation by collecting baselines prior to the migration.

&nbsp;
<h2>No Rollback Plan</h2>
As a production DBA, I was involved in thousands of deployments. I can count on one hand the number of times a change was rolled back. That's not me bragging saying that our change control process was near perfect That's me telling you that the rollback plans were a myth. We didn't rollback because the teams involved always wanted to keep moving forward. Instead, we would fix whatever was needed in production in order to have signoff. We would spend hours making fixes to deploy changes. And I would get frustrated thinking we should rollback to the previous stable version. At some point, you need to stop and rollback. (And, when you do, you'd better have a good backup.)

&nbsp;
<h2>Poor Validation Testing</h2>
When the migration is complete, and before you hand the database off for testing, you must perform validation checks. For example, you can build and run a script that checks the database views are returning results and not errors. You can compare a count of objects between the databases, and rowcounts, too. The users are likely to test for upstream and downstream processes, so make sure that is in the project plan.

&nbsp;
<h2>Summary</h2>
Look, data isn't perfect. Sometimes data migrations fail because the data itself is the issue. But the reality is that many failures are human mistakes that can be avoided.

Data is becoming so valuable it is a commodity. But data is worthless unless you know how to work with it effectively.

Data migrations allow you the opportunity to make your data better for your end users. The more committed you are to understanding your data, the more care you take during migration projects, the more value you and your company will have out of your data.