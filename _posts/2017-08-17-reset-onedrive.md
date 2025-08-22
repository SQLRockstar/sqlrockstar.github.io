---
layout: post
title: How To Reset Your OneDrive
date: '2017-08-17 14:59:19 +0000'
categories:
- SQL MVP
tags:
- OneDrive
- reset
---

This post isn't really for you. It's for Future Tom. A note for me to find again when I need to reset OneDrive.

The other day OneDrive stopped working on my Surface Book. I bounce between my SB and my iMac throughout the day for various tasks. It was easy to see OneDrive had stopped because files weren't being synced with my iMac.

Digging into the issue on my SB I tried everything I could. Before I knew it, an hour had passed. I tried reinstalling. Unlinking. Nothing would work. OneDrive just kept crashing, saying there was an issue trying to connect.

With my old Surface Pro 2 I had a "fix it" tool for this scenario. But the tool was for Win 8.1, not Win 10. With OneDrive embedded in Win 10 it seemed there had to be a simple way to reset my OneDrive.

Turns out there is an easy way to reset your OneDrive, as long as you aren't afraid of a command line.

From the Run box (hit Windows + R to open the Run box) you will type:
<pre lang="DOS">%localappdata%\Microsoft\OneDrive\onedrive.exe /reset</pre>
This is what it should look like, hit OK (or press Enter):

<a href="https://thomaslarock.com/wp-content/uploads/2017/08/onedrive-reset.png"><img class="aligncenter wp-image-18015 size-medium" src="https://thomaslarock.com/wp-content/uploads/2017/08/onedrive-reset-541x315.png" alt="How to reset your onedrive" width="541" height="315" /></a>

The OneDrive cloud icon will disappear from your system tray. It *should* reappear in a few minutes. But, if you are like me, and a few minutes seems to be way too long, then just start it manually with this:
<pre lang="DOS">%localappdata%\Microsoft\OneDrive\onedrive.exe</pre>
<a href="https://thomaslarock.com/wp-content/uploads/2017/08/onedrive-start-1.png"><img class="aligncenter size-medium wp-image-18019" src="https://thomaslarock.com/wp-content/uploads/2017/08/onedrive-start-1-541x315.png" alt="How to reset your onedrive" width="541" height="315" /></a>When I run that command it opens up an explorer window with the focus on OneDrive, showing that folders are syncing. Also, the OneDrive cloud icon should be displayed and showing it is syncing.

That's it, Future Tom, how to reset your OneDrive.