---
layout: post
title: What I don't like on K750i
lang: en
tags:
- Mobile
- Sony Ericsson
- Nokia
- User Interface
---

This month I bought a [Sony Ericsson K750i phone](http://www.sonyericsson.com/cws/products/mobilephones/overview/k750i) ([Wayback Machine](http://web.archive.org/web/20070804153157/http://www.sonyericsson.com/cws/products/mobilephones/overview/k750i)). It is a very good phone, with the following features:


* 176x220 pixels at 65536 colors LCD (specifications and reviews say it has 262144 colors, but AFAIK J2ME can only use 64K colors)
* Lithium battery (which is also recharged when you plug the USB cable)
* GSM, with support for internet connection using GPRS
* XHTML browser with SVG Tiny support
* Bluetooth v2.0
* Infrared
* USB cable (works as USB 1.0 or 1.1 device)
* Stereo headphone
* A proprietary port to connect headphones, USB cable or battery charger
* 34MB of internal phone memory
* Reads Memory Stick Pro Duo cards with at most 2GB (comes with a 64MB one, and of course I bought a 2GB one)
* Themes support
* T9 support (I guess all non-ancient phones have this)
* Allows you to edit a phone number (from recent calls or from contact list) before dialing
* 2 megapixels camera (1632x1224, 640x480 or 160x120 resolutions) with auto-focus
* Can record videos at 128x96 or 176x144
* Both photos and videos support digital zoom, night mode and macro mode
* Camera LED light (not exactly a camera "flash"), which can also be used as a flash light, or as SOS light
* Camera lens is protected by a sliding cover
* FM radio (only when headphone is plugged, because the cord acts as an antenna)
* MP3 player
* Allows the use of MP3 player and radio even with phone locked (only when headphone is plugged)
* Java MIDlets with MIDP 2.0 and CLDC 1.1
* It can run Java MIDlets that use Nokia API
* It can install MIDlets using only the JAR file, the JAD is not necessary

Its Java (J2ME) implementation supports the following JSRs:

* JSR-75 (PDA optional packages; in other words, access to filesystem and contact list)
* JSR-82 (Bluetooth)
* JSR-118 (MIDP 2.0)
* JSR-120 (Wireless Messaging API; in other words, send and receive SMS)
* JSR-135 (Mobile Media API; in other words, access to phone camera)
* JSR-139 (CLDC 1.1)
* JSR-184 (Mobile 3D Graphics API; although not as fast as most old computers, it can run most 3D MIDlets at an acceptable speed)
* JSR-185 (Java Technology for the Wireless Industry; I have no idea what this means)

Its _organizer_ has the following features:

* Alarms (including recurrent alarm)
* Calendar (including month and week views)
* Tasks (something like to-do list)
* Notes (just plain text notes)
* Timer
* Stopwatch
* Calculator (with ÷ × - + %)

It also has:

* Sound recorder (allows you to record your voice for quick memos, and record your calls)
* Bluetooth remote control (allows you to control a computer using bluetooth, useful in presentations or to control your computer media player)

Note it **cannot** use infrared to control other devices (like a TV set or DVD). Infrared is used only for communication (file/contact/etc. transfer) between phone and computer or phone and phone.

_Pause for breath…_

<figure class="singleimage polaroid">
<img src="{{ site.url }}/blog/images/k750i-01.jpg" alt="">
</figure>

Damn! It has tons of very good features! But in this article, I intend to point what are the worst things, the most annoying things in Sony Ericsson K750i.

## Previous Mobile Phones

Long time ago, I had a Siemens C45. That one was a bad phone. Slow, bad user interface, bad games, bad battery… When I stopped using it, its battery could not last even 24h of standby. In fact, not even 12h. When the battery was new, it could not last 2 or 3 days.

That user interface was really bad. Sometimes you pressed the right [softkey](http://en.wikipedia.org/wiki/Softkey), sometimes the left softkey. So, when doing something, you needed to keep moving your finger from one key to another…

However, Siemens C45 had "Notes" feature, to allow me write small text notes. I missed this feature on my next phone (and now I have it again with K750i).

Then I had a [Nokia 3100](http://en.wikipedia.org/wiki/Nokia_3100). Oh, that was a good phone. Excellent interface (some shortcuts available, but most things I could do pressing only one softkey a few times and sometimes the arrow keys). This was lots of times better than Siemens interface. It was also fast, no need to wait as much as that Siemens. I don't want to use a Siemens phone ever again!

Nokia 3100 also had support to GPRS and Java MIDlets. I downloaded a couple of games and applications to it, including, of course, [Opera Mini](http://www.opera.com/mobile/mini/other) (basic version). Although it was good, it only supported J2ME MIDP 1.0, which is very limited. It also had small amount of memory for MIDlets, so Opera Mini always runned out of memory on that phone.

It came with headphone (+ mic) to allow talking without holding the phone near your ear. That was a little nice feature, but I used it only a few times in two years. Unfortunately, it did not come with USB cable (which I bought later), and the USB connection allowed me to only backup my contact list, backup the SMS inbox and backup some files (ringtones, images). In addition, there is no good support for this phone on GNU/Linux system ([gnokii](http://www.gnokii.org/) ([Wayback Machine](http://web.archive.org/web/20061220092722/http://www.gnokii.org/)) was the only program that half-worked, [gammu](http://www.gammu.org/) ([Wayback Machine](http://web.archive.org/web/20061219014009/http://www.gammu.org/wiki/index.php?title=Main_Page)) did not work).

After Nokia 3100, I got this Sony Ericsson K750i.

I also had contact to a Siemens A50, but fortunately never used it. Wow, it was even worse than Siemens C45! It had almost all C45 features, except the "Notes" (they removed the only feature I liked!) and one bad game nobody played.

## What I don't like on K750i

### 5-way joystick/navigation button

I don't like the idea of 5-way joystick/navigation button in general. I think it is too easy to accidentally move the joystick to sides while trying to press it in middle. It is so easy that it happens all the time. I guess my mom won't like that too, whenever she needs/wants to use this phone.

Unfortunately, most phones have this (but Nokia 3100 didn't have), and we have to get used to it. Fortunately, the K750i joystick is a lot better than Nokia 3100 4-way navigation key.

### Bad contact list

The Sony Ericsson contact list is limited and not very practical. I miss Nokia's contact list.

1. There are "extra fields", like address, info, birthday, e-mail and website. However, we can't see these fields without editing the contact. E-mail and website is shown without editing, but most of time it does not fit in screen width and is cropped.
2. We need to press 4 keys to edit a contact: "More" (right softkey), down, down, "Edit contact" (left softkey or joystick center).
3. All fields have a very small limit of characters. Name field has a 30-char limit, address (street) field has a 25-char limit (making this field completely useless).
4. There are 5 phone number types: mobile, home, work, fax and other. However, you can only add one number of each type (so, each contact can have at most 5 numbers). If you (like me) have a contact who has more than one phone number of same type, you will need to add it to the wrong type, or even create another contact.
5. While you can mark several contacts at once, you can only do that to send a message. You cannot delete or copy more than one contact at same time.
6. You cannot copy contacts between phone memory and SIM card intuitively. The most intuitive way would be: select a contact → More → Copy to SIM/phone. However, we are forced to do: Options → Advanced → Copy from/to SIM → Copy all/Copy a number → select the contact.
7. We cannot move contacts between phone memory and SIM card.

We can compare it to Nokia 3100 contact list:

1. Only the contact name is shown, and the left softkey is "Details", which shows all fields. If the value is too big for screen (and is cropped), you can always use Options (left softkey) → View (4th item).
2. You don't enter "contact edit mode", you just edit each field as needed. And "Edit" is the first item at "Options" menu when viewing contact details.
3. Nokia address field has a 60-char limit.
4. Contacts can have any quantity of any field. (ok, there must be some limit, but I never reached it)
5. Nokia can't mark multiple contacts.
6. Select a phone number in contact details → Options → Copy number → Keep original.
7. Select a phone number in contact details → Options → Copy number → Move original.

However, at least Sony Ericsson contact list allows you to use T9 while editing a contact, while Nokia doesn't.

### USB connection requires drivers in Windows

Because phone identifies itself as having many USB interfaces (to act as a modem, as a mass storage device, and as a serial device), Windows asks to install drivers. This way, I can't use my phone with 2GB Memory Stick as a [USB flash drive](https://en.wikipedia.org/wiki/USB_flash_drive).

In fact, this is not a problem with this phone, but a problem with Windows. I can use it as a USB drive with no problems at GNU/Linux.

### The big screen does not mean more space

If the screen is bigger, then that should mean we can have more items at same time, right? Wrong. The K750i text font is big. While on Nokia 3100 we had 5 items at 128x128 screen, at K750i with 176x220 screen we have… 6 items at file manager, 5 items almost everywhere else, and only 4 items at "Shortcuts" menu.

### Ugly number font

The (big) font used for numbers is ugly, confusing, and hard to read (mostly due to its mix of thin and thick lines).

<figure class="singleimage polaroid">
<img src="{{ site.url }}/blog/images/k750i_number_font.jpg" alt="">
</figure>

### Not very good missed calls list

If someone calls you more than once (and you miss those calls), K750i will show the contact name, date and time of call, and how many times you missed it (if more than one). However, it will show only one date/time. Nokia 3100 allowed you to see the time of each missed call (even from same contact).

On the other hand, it can show all calls (received, missed and dialed) in only one list (which sometimes can be useful) or in separated lists.

### Not very beautiful or intuitive menu icons

I don't like the main menu icons. They are not very intuitive. The Radio icon looks like a [clapperboard](http://en.wikipedia.org/wiki/Clapperboard). The Calls icon looks like "Phone info". The Contacts icon (when not selected), does not look like anything.

<figure class="singleimage polaroid">
<img src="{{ site.url }}/blog/images/k750i_main_menu.jpg" alt="">
</figure>

### Cannot customize icons/sounds with themes

We can use themes! Nice! However, we can't change phone icons or phone sounds with themes. That is only (half-)possible by hacking the phone, flashing its memory while in "service mode".

### Cannot disable menu animation

I don't like menu animation. In fact, most of time I don't like any interface animation. I guess it distracts me a bit. I would like to disable menu animation, but I can't.

### Camera shutter sound

Oh… That camera shutter sound is really annoying. And inconvenient while you are at certain places. EVERYONE wants to disable it, but we can't. Some people say there is a law somewhere that forbids taking photos without sound, to avoid privacy invasion. Other people say that happens to avoid that students cheat during exams.

I really don't care about these things, because forcing camera sound won't fix the problem, and because I want to take legitimate and lawful photos without disturbing other people.

Some older versions of K750i allowed you to disable the shutter sound by entering "silent" mode. In newer versions, this does not work anymore.

There are two ways to make the camera silent:

1. Make a call (to a free number, like your operator number). While the call is running, the camera will be silent.
2. Hack the phone, by flashing the internal memory.

### Camera is not like a real camera

I have one friend that says "this phone has a cybershot camera, it is like a 'real' digital camera". By "real", we mean a "dedicated" camera.

This is not true. A "real" camera has many more options to change how the photo will be taken (sensibility, shutter speed,…). Also, a "real" camera has "Carl Zeiss" lenses (whatever that means) or at least some "glass" lens. The phone camera has plastic lens.

Most "real" cameras have [CCD](http://en.wikipedia.org/wiki/Charge-coupled_device) sensors, while the phone has a [CMOS](http://en.wikipedia.org/wiki/CMOS) sensor (as far as I know).

I guess most "real" cameras can do auto-focus faster than phone camera.

Any "real" camera can load, zoom and pan (scroll) an image much faster than this phone. Wow, doing any of above operations on a 2 megapixel image is damn slow. While on my "real" camera it is instantaneous.

To be fair, I don't think these things are so bad in a cell phone. It is a phone, and not a camera, after all. It is just nice to have a good camera at hand (though not as good as a dedicated camera).

**New info added on 2007-02-21**: I've read at [another review](http://spicygadget.com/2006/12/18/sony-ericsson-k800-k790-review/4/) ([Wayback Machine](http://web.archive.org/web/20071110003240/http://spicygadget.com/2006/12/18/review-sony-ericsson-k800/4/)) that CMOS sensor uses 100 times less energy than CCD sensor. It also said that small lens does mean greater exposure times, which does mean images more likely to be blurred. A friend also told me that CMOS sensor does not capture the entire image at once. This means more software work to try to compensate color and noise. This also means that photos of moving objects can be distorted in CMOS, while they usually are blurred in CCD or analog films (try taking a photo of trees or lamp posts while you are moving inside a car or train; also try turning the camera 90° and repeating the photo).

### Phone light interface is not easy/fast-to-use

This phone can also act as a flash light. Of course, very useful to have one at hand in those blackout days or dark places.

However, all the path until you can (de)active the light is too long and cumbersome. If you don't add it to your shortcuts menu, you must do this: Menu → Organizer → Light (the 9th item). Then you must select "On for 1 minute", "On", "Off" or "SOS", and then press the left softkey ("Select").

If you want it quickly, you just can't get it as quickly as you would want.

### Radio issues

The radio allows you to save channels (at most 20), and also name them. However, you cannot move, rearrange or sort the list. If you want to do that, you must save the channel again at new position, type its name again, and delete the previous one. Boring…

While you can name the channels, the name is only shown at your saved channels list, and nowhere else.

It has the feature to automatically search and save all channels. Unfortunately, that will erase your current saved channels list.

The radio has support to [RDS](http://en.wikipedia.org/wiki/Radio_Data_System), which allows it to automatically get and show the channel name. However, when you save the channel, the name is not automatically typed in name field.

Finally, inside radio application, the up/down arrow keys select a channel from your saved list. Outside it (while it is minimized), however, keep pressing volume up/down will search the next/previous radio channel ignoring the saved channels list.

### Volume issues

There are a few volume issues with K750i.

The radio volume is too loud. One or two "bars" (out of 8) is about the same volume of 5 or 7 bars anywhere else on phone (MP3/Media player, Java MIDlets).

We can change the volume inside a MIDlet (using volume keys). However, if suddenly the MIDlet stop playing any sound, whenever it starts playing again the volume will be the old one. But, if you press any volume button, the phone will remember the new volume. The only "workaround" for this is to set volume outside a MIDlet (setting it while inside Media Player is a good idea).

## Conclusions

After all this, I guess you are tired. Well, at least I am. :)

I must say this phone still is a good phone. Most (or all?) of these issues are small bugs, interface problems (many times the interface is not consistent), and some limitations (mostly in the contact list).

I would be really thankful if Sony Ericsson could fix at least some of these things. I would be much more happy and thankful if most of these were fixed. And since most of these are software issues, they can be fixed by a firmware update, if Sony Ericsson really cares to fix them.

## Links

* [Sony Ericsson K750i at Wikipedia](http://en.wikipedia.org/wiki/Sony_Ericsson_K750i)
* [Sony Ericsson K750i at FoneWiki](http://fonewiki.org/index.php?title=Sony_Ericsson_K750i) ([Wayback Machine](http://web.archive.org/web/20061119194910/http://www.fonewiki.org/index.php?title=Sony_Ericsson_K750i))
* [Sony Ericsson K750i at Esato](http://www.esato.com/phones/index.php/phone=168)
* [FPC Bench test results](http://www.dpsoftware.org/result/sony/k750.html) ([Wayback Machine](https://web.archive.org/web/20061014024646/http://www.dpsoftware.org/result/sony/k750.html))
