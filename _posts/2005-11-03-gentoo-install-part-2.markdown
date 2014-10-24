---
layout: post
title: Gentoo Install - part 2 - Stage3
lang: en
tags:
- Linux
- Gentoo
---

This time, I installed stage3. I `rm -rf` the old incomplete stage1 install and started the stage3.


Stage3 is a lot easier than stage1, since everything is already done. I just unpacked the stage3 tarball, then unpacked portage snapshot, then edited some config files at /etc, and it was almost done.

I've then emerged some things (one of the first things was [vim](http://www.vim.org/)), and also configured the Linux 2.6 kernel. It was the first kernel 2.6 to my system, and I noticed it does not have "USB Scanner" option, while kernel 2.4 had.

I emerged xorg-x11. It was very strange. It said "Previous xorg-x11 installation detected.", but, unless stage3 comes with X11, I did not have any X installed on gentoo. Then, at final part of xorg-x11 install, lots of strange messages were printed:

     * Previous xorg-x11 installation detected.
     * Enabling PAM features in xorg-x11.
     * Migrating from /usr/X11R6/bin to /usr/bin...
     *   /usr/X11R6/bin doesn't exist, not migrating
     *     Symlinking //usr/X11R6/bin -> ../bin
    ln: creating symbolic link `//usr/X11R6/bin' to `../bin': No such file or directory
     * Migrating from /usr/X11R6/include to /usr/include...
     *   /usr/X11R6/include doesn't exist, not migrating
     *     Symlinking //usr/X11R6/include -> ../include
    ln: creating symbolic link `//usr/X11R6/include' to `../include': No such file or directory
     * Migrating from /usr/X11R6/lib to /usr/lib...
     *   /usr/X11R6/lib doesn't exist, not migrating
     *     Symlinking //usr/X11R6/lib -> ../lib
    ln: creating symbolic link `//usr/X11R6/lib' to `../lib': No such file or directory
     * Migrating from /usr/X11R6/man to /usr/share/man...
     *   /usr/X11R6/man doesn't exist, not migrating
     *     Symlinking //usr/X11R6/man -> ../man
    ln: creating symbolic link `//usr/X11R6/man' to `../man': No such file or directory
     * Preparing any installed configuration files for font move...
    find: //usr/share/fonts/encodings: No such file or directory
    find: //usr/share/fonts/local: No such file or directory
    find: //usr/share/fonts/misc: No such file or directory
    find: //usr/share/fonts/util: No such file or directory
    find: //usr/share/fonts/TTF: No such file or directory
    find: //usr/share/fonts/Type1: No such file or directory
    find: //usr/share/fonts/75dpi: No such file or directory
    find: //usr/share/fonts/100dpi: No such file or directory
    find: //usr/share/fonts/cyrillic: No such file or directory
    find: //usr/share/fonts/ukr: No such file or directory
     * //usr/X11R6/lib/X11/fonts does not exist.
     * Migrating from /usr/X11R6/lib/X11/fonts to /usr/share/fonts...
     *   /usr/X11R6/lib/X11/fonts doesn't exist, not migrating
     *     Symlinking //usr/X11R6/lib/X11/fonts -> ../../share/fonts
    ln: creating symbolic link `//usr/X11R6/lib/X11/fonts' to `../../share/fonts': No such file or directory
     * Preparing for /usr/X11R6 -> /usr migration...
     * Remaining symlinks in /usr/X11R6:
    find: //usr/X11R6/: No such file or directory
     * Migrating from /usr/X11R6 to /usr...
     *   /usr/X11R6 doesn't exist, not migrating
     *     Symlinking //usr/X11R6 -> ../usr
     * >>> SetUID: [chmod go-r] /gentoo/tmp_portage/portage-pkg/xorg-x11-6.8.2-r4/bin/usr/bin/Xorg  ...     [ ok ]


I have absolutely no idea about what they are, and I don't know if it was installed correctly. I hope yes.

In additon, portage told me to run `etc-update`. And I did it:

    # etc-update
    Scanning Configuration files...
    Exiting: Nothing left to do; exiting. :)

I hope everything is ok with my gentoo install. The impression I have is that gentoo has a lot of flaws, and things works by miracle. I think if there were no flaws, then stage1 would work, and xorg-x11 should not give too many (error) messages.

No, I'm not expecting a perfect system, because there is no such thing, but I was expecting something better.

Now I need to configure and install grub, then hope Gentoo can boot.
