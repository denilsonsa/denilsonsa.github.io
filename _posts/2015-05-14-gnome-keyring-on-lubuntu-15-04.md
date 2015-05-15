---
layout: post
title: Finding out how gnome-keyring gets started on Lubuntu 15.04
lang: en
tags:
- Linux
- Ubuntu
---

This week I've updated my Lubuntu 13.10 to 14.04 to 14.10 and finally to 15.04.

Then I noticed something strange, that I had never seen before: a *gnome-keyring* dialog showing up whenever I was asked to provide the passphrase for my [ssh key][sshkeys]. I don't really understand why I need *gnome-keyring* dialog in my face when previously I could just type the passphrase at the terminal. (Feel free to enlighten me, explaining why this is better.)


Then I spent the next [couple of hours][couple] trying to disable it, and trying to track down how it gets run, so I can have a better understanding of how my system works.

## Easiest solution: just remove it!

What if I just remove the `gnome-keyring` package?

    # apt-get remove gnome-keyring
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    The following packages will be REMOVED:
      gnome-keyring lubuntu-desktop
    0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
    After this operation, 3,730 kB disk space will be freed.
    Do you want to continue? [Y/n]

It will also remove the `lubuntu-desktop` metapackage. While at first it might seem harmless, it may cause me trouble in the future. Packages that were previously installed because were dependencies of `lubuntu-desktop` will get autoremoved. New packages that may be introduced as dependencies of that metapackage won't be installed. This can become specially troublesome during a `dist-upgrade`.

I want to find a way to disable it without uninstalling the package.

## Finding all the places where LXDE starts applications

[Lubuntu][] uses [LXDE][] as the [desktop environment][de], so it makes sense to check all the places where it runs applications.

First location is at *Start menu → Preferences → Default applications for LXSession*, or by simply running `lxsession-default-apps`. At the *Core applications* tab, there is an item called *Security (keyring)*, which can have either `ssh-agent` or `gnome` as value. It was `ssh-agent` for me, and clearing that value to blank did not prevent `gnome-keyring`.

Then, at the same configuration tool, at *Autostart* tab, I looked for anything suspicious. Nothing relevant in there.

A [blog post from 2012][dtek] ([Wayback Machine][wbmdtek]) mentions that there are several `*.desktop` files that get autostarted, but are hidden from the [Unity][] Startup Applications manager. So I tried un-hiding them:

    sudo sed -i 's/NoDisplay=true/NoDisplay=false/' /etc/xdg/autostart/gnome*.desktop

No luck, still nothing exceptional was shown in the configuration tool.

As a last resort, I configured LXDE to completely disable autostart. I did it by changing *Disable autostarted applications?* (also found at the *Autostart* tab) from *config-only* to *all*. This option gets saved to `~/.config/lxsession/Lubuntu/desktop.conf` as `disable_autostart=all`. After logging out and logging back in, I have an empty desktop with the window manager ([Openbox][]) and nothing more. I open a terminal window and try using `ssh`… Damn, *gnome-keyring* is still running.

## Testing other sessions and window managers

So, why exacly does *gnome-keyring* show up when running `ssh`? A quick check at the environment variables shows the reason:

    $ env | sort | fgrep -i $'gnome\nssh'
    GNOME_KEYRING_CONTROL=
    GNOME_KEYRING_PID=
    SSH_AUTH_SOCK=/run/user/1000/keyring/ssh

Interesting… If I log out and log in using a different session (such as *TWM*, *Fluxbox* or *Openbox*), those vars are not set. So, I'm actually seeking whatever script or binary that sets those vars. Unfortunately, it wasn't that easy, because searching for those names (using `grep` or [`ack`][ack]) in `/etc/` yielded no results that could help me.

## Searching elsewhere

Someone must have gone through this trouble and documented the solution somewhere, right?

I searched through the [lubuntu-users mailing list][lubuntu-users], nothing relevant there.

I found [GNOME Keyring page at ArchWiki][arch] ([Wayback Machine][wbmarch]), and it suggests removing the `gnome-keyring-ssh.desktop` file from `/etc/xdg/autostart/` (actually, it suggests symlinking it to `/dev/null`).

I searched [Ubuntu Forums][], and found an [interesting post by gmoore777][post] ([Wayback Machine][wbmpost]), dated from 2010. Certainly outdated, but contained the most detailed info so far. The post suggested removing the `+x` permission from `gnome-keyring` binary. Yes, it works, but that's not something I wanted to do. Then it had several other suggestions, which I also tried.

So, no one described how it works and how to disable it… yet! This is why I'm writing this post.

## Investigating the installed files

I started investigating further. (Or maybe *nearer*, because now I'm looking at stuff in my local machine, instead of stuff over the web.) What are the files installed by `gnome-keyring`?

    $ dpkg -L gnome-keyring
    [… several non-relevant files omitted …]
    /etc/xdg/autostart/gnome-keyring-ssh.desktop
    /etc/xdg/autostart/gnome-keyring-secrets.desktop
    /etc/xdg/autostart/gnome-keyring-gpg.desktop
    /etc/xdg/autostart/gnome-keyring-pkcs11.desktop
    /usr/share/dbus-1/services/org.freedesktop.secrets.service
    /usr/share/dbus-1/services/org.gnome.keyring.service
    /usr/share/upstart/sessions/gnome-keyring.conf
    /usr/share/upstart/sessions/gnome-keyring-ssh.conf
    /usr/share/upstart/sessions/gnome-keyring-gpg.conf

I've already checked `/etc/xdg/autostart/gnome-*.desktop` files, and they are not being used.

I've tried removing those files from `/usr/share/dbus-1/services/`, but still no luck. (And, of course, I moved them back into place.)

I've also checked `/etc/pam.d/` and commented the following line on `lightdm` and `lightdm-greeter`:

    session optional        pam_gnome_keyring.so auto_start

As all other tries, nothing happened.

Only one directory I have not checked yet: `/usr/share/upstart/sessions/`

## Putting all the pieces together

What is the process that is listening to that socket?

    $ env | fgrep SSH
    SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
    $ lsof /run/user/1000/keyring/ssh
    COMMAND     PID     USER   FD   TYPE             DEVICE SIZE/OFF   NODE NAME
    menu-cach 16218 denilson    3u  unix 0x0000000000000000      0t0 243759 /tmp/.menu-cached-

Hmm… Whatever this process is, it is not relevant. Maybe I need to run `lsof` as *root*?

    $ sudo  lsof /run/user/1000/keyring/ssh
    lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1000/gvfs
          Output information may be incomplete.
    COMMAND     PID     USER   FD   TYPE             DEVICE SIZE/OFF   NODE NAME
    gnome-key 16050 denilson   13u  unix 0xffff8800bb6ae680      0t0 240512 /run/user/1000/keyring/ssh
    menu-cach 16218 denilson    3u  unix 0xffff8800c1560a80      0t0 243759 /tmp/.menu-cached-

A-ha! There it is: `gnome-keyring` with PID 16050. Maybe I can find its parent process… Sure, I could spend a lot of time reading `ps` manpage to find what which parameters will give me the info I need; or I could just run [`htop`][htop], press <kbd>T</kbd> to enter the *tree* mode, find the `gnome-keyring` process there, then follow the line up to its parent. That's what I did.

And I found that `upstart --user` is the parent of `gnome-keyring`. In fact, the tree looks like this:

    ├─ /usr/sbin/lightdm
    │  ├─ lightdm --session-child 12 19
    │  │  ├─ /sbin/upstart --user
    │  │  │  ├─ …
    │  │  │  ├─ /usr/bin/lxsession -s Lubuntu -e LXDE
    │  │  │  │  └─ …
    │  │  │  ├─ upstart-dbus-bridge --daemon --session --user --bus-name session
    │  │  │  ├─ upstart-dbus-bridge --daemon --system --user --bus-name system
    │  │  │  ├─ upstart-file-bridge --daemon --user
    │  │  │  ├─ upstart-udev-bridge --daemon --user
    │  │  │  ├─ gnome-keyring-daemon --start --components pkcs11,secrets
    │  │  │  └─ dbus-daemon --fork --session --address=unix:abstract=/tmp/dbus-RaSShjXvPa

So the login UI `lightdm` calls `upstart --user`, which in turn runs both `gnome-keyring` and `lxsession`. But why it doesn't run on *TWM*, *Fluxbox* and *Openbox* sessions? The answer lies in `/etc/upstart-xsessions`:

```
# xsessions listed below are run inside an Upstart user session.
gnome
gnome-classic
gnome-fallback
gnome-flashback-metacity
gnome-flashback-compiz
kde-plasma
Lubuntu
Lubuntu-Netbook
lubuntu-nexus7
lxgames
qlubuntu
ubuntu
ubuntustudio
xfce
xubuntu
unity8-x11
unity8-mir
```

## Solutions

The first real solution to prevent *gnome-keyring* from starting is to use another X session. I could select *LXDE* instead of *Lubuntu*, and since that one is not listed in `/etc/upstart-xsessions`, it won't run `upstart --user`.

The second solution is to override the job properties. [Session jobs][sessionjob] ([Wayback Machine][wbmsessionjob]) are started by `upstart --user`, and the configuration is read from:

* `$XDG_CONFIG_HOME/upstart/` (or `$HOME/.config/upstart/` if `$XDG_CONFIG_HOME` not set)
* `$HOME/.init/` (deprecated - supported for legacy User Jobs)
* `$XDG_CONFIG_DIRS`
* `/usr/share/upstart/sessions/`

So I can create some `*.override` files with the [`manual` directive][manual] ([Wayback Machine][wbmmanual]).

> This stanza will tell Upstart to ignore the start on / stop on stanzas.

And that's what I did:

    $ mkdir -p ~/.config/upstart
    $ echo manual > ~/.config/upstart/gnome-keyring.override  # See note below.
    $ echo manual > ~/.config/upstart/gnome-keyring-ssh.override
    $ echo manual > ~/.config/upstart/gnome-keyring-gpg.override

After logging out and logging back in… Success! Woohoo! No more *gnome-keyring* and no root access was required! And also now I have a better understanding of my system and of upstart!

However, it was not without side-effects. Completely disabling *gnome-keyring* breaks `nm-applet` from *Network Manager*. The solution is to disable both *ssh* and *gpg* components of *gnome-keyring*, but leave the main deamon enabled and running.

Here is the final solution:

    $ mkdir -p ~/.config/upstart
    $ rm ~/.config/upstart/gnome-keyring.override
    $ echo manual > ~/.config/upstart/gnome-keyring-ssh.override
    $ echo manual > ~/.config/upstart/gnome-keyring-gpg.override


[lubuntu]: http://lubuntu.net/
[lxde]: http://lxde.org/
[openbox]: http://openbox.org/
[de]: https://en.wikipedia.org/wiki/Desktop_environment#Desktop_environments_for_the_X_Window_System
[sshkeys]: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
[couple]: https://xkcd.com/1070/
[dtek]: http://dtek.net/blog/how-stop-gnome-keyring-clobbering-opensshs-ssh-agent-ubuntu-1204
[wbmdtek]: https://web.archive.org/web/20141006181510/http://dtek.net/blog/how-stop-gnome-keyring-clobbering-opensshs-ssh-agent-ubuntu-1204
[unity]: https://en.wikipedia.org/wiki/Unity_(user_interface)
[lubuntu-users]: https://lists.ubuntu.com/archives/lubuntu-users/
[arch]: https://wiki.archlinux.org/index.php/GNOME_Keyring#Disable_keyring_daemon
[wbmarch]: https://web.archive.org/web/20141228182841/https://wiki.archlinux.org/index.php/Gnome_Keyring#Disable_keyring_daemon
[Ubuntu Forums]: http://ubuntuforums.org/
[post]: http://ubuntuforums.org/showthread.php?t=1655397&p=10301640#post10301640
[wbmpost]: https://web.archive.org/web/20140819091832/http://ubuntuforums.org/showthread.php?t=1655397#post10301640
[ack]: http://beyondgrep.com/
[htop]: http://hisham.hm/htop/
[sessionjob]: http://upstart.ubuntu.com/cookbook/#session-job
[wbmsessionjob]: https://web.archive.org/web/20150402150055/http://upstart.ubuntu.com/cookbook/#session-job
[manual]: http://upstart.ubuntu.com/cookbook/#manual
[wbmmanual]: https://web.archive.org/web/20150402150055/http://upstart.ubuntu.com/cookbook/#manual
