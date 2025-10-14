---
layout: post
title: Using Templates With SQL Server Management Studio
date: '2015-01-22 13:39:33 +0000'
categories:
- Database Design
- MSSQL
- SQL MVP
tags:
- SSMS
- templates
---

I love learning new things. I feel like a kid again at times, my eyes get wide as I imagine new possibilities using whatever things it is I have found. This is how I felt last week when I came across a feature of SQL Server Management Studio (SSMS) that I had not seen before <em>despite it having existed since SQL 2005</em>.

Yeah, that's right, since 2005. Ten years. Ten long years of not knowing.

I'm not ashamed to admit that I don't know everything. And I bet there's someone reading this post (if not today, then <a title="Someday…" href="https://thomaslarock.com/someday/" target="_blank"><em>someday</em></a> they will) who never knew about this feature either.

The feature is embedded inside of the templates feature in SSMS. So let's start there, as I know this is also a little-used feature. You can access the templates with SQL Server Management Studio from the main menu, under View, like so:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/template_explorer1.png"><img class="aligncenter size-full wp-image-11971" src="https://thomaslarock.com/wp-content/uploads/2015/01/template_explorer1.png" alt="template_explorer" width="302" height="160" /></a>

Selecting "Template Explorer" will open up the Template Browser on the right-hand side of SSMS and reveal dozens of available templates for you to use:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/template_browser.png"><img class="aligncenter size-medium wp-image-11965" src="https://thomaslarock.com/wp-content/uploads/2015/01/template_browser.png" alt="template_browser" width="252" height="263" /></a>

I'm going to select "Extended property" because who doesn't love metadata, amirite? I will select "Add Extended Properties to Table" as you see here:
<a href="https://thomaslarock.com/wp-content/uploads/2015/01/extended_property.png"><img class="aligncenter size-medium wp-image-11964" src="https://thomaslarock.com/wp-content/uploads/2015/01/extended_property.png" alt="extended_property" width="247" height="54" /></a>

Doing so will open up the template in a new query window inside of SSMS. In this example what you should see is this:
<a href="https://thomaslarock.com/wp-content/uploads/2015/01/extended_property_template.png"><img class="aligncenter size-medium wp-image-11963" src="https://thomaslarock.com/wp-content/uploads/2015/01/extended_property_template-396x315.png" alt="extended_property_template" width="396" height="315" /></a>

This is where my day suddenly became full of awesome. I found out that I can specify the values for all of the parameters in the script and have them replaced automatically! Go to the Query menu and you will see this option:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/specify_values1.png"><img class="aligncenter size-full wp-image-11973" src="https://thomaslarock.com/wp-content/uploads/2015/01/specify_values1.png" alt="specify_values" width="440" height="142" /></a>

That will launch this dialogue box:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/input_values.png"><img class="aligncenter size-medium wp-image-11961" src="https://thomaslarock.com/wp-content/uploads/2015/01/input_values.png" alt="input_values" width="440" height="312" /></a>

And here is where I saw real value. I don't need to supply literal values here. I could put in variables instead. That means I could use these templates as a way to generate scripts to use for Powershell or SQLCMD (for those of us that still like it old-school).

And this is what the finished product looks like:

<a href="https://thomaslarock.com/wp-content/uploads/2015/01/template_completed.png"><img class="aligncenter size-medium wp-image-11960" src="https://thomaslarock.com/wp-content/uploads/2015/01/template_completed-207x315.png" alt="template_completed" width="207" height="315" /></a>

&nbsp;

Sometimes, it's the simple things in life, you know what I mean?

Enjoy!