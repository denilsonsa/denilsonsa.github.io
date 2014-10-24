---
layout: post
title: Gentoo, the feature-less system
lang: en
tags:
- Gentoo
- Linux
---

Once I had Slackware 9.0, with 2.4 kernel, XFree86 4.3 and OSS (Open Sound System, also known as Old Sound System). Once I could listen sound and music, I could run OpenGL applications and games with decent framerates, I could use a second monitor on my GeForce 5500 FX.


Once, everything just worked. Once, I was happy and didn't notice.

Today, I have Gentoo, with 2.6 kernel, X.org 6.8.2 and ALSA (Advanced Linux Sound Architecture). Today, aplay/alsa causes a deadlock that mutes all sound, and leaves dozens of locked processes that won't die. Today, nvidia driver crashes and trashes my (single) monitor display, leaving my computer at unusable state for a desktop. Today, nv driver does not crash, but also does not use the expensive 3D hardware acceleration, and even OpenGL xscreensaver hacks are slow.

Today… hum… Today I hope a better tomorrow. And I hope it soon.

P.S.: People may think I don't like Gentoo. In fact, I want to like it, but it just don't want to work. In addition, I understand the alsa-related deadlock can happen with any distro with my emu10k1 sound card, since this is a bug in alsa/kernel drivers, and not a Gentoo-specific bug.
