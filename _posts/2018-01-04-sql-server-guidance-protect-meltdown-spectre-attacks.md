---
layout: post
title: SQL Server Guidance to Protect Against Meltdown and Spectre Attacks
date: '2018-01-04 11:36:29 +0000'
categories:
- Data Security and Privacy
- SQL MVP
- SQL Server 2016
- SQL Server 2017
- SQL Server Performance
tags:
- meltdown
- spectre
- SQL Server 2016
- sql server 2017
- sql server security
---

<img class="aligncenter size-large wp-image-18489" src="https://thomaslarock.com/wp-content/uploads/2018/01/meltdown_spectre-600x333.png" alt="SQL Server Guidance to Protect Against Meltdown and Spectre Attacks" width="600" height="333" />

[UPDATE: I've written a related post on this topic that you may find useful: <a href="https://thomaslarock.com/2018/01/check-database-server-protected-meltdown-spectre/" target="_blank" rel="noopener">How to Check if Your Database Server Is Protected Against Meltdown and Spectre</a>]

You may have heard about the latest <a href="http://www.businessinsider.com/intel-chip-bug-meltdown-and-spectre-explained-2018-1" target="_blank" rel="noopener">security issues with CPUs that affect Intel, AMD, and ARM processors</a>. The attacks, named Meltdown and Spectre, were prompting DBAs around the globe to ask "how will this patch affect SQL Server performance". The answer is simple: We don't know for certain.

Today Microsoft released a <a href="https://support.microsoft.com/en-us/help/4073225/guidance-for-sql-server" target="_blank" rel="noopener">KB article to provide guidance</a> for SQL Server installations in response to the Meltdown and Spectre side-channel attacks. You should take the time to review that KB article. Here's what Microsoft has to say about performance:
<blockquote>Microsoft continues to do performance evaluation on the patched binaries. However, at the time of publication, Microsoft has not yet validated SQL Server performance with all microcode patches, nor has it validated performance in all Linux environments. Customers are advised to evaluate the performance of their specific application when applying patches. Please validate the performance impact of enabling microcode changes before deploying into a production environment. Microsoft will update this section with more information when it is available.</blockquote>
Translation: We have no idea right now if your performance will be worse after patching.

&nbsp;
<h2>Not everyone is at risk</h2>
But there is some good news, too. For example, if you are running on bare metal (no VMs), and you have no untrusted application logic on the server, and no untrusted SQL Server features (such as CLR), then you are likely fine for right now and there is no need to patch. The KB article lists out recommendations for users based upon scenarios such as bare metal, Azure VMs, and even for SQL Server on Linux.

And there is even more good news: these attacks only work if there is code, or malware, on your database server. It's not as if the attackers can magically scrape the contents of your RAM through the CPU without having the code present on your system. This post does a great job of <a href="http://www.bbc.com/news/technology-42564461" target="_blank" rel="noopener">explaining the details about what is needed</a>. That link also sheds some light onto who is likely to be using such attacks:
<blockquote>Even if an attacker did get access, they would get only "snippets" of data from the processor that could eventually be pieced together to reveal passwords or encryption keys, says cyber-security expert Alan Woodward, at the University of Surrey.

That means the incentive to use Meltdown or Spectre will at first probably be limited to those prepared to plan and carry out more complex attacks, rather than everyday cyber-criminals.</blockquote>
Translation: These attacks require more work on the backend to piece together the data they are scraping. Therefore, they are likely to attack systems where it is worth the risk.

&nbsp;
<h2>SQL Server Features at risk for Meltdown and Spectre</h2>
This is the list of SQL Server features you should check for immediately. If you are using any one of these, you need to review the mitigation steps provided in the KB article:

- SQL CLR assemblies
- R and Python packages running through the external scripts mechanism or run from the standalone R/Machine Learning studio on the same physical machine as SQL Server
- SQL Agent extensibility points running on the same physical machine as SQL Server (ActiveX scripts)
- Non-Microsoft OLE DB providers used in Linked Servers
- Non-Microsoft Extended Stored Procedures

I find the advice in the KB about migrating CLR code to T-SQL amusing. If you *could* do that, then you shouldn't have been using CLR in the first place. But I digress.

Here's my take on events this week: You shouldn't be afraid to patch your systems. It's 2018, and either you can deploy patches and updates with confidence, or you are doing it wrong.

Take the time this week to review your deployment process. Looks for ways to improve how you roll out patches. Embrace the use of automation to build a test environment, apply patches, and verify workload performance.

Take advantage of this situation to make your environment, and your team, better prepared for the next time.

Because there is always a next time.

[UPDATE: Allan Hirt (<a href="http://sqlha.com/blog/" target="_blank" rel="noopener">blog</a> | <a href="https://twitter.com/SQLHA" target="_blank" rel="noopener">@SQLHA</a>) has a nice summary on his blog titled <a href="http://sqlha.com/2018/01/04/no-good-terrible-processor-flaw-sql-server-deployments-nearly-everything-need-know/">The No Good, Terrible Processor Flaw and SQL Server Deployments – Nearly Everything You Need To Know</a>, you should go read this.]