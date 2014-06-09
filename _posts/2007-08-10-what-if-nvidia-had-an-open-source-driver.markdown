---
layout: post
title: What if nVidia had an open source driver?
lang: en
tag:
- Linux
- Nvidia
- driver
- Open Source
---

The _Free Software_ and _Open Source_ community is always asking for hardware manufacturers to write free and open source software (from now on called [FOSS](http://en.wikipedia.org/wiki/Alternative_terms_for_free_software)) drivers. So, let's try to guess what would happen if [nVidia](http://www.nvidia.com/) decided to release the graphics drivers as FOSS.


**This is only a supposition, don't think the information here is true, has happened or is going to happen.** (but I guess most of us would love to see it happen)

## Day 0: nVidia announces it will be releasing the graphics drivers as FOSS

On this day, nVidia caused a big repercussion on all world. All computer-related news sites comment about this move. Many news sites for the average public also publish this. nVidia homepage is [slashdotted](http://en.wikipedia.org/wiki/Slashdot_effect) and goes down just half hour after the announcement. Many bloggers all around the world also update their blogs to write comments on this subject. Both bloggers and slashdot users are divided into two groups: those who approve this decision, and those who doubt it will actually happen.

## Day 70: nVidia releases the first FOSS graphics driver

More than two months later, when many people were thinking it wouldn't happen, nVidia publishes the first FOSS version of its graphics driver. Again, news sites all around the world talk about this. nVidia homepage is slashdotted, again, and nVidia FTP can't handle the number of downloads. Fortunately, many people are already distributing the [tarball](http://en.wikipedia.org/wiki/Tarball) by bittorrent, unofficial HTTP mirrors and [IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat) [DCC](http://en.wikipedia.org/wiki/Direct_Client-to-Client). Two hours after the release, there is already a masked ebuild in [Gentoo repository](http://packages.gentoo.org/) and a copy of the tarball at Gentoo mirrors.

Contrary to what skeptical people thought, this release is an actual [Free Software](http://en.wikipedia.org/wiki/Free_software). **Note: This is a key point. The driver source-code must not only be viewable, but must be free to be modified and redistributed.** (If the driver is not Free Software, then nothing of what is said here is possible)

Someone creates a project at [SourceForge.net](http://sourceforge.net/) to host the first fork of nvidia-driver.

## Day 91: The community starts to organize the work

By now there are at least five forks of the nVidia driver, plus hundreds of patches floating on many blogs, forums, personal homepages, bug trackers and mailing lists.

Part of the community starts to organize itself and concentrate efforts towards one project. This project may be officially supported by nVidia itself, or it may be a completely thirdy-party fork.

Besides this project, other two or three forks also try to concentrate efforts. Some people also try to merge the current nv driver with the new FOSS nvidia-driver. Eventually, at most two or three forks will "survive" in long-term.

nVidia announces it won't support systems which use non-official drivers. (But, hey! Tell me a big company that **actually** has a good support for users. If you, like me, can't name any of them, then this announcement won't hurt the users so much.)

## Day 127: Work starts to generate good results

In this short period of time, hundreds of thousands hackers (i.e., programmers) read, test and modify the code on all types of hardware and software combinations. The amount of people involved surpasses by far the number of programmers nVidia was ever able to hire. The amount of different motherboards, CPUs, memories, operating system versions and X.org versions onto which nvidia cards and drivers were tested is far greater than the number of test computers at nVidia development offices.

Because of this, hundreds bugs are discovered and fixed. Most of them nVidia would never be able to replicate itself, because they only happened on specific hardware/software combinations. Other bugs known by users for months (or years) also get fixed.

And why would all of these people _work for free_? Because they want to use their computer. Let's suppose one of these people finds a bug, and this bug is annoying or severe enough to disrupt his own work, so he can't use the computer the way he should. Then this guy can try to fix the bug himself, or at least track down the bug. Whatever he does about this it, he shares what he finds with other people (the "community"). This way, other people can help him to fix the bug, and, when it is finally is fixed, everyone benefits from work. Thus, the end-product of this process should be a better, more robust and less buggy software. And with a less buggy software, all people (both those who are technically-skilled and those who don't know what a graphics driver is) can use computers with less problems.

Of course, there are more advantages. If needed, the free driver can be ported to other operating systems, including those which nVidia does not officially support (like OpenBSD and NetBSD). With a free driver, people can also compile support for only for the actual GPU on system, resulting on a smaller driver and a smaller kernel, which could be important on some situations.

## Day 150: nVidia sales have grown

Even when nvidia-driver was closed source, many people preferred to buy nVidia cards over ATI cards because nvidia-driver worked better than ATI's, at least on Linux.

With all the fuss about FOSS nvidia-driver, nVidia sales have increased and it is now dominant on video card market.

ATI, worried about losing more market share, starts to think about making its driver free too.

## Day 160: Cross-operating system driver

One of the forks try to keep an unified core, common to all operating systems (Windows, Linux, \*BSDs, …), and make wrappers for each one.

_Note: I guess (or I hope) this is roughly how nVidia develops its driver._

## Day 224: The stable driver

After long testing and development, the new FOSS nvidia-driver (or the most successful fork of it) is now much less buggy than what nvidia-driver originally was. But the development goes on.

By now, many people have burnt their video cards by testing/developing the driver or by overclocking it.

Gentoo marks this new FOSS nvidia-driver as stable on its repository.

## Day 240: Ubuntu live-cds

The so famous and ubiquitous Ubuntu distribution adds the FOSS nvidia-driver to its repository. It is also announced that next live-cds will already come with FOSS nvidia-driver pre-installed, allowing people to enjoy Ubuntu and 3D desktop (either with Compiz, Beryl, Compiz/Beryl fusion, or whatever is available in that time) without even installing it.

## Day 999: Debian repository

The first FOSS nvidia-driver reaches the "stable" Debian distribution.

_Note: I'm not sure if this date is underestimated._

## Day ???: Other hardware drivers

Other hardware manufacturers also follow the nVidia decision and release FOSS of their drivers.

## Final considerations

I'm not saying FOSS is a magic solution that will magically make all software better. Actually, I believe this is going to work with nVidia drivers because that software is already in a good state and because many people "need" to use it, thus many people will test and modify it.

A manufacturer of very specific or less-known hardware pieces should also release the drivers as FOSS, because, then, it will be possible to improve or fix these drivers whenever needed. Of course, releasing a badly-written driver as FOSS is not good.

Finally, let's take a look at [winmodem (softmodem)](https://en.wikipedia.org/wiki/Softmodem) drivers for Linux and learn why manufacturers must not release only closed-source drivers. Some (or many?) of these modem drivers are closed-source and were compiled for kernel-2.4 with gcc-2.9. This means the user won't ever be able to upgrade his system, or install one of the newest distros, else his modem won't work. The user can't also fix the modem driver, because the driver is not free.

Computer world changes very fast. Software changes at a blazing speed. Even though hardware changes too, hardware must be bought, can't be just updated like software. After some time, it always happens that new software runs on old hardware. This is how things work, manufacturers can't change it and they must not try to change it.

Manufacturers don't update drivers for old hardware. In my opinion, that's ok, they have to worry about new hardware and they can't focus on updating all old software. But, if the software is free, then the users can (and will) update the drivers as needed.

Again, Free Software is not a miraculous solution to all software problems. But the world would be a better place if all hardware had open drivers.
