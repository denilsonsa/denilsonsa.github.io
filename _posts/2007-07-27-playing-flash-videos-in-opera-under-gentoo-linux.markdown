---
layout: post
title: Playing Flash videos in Opera under Gentoo Linux
lang: en
tags:
- Linux
- Opera
- Gentoo
---

This post is actually an adaptation of a bug report I submitted to Opera Software, based on my own experience and on what I learnt from [Gentoo Bug 127200 (netscape-flash misbehaves in Opera)](http://bugs.gentoo.org/show_bug.cgi?id=127200). I think this information is too valuable to be hidden at internal Opera Software bug tracker and at [Gentoo bugzilla](http://bugs.gentoo.org/).

## The issue: Flash videos are not played.


I can try [YouTube](http://www.youtube.com/), [Google Videos](http://video.google.com/) or any other site. It does not work.

### My system

* Gentoo Linux x86
* Opera 9.x
* Flash Player plugin 9.0.x.x

## Why this happens

Depending on where the `libflashplayer.so` is installed (or, if more than one is installed, which one is "default"), then the video won't be played.

The _gory_ details about why this happens are described at [Gentoo bug 127200 (netscape-flash misbehaves in Opera)](http://bugs.gentoo.org/show_bug.cgi?id=127200).

In summary, from what I could understand:

* If `libflashplayer.so` detects `netscape` in its own pathname, then videos won't be played (at least not in Opera). I guess it enters some crazy compatibility mode with Netscape browser ([R.I.P.](http://en.wikipedia.org/wiki/Rest_in_peace))
* Gentoo installs `libflashplayer.so` at `/opt/netscape/plugins/`, and installs a symlink at `/usr/lib/nsbrowser/plugins/`.
* Gentoo Opera ebuild makes a symlink `/opt/opera/lib/opera/plugins/libflashplayer.so -> /opt/netscape/plugins/libflashplayer.so`.
* Gentoo Opera ebuild sets `/opt/netscape/plugins=2` at `/opt/opera/share/opera/ini/pluginpath.ini`, but I guess this file might be ignored.
* Some Opera users (like me) might have `opera6.ini` selecting `/opt/netscape/plugins/libflashplayer.so` as Flash Player plugin. For these users, Flash videos won't be played.
* New Opera users (with a brand-new empty profile directory) will get the correct paths since the first time, and Flash videos will work for them.

This combination of factors might be too specific, but it happens. I guess other people on the world might have the same issue, and these people are very unlikely to find out its cause nor how to fix it. They will just think: _"Flash videos don't work inside Opera"_ (like I did think for **many months**, maybe a year or more).

## The solutions

The solution consists in telling Opera to not use `/opt/netscape/plugins/libflashplayer.so`. This can be done in three ways:

**Solution 1:** Preferences → Advanced → Downloads → _application/x-shockwave-flash swf_ → Edit… → Select the correct plugin at "Use plug-in" drop-down (if more than one is displayed, select any one that does not contain "netscape" in path). Repeat this for _application/futuresplash spl_ file type. There is no need to restart Opera after this change.

**Solution 2:** Manually edit ~/.opera/opera6.ini while Opera is closed and change the paths.

**Solution 3:** Add `/opt/netscape/plugins=2` to `~/.opera/pluginpath.ini`.

## Suggestion to Opera Software

Opera Software can workaround this. The Opera launcher script should check if the `/opt/netscape/plugins/libflashplayer.so` path (or the `/netscape.*libflashplayer.so/` [regex](http://en.wikipedia.org/wiki/Regular_expression)) is present in `~/.opera/opera6.ini`. If it is present, then warn the user that this is known not to work (a simple message printed to terminal will be helpful enough).

## Suggestion to Macromedia/Adobe

I think Flash technology is great, is powerful, is easy and fun to use.

But I think Flash sucks. Flash player is limited to Windows platform plus some few buggy and slow (or slower than Windows) implementations on other platforms. The Flash format should be open, and anyone should be able to write a compatible Flash player without need for reverse engineering. This would also allow anyone to fix bugs like this one.

Adobe site also sucks.

## Suggestion to webmasters

Avoid using Flash without a really good reason. Don't make Flash-based sites, they are slow and sometimes buggy. Don't use Flash for things that can be done without it (menus, for example). Don't use transparent Flash objects over other objects, because many times this is not supported by browser.

I was thinking about writing above paragraph in bold font with a big font size, but even that way it won't reach the right people. If you are still in doubt, also see [Web Pages That Suck](http://www.webpagesthatsuck.com/).

Am I saying any Flash is bad? No. Flash videos are the latest "revolution" in web pages, as well as [AJAX](http://en.wikipedia.org/wiki/Ajax_(programming)). Flash player allowed us to watch videos without downloading hundreds of codecs and plugins (RealPlayer plugin, Quicktime plugin, codecs, more codecs, yet another video plugin…). This is great, but don't abuse (or misuse) Flash.

## Updates/trackbacks _(section added on 2007-12-30)_

~~Supposedly, this blog should automatically detect and list [trackbacks](http://en.wikipedia.org/wiki/Trackback), [linkbacks](http://en.wikipedia.org/wiki/Linkback) and things like that. Well, in case it does not work well, I will post here or in comments whatever I find.~~ The 2014 reincarnation of this blog as static pages does not support trackbacks.

_2007-12-30:_ It was a happy surprise to find a YouTube video showing the user applying this solution and linking back to this post. I'm glad to find it is being useful for other people. [YouTube works in Opera (Linux). Honest.](http://youtube.com/watch?v=EeYMugP22K0) (looks like the video was published on 2007-09-16, but I found it only today, 2007-12-30)

## Update on 2010-07-16

And this bug comes to life again with Opera version 10.60 (64-bit) and Adobe Flash plugin 10.1.53.64 (32-bit) on Gentoo. Please follow [bug 328639](http://bugs.gentoo.org/show_bug.cgi?id=328639) and [bug 326841](http://bugs.gentoo.org/show_bug.cgi?id=326841), as well as [this forum topic](http://my.opera.com/community/forums/topic.dml?id=653262).
