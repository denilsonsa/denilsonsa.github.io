---
layout: post
title: Gentoo Install - part 4 - The working system
lang: en
tags:
- Gentoo
- Linux
---

Ok, my Gentoo system is now working, and I'm using it. nVidia driver did not work, I am using "generic" `nv`. I must remember to submit a bug report.


Apache works, PHP works, MySQL is installed but I'm not using it… After some trouble, I could modify `mplayer` ebuild to make it play realmedia files without installing `realplayer` (see [my forum post](http://forums.gentoo.org/viewtopic-t-406800.html)).

There are some old bug reports that nobody bothered to fix:

  * [Bug 42410 - Does yafray really need to be a dependency of blender 2.32?](http://bugs.gentoo.org/show_bug.cgi?id=42410)
  * [Bug 54238 - vuescan-8.0.4.ebuild (New Package)](http://bugs.gentoo.org/show_bug.cgi?id=54238)

Now my system is stable, with 9 days of uptime, most things (or almost everything) works. I don't have gnome or KDE installed, although I have kdelibs and some gnome libs.

I've done `emerge -avuDN world` (update entire system) once. It updated glibc, gcc and lots of other packages. System survived this update with no problems. The bad side is needing to update 30 or 40 etc files when running `etc-update`.

Although everything was compiled specifically for my system, I do not notice any speedup (compared to my good and old Slack).

Some things I've not yet tested: scanner, digital camera, USB card-reader, printer. I guess some would give me some trouble.
