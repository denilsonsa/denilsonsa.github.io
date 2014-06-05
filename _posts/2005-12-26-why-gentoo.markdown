---
layout: post
title: Why Gentoo?
excerpt: 'Today I found some pages about Gentoo and about the arguments people use to explain why to use Gentoo, so I stopped for a while and asked to myself: Why do I use Gentoo?'
lang: en
tags:
- Linux
- Gentoo
---

Today I found some pages about Gentoo, and about the arguments people use to explain why to use Gentoo:

* [GENTOO is Rice](http://www.funroll-loops.org/) ([Wayback Machine](http://web.archive.org/web/20051226113905/http://funroll-loops.org/))
* [Mandrake Expatriate Syndrome](http://greenfly.org/mes.html) ([Wayback Machine](http://web.archive.org/web/20051225044345/http://greenfly.org/mes.html))
* [Gentoo forum thread about www.funroll-loops.org](http://forums.gentoo.org/viewtopic-t-181330.html)

So, I stopped for a while and asked to myself: Why do I use Gentoo?


## History before Gentoo

My first experience with Linux was with some old Red Hat distro. Really old. From year 199x. :D

It was nice, but I was not really knowing what I was doing. It was cool, but I never did anything useful with it. I could run WindowMaker, FVWM, AfterStep… Just choosing from window manager menu. I could play some MP3, I could make two screenshots using Gimp. But I really did nothing more than that.

A lot of time later, in first half of 2003, I started using Linux again, this time for real. Windows was too bad. Too many crashes, loooooong startup time (more than 2 or 3 minutes). Then I installed [Slackware](http://www.slackware.com/) 9.0 and I had some friends helping me to learn more and more about Linux and Vi (thank you, Igor Correa and Cassio Neri!). Soon, I could install and configure a Slackware system, with X running, and also compiling a new kernel. My Slackware system could boot in less than 30 seconds (without X). When I moved it to another (faster) hard disk, the boot time took even less time (about 18 seconds, from pressing <enter> at LILO screen to getting a login prompt).

Since this, I never stopped using Linux anymore. Rebooting to start Windows became more and more rare, and, after some months, I never started Windows anymore. Because of Linux, I found also that I had a bad RAM chip. Using [memtest86](http://www.memtest86.com/) or [memtest86+](http://www.memtest.org/), I could discover there was a failing bit at position 213MB of RAM. Then, I modified lilo.conf to pass "mem=200m" as kernel parameter. This reduced the available memory, but also solved most of crashes (there were some other failing bits at random locations, at random times). Could I do something like that on Windows? No, I couldn't! Unless I (or someone) could write a low-level driver that could lock that RAM and no other process (or even kernel) could access it. No, I don't plan to write a low-level driver for Windows. So I stopped using it.

(enough history!)

## Why stop using Slackware?

Since 2003 until middle of 2005, my Slackware 9.0 system was not updated. Some weeks after I installed slack 9.0, the 9.1 version was released. I thought: "Damn, I've just installed 9.0, I don't want to reinstall it!"

By the second half of 2005, Slackware 10.2 was available. As you can notice, my installed slackware system was becoming really old. It had XFree86 4.3, 2.4 kernel with OSS, glibc 2.3.1 and GTK 2.2.

I thought: "My system is old, I must upgrade soon. But what to do? Try to upgrade the running stable slack 9.0 system, reinstall a newer slack, or try another distro?" Let's analyse the options:

1. **"upgrade the running stable slack 9.0"** - This is the first obvious solution. But then the following question arises: "How?"

    1. **using slackware tools for managing packages** - Damn, slackware package management is almost NULL. I once broke a Slack 8 system when I used its own tools to try to upgrade it to 9.0 (or 9.1). So, really this is not a solution.

    2. **using third-party tools** - I have some friends who updated their slackware systems using `slackpkg` or `swaret` tools. But how far can I trust them? I have another friend who tried to use one of them and, every time he tried, the slackware system became broken (in fact, the first thing those tools tried was to update glibc, and then everything froze). No, really this is not a solution, either.

    3. **update everything by hand** - Yes, I could `./configure && make && make install` all packages on my system, doing all updates by hand. However, I don't like this solution because it will require a lot of time to manually configure and install all software (and uninstall old software too), and there is also the risk of breaking something. I have a friend who updated the GTK and XFree from his slack 8.0 system to GTK 2.6 (I guess) and X.org, all by hand. He needed to find and download and compile and install all dependencies. And, after everything was done, there were some bugs, then he found he needed to recompile freetype with some options. He could finally got everything up and working, but I don't feel this is a feasible solution.

2. **"install a newer slack"** - I know how to do it, it is easy to do, but this is not a solution I want. If I install a new slackware, I will need also to reinstall all software I installed manually on my old slack (and they are too many to remember). In addition, this is not a solution in long-term. One or two years in future, I will need to update this "second" slackware install, and I will, again, ask to myself how to do it.

3. **"try another distro"** - Yes, I probably will install another distro. But which one?

    1. **[Mandrake/Mandriva](http://www.mandriva.com/)** - No way. Mandrake is not good. Too much problems, too much "dumb user". Just as Conectiva. It will give me more problems than solutions.

    2. **[Fedora](http://fedora.redhat.com/), or some other RPM-based distro** - Fedora is derived from Red Hat, and I don't like Red Hat. Not sure why, but I feel that RPM-based distros give too much problems. Another doubt I have is about how to upgrade from one version to another. Ok, there is package management, but how to upgrade from a major distro version to another? I know it is possible using those install CDs, but I never really investigated how to do it, and if it really works well. Since I don't like Fedora/RedHat/RPM-based distros, I never researched about this.

    3. **[Debian](http://www.debian.org/)** - Debian is cool. Debian is stable, and works. Debian configuration is also as low-level as slackware and gentoo (nothing of those GUI-configurators that fail often). Debian has a huge package repository, and updating it is not difficult. Debian is a really good candidate. However, most packages are old, Debian community is known by not being too much "friendly", and many packages are "customized" by debian, not having "default" configurations.

    4. **[Gentoo](http://www.gentoo.org/)** - And now Gentoo. How about it? It has a great package management system, a big and friendly community, packages aren't too much customized (there are some patches, though). I also have some good friends with Gentoo installed (this is important when I need to ask help or talk about something). The bad side: need to compile everything. This slows down the installation of any package. But I'm used to do it every time I installed a software on slackware, so, no problem. In addition, compiling everything is a good hardware test, and also allows users to tune each software according to his/her needs (the so famous USE flags).

There was one more cool thing about Gentoo: I can install it from my running system. So, the downtime will be minimal. I can continue using my slackware while gentoo is being installed on another partition. I have a friend who did that.

After all of these possible solutions, installing Gentoo was the choosen one.

## Installing Gentoo

I will skip this section.

## So, why Gentoo?

I got my Gentoo system up and running. Everything I need now is working. It wasn't too difficult. Sometimes, it was even easier than slackware (because of automated install using ebuilds and portage). Most programs I need are available at [portage](http://packages.gentoo.org), which is a repository as huge as [Debian's one](http://packages.debian.org/).

Am I satisfied with Gentoo? Yes. It is working.

Is it working fully? No, not really. gphoto2 still doesn't work, but I made no effort to solve this. nVidia driver also does not work, but this is a known bug, and looks like is a bug inside X.org. If this is true, then any distro can have this problem, not only Gentoo. (I never had it in slackware because it had XFree86, and the bug is believed to be introduced in X.org series) I also read somewhere that nVidia sent some patches to fix the X.org bug.

Besides gphoto2 (which I haven't even tried to solve) and nVidia driver problem, is this Gentoo system working fully? Yes, I guess yes. If something doesn't work, I can [fill a bug report](http://bugs.gentoo.org/) or post at [Gentoo Forums](http://forums.gentoo.org/) or ask at [#gentoo](irc://irc.freenode.net/gentoo). Of course, other distros probably have similar ways of solving problems.

What are the key features of Gentoo, for me?

* USE flags - For now, I don't have any samba machine nearby, no samba server and also don't plan to have one soon. So, I can just disable `samba` useflag and save me from the trouble of installing samba dependencies. I also know I can set the `samba` useflag whenever I want and recompile everything (with one or two commands) to enable samba. This is really a nice feature, and works.
* USE flags VS dependency hell - With Gentoo the dependency hell is not as hellish as with other distros. I don't want to have entire Gnome or KDE installed, and I can use and install most programs this way. I've also tried to install [gaim](http://gaim.sourceforge.net/), and it asked me to install dozens of packages, including almost the entire gnome plus evolution client. So I found `eds` (Evolution Data Server) useflag and disabled it. Now I have Gaim with only a few dependencies.
* Updates are easy (but not really fast) - It is easy to update the entire system. Since Gentoo does not have "releases", there is no "trouble" updating from a major Gentoo version to another. Gentoo does have, however, "profiles". Updating them is as easy as changing a symlink.
* Easy to customize - If I want a program that is not available at portage, or if I want to change the ebuild used in portage, I can do that easily. I just need to create a [portage overlay](http://gentoo-wiki.com/Portage_Overlay). Of course, some other distros have similar features (I hope so).
* Easy to understand how portage installs a software - If I just read the ebuild, I can understand what portage does to install any software, and can edit it (see previous item) or just learn from it.
* Excellent package management - [portage](http://www.gentoo-portage.com/) rocks! Of course other distros package management systems may rock too.

Is Gentoo better than other distros? No, there is not such concept of "better" distro. In addition, all distros use the same softwares. The distros "only" differ by the way these softwares are organized (as well as configuration files), how the package management works, booting scripts, and how some (smaller or bigger) things work.

Is Gentoo faster than other distros? I don't think so. My slackware system was already fast, I don't feel any improvement while using Gentoo. This so talked "optimized packages for each machine" argument is not 100% true. If there is a speed gain (which I could not feel) it is not that big.

What makes it different from other distros? **USE flags**. And also the fact it uses source-packages for almost everything.

In short: why I like Gentoo? **portage** rocks. **USE flags** rock. Installing and updating are easy. Packages aren't highly customized for the distro, like what happens with Red Hat, Fedora or Debian. Configuring it is as easy and as low-level as Slackware or Debian.
