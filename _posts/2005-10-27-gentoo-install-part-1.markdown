---
layout: post
title: Gentoo Install - part 1 - Stage1
lang: en
tags:
- Gentoo
- Linux
---

My computer is running Slackware 9.0. It is old, and almost all libraries need updates. Since I don't want to update my entire system "by hand", I thought that installing Gentoo would be easier, faster and would require less work.


Bad thought... Well, not really bad, but not good.

Two weeks ago, I started a Gentoo installation. I was installing it without shutting down my current Slackware system. I just did a chroot to the brand new Gentoo partition I created.

I have a printed version of Gentoo handbook. Unfortunately, this was printed in 2004, but I guess not many things has changed since. (Now I think this was a wrong guess) I was following this handbook, and then switched to online handbook.

I choosed to install Gentoo from stage1. Downloaded the stage1 tarball, uncompressed it, followed the handbook doing one or two things, then did a bootstrap. Then, I tried `emerge --sync`. This command gave me the first bad impression on Gentoo, because this was the first command (of a series) that failed.

`emerge --sync` has failed AFTER `rsync` finished downloading everything. So, the problem WAS NOT ANY FIREWALL, like many people on [#gentoo](irc://irc.freenode.org/gentoo) said. (I know all you were trying to help, don't be angry to me, but I also know that I can use rsync) One guy said me to run `emerge --metadata`, and so did I.

Then, `emerge --emptytree system`. Oh, this takes long time. I guess I left the computer compiling for one day. However, when I returned, I found one error message, in middle of emerge process. The _portage_ already did emerge gcc, glibc and some other important things, but in middle of process, it gave me one error.

Unfortunatly, there was a blackout and I lost the exact error message, but it was something like "i686-linux-gcc" was not found. I felt it was VERY strange, since it could compile other things just some minutes (or some "shift+pageUps") ago.

This time, I didn't know about the existence of `emerge --resume`. The so-claimed-so-good Handbook does not say about this command.

Then I tried `emerge system`, since this would not re-emerge already merged packages (which would save me a lot of time). However, people at [#gentoo](irc://irc.freenode.org/gentoo) suggested me to retry the `emerge --emptytree system`, because my system could already be in an "inconsistent state".

This is another big failure of Handbook: it does not say what to do when something fails. Someone at Gentoo IRC channels said it is difficult to write what to do about something that was not supposed to fail. Ok, but it failed anyway, and everybody knows that there is no perfect software.

At this time, it was more than one week after the start of installation (ok, I was not installing it full-time, there were some days I didn't even touch the gentoo partition) and I was getting angry, because I lost too much time trying to get something supposedly fail-proof to work, and all I got was different answers from people at Gentoo IRC channels and a possibly inconsistent system.

Many (or almost all) people told me I should start from stage3. At first I could not understand why. If there are 3 stages, I can choose to start from any of them. I suppose all of them work.

But I was wrong. I feel that Gentoo community is starting to give no support for stages 1 and 2. The only reason I can see for this is because probably stages 1 and 2 are broken, don't work anymore.

Gentoo is confusing. There are two handbooks (maybe more):

* [http://www.gentoo.org/doc/en/handbook/index.xml](http://www.gentoo.org/doc/en/handbook/index.xml)
* [http://www.gentoo.org/doc/en/handbook/2005.1/index.xml](http://www.gentoo.org/doc/en/handbook/2005.1/index.xml)

The first is "generic" handbook (as someone called it). The second is the "networkless" handbook. I feel the first handbook (the "generic" one) is not supported by Gentoo IRC users. But why?

Now, my installation is stopped. I will `rm -rf` all data in that partition and restart the install process from scratch sometime soon. This time, from stage 3 (Why the !@#$ can't the !@#!$%! stage 1 work?).
