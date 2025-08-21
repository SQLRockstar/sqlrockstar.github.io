---
layout: post
title: Quantum Computing Will Put Your Data at Risk
date: '2018-12-06 13:26:54 +0000'
categories:
- Cloud Computing
- SQL MVP
tags:
- quantum computing
---

“<em>Too many secrets</em>.” – Martin Bishop

One of the pivotal moments in the movie <a href="https://www.imdb.com/title/tt0105435/" target="_blank" rel="noopener">Sneakers</a> is when Martin Bishop realizes that they have a device that can break any encryption methodology in the world.

Now 26 years old, the movie was ahead of its time. You might even say the movie predicted quantum computing. Well, at the very least, the movie predicts what is about to unfold as a result of quantum computing.

Let me explain, starting with some background info on quantum computing.

&nbsp;
<h1>Quantum computing basics</h1>
To understand quantum computing, we must first look at how traditional computers operate. No matter how powerful, standard computing operates on binary units called “bits.” A bit is either a 1 or a 0, on or off, true or false. We’ve been building computers based on that architecture for the past 80 or so years. Computers today are using the same bits that <a href="https://blogs.scientificamerican.com/guest-blog/how-alan-turing-invented-the-computer-age/" target="_blank" rel="noopener">Turing invented to crack German codes in World War II</a>.

That architecture has gotten us pretty far. (In fact, to the moon and back.) But it does have limits. Enter quantum computing, where a bit can be a 0, a 1, or a 0 and a 1 at the same time. Quantum computing works with logic gates, like classic computers do. But quantum computers use quantum bits, or qubits. With one qubit, we would have a matrix of four elements: {0,0}, {0,1}, {1,0}, or {1,1}. But with two qubits, we get a matrix with 16 elements, and at three qubits we have 64. For more details on qubits and gates, check out this post: <a href="https://towardsdatascience.com/demystifying-quantum-gates-one-qubit-at-a-time-54404ed80640?gi=a778331cc23a" target="_blank" rel="noopener">Demystifying Quantum Gates—One Qubit At A Time</a>.

This is how quantum computers outperform today’s high-speed supercomputers. This is what makes solutions to complex problems possible. Problems today’s computers can’t solve. Things like predicting weather patterns years in advance. Or comprehending the intricacies of the human genome.

Quantum computing brings these insights, out of reach today, into our grasp.

It sounds wonderful! What could go wrong?

Hold that thought.

&nbsp;
<h1>Quantum Supremacy</h1>
Microsoft, Google, and IBM all have working quantum computers available. There is some discussion about capacity and accuracy, but they exist.

And they are getting bigger.

At some point in time, quantum computers will outperform classical computers at the same task. This is called “Quantum Supremacy.”

The following chart shows the linear progression in quantum computing for the past 20 years.

<a href="https://thomaslarock.com/wp-content/uploads/2018/12/quantum.jpg"><img class="aligncenter size-large wp-image-19413" src="https://thomaslarock.com/wp-content/uploads/2018/12/quantum-600x421.jpg" alt="quantum computing" width="600" height="421" /></a>
<p style="text-align: center;">(SOURCE: <a href="https://www.futuregrasp.com/quantum-supremacy-is-near" target="_blank" rel="noopener">Quantum Supremacy is Near</a>, May 2018)</p>
There is some debate about the number qubits necessary to achieve Quantum Supremacy. But many researchers believe it will happen within the next eight years.

So, in a short period of time, quantum computers will start to unlock answers to many questions. Advances in medicine, science, and mathematics will be within our grasp. Many secrets of the Universe are on the verge of discovery.

And we are not ready for everything to be unlocked.

&nbsp;
<h1>Quantum Readiness</h1>
Quantum Readiness is the term applied to define if current technology is ready for quantum computing impacts. One of the largest impacts to everyone, on a daily basis, is encryption.

Our current encryption methods are effective due to the time necessary to break the cryptography. But quantum computing will reduce that processing time by an order of magnitude.

In other words, in less than ten years, everything you are encrypting today will be at risk.

Everything.

Databases. Emails. SSL. Backup files.

<strong>All of our data is about to be exposed.</strong>

Nothing will be safe from prying eyes.

&nbsp;
<h1>Quantum Safe</h1>
To keep your data safe, you need to start using cryptography methods that are “Quantum-safe.”

There’s one slight problem—the methods don’t exist yet. Don’t worry, though, as we have "<a href="https://www.youtube.com/watch?v=yoy4_h7Pb3M" target="_blank" rel="noopener">top men</a>" working on the problem right now.

The <a href="https://openquantumsafe.org/" target="_blank" rel="noopener">Open Quantum Safe Project</a>, for example, has some promising projects underway. And if you want to watch mathematicians go crazy reviewing research proposals during spring break, the <a href="http://www.math.fau.edu/pqcrypto2018/" target="_blank" rel="noopener">PQCrypto conference</a> is for you.

Let’s assume that these efforts will result in the development of quantum-safe cryptography. Here are the steps you should be taking now.

First, <strong>calculate the amount of time necessary to deploy new encryption methods throughout your enterprise</strong>. If it takes you a year to roll out such a change, then you had better get started at least a year ahead of Quantum Supremacy happening. Remember, there is no fixed date for when that will happen. Now is your opportunity to take inventory of all the things that require encryption, like databases, files, emails, etc.

Second, <strong>review the requirements around your data retention policies</strong>. If you are required to retain data for seven years, then you will need to apply new encryption methods on all of that older data. This is also a good time to make certain that data older than your policy is deleted. Remember, you can’t leave your data lying around—it will be discovered and decrypted. It’s best to assume that your data will be compromised and treat it accordingly.

One thing worth mentioning is that some data, such as emails, are (possibly) stored on the servers they touch as they traverse the internet. We will need to trust that those responsible for the mail servers are going to apply new encryption methods. Security is a shared responsibility, after all. But it’s a reminder that there are still going to be things outside your control. And maybe reconsider the data that you are making available and sharing in places like private chat messages.

&nbsp;
<h1>Summary</h1>
Don’t wait until it’s too late. Data has value, no matter how old. Just look at the spike in phishing emails recently, <a href="https://www.businessinsider.com/new-email-scam-uses-old-password-fake-porn-threats-webcam-video-bitcoin-2018-7" target="_blank" rel="noopener">where they show you an old password and try to extort money</a>. Scams like that work, because the data has value, even if it is old.

Start thinking how to best protect that data. Build yourself a readiness plan now so that when quantum cryptography happens, you won’t be caught unprepared.

Otherwise…you will have no more secrets.