---
layout: post
title: nVidia versus fonts!
lang: en
tag:
- Gentoo
- Linux
- driver
- Nvidia
- X.org
---

Well, looks like disabling AGP resulted in a stable system. No crashes so far (since yesterday).

However, as soon as I started X with `nvidia` driver, I could notice something wrong… Fonts of most applications were smaller! Both [Psi](http://psi-im.org/) (QT application) and [X-Chat](http://www.xchat.org/) (GTK application) displayed fonts way too small. So, I started hunting the cause of this…


When using `nv` driver, it correctly autodetects my screen size (280x210mm) and sets DPI to 92x92. However, when running `nvidia` driver, it sets DPI to 72x72 and screen size to 361x271mm. You can see these values by running `xdpyinfo | grep -B1 dot` (as described at [nVidia driver README](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/appendix-y.html)). You can also see the screen size (but not DPI) using `xrandr` command.

Well, the first thought was to set the screen size manually, in `/etc/X11/xorg.conf`. So I added `DisplaySize 280 210` to the `"Monitor"` section. Then I restarted X and… no change. The `xdpyinfo` still showed the same DPI and resolution.

**Conclusion 1:** `nvidia` driver ignores `DisplaySize` setting.

Asking at [#nvidia](irc://irc.freenode.net/nvidia), people told me set DPI. So I tried it.

There are a couple of ways of doing it. One of them is using the _-dpi_ command-line parameter. Note that:

    startx -dpi 75x75

does not work. You must use:

    startx -- -dpi 75x75

There is a reason for that (read the `startx` manpage to learn). Only parameters after `--` are passed to X server (the others are passed to client, and also define it). The manpage has three examples:

    startx -- -depth 16
    startx -- -dpi 100
    startx -- -layout Multihead

Well, back on-topic, I tried to run `startx` using the DPI parameter. It worked, the fonts are now at their normal size. In addition, it also changed the screen dimensions.

**Conclusion 2:** Setting the correct DPI solves the font-size problems (as [Chapter 5 - Common Problems](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/chapter-05.html) explains).

To avoid passing `-dpi` parameter all the time, I added the following lines to "Device" section corresponding to my videocard with `nvidia` driver:

    Option "UseEdidDpi"   "false"
    Option "Dpi"          "92 x 92"

Not setting the `"UseEdidDpi"` option causes `nvidia` driver ignore the `"Dpi"` option and set the DPI based on some EDID info, or based on telepathic powers.

After those tries (a few more than listed here), and after reading the [Appendix Y - Dots Per Inch](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/appendix-y.html), I finally understood how it works:

**Conclusion 3:** `nvidia` calculates the screen dimensions based on DPI and resolution (1024/92dpi = 283mm; 768/92dpi = 212mm).

So, if you want to display fonts at the correct size on your screen, DON'T waste time setting `"DisplaySize"`. Instead, measure your monitor width (only the viewable area), convert that to inches, and divide your resolution by it. Set this value as `"Dpi"` option, and don't forget to set `"UseEdidDpi"` to `"false"`. Thanks nVidia for this.

This is completely wrong, in my opinion. Following the way `nvidia` behaves, the monitor dimensions are the variable to be calculated. In other words, **according to _nvidia_ driver, your monitor size is not constant**. This is stupid. If I change the resolution, the DPI keeps constant, and my monitor screen that became smaller. It is like my monitor must shrink to fit `nvidia` calculations.

Read the following two excerpts from [Appendix Y](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/appendix-y.html):

{% comment %} https://stackoverflow.com/questions/3358056/multiple-blockquotes-in-a-row-using-markdown-syntax {% endcomment%}

> If the display device provides an EDID, and the EDID contains information about the physical size of the display device, that is used to compute the DPI. _[…]_

> Note that the physical size of the X screen, as reported through `xdpyinfo` is computed based on the DPI and the size of the X screen in pixels.

As I can understand, `nvidia` driver gets the physical size from monitor, uses it to calculate DPI, then use DPI and screen resolution to calculate the physical size. I can't understand why nVidia chose to do it. Makes no sense for me.

It is stupid, but true.
