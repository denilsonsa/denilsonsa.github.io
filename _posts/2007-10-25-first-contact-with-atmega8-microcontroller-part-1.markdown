---
date: 2007-10-25 15:10:00+00:00
excerpt: 'Last week I bought an <a href="http://www.atmel.com/dyn/products/product_card.asp?part_id=2004"
  rel="nofollow" target="_blank">ATmega8</a> <a href="http://en.wikipedia.org/wiki/Microcontroller"
  rel="nofollow" target="_blank">microcontroller</a>. I plan to use it to build an
  arcade <a href="http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm" rel="nofollow"
  target="_blank">USB Joystick</a>, but first I need to understand how it works and
  how to use it.<br/><br/>This and the following posts are an attempt to document
  my first contact with this microcontroller and to describe all needed hardware and
  software so you can start using a microcontroller too. ... '
layout: post
title: First contact with ATmega8 microcontroller - part 1
lang: en
tag:
- AVR
- ATmega8
- Gentoo
- Linux
- Microcontroller
---

Last week I bought an [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) [microcontroller](http://en.wikipedia.org/wiki/Microcontroller). I plan to use it to build an arcade [USB Joystick](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) ([Wayback Machine](http://web.archive.org/web/20071026031301/http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm)), but first I need to understand how it works and how to use it.

This and the following posts are an attempt to document my first contact with this microcontroller and to describe all needed hardware and software so you can start using a microcontroller too. ...

<!-- more -->Go to: **part 1**, [part 2](http://my.opera.com/CrazyTerabyte/blog/2007/10/26/first-contact-with-atmega8-microcontroller-part-2), [part 2.1](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1) ([video](http://www.youtube.com/watch?v=sr0B-5Bhxdg)), [part 3](http://my.opera.com/CrazyTerabyte/blog/2007/11/02/first-contact-with-atmega8-microcontroller-part-3), [part 4](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4) ([video](http://www.youtube.com/watch?v=V7ESjm2bG-A)).

**What is a microcontroller?**

A [microcontroller](http://en.wikipedia.org/wiki/Microcontroller) is a simplified [CPU](http://en.wikipedia.org/wiki/CPU), plus some amount of [RAM](http://en.wikipedia.org/wiki/RAM), plus some amount of [(re)programmable ROM](http://en.wikipedia.org/wiki/Read-only_memory), plus some [I/O ports](http://en.wikipedia.org/wiki/Input/output) (including some analog I/O ports), and all of this in a single small [chip](http://en.wikipedia.org/wiki/Integrated_circuit).

Microcontrollers are used at many electronic devices, including microwave ovens and washing machines. They are simple and useful enough to be used in many DIY (do it yourself) projects. They usually can run at a [clock rate](http://en.wikipedia.org/wiki/Clock_signal) of a few MHz.

**What is ATmega8?**

[ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) is a microcontroller from [Atmel AVR family](http://en.wikipedia.org/wiki/Atmel_AVR). Like (all?) other microcontrollers from that family, it has an [8-bit](http://en.wikipedia.org/wiki/8-bit) [RISC](http://en.wikipedia.org/wiki/Reduced_instruction_set_computer) CPU core. Both [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) and [ATmega16](http://www.atmel.com/dyn/products/product_card.asp?part_id=2010) are very popular and inexpensive microcontrollers.

The very popular [Arduino](http://www.arduino.cc/) project uses [ATmega16](http://www.atmel.com/dyn/products/product_card.asp?part_id=2010), but has an [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) version. [Make Magazine](http://www.makezine.com/) often features some projects using AVR microcontrollers [(1)](http://forums.makezine.com/comments.php?DiscussionID=2397) [(2)](http://www.instructables.com/id/SpokePOV%3a-LED-Bike-Wheel-Images/) [(3)](http://makezine.com/10/brainwave/) [(4)](http://www.makezine.com/blog/archive/2007/09/its_the_end_of_the_weeken.html).

[Atmel](http://www.atmel.com/) company provides some software tools to work with AVR microcontrollers, but there are also enough free software tools for that.

**Why ATmega8 and not ATtiny or some other model?**

There are many [AVR models](http://www.avrfreaks.net/index.php?module=FreaksDevices). ATtiny, in special, tend to be smaller and to have smaller memory and fewer I/O pins. I really don't know too much about them (or any other AVR microcontroller), but there is one big reason why I've choosen ATmega8: [Cerne-Tec](http://www.cerne-tec.com.br/) (the place where I bought the microcontroller)
[only has two AVR models](http://www.cerne-tec.com.br/avr.htm): [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) and [ATmega16](http://www.atmel.com/dyn/products/product_card.asp?part_id=2010).

**Why ATmega8 and not ATmega16?**

There are two main reasons why I've choosen [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) over [ATmega16](http://www.atmel.com/dyn/products/product_card.asp?part_id=2010): it's cheaper and it's the microcontroller used in [the project I want to make](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) sometime soon.

**Before you continue...**

I don't have much experience with electronics (yet), so please don't think everything here is 100% correct (actually, if something is wrong, please tell me!). If you are not careful enough, you may damage the microcontroller or even the USB port or the parallel port from your computer.

I use [Gentoo/Linux](http://www.gentoo.org/) system on x86 arch. I don't have access to Windows, Mac or BSD computers, so I don't know exactly what you must do on those systems.

This post is intended to be a very quick introduction to [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004) microcontroller. This post (and probably future posts about the same subject) can be viewed as crash course about [ATmega8](http://www.atmel.com/dyn/products/product_card.asp?part_id=2004).

In this post I'm going to assume you have some very basic electronics background: you know what are [DC](http://en.wikipedia.org/wiki/Direct_current), [Vcc](http://en.wikipedia.org/wiki/IC_power_supply_pin) and [GND](http://en.wikipedia.org/wiki/Ground_(electricity)); you can recognize a [resistor](http://en.wikipedia.org/wiki/Resistor), a [capacitor](http://en.wikipedia.org/wiki/Capacitor), a [LED](http://en.wikipedia.org/wiki/Light-emitting_diode) and other components; you know [how to solder](http://www.ladyada.net/learn/soldertut/index.html) ([video](http://www.makezine.com/blog/archive/2007/01/soldering_tutor_1.html) and [PDF](http://www.makezine.com/blog/archive/2007/01/soldering_tutor.html)) and [how to use a multimeter](http://www.ladyada.net/learn/metertut/index.html) ([video](http://www.makezine.com/blog/archive/2007/01/multimeter_tuto.html) and [PDF](http://www.makezine.com/blog/archive/2007/01/multimeter_tuto_1.html)). I'm also going to assume you can use your computer, whatever the system is, but I'm going to focus on Linux. Finally, I'm going to assume you can understand [C programming](http://en.wikipedia.org/wiki/C_(programming_language)), [Makefile](http://en.wikipedia.org/wiki/Make_(software)) and [assembly](http://en.wikipedia.org/wiki/Assembly_language).

**Objectives**

The main objectives in this post are:



  * to make the microcontroller **work**
  * to make it work using my **Linux** (without the need of Windows or any proprietary software)
  * the total cost of components must be low (the project must be as **cheap** as possible)
  * it must be **simple**
Fortunately, all objectives were met.

**What you need**

**Hardware**

_**Update at 2011-08-10:** This list is obsolete. It has been left here for historical purposes._



  * 1x ATmega8
  * 1x 28-pin socket (optional)
  * 1x USB-B connector (optional)
  * 1x DB-25 male connector (plus case)
  * 1x 220 ohms resistor
  * 3x 330 ohms resistors
  * about 1 meter of cable (with 5-wires or more)
  * a pair of male/female connectors with 5 pins or more
  * 1x [breadboard](http://en.wikipedia.org/wiki/Breadboard) (AKA [protoboard](http://en.wikipedia.org/wiki/Protoboard))
  * many short wires
  * some LEDs and resistors
  * basic electronic tools [(1)](http://www.ladyada.net/make/minipov3/make.html) [(2)](http://www.ladyada.net/library/equipt/kits.html): soldering iron, solder, wire cutter, wire stripper (with practice, a pair of scissors can be used to strip wires), pliers, helping hands [(1)](http://www.instructables.com/id/Build-a-Pair-of-Helping-Hands/) [(2)](http://www.instructables.com/id/make-your-_helping-hands_-100x-more-useful-for-sol/)...

For the final version of any project, consider either making a [PCB](http://en.wikipedia.org/wiki/Printed_circuit_board) or using a [stripboard](http://en.wikipedia.org/wiki/Stripboard). The project from this post, however, is just for learning the basics and, thus, won't generate anything useful at the end (except the knowledge acquired).

**Software**



  * A compiler: avr-gcc or [tavrasm](http://www.tavrasm.org/)
  * A programmer: [avrdude](http://www.nongnu.org/avrdude/) [(old homepage)](http://www.bsdhome.com/avrdude/) or [uisp](http://www.nongnu.org/uisp/) (or maybe [PonyProg](http://www.lancos.com/prog.html), but I haven't tried it)
  * ppdev Linux kernel module (_Device Drivers -> Character devices -> Support for user-space parallel port device drivers_) (_**Update at 2011-08-10:** This is not needed if you don't use a parallel port programmer._)
  * [giveio](http://web.mit.edu/6.115/www/pic.shtml) [(direct download)](http://web.mit.edu/6.115/www/miscfiles/giveio.zip) (only for Windows, I don't know how this works nor how to install it)

Installing them on [Gentoo](http://www.gentoo.org/):


    emerge -av crossdev tavrasm avrdude uisp
    crossdev -t avr

If you use a parallel port programmer, run **modprobe ppdev** and add your user (your ordinary user, not the root) to the **lp** group, or instead change the permissions of **/dev/parport0**.

**Total cost**

I already had the [breadboard](http://en.wikipedia.org/wiki/Breadboard), some resistors, some leds and some wires. The other components I bought at [Cerne-Tec](http://www.cerne-tec.com.br/) (I went to their physical office in Rio de Janeiro). The prices here are in Brazillian Reais (R$). Today, US$ 1.00 = R$ 1.78.

_**Update at 2011-08-10:** This shopping list was meant for building a parallel port programmer. If you don't build one, then this list has no use for you. It has been left here for historical purposes._



  * R$ 9.90 - 1x ATmega8
  * R$ 1.00 - 1x 28-pin socket
  * R$ 4.00 - 1x USB-B connector
  * R$ 4.50 - 1x DB-25 male connector (plus case)
  * R$ 0.20 - 1x 220 ohms resistor
  * R$ 0.60 - 3x 330 ohms resistors
  * R$ 2.00 - about 1 meter of cable (with 5-wires or more)
  * R$ 1.50 - a pair of male/female connectors with 5 pins or more
  * **R$ 23.70 - Subtotal (US$ 13.30)**
  * R$ 4.60 - 2x subway tickets for transportation
  * R$ 28.30 - Total (US$ 15.90)

The [ATmega16](http://www.atmel.com/dyn/products/product_card.asp?part_id=2010) was priced at R$ 24.90, which is a bit more than the total cost of all these components. There was also a large [stripboard](http://en.wikipedia.org/wiki/Stripboard) available for sale at around R$ 20.00 ~ R$ 25.00, which is almost the price of all these componentes together. Since I don't want to double this project cost, I'm using the breadboard I already have for now.

**Note:** There is no guarantee the prices will be the same at the time you go buy your components. I'm not affiliated with Cerne-Tec. The prices listed here are just for illustration.

**Update at 2007-10-26:** I found a small stripboard (about the exact size I need, maybe just a bit larger) for sale at R$ 2.50 at an electronic store near my house. I haven't bought it yet, but I'm probably going to.

**Update at 2007-12-29:** The USB-B connector turned out to not be needed for these experiments and was substituted by a simple USB cable (priced at R$ 2.79, or US$ 1.57). However, I know I'm going to use it sometime in future, in other project. (_**Update at 2011-08-10:** It turns out I've never used that USB-B connector, and I'm not even sure if I will ever use it._)

**Overall plan of this project**

Since I wanted to learn how to use the ATmega8, I wanted to make a simple "[Hello, world](http://en.wikipedia.org/wiki/Hello_world_program)" program and put it on the microcontroller. Well, my microcontroller does not have a terminal, a screen or an LCD to print something, so the "Hello, world" is going to be just some blinking LEDs. Also I need something to write the program into the microcontroller, so I need to build such tool.

So, these are the steps to be followed in this project:



  1. Build a simple, cheap and working parallel port AVR Programmer [(part 2)](http://my.opera.com/CrazyTerabyte/blog/2007/10/26/first-contact-with-atmega8-microcontroller-part-2)
  2. Build and/or buy a simple, cheap and working USB port AVR Programmer [(part 2.1)](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1) _(added at 2011-08-10)_
  3. Write a simple "Hello, world" for the microcontroller [(part 3)](http://my.opera.com/CrazyTerabyte/blog/2007/11/02/first-contact-with-atmega8-microcontroller-part-3)
  4. Compile the "Hello, world" [(part 3)](http://my.opera.com/CrazyTerabyte/blog/2007/11/02/first-contact-with-atmega8-microcontroller-part-3)
  5. Mount the microcontroller on the breadboard [(part 4)](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4)
  6. Use the AVR Programmer to write the "Hello, world" to the microcontroller [(part 4)](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4)
  7. Be happy and watch the blinking LEDs! [(part 4)](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4)

See you at the next part!

**Update at 2008-02-02:** I've uploaded a [video of this project at YouTube](http://www.youtube.com/watch?v=V7ESjm2bG-A). Everybody loves videos, so check it out!

**Update at 2011-08-10:** Parallel ports are from the past, and nobody uses them anymore. Thus I've revisited this series of posts and added [part 2.1](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1), that shows how I built USBasp. It also has a [video](http://www.youtube.com/watch?v=sr0B-5Bhxdg).

**Update at 2011-08-11:** The source-code for this "blinking LEDs" firmware (see [part 3](http://my.opera.com/CrazyTerabyte/blog/2007/11/02/first-contact-with-atmega8-microcontroller-part-3)) is now available at: [https://bitbucket.org/denilsonsa/atmega8-blinking-leds](https://bitbucket.org/denilsonsa/atmega8-blinking-leds)

Go to: **part 1**, [part 2](http://my.opera.com/CrazyTerabyte/blog/2007/10/26/first-contact-with-atmega8-microcontroller-part-2), [part 2.1](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1) ([video](http://www.youtube.com/watch?v=sr0B-5Bhxdg)), [part 3](http://my.opera.com/CrazyTerabyte/blog/2007/11/02/first-contact-with-atmega8-microcontroller-part-3) ([part 4](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4), [video](http://www.youtube.com/watch?v=V7ESjm2bG-A)).
