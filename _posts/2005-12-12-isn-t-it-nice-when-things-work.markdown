---
layout: post
title: Isn't it nice when things work?
lang: en
tags:
- Gentoo
- Linux
- USB
- Nvidia
---

I've updated my kernel to latest (2.6.14.2) and also disabled in-kernel alsa drivers to install external alsa drivers (from `alsa-driver` package). This solved my problem with deadlock. (just in case someone wanna look at bug report: [115333](http://bugs.gentoo.org/show_bug.cgi?id=115333))


Now I have alsa, alsa works, I can have full 5.1 surround.

I also have CUPS working. Configuring my USB printer in CUPS was a piece of cake, I had no problems.

Scanner is also working. And I did nothing to make it work, just plugged it to USB and started [vuescan](http://www.hamrick.com/vsm.html). It was the first real plug-and-play device I used.

My USB multi-card reader also works fine. Whenever a card is not recognized, I should just unplug and plug it again to USB, then it works.

The only two pieces of hardware that still don't work are camera (using gphoto2) and nVidia GeForce 5500FX.
