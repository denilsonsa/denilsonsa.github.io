---
layout: post
title: nVidia (driver) strikes back (again)
lang: en
tags:
- X.org
- Linux
- Nvidia
- Gentoo
- driver
---

This is not the first time I post here a problem related to nVidia binary driver on my system. Neither this is the second time. Neither the third… Well, I could even rename my blog to "Crazy nVidia bugs".


Recently, [nvidia-drivers-100.14.09 has been marked stable in Gentoo](http://packages.gentoo.org/packages/?category=x11-drivers;name=nvidia-drivers). I looked at that and thought to myself: _"Wtf? What is this weird version number? Hum, maybe a whole new development branch? Maybe a code rewrite? I don't like the way it looks, I predict it might be buggy."_

Unfortunately, it **is** buggy.

The new bug is: when exiting X and returning to text-mode console, sometimes the screen goes black. When this happens, I can't see what's written on console, but I still can use it (I could hear some beeps when pressing some keys, and I managed to startx again). I tried to ssh into this machine, and I found nothing strange, no process was eating lots of CPU (like what happens with that X.Org-freezing bug, described in many previouos posts here).

I've added a bug report at [Gentoo Bugzilla](http://bugs.gentoo.org/). It is [bug #186596](http://bugs.gentoo.org/show_bug.cgi?id=186596).

I've also sent some e-mails to nVidia Linux bug report address. I got a very quick response telling me that 100.14.09 version is no longer supported, and asking me to test 100.14.11. I did, and the bug is present in both versions.

If you wanna keep track of this issue, watch [bug #186596](http://bugs.gentoo.org/show_bug.cgi?id=186596). But, for now, I'm masking 100.14.09 and 100.14.11 versions and I'm going to use 1.0.9639 version.
