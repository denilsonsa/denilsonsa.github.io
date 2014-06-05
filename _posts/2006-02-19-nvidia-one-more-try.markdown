---
layout: post
title: nVidia, one more try
tag:
- Gentoo
- Linux
- Nvidia
- X.org
---

Last night, I came upon _Shirakawasuna2_ at [#gentoo](irc://irc.freenode.net/gentoo) channel. He was asking for help with X.org lock-ups with via+nvidia+agp. I told him I had the same problem, and I was using `nv` driver. He told me he could "stabilize" using the `nvidia` driver. Then I asked how, and start writing one more chapter of my nvidia series…


Taking the long story (and conversation) short, he could "stabilize" his system by disabling AGP. To do that, the best way is change `NvAGP` option in xorg.conf file. The possible values are:


    0 - disable AGP
    1 - use NVIDIA's internal AGP support, if possible
    2 - use AGPGART, if possible
    3 - use any AGP support (try AGPGART, then NVIDIA's AGP) [default

([from nVidia driver README](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/appendix-d.html))

So, I emerged latest drivers: `nvidia-glx-1.0.8178` and `nvidia-kernel-1.0.8178-r3`. At first, I tried with default `NvAGP = 3`. Looking at `/proc/driver/nvidia/agp/status`, I saw it was using AGPGART. It froze after some minutes, and I could bring the computer up again, without rebooting, by pressing <kbd>Alt+SysRq+K</kbd>, then <kbd>Ctrl+Alt+F1</kbd> and <kbd>Alt+SysRq+K</kbd> again (on my previous crashes, months ago, this could not always bring a working console).

_Shirakawasuna2_ tried value 3 on his system. At first, the NVAGP was used, because `via_agp` module was not loaded on his computer. It froze very fast. Then, he `modprobe`'d that module, and nvidia used AGPGART. X.org froze too, did not take too long. Fortunately for him, he could ssh into the box and kill X.

I did not even try NVAGP, since it will certainly crash. [nVidia README](http://download.nvidia.com/XFree86/Linux-x86/1.0-8178/README/appendix-f.html) does not list my chipset as supported for NVAGP.

So, I started X disabling AGP (`NvAGP = 0`). This will degrade the performance a little, but should be a lot faster (and flicker-less!) than with `nv` driver.

Sidenote: On my old slack system, when I had AGP disabled and Riva TNT2 card, high-res videos were played VERY slow. Enabling AGP solved it. However, on my current system I could not reproduce this slowdown.

Well, I'm not really sure if disabling AGP will make this "stable", but I can notice it is far more stable than before! Not sure yet if as stable as `nv` driver. (Now I can play OpenGL games! I haven't played any of those for months!)

Thanks _Shirakawasuna2_ for your suggestion of disabling AGP (well, you did not exactly suggest that, but this was our conclusion).
