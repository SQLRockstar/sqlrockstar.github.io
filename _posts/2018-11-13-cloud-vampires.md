---
layout: post
title: Cloud Vampires
date: '2018-11-13 15:18:20 +0000'
categories:
- AWS
- Azure
- Cloud Computing
- SQL MVP
- SQL Server Performance
tags:
- cloud
---

<a href="https://thomaslarock.com/wp-content/uploads/2018/11/cloud_vampire.jpg"><img class="aligncenter size-large wp-image-19393" src="https://thomaslarock.com/wp-content/uploads/2018/11/cloud_vampire-600x476.jpg" alt="cloud vampires" width="600" height="476" /></a>

I don’t want to alarm you, but your cloud is infested with vampires.

No, not the kind who wear fashionable cloaks. I’m talking about vampire resources. These are the cloud resources you’ve created but are no longer used. Over-provisioned VMs, orphaned disks, load balancers, and whatever else you forgot about.

These cloud vampires are costing you money. They are also difficult to find. Neither AWS nor Microsoft Azure provide default reports to help identify vampire resources. This should not be surprising, as it is not in their best interests to remind you to spend less.

&nbsp;
<h1>Cloud Vampire Resources</h1>
Here’s a list of resources you want to watch to bring vampire resources into the light of day.

<strong>Underutilized Virtual Machines</strong> – You built a VM according to the requirements. But the requirements were wrong. In the cloud you pay for resource consumption, disk storage, and network egress. Even using a minimal amount of VM capacity means you get billed the full amount for the hour. Either downsize or move that workload to a different VM.

<strong>Unused Virtual Machines</strong> – These are VMs that you built for Adam in Accounting a year ago and he’s never used. Or it’s a case of shadow IT, and employees are spinning up cloud VMs for their personal sandboxes. Even with these rogue VMs powered off you still pay for storage used by the VM disks, even when they are idle.

<strong>Orphaned Disks</strong> – You removed the virtual machine, but disks remained. This is by design, in case the VM removal was an accident. You’re paying for them, and there’s zero chance they are being used. Get rid of them.

<strong>Data Egress</strong> – The Cloud is like New Jersey—it’s free to get in, but you pay to get out. Your applications and systems should only pull data from the cloud when necessary. Too many extra API calls will lead to a bump in your monthly bill.

<strong>Geo-replication</strong> – Cloud resources often have options for automatic high availability and disaster recovery. Those services aren’t free. And they are not needed for every system. Check to make sure that systems using HA and DR need these options.

<strong>Load Balancing</strong> – Another HA feature that sounds great, but not needed by Developer Dan. You’ll want to review deployments of load balancers and ensure they are necessary.

<strong>Snapshots</strong> – Snapshots are a great way to rollback your VM in case an update goes awry. But don't keep those snapshot lingering around too long. The extra overhead leads to extra dollars from your budget.

<strong>Unused IP Addresses</strong> – You have an option to create static IP addresses for your VMs. But those IP addresses are distinct objects, separate from your VM. So if you stop your VM, you are still charged for that static IP address.

&nbsp;
<h1>Summary</h1>
I’ve listed some common vampire resources here. But this list is not meant to be comprehensive. It’s up to you to understand the cloud services you have deployed. You must track if they are in use, and the associated costs.

When transitioning workloads to the cloud, you must transition how you approach monitoring. Traditional methods of monitoring for outages and performance are not enough. You must also track resource usage, as well as use of cloud services.

And when you find cloud vampire resources, drive a stake through their heart. It’s the only way to be sure.