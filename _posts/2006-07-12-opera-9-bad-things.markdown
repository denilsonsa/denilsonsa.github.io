---
layout: post
title: Opera 9 - bad things…
lang: en
tags:
- Opera
- User Interface
---

Every new major Opera version is the same thing: Opera breaks some expected or well-accepted behavior, and require us to either get used to it (until next major version, of course) or fiddle with different files to get back the old behavior.


## Hidden items at frame submenu

[See this forum post](http://my.opera.com/community/forums/topic.dml?id=134582) ([archive.org download](https://archive.org/details/myopera-forums-100001-200000)). In summary, frame submenu (from a right-click at document) does not have anymore "Save frame" option. No, we can't just open the frame at a new tab and save it there. Sometimes it does not work (javascript detecting frames, or some form-post page), beyond it is an extra work that was not needed before.

This change was done in Opera 8, "when Opera devs became crazy and removed tons of features" (like I've said at that post).

Well, at least those menu items are still available, but commented at `standard_menu.ini`. So, we can edit that file (or create a new menu set) and uncomment those entries. **PLEASE, OPERA DEVELOPERS, DON'T DELETE THOSE LINES! KEEP THEM COMMENTED BUT DON'T DELETE THOSE LINES.** Leave them commented, to allow people still know what to uncomment to unhide those features. Or, even better, add those features back.

## No more "Identify as …" items at Quick Preferences (F12) menu

Oh, this was good… This was very useful… But now it is gone… In place of "Identify as …", we need to use "Edit site preferences", which will store the settings.

But if we need quick-switching? Well… Then do not uncomment those lines, because numbers 1, 2 and 3 are understood the same way by Opera (identify as Mozilla). So, instead, add this line:

    Include, Identify As Menu

## Big mail header toolbar

Ouch! I could not believe when I opened my mail at Opera 9. The old, small, nice mail headers are gone! Now there is an "improved" mail header toolbar.

Now, addresses in mail header are really contact buttons. You can add them to contacts, or edit the preferences from there. Intuitive? Not so. I still think the most intuitive way would be just drag the contact (or the message) from message list to contacts panel.

If the subject is too large, then the date will be displayed below the subject, but with NOTHING at left of it, wasting a whole line of available space. A whole line that could have another fields displayed.

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/mailheadertoolbar-1.png" alt="">
</figure>

The same thing happens on IRC header toolbar, when room's topic is too large. This is an issue with how toolbar widgets are handled.

And what will happen I receive a message with a very big "To" or "Cc" field (with dozens of addresses there)? Very common when someone else tries to send a message to everyone in his list. Then, fortunately Opera will display a scrollbar for that field. Unfortunately, Opera becomes very slow. Unfortunately too, that interface is not easy to use. To find an address in that list, it is better to switch back to Opera 8 mail headers or right-click and select "View all headers and message.

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/mailheadertoolbar-2.png" alt="">
</figure>

Finally, but most important of all, the old Opera 8 interface did scroll with message body, while this new Opera 9 does not. This means we now have a very small useful area to read the message. This remembers OutLook Express 5 (or 4), it had this behavior (headers are fixed on screen, do not scroll). Oh, how I hate this behavior…

I've submitted this last issue as _bug-219999: New Opera 9 mail header toolbar wastes too much screen space_.

[shoust](http://my.opera.com/shoust) ([Wayback Machine](http://web.archive.org/web/20060621121634/http://my.opera.com/shoust/blog/)) told me about `opera:config#UserPrefs|ShowMailHeaderToolbar`. This way, we can disable that toolbar, but it will not re-enable automatically the old interface. To do that, we must mess with `mime.css` file (which supposedly has some comments about how to restore the old interface, but I did not find any).

## Annoying system tray icon

Now Opera has a system tray icon. Nice. It also does have a little mail icon on top of Opera's icon, probably indicating new messages (like that little exclamation point at mail panel icon). For our deception, it does not (**inconsistent interface!**). It appears to display the existence of unread message. Hey, I have tons of unread messages I won't read, so then I can't get rid of that mail notification at my system tray!

Since I can't get rid of mail icon, I want to get rid of the entire opera icon at system tray. Let's try it! Let's look for an option to disable it at preferences dialog. Found it? No. Let's try to find an option at some menu. Found it? No. Let's try again, looking more carefully. Found it? No. Finally, let's try `opera:config`. It must have an option to disable it. Found it? NO!!!

People at [#Opera](irc://irc.opera.com/Opera) told me to use `-notrayicon` parameter when launching Opera. Though this works, this is not a good solution, because this means I need to change all my Opera shortcuts, which includes one at [wmappl](http://wmappl.sourceforge.net/), plus two at [fluxbox](http://fluxbox.org/) menu, plus all other shortcuts at other window managers. But what happens when Opera is launched by another application? Of course, it will not have that parameter, and it will display the f… the fine icon.

I've submitted this issue as _bug-220000: There is no option to disable system tray icon_.

## Yellow tooltips, but white thumbnail tooltips?

Over your mouse on a mail tab. What happens? The tooltip is displayed with yellow background. Now over your mouse on a page tab. What happens? The tooltip has a white background. (inconsistent interface again!)

## Create search with empty keyword

A nice new feature is the ability to create a search from any form. This is very useful. However, if you _forget_ to fill the "keyword" field at "Search engine" dialog, Opera will not warn you. Why is this a problem? Go to Preferences → Search and try to find your search engine there. You simply are not able to find a search engine without a keyword (well, maybe you can, messing with `search.ini`).

## Closing panel also closes panel buttons

One thing I love to do is leaving the panel buttons always displayed. It allows me to access any one of them very fast. Unfortunately, at the new Opera 9 default toolbar, when closing a panel (using that close button), the panel buttons (AKA panel selector) will also be closed.

Though some people may like it, I find this very inconvenient. Fortunately for me, my toolbar set keeps the old behavior.

## No semi-transparent widgets on Linux

I know it is a little difficult to implement without X Composite extension, but currently Opera 9 does not support semi-transparent widgets on Linux platform. This leads to very ugly widget border. Anyway, this is not as important as other issues listed here.
