---
layout: post
title: Printing to a HP printer with CUPS
lang: en
tags:
- Gentoo
- Linux
- driver
---

This is a quick post just to document how I configured my HP 930C printer to print correctly (or almost correctly).


First, I had only CUPS installed, and I was using some generic CUPS-HP-Deskjet "driver". This was ok, until I tried to print some CD labels, and I found it was printed misaligned, and some milimeters smaller.

After hours testing, and lots of paper… I found the solution: `USE="cups foomaticdb ppds" emerge hpijs ; /etc/init.d/cups restart`

After the above command, I reconfigured CUPS using web interface, and I found dozens, maybe hundreds, of HP printers in model/driver list. I could also find my exact printer there. So I selected it, and finally could print my CD labels!

Some related links:

* [[Howto] HPLIP & CUPS - Gentoo Forums](http://forums.gentoo.org/viewtopic-t-365403.html)
* [HP Linux Printing Project (open source, hosted at sourceforge)](http://hpinkjet.sourceforge.net/)
* [HP Linux Printing Project - Sourceforge project page](http://sourceforge.net/projects/hpinkjet/)
* [LinuxPrinting.org CUPS Quick Start](http://www.linuxprinting.org/cups-doc.html) (maybe not very updated or not very useful)
* [LinuxPrinting.org](http://www.linuxprinting.org/)

P.S: Of course I did not pass the USE-flags at command-line. I added them to `/etc/portage/package.use`.
