---
layout: post
title: (Not) moving from beryl to compiz-fusion
excerpt: "Description of my first contact with Compiz Fusion. As a former Beryl user, I can compare them and have an opinion about which one of them is best (or which one I like more). Read this post to discover all bugs and annoyances I found in Compiz Fusion, and if I've really moved to it or if I went back to Beryl."
lang: en
tags:
- Compiz
- Gentoo
- Linux
---

Description of my first contact with [Compiz Fusion][] ([Wayback Machine][compiz fusion wbm]). As a former [Beryl][] ([Wayback Machine][beryl wbm]) user, I can compare them and have an opinion about which one of them is best (or which one I like more).

Read this post to discover all bugs and annoyances I found in Compiz Fusion, and if I've really moved to it or if I went back to Beryl.


Lately, [some gentoo developer has messed with beryl and compiz-fusion packages](http://bugs.gentoo.org/show_bug.cgi?id=198248). Trying to fix that, the "solution" was to remove `beryl-0.2.1` packages from portage.

Last week, the `libwnck` update has broken emerald and some part of [Beryl][] ([Wayback Machine][beryl wbm]) on my system. So, I thought this was a good time to try out the [Compiz Fusion][] ([Wayback Machine][compiz fusion wbm]) 0.6.x.

Once I've added all the required packages to `/etc/portage/package.keywords`, the emerge process was painless and fast. Well, almost. `compiz-fusion` tried to update `emerald-themes` to latest version, but didn't try to update `emerald` itself. [I filed a bug about this](http://bugs.gentoo.org/show_bug.cgi?id=201507), and they just said _“We don't care”_. Well, this is not good… I didn't like his answer at all, it seems as the devs don't care about users.

Anyway, I've updated emerald package manually, after all, that's all I could do. Then, I tried to start `compiz-fusion` (note that I don't use any session manager, like _gdm_ or _kdm_):

    startx `which compiz`

And then, also from the console terminal (<kbd>Ctrl+Alt+F[1-6]</kbd>), I started an xterm:

    DISPLAY=:0.0 xterm

Ok, let me try it on the graphics screen… Huh? Nothing works? What? Why? WTF?

Ok, let me try again:

    startx /usr/bin/compiz-start

Huh, nothing again? WTF?!??!??

(Honestly I don't remember if what I describe next happened with the first or the second command-line, or both)

Ok, let me kill this f… fine thing. <kbd>Ctrl+Alt+Backspace</kbd>… Huh? It does not work!? Damn it!

Ok, I have [SSH access from my cellphone](http://www.midpssh.org/) ([Wayback Machine](http://web.archive.org/web/20090707182943/http://www.midpssh.org/)), I may try that. What? Could not connect? Is the _sshd_ on my machine down? No, wait, just the GSM/GPRS signal is not strong enough here. Let me walk to somewhere else and try again. Hum… Ok, I'm in. Now I need to type… `killall -9 compiz` Typing with a [cellphone keyboard]({% post_url 2006-12-25-what-i-don-t-like-on-k750i %}) sucks. Ok, let me walk back to the computer to see if it has worked… Yes, I got my console terminal back! Linux is great!

But, what the fuck has just happened? Compiz did not work! I saw no window decorations (I've tried starting `emerald` and `gtk-window-decorator`). I could not move any window (<kbd>Alt+left click</kbd> and drag). I has just failed to work at all!

Ok, let me calm down and try to look for help… Opening a X session with just an xterm, no window manager:

    startx `which xterm`

This sucks, but at least I can test running the window manager easily, since no other window manager is running. Huh, let me start Firefox and search a little… [Gentoo-wiki](http://gentoo-wiki.com/Compiz_Fusion) ([Wayback Machine](http://web.archive.org/web/20071111004331/http://gentoo-wiki.com/Compiz_fusion)), [Gentoo Xeffects wiki](http://wiki.gentoo-xeffects.org/Compiz_Fusion) ([Wayback Machine](http://web.archive.org/web/20071108125729/http://wiki.gentoo-xeffects.org/Compiz_Fusion)), [Compiz Fusion FAQ](http://wiki.compiz-fusion.org/FAQ) ([Wayback Machine](http://web.archive.org/web/20071207204606/http://wiki.compiz-fusion.org/FAQ)), [Compiz Fusion Troubleshooting](http://wiki.compiz-fusion.org/Troubleshooting) ([Wayback Machine](http://web.archive.org/web/20071207204642/http://wiki.compiz-fusion.org/Troubleshooting))… Nothing! Damn… I'm starting to really miss Beryl.

Well, I have a friend who installed Compiz Fusion a few weeks ago, also on a Gentoo system. Let me login at GMail inside Firefox and hope that he is online. Yeah! I'm feeling lucky! He is online! A few minutes later, the solution:

    compiz --replace ccp

What the fuck is `ccp`? Well, we don't know (yet), but it is something that makes Compiz work!

After looking for _ccp_ at Compiz-related files, I discovered it is the _CompizConfig Plugin_. Well, whatever.

But, if it is “required”, why do I need to specify it at the command-line? And why the fuck they ship a `compiz-start` shell script that is broken? (mental note: bug report this later)

Well, Compiz is finally working. Now I can configure it. Wait, did I say “can”? Sorry, I wanted to say that I NEED to configure it. Right now it is too slowish, and I don't like the default shortcuts. I usually set all window manager-related shortcuts to the [Win/Super key](http://en.wikipedia.org/wiki/Windows_key), so they won't ever interfere with applications shortcuts, and also it makes sense (_windows_ key for _window managing_ functions).

By the way, talking about slowish, I felt it was freaking slower than Beryl. Fortunately, it started to feel a lot smoother after changing these settings:

    General Options
     '--> Display Settings
           |--> Detect Refresh Rate = NO
           |--> Refresh Rate = 60
           '--> Sync to VBlank = NO

Looking at my Beryl settings, looks like I've also changed these in there. (in case you don't know how to configure Compiz, just run `ccsm`, which is the _CompizConfig Settings Manager_)

**Annoyance/bug #1** Now I need to go through all or most of Compiz settings and fine-tune them. Hum… That reflection below the cube was a nice addition… Wait? Was it? It looks too jumpy for me. Whenever I rotate the cube, it zooms in and out automatically (and I don't like it, does not look good to me). Also, the reflection is really jumpy below the cube. Or the cube is jumpy above the reflection. Sorry, but I really didn't like it, and I've tried all four _Reflection modes_ in [Cube Reflection](http://wiki.compiz-fusion.org/Plugins/Cube#Reflex) ([Wayback Machine](http://web.archive.org/web/20071207204626/http://wiki.compiz-fusion.org/Plugins/Cube#Reflex)). And more, I feel this reflection slows down the cube on my system (Pentium III 800, GeForce FX 5500).

**Update:** Just some clarification. I also think I didn't like the reflection because I use a space skydome, and thus the reflection didn't look appropriate. This annoyance is more like a personal taste. The reflection looked so cool on screenshots, but I didn't like it when I actually tried it.

Ok, bye bye, _Cube Reflection_. What more may I configure? Hum, I feel 4 faces (4 pseudo-workspaces) are not enough for me. Then I've increased this number to 5 (_General Options → Desktop Size → Horizontal Virtual Size_). Actually, I really wanted 6, but I mistakenly set it to 5. This was “good”, because I found another bug:

**Annoyance/bug #2** Whenever the number of cube faces is odd, the cube caps are shown (even if the _Cube Caps_ is disabled); and if the cube is set to _Inside Cube_, then the cube caps are wrongly drawn. See this screenshot:

<figure class="singleimage">
<img src="{{ site.baseurl }}/blog/images/compiz-fusion_odd_inside_cube_caps.jpg" alt="Inside Cube screenshot showing the bottom cube cap being drawn with the corner at the center of the cube face, instead of the cap corner being aligned at the face corner.">
</figure>

This is a bug, it must be fixed, but it does not directly affect me, because I use 6 cube faces, I disable the drawing of the cube caps and I don't use _Inside Cube_.

**Annoyance/bug #3** Now, talking about the cube… There is one thing which is annoying me… In Beryl, the cube zoomed out whenever I started rotating it with the mouse drag motion. However, if I just switched to another cube face (using either keyboard shortcuts or mouse wheel, or even dragging and dropping a file onto another application at another face), then the cube just rotated but did not zoom-out. In my opinion, this gives the best visual effect. It is a simple motion, easy to the eyes. However… Somehow this has been removed in Compiz Fusion. The cube ALWAYS zooms out whenever it rotates.

Someone at [#compiz-fusion](irc://irc.freenode.net/compiz-fusion) told me to look at _Auto zoom only on Mouse Rotate_, from _Cube Reflection_ plugin. However, this is not what I want because I don't use this plugin and because I'm talking about the "fixed" zoom, and not the "auto" zoom. The fixed zoom amount is set at _Rotate Cube → Zoom_.

By the way, the same person at [#compiz-fusion](irc://irc.freenode.net/compiz-fusion) told me that the `compiz-start` shell script is not part of upstream compiz-fusion package, but was added by Gentoo devs. He also told me that script was written by the time of compiz-0.2.x (while current one is 0.6.x) and, thus, it is now obsolete or incorrect. There is already a [bug report about the compiz-start script](http://bugs.gentoo.org/show_bug.cgi?id=197455), but it seems that no one cares, or no one wants to fix.

Anyway, back talking about the cube. In Beryl, I used to middle-click on the desktop to drag-rotate the cube. Also, I could use the mouse wheel on the desktop to switch to the next or previous cube face. Then I missed this feature at Compiz Fusion. Some minutes later, I found it was moved to a plugin at its own. It's called [Viewport Switcher](http://wiki.compiz-fusion.org/Plugins/ViewportSwitcher) ([Wayback Machine](http://web.archive.org/web/20071117225444/http://wiki.compiz-fusion.org/Plugins/ViewportSwitcher)). Damn, that's a really bad name. If I could, I would name it as “Cube Desktop”, or “Desktop Actions”. Anyway, it allows me to set actions on mouse clicks on the desktop.

**Annoyance/bug #4** The default _Viewport Switcher_ settings, however, don't work out of the box with cube. I needed to unmap _Move Next/Prev_ actions and use _Move Left/Right_. Now the mouse wheel on the desktop rotates the cube…

**Annoyance/bug #5** …well, almost. It rotates the cube almost always, but sometimes it just… fails. I found this happens because it does not allow the cube to wrap around. I mean, if you are at the first cube face and try to rotate left (thus, going to the last face), then it won't work with this plugin, even though it does work with keyboard shorcuts from _Rotate Cube_ plugin.

**Update:** It also seems that sometimes the actions on desktop stop working, and then they start working again out of nowhere. I feel this plugin is a bit too buggy.

**Annoyance/bug #6** Enough? Not yet. I'm still missing one feature from the Beryl's cube: the 3D Windows. I simply haven't found it anywhere in Compiz Fusion. Although it is mostly eye-candy, it does give that feeling of windows really piled (or floating) on top of each other. It also allows me to quickly see what's on a window below, by just carefully rotating the cube. Right now I've discovered that the [3D Windows plugins is not part of any package yet](http://wiki.compiz-fusion.org/Plugins/Cube#3d) ([Wayback Machine](http://web.archive.org/web/20071207204626/http://wiki.compiz-fusion.org/Plugins/Cube#3d)). That's sad, but at same time it's funny to see that the screenshot from the [Compiz Fusion Wiki main page](http://wiki.compiz-fusion.org/) ([Wayback Machine](http://web.archive.org/web/20071206083934/http://wiki.compiz-fusion.org/)) uses a plugin that is not actually available (yet) to the users. Looks like misleading advertising.

Ok… So many bugs and annoyances until now, but I guess I can live with them. Well, at least I hope so, since they all are minor (but important) things. And note that so far I've only talked about cube-related things!

Beware, I think the next bugs/annoyances are much more serious and much more annoying!

**Annoyance/bug #7** There is one thing that I could not understand why it happened. Every now and then, the mouse cursor just disappears! Well, it disappears but the mouse still works, and if I move to some other positions (probably positions that would change the pointer image), then it is shown again. But, if I move back to where i has disappeared, it disappears again. I really can't understand this, and I guess nobody wants to use a system with an invisible mouse pointer.

**Update:** This is a known issue with [_Enhanced Zoom Desktop_ + _Hide original mouse pointer_ + animated cursors](http://dev.compiz-fusion.org/~kristian/2007/08/25/xfixes-the-problem-and-the-dirty-workaround/) ([Wayback Machine](http://web.archive.org/web/20080607015535/http://dev.compiz-fusion.org/~kristian/2007/08/25/xfixes-the-problem-and-the-dirty-workaround/)).

I think this might be related to the XCursor theme that I use: [A-1]({{ site.baseurl }}/blog/files/A-1_fixed.tar.bz2). I probably got this theme from [GNOME-Look](http://www.gnome-look.org/content/show.php/A-1?content=12651) ([Wayback Machine](http://web.archive.org/web/20090708000006/http://www.gnome-look.org/content/show.php/A-1?content=12651)) or [KDE-Look](http://kde-look.org/content/show.php/A-1?content=12651) ([Wayback Machine](http://web.archive.org/web/20070813090407/http://www.kde-look.org/content/show.php/A-1?content=12651)) and then modified one of the cursors to fix its hot-spot. Maybe Compiz Fusion is hiding the mouse pointer whenever it should be displayed as “busy” (which, by the way, is when the pointer should be displayed animated). Well, I don't know exactly why this happens, but once it starts happening, it will continue happening untill I close the session. I can usually see this when I'm on Opera o Firefox browser.

I use the [Trailfocus](http://wiki.compiz-fusion.org/Plugins/Trailfocus) ([Wayback Machine](http://web.archive.org/web/20071120034154/http://wiki.compiz-fusion.org/Plugins/Trailfocus)) plugin since Beryl. It is nice, it makes the “less used windows” semitransparent or less saturated. It works by keeping a list of recently used windows and fading them as they become farther from the top of this list. Not only it does look cool, but I feel it gives me a hint of which windows I haven't payed attention to recently.

**Annoyance/bug #8** But, for some reason, this plugin does not appear to be tracing the _xterm_ windows. I'm not sure if this worked on Beryl, because on Beryl I had set the xterm opacity to 90%, so maybe Trailfocus didn't (or couldn't) change the opacity then. But, in Compiz Fusion, I haven't set anything like that yet, and xterm windows are always 100% opaque.

**Annoyance/bug #9** Talking about setting some fixed opacity values for some windows, here is how we do it: _General Options → Opacity settings → Window opacities → Add/Edit_. Then you write a window-matching string (more on this later) and set the desired opacity value. However… The opacity slider in this dialog goes from -32K to 32K! I guess someone forgot to set the correct limits here.

**Annoyance/bug #10** Now, talking about that [window-matching string](http://wiki.compiz-fusion.org/WindowMatching) ([Wayback Machine](http://web.archive.org/web/20071209224917/http://wiki.compiz-fusion.org/WindowMatching))… This is a very powerful and flexible feature and I once wanted to be available on Beryl. This is basically a way to match a window by using a expression with boolean operators, comparisons, and some other things. Very powerful. However, very programmer-oriented (hey, I'm programmer). The end-user (but, for compiz-fusion, I'm not a programmer, I'm an end-user), however, won't find it is intuitive. I think the basic idea of this feature is correct, just the way we edit it is wrong. I think there should be a dedicated editor for this, that would allow us to specify things easily, with built-in help and built-in list of choices. The editor should also allow the user to hand-write or hand-tune the string using a **multi-line** textbox (the current single-line textbox is awful to use).

**Annoyance/bug #11** Well, since we were talking about opacity and trailfocus, let me describe one more issue… If you use [Gimp](http://www.gimp.org/), [Inkscape](http://www.inkscape.org/) or any other graphics editor, you will probably want to set their windows to 100% opaque (maybe leaving their toolboxes transparent). If you use the _Trailfocus_ plugin, like I used, then whenever you open a dialog on Gimp (e.g. _Color curves_ dialog), the main image becomes transparent. In Beryl, I could use <kbd>Super+Alt+Mouse Wheel</kbd> to change opacity of the windows on-the-fly. Probably because of a bug, whenever I used this feature on a window, that window would stop receiving effects from _Trailfocus_ plugin. This means that, in Beryl, I could easily change opacity on a non-foreground window and the opacity would be kept fixed to that value forever (well, until the window was closed). Even though this might have been a bug in Beryl, it was damn useful to use on Gimp windows, as well as some other windows that I wanted to be kept opaque now, but I didn't want to write a rule to match all similar windows forever.

In Compiz Fusion, however, this “bug” seems to have been fixed. That shortcut does not increase anymore the opacity of a window. In other words, the _Trailfocus_ seems to be “dominant”, its effects are stronger than the effects from that shortcut. This implies that Gimp windows are now transparent unless I learn how to write those window-matching strings or unless I disable the _Trailfocus_ plugin.

**Annoyance/bug #12** Thinking about that issue, I found the [Opacify](http://wiki.compiz-fusion.org/Plugins/Opacify) ([Wayback Machine](http://web.archive.org/web/20071124035109/http://wiki.compiz-fusion.org/Plugins/Opacify)) plugin. Looking at its name, I guess it was meant to make windows opaque. Probably making them opaque by moving the mouse over them. Damn, I was wrong. Very wrong. This plugin makes many windows completely transparent, whenever you leave your mouse over some other window. This is meant to be able to see that other window without changing focus to it. But I didn't like it. The first time I used it I felt like “Hey, this f… thing disappeared with other windows! Damn, this is not what I want, I'm probably going to accidentally trigger this many times! I'm going to disable this now and never use it again!” Oh, and by the way the opacity of the window that is overed by mouse is not affected at all. If I could, I would name this plugin as “Transparentify” or “See-thru”.

Right now, I'm guessing I'm going to live with transparent Gimp windows, unless I go to another window manager or unless I learn how to match just the Gimp windows.

**Update:** According to Fyda from [#compiz-fusion](irc://irc.freenode.net/compiz-fusion), `(class=Gimp & role=gimp-image-window)` should match the window (he spent about 10 minutes testing that with the completly unfriendly `xprop` tool). Anyway, I completely agree on what he said: _Of course, having to specify this for every possible app is just a pain…_

**Annoyance/bug #13** Since I was talking about Gimp, there is one feature that I love on it: the detachable menus. We can click on that horizontal bar with an arrow (which is the very first menu item) and then that menu will be detached. This means it will work like a window, and we will be able to move it around and leave it at some quick-to-access place. A simple but excellent time-saver, much better (easier and faster) than navigating through the same menus all the time (and this is one of the things I missed in Photoshop, when I used it for the first time). Let me try it on Compiz Fusion! I deatch a menu then I try to move and… and… and…??? It does not move at all?!?!?! No, really, no… I don't believe… NOOOOO!!!!! Compiz Fusion has just broken a killer-feature from Gimp! (oh, by the way also available on other applications, like [gvim](http://www.vim.org/))

That's enough. I think I could live with most of those bugs. Live sadly, and would probably be a lot angry sometimes, but I guess I could live with them. But this one… I can't. It is one of the Gimp features I use most. I can't go on with Compiz Fusion unless this gets fixed.

Asking about this at [#compiz-fusion](irc://irc.freenode.net/compiz-fusion), one guy told me he not only could move the detached menu, but also the menu had window decorations. Mine doesn't (even though [Window Decoration](http://wiki.compiz-fusion.org/Plugins/Decoration) ([Wayback Machine](http://web.archive.org/web/20071116171319/http://wiki.compiz-fusion.org/Plugins/Decoration)) plugin has _any_ as _Decoration windows_ option). Another guy, however, confirmed that he couldn't move the menu.

On older [fluxbox](http://fluxbox.org/) ([Wayback Machine](http://web.archive.org/web/20071019215856/http://www.fluxbox.org/)) versions, the detached menus had window decorations, which was really nice, since I could shade them, leaving just the title visible. Very useful. On Beryl, they didn't have window decorations, but at least I could move them, and I could find them easily using [<kbd>Alt+Tab</kbd>](http://wiki.compiz-fusion.org/Plugins/Switcher) ([Wayback Machine](http://web.archive.org/web/20071130080122/http://wiki.compiz-fusion.org/Plugins/Switcher)) (in my case, <kbd>Win+Tab</kbd>) or using [Scale](http://wiki.compiz-fusion.org/Plugins/Scale) ([Wayback Machine](http://web.archive.org/web/20071208035039/http://wiki.compiz-fusion.org/Plugins/Scale)) (that [Exposé-like](http://www.apple.com/pro/tips/switch_expose.html) ([Wayback Machine](http://web.archive.org/web/20071102003738/http://www.apple.com/pro/tips/switch_expose.html)) feature).

Ok, although the last bug/annoyance was the last straw, there are still two more I need to comment.

**Annoyance/bug #14** I like the [Wobbly Windows](http://wiki.compiz-fusion.org/Plugins/Wobbly) ([Wayback Machine](http://web.archive.org/web/20071125104308/http://wiki.compiz-fusion.org/Plugins/Wobbly)). They are mostly eye-candy, but are cool and don't disturb me. Also cool is that it can have "window snapping" feature, which means a window can stick to another or to a screen edge. The problem is that this feature is broken in Compiz Fusion, or broken in _ccsm_ (CompizConfig Settings Manager). In _Wobbly Windows → Actions → General → Snap windows_, we are supposed to set which shortcut should toggle between snapping and no-snapping behavior. That would be excellent, if it allowed for the <kbd>Shift</kbd> key. It seems the _ccsm_ is buggy and does not accept this key as a shortcut. To make things more weird, the default value of this shortcut is <kbd>Shift</kbd>. Since I didn't want to hand-edit the config file (which could be overwritten next time I run _ccsm_), I'm going to miss this feature.

**Annoyance/bug #15** Compiz Fusion has a nice and flexible [Color filter](http://wiki.compiz-fusion.org/Plugins/Colorfilter) ([Wayback Machine](http://web.archive.org/web/20071123221240/http://wiki.compiz-fusion.org/Plugins/Colorfilter)) plugin. It basically allows you to apply one color filter (defined in one external file) to one or more windows. This can go from coolness (sepia, grayscale, green matrix-like) to useful (people with sight problems might want some filters enabled, and also people with perfect vision will be able to simulate some color blindness).

Ok, this is nice, but the point is that it comes pre-configured with 5 filters (negative, negative-green, blueish-filter, sepia, grayscale) but only 3 of them (grayscale, negative, negative-green) are actually installed at `/usr/share/compiz/filters/`! What's more, there is one installed (contrast) that is not listed by default. I was expecting these things being set correctly out of the box.

## Conclusions

Compiz Fusion has some nice improvements and some nice new plugins. However, I feel it is in a more rough shape than beryl 0.2.1 was. Heck, as you can see, I found about 15 annoyances/bugs (plus the first two about starting compiz, which I haven't counted) and I was using it for just 3 days (actually, 3 nights).

Or maybe I am too used to beryl.

But it is also a bit unfair, because today I can compare Compiz Fusion to Beryl. In past, however, I could only compare Beryl 0.2 with Beryl 0.1 (which was completely buggy). Probably, if I wasn't a Beryl user, I wouldn't have noticed many of these issues.

Anyway, I'm not going to use Compiz again unless someone confirms me that at least most of these annoyances/bugs are fixed. Until that time, I'm going to stick to beryl.

Since it has been removed from official portage and it is not available at gentoo xeffects overlay, I'm going to get a copy of the required files from CVS. If you want to do so, [start here](http://sources.gentoo.org/viewcvs.py/gentoo-x86/x11-wm/beryl/?hideattic=0) and go downloading all you need.

P.S.: I would post all of these annoyances/bugs to Compiz Fusion bug report, since I'm not used to the Compiz Fusion project, I would prefer if someone else posted them.

## Other comments

A few minutes after I posted this, we started talking at [#compiz-fusion](irc://irc.freenode.net/compiz-fusion). I think there are a few very important points cited there that I would like to add here (being somewhat semi-off-topic):

> \<Fyda> CrazyTB: As for the Viewport Switcher plugin -- I think architecturally it was a good idea to move that function into its own new plugin. But the problem is that users also have to adapt to the plugin architecture.
>
> \<Fyda> CrazyTB: If we had a sane, user-friendly config tool, it'd take the confusion out of that. Users wouldn't have to know about how plugins depend on each other, or which modules do what.
>
> \<Fyda> CrazyTB: But, CCSM is not really an end-user tool; there's a reason Ubuntu packages it as "Advanced Compiz Settings Manager" or somesuch :P
>
> \<amphi> Fyda: people keep saying this, I don't know why - it's a friendly gui configurator - or perhaps 'end user' is some special term I don't understand
>
> \<CrazyTB> Fyda: ccsm is not too bad. It is somewhat like beryl-settings. Ok, it's an advanced config tool, but it is already years ahead of plaintext files or gconf.
>
> \<Fyda> amphi: You're right, I'm using the term inaccurately. Perhaps "average user".
>
> \<Fyda> amphi: I was borrowing crdlb's words
>
> \<Fyda> CrazyTB: I've seen complaints about how user-unfriendly it is. "Too many plugins exposed! Too many options! Just give me sane defaults!"
>
> \<amphi> Fyda: 'greatly below average' I would hope, unless things have degenerated greatly in recent times
>
> \<CrazyTB> Fyda: sane defaults is something very important.
>
> \<Fyda> amphi: The problem, I think, is that we do not see "average users" here at all. This is IRC.
>
> \<CrazyTB> But ability to fine-tune things is nice
>
> \<Fyda> CrazyTB: Very much so.
>
> \<CrazyTB> the *need* to fine-tune things is not nice.
>
> \<amphi> Fyda: the problem is, AFAICS, people who are not prepared to explore, read, or think

## (Update) Steps to re-emerge beryl on Gentoo

I'm supposing that you already have an [overlay](http://gentoo-wiki.com/Portage_Overlay) ([Wayback Machine](http://web.archive.org/web/20071128012545/http://gentoo-wiki.com/Portage_Overlay)) set on your system. Also, I'm supposing you have already copied all beryl-related ebuilds from [gentoo CVS](http://sources.gentoo.org/viewcvs.py/gentoo-x86/x11-wm/beryl/?hideattic=0).

Add this to your `/etc/portage/package.unmask` and to `/etc/portage/package.keywords`

    #Beryl Core
    =x11-wm/beryl-0.2.1
    =x11-wm/beryl-core-0.2.1
    =x11-plugins/beryl-plugins-0.2.1
    =x11-plugins/beryl-plugins-0.2.1-r1
    #=x11-plugins/beryl-plugins-unsupported-0.2.1
    #x11-plugins/beryl-plugins-vidcap
    #x11-plugins/beryl-dbus
    =x11-misc/beryl-manager-0.2.1
    =x11-misc/beryl-settings-0.2.1
    =x11-misc/beryl-settings-bindings-0.2.1
    #=x11-misc/xwinwrap-1.1.1_alpha20060318-r2

    #Window Decorators
    =x11-wm/emerald-0.2.1
    =x11-themes/emerald-themes-0.2.1
    =x11-wm/heliodor-0.2.1
    =x11-wm/aquamarine-0.2.1

Add this to your `/etc/portage/package.mask`

    # Masked because x11-wm/emerald-0.2.1 fails to build with these versions.
    >=x11-libs/libwnck-2.20


[Compiz Fusion]: http://www.compiz-fusion.org/
[compiz fusion wbm]: http://web.archive.org/web/20071206083914/http://www.compiz-fusion.org/
[Beryl]: http://www.beryl-project.org/
[beryl wbm]: http://web.archive.org/web/20071208001657/http://www.beryl-project.org/
