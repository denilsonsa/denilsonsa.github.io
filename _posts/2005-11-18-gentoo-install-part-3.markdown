---
layout: post
title: Gentoo Install - part 3 - The nVidia strikes back
lang: en
tags:
- Linux
- Gentoo
- Nvidia
- driver
- X.org
---

Damn Gentoo!


Ok, my Gentoo system appears to work. X can startup (using the plain NV driver), I do have Opera (why Opera depends on OpenMotif? huh? plugin interface? ok), screen, fluxbox, vim, mirrorselect…

Of course I wanted to enable [nVidia drivers](http://www.nvidia.com/object/unix.html). I have a _GeForce FX 5500_ videocard, with two monitors, so I need nvidia drivers to enable dual-display, as well as 3D acceleration.

Ok, I've once had saw one computer where the latest "stable" ebuild for nvidia drivers did not work. Then, before anything else, I unmasked any nvidia ~testing ebuild at `/etc/portage/package.keywords`. Go emerge it! `nvidia-glx-1.0.7676-r1` and `nvidia-kernel-1.0.7676-r1` merged. Run `modprobe`, run some other things… Now `startx`!

    (II) LoadModule: "nvidia"
    (WW) Warning, couldn't open module nvidia
    (II) UnloadModule: "nvidia"
    (EE) Failed to load module "nvidia" (module does not exist, 0)
    (EE) No drivers available.

Ok, ask about this at [#nvidia](irc://irc.freenode.org/nvidia) channel. Hum… The problem is with `nvidia-glx` package, and not with `nvidia-kernel`. Hum… This package installed the nvidia driver at `/usr/lib/xorg/modules/drivers`, however all other drivers are at `/usr/X11R6/lib/modules/drivers`. This explains why X.org/X11 can't find the nvidia driver.

Let me try adding "ModulePath" to `/etc/X11/xorg.conf`… Adding two entries, one for "old" (default) path, and another for nvidia-only path. Trying to `startx`… Monitor blinks… And X is aborted "caught signal 11".

Ok, unmerge all of these nvidia-related things… Just remember to return opengl to xorg-x11 and unload nvidia kernel module.

Now, let me try with the latest stable version: `nvidia-kernel-1.0.6629-r4` and `nvidia-glx-1.0.6629-r6`
Emerge, wait download, compile, install…
`startx`

It works!!! I can have my fluxbox desktop! Very nice!

And I was almost happy when, some hours after, X freezes. Mouse still moves, but the image is frozen. Background music still runs, so system is alive, only display is crashed. Ok, <kbd>Alt+SysRq+K</kbd> (this is a kernel shortcut to kill all processes running on current terminal, very useful to have these shortcuts enabled in kernel). Apparently nothing happened. Then I press <kbd>Ctrl+Alt+Del</kbd>. I wait some time and the system cleany reboots. Linux rocks! Even frozen it still works. :P

Ok, let me use X and Opera some more time. Let me read one more page… oops? Frozen again? Oh no! <kbd>Alt+SysRq+K</kbd>, <kbd>Ctrl+Alt+Del</kbd>, reboot, wait, wait…

I know what is the cause of these crashes. This nVidia driver version does not work well with my videocard. On my Slackware system, I got the same problem. On my Slackware system, however, I could solve it by updating the drivers. If I will be able to update the drivers on Gentoo, the problem will be solved.

For the second time today (in fact, it all happened yesterday), unmerge all nvidia-related packages.

So I take a look at ebuilds at `/usr/portage/media-video/nvidia-glx/`. With the help of `fgrep`, I can see which packages install drivers at `/usr/lib/xorg`, instead of default path. I notice 7167-r2 is the latest version that installs it at "correct" place.

Edit `/etc/portage/package.keywords`, unmask this specific version of these ebuilds. Once again, emerge nvidia-glx and nvidia-kernel.

Emerge finished, now I must test if the system will continue as stable as my Slack.

To be continued…
