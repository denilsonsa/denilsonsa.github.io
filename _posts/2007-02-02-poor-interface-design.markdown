---
layout: post
title: Poor interface design
lang: en
tags:
- Java
- User Interface
- Opera
- WTF
---

I'm not (yet) a Java developer. In fact, I hate Java. But I started to learn J2ME to be able to write programs for cell phones (now I have a phone that has good J2ME support, large memory, somewhat fast processor…). So, I installed [NetBeans 5.5](http://www.netbeans.org/) and the NetBeans Mobility kit. Some people prefer [Eclipse](http://www.eclipse.org/), some prefer NetBeans. Since I never really used any of them, I tried NetBeans.


**Problem 1:** I can't type quotes inside any Java application. No joking, under GNU/Linux, the Sun Java virtual machine seems to have problems with [deadkeys](http://en.wikipedia.org/wiki/Dead_key), and I have [US-International](http://en.wikipedia.org/wiki/Keyboard_layout#US-International) keyboard.

* **Solution 1:** Open another program and copy/paste the quote character.
* **Solution 2:** Write a macro inside NetBeans so I can type a combination and it enters a quote.
* **Solution 3:** Press <kbd>AltGr+quote</kbd>. This works anywhere inside X.

Being a [Vim](http://www.vim.org/)-addicted user, I usually type <kbd>Ctrl+N</kbd> and <kbd>Ctrl+P</kbd> inside NetBeans… (If you don't know what those keys do, open Vim and type [`:help i_^N`](http://vimdoc.sourceforge.net/htmldoc/insert.html#i_CTRL-N))

But today I accidentally found two shortcuts that do exactly what <kbd>Ctrl+N</kbd> and <kbd>Ctrl+P</kbd> do inside Vim! They are <kbd>Ctrl+L</kbd> and <kbd>Ctrl+K</kbd>. Of course, I wanted to remap these two actions to the same keys as in Vim. Then I found one of the most scaring dialogs:

## The NetBeans keymap window

Before showing how it is, let's see how Opera Software designed that dialog in Opera browser for desktop.

<figure class="singleimage">
<img src="{{ site.baseurl }}/blog/images/Keymap_Opera2.jpg" alt="">
</figure>

Oh, how neatly arranged and organized. It has two columns, one for the keyboard shortcut and another for the action. It also has a quick-find field, an invaluable feature when the program has more than just a few actions and shortcuts. And this dialog is also used for editing mouse gestures. Very neat, well-thought, well-designed and easy-to-use.

Now beware! The NetBeans keymap window is coming! Don't say I haven't warned you!

<figure class="singleimage">
<img src="{{ site.baseurl }}/blog/images/Keymap_NetBeans2.jpg" alt="">
</figure>

All actions are available at this dialog, and they are divided into 16 categories:

<figure class="singleimage">
<img src="{{ site.baseurl }}/blog/images/Keymap_NetBeans1.jpg" alt="">
</figure>

The keyboard shortcut is just a string between square brackets concatenated to action name. There are no columns. There is no font change, no color change, no bold, no spacing… Nothing that you can easily spot.

Well, I discovered the <kbd>Ctrl+L</kbd> shortcut and wanted to change it, but I have no idea on what is the action it calls. I would seach… but there is no search field, and I won't waste my time looking at all actions, one-by-one.

Enough bad design for now. And if someone knows what are the actions of <kbd>Ctrl+L</kbd> and <kbd>Ctrl+K</kbd>, please tell me.

**P.S.:** Dear [Firefox](http://www.mozilla.com/firefox/) users, I'm so sorry about you. Your browser does not even have a shortcut editor. I know, you can search until you find an extension that adds that feature. And hope that extension works. Until then, you need to live with backspace not going back to previous page…
