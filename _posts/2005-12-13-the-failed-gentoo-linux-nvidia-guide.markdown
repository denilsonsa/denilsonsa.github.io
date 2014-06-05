---
layout: post
title: The Failed Gentoo Linux nVidia Guide
lang: en
tags:
- Linux
- Nvidia
- driver
- X.org
- Gentoo
---

In this guide you will learn how to try to install [nVidia graphics drivers](http://www.nvidia.com/object/unix.html) for Linux/x86. You will also learn some of the various ways the installation may fail.


My hardware is Pentium III 800MHz on Asus CUV4X board (with Via chipset and AGP 4x) and nVidia GeForce FX 5500. My current system is a [Gentoo](http://www.gentoo.org/)/x86 "stable", using [vanilla-kernel](http://www.kernel.org/) 2.6.14.2.

Just as sidenote and for comparison, nVidia driver worked flawlessly at my old [Slackware](http://www.slackware.com/) 9.0 system with kernel 2.4.2x, with the exact same hardware.

## Install try #1:

First let us try the latest "stable" driver (available at [Gentoo portage](http://packages.gentoo.org/search/?sstring=nvidia)). It currently is 1.0.6629-r6 for `nvidia-glx` and 1.0.6629-r4 for `nvidia-kernel`. Just run, as root:

    # emerge -av nvidia-{kernel,glx}
    # etc-update
    # modprobe nvidia
    # opengl-update nvidia

Don't forget to edit `/etc/X11/xorg.conf` to enable nvidia driver. Now, it is installed and configured, just `startx` as a normal user.

So I did it, and I played [Cube](http://www.cubeengine.com/) a little, to enjoy the so-missed OpenGL acceleration. Oh nice. Then I closed it and opened [Opera](http://www.opera.com/) to write this blog. After I wrote 20 lines or more, I decided to save the text as a _note_ just to keep it in case of a crash. I selected the text and… Screen froze.

Oh, no, I remember this problem! Will I be able to get out of it without rebooting? <kbd>Alt+SysRq+K</kbd>. Hum, screen is now messed. <kbd>Ctrl+Alt+F1</kbd>, <kbd>Alt+SysRq+K</kbd>. Wow! I can see my terminal login screen again! Nice, system survived this time!

(sidenote: I do not use framebuffer terminal, nor XDM/GDM/KDM)

Looking at `dmesg` output (as well as `/var/log/messages`) I find these messages:

    Dec 13 13:11:34 NOVO NVRM: loading NVIDIA Linux x86 NVIDIA Kernel Module  1.0-6629  Wed Nov  3 13:12:51 PST 2004
    Dec 13 13:11:41 NOVO agpgart: Found an AGP 2.0 compliant device at 0000:00:00.0.
    Dec 13 13:11:41 NOVO agpgart: Putting AGP V2 device at 0000:00:00.0 into 4x mode
    Dec 13 13:11:41 NOVO agpgart: Putting AGP V2 device at 0000:01:00.0 into 4x mode
    Dec 13 13:11:41 NOVO agpgart: Found an AGP 2.0 compliant device at 0000:00:00.0.
    Dec 13 13:11:41 NOVO agpgart: Putting AGP V2 device at 0000:00:00.0 into 4x mode
    Dec 13 13:11:41 NOVO agpgart: Putting AGP V2 device at 0000:01:00.0 into 4x mode
    Dec 13 13:46:18 NOVO NVRM: Xid: 6, PE0000 1ffc 00000080 0000fae0 fef0ffff 00000080

The last line is the nvidia driver crashing and trashing X.

## Install try #2:

Ok, let's try the latest driver, then. Currently it is 1.0.8174-r1 (for both `nvidia-kernel` and `nvidia-glx`). Edit `/etc/portage/package.keywords` to add these lines:

    media-video/nvidia-glx ~x86
    media-video/nvidia-kernel ~x86
    media-video/nvidia-settings ~x86
    app-admin/eselect-opengl ~x86
    app-admin/eselect ~x86

Any nvidia package newer than 6629 requires `eselect-opengl`, which requires `eselect`. Now emerge it:

    # opengl-update xorg-x11
    # modprobe -r nvidia
    # emerge -av nvidia-{kernel,glx}
    # etc-update
    # modprobe nvidia
    # eselect opengl set nvidia

Now `startx` as normal user. Nice, X starts. Let's check if OpenGL works. `glxgears`… What? I'm back to terminal, with a message that X segfaulted (signal 11). Let's try again. `startx`, open xterm, type `glxinfo > glxinfo.log`. Yes, confirmed, X segfaults whenever OpenGL is used. Here is the `glxinfo` output from previous command:

    X Error of failed request:  BadWindow (invalid Window parameter)
      Major opcode of failed request:  144 (NV-GLX)
      Minor opcode of failed request:  4 ()
      Resource id in failed request:  0x2400002
      Serial number of failed request:  22
      Current serial number in output stream:  22
    name of display: :0.0

## Install try #3:

So, 8174 driver does not work. Let's try the latest 7xxx driver. Edit `/etc/portage/package.keywords`:

    =media-video/nvidia-glx-1.0.7676-r2 ~x86
    =media-video/nvidia-kernel-1.0.7676-r1 ~x86

Then run as root:

    # modprobe -r nvidia
    # eselect opengl set xorg-x11
    # emerge -av nvidia-{kernel,glx}
    # etc-update
    # modprobe nvidia
    # eselect opengl set nvidia

Once more, `startx` as user. Huh? X doesn't even start now! It prints "Could not load GLX module" (sorry, I did not take note of the exact error message)

## Conclusion:

    # eselect opengl set xorg-x11
    # modprobe -r nvidia
    # emerge unmerge nvidia-{kernel-glx} eselect{,-opengl}

And edit `/etc/X11/xorg.conf` to use `nv`.

## Appendix A:

There are other known ways to make nvidia driver not work. Try any of the following commands, when installing any nvidia driver greater than 6629 (i.e. 7xxx or 8xxx):

    # FEATURES=buildpkg emerge nvidia-glx
    # emerge --buildpkg nvidia-glx
    # emerge --buildpkgonly nvidia-glx

They all will build a package containing `nvidia-glx`, but the driver inside package will be placed at X.org-7 location, instead of X.org-6 location. Thus, a "stable" `xorg-x11` won't be able to find these drivers. ([bug report 115462](http://bugs.gentoo.org/show_bug.cgi?id=115462))


P.S. 1: In fact, I installed the different driver versions in a different order than listed in this post. It was: 8174, 7676, 6629.

P.S. 2: [#gentoo](irc://irc.freenode.org/gentoo) channel has the following advice at topic: ">=2.6.13 & xorg not loading nvidia? [http://tinyurl.com/78nyz](http://bugs.gentoo.org/show_bug.cgi?id=104369
#c18)". This problem/bug, however, did not happen here. After each install, I checked if there was /dev/nvidia* devices, and they were there.

Edit: Added bug report number.
