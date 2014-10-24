---
layout: post
title: NVIDIA = No VIDeo for vIA
lang: en
tags:
- Gentoo
- Linux
- nvidia
- X.org
- driver
---

If you read this blog, you might remember how many times I tried to make `nvidia` driver work with X.org, without freezing it. The solution was disable **AGP** support and wait until X.org 7 was released, since I read somewhere that _nVidia_ sent some patches to it.


7 months since my previous try, now I have _modular X.org_ 7.0 and Gentoo "told me" to update my nvidia drivers. It is a good time to try again.

Versions: Modular X.org 7.0.0, nvidia-drivers-1.0.8762-r1, vanilla-kernel-2.6.17.6.

Hardware: Pentium III 800MHz, Asus CUV4X motherboard (with Via chipset), GeForce FX 5500 videocard.

I edited my `xorg.conf` file and commented the following line:

    #Option      "NvAGP"        "0"

This way, the AGP setting was "automatic". After I started X, module `via_agp` has been loaded, and `/proc/driver/nvidia/agp/status` told me the AGP was enabled as 4X (my video card supports 8X, but my motherboard only supports 4X).

For some time, everything was fine. I noticed no speed-up by having AGP enabled. If there was some speed-up, it was minimal.

Then, suddenly, X froze. Exactly the same symptoms as before: keyboard dooes not work, nothing work, but mouse cursor still moves on screen. Although I could't check that, people say the system is still up and running, and, when opening an **ssh** session, we can see that X process is taking almost 100% of CPU.

Well, no **ssh** for me, no way to check or kill X process. So I did <kbd>Alt+SysRq+K</kbd> (see footnote), which killed X and returned me to a plain text console (I don't use framebuffer, bootsplash or similar). Fortunately, the console was a pure and **working** text console. I remember some other times I was forced to do that, the monitor display was still graphic and displaying completely garbled pixels, even though the console was "working" (I could type commands, but could not see what was printed).

Looking at `dmesg` output, I can see some very familiar lines:


    agpgart: Found an AGP 2.0 compliant device at 0000:00:00.0.
    agpgart: Putting AGP V2 device at 0000:00:00.0 into 4x mode
    agpgart: Putting AGP V2 device at 0000:01:00.0 into 4x mode
    NVRM: Xid (0001:00): 6, PE0000 1ffc 00000000 0000f74c 0000ffff 00000000
    SysRq : SAK

That `NVRM: Xid …` line was always present everytime X froze (maybe with other values). Looking at this blog archive, you might find that line on other posts.

**Conclusion:** X.org 7 did not fix this issue (as I thought it would). In fact, I don't even know from where this issue is: `agpgart` module, `via_agp` module, `nvidia` module, X.org or even Via hardware.

**Solution:** Put `Option "NvAGP" "0"` line at your `xorg.conf`, near `Driver "nvidia"` line. If you run `cat /proc/driver/nvidia/agp/status`, it will print `Status: Disabled`, because AGP support will be disabled. This causes no noticeable slowdowns, and everything else will still be working fine, including 3D OpenGL programs and games. And, at least, X won't be crashing and you will have a stable system again.

Oh, one last advice: I've tested if that (wrong) behavior described at [nVidia versus fonts!]({% post_url 2006-02-20-nvidia-vs-fonts %}) has been changed, and I found it is still the same behavior. So, all information on that old post is still valid.

**Footnote about SAK/SysRq:** <kbd>Alt+SysRq+K</kbd> (_SysRq_ is the same key of _Print Screen_) combination is trapped by kernel and does mean _Secure Access Key_ (_SAK_). It will kill all programs on the current virtual console. To enable that, you might want to recompile your kernel with `Magic SysRq key`, or modify your keyboard mapping. Read more at `/usr/src/linux/Documentation/sysrq.txt` and `/usr/src/linux/Documentation/SAK.txt`.

**Edit:** A friend told me he had the same problem. He has AMD Semprom 2200+ on Abit VA-10 motherboard (Via chipset) and GeForce 4 MX 440 64 MB.
