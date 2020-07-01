---
layout: post
title: First contact with ATmega8 microcontroller - part 1
excerpt: "Last week I bought an ATmega8 microcontroller. I plan to use it to build an arcade USB Joystick, but first I need to understand how it works and how to use it. This and the following posts are an attempt to document my first contact with this microcontroller and to describe all needed hardware and software so you can start using a microcontroller too."
lang: en
tags:
- AVR
- ATmega8
- Gentoo
- Linux
- Microcontroller
- Hardware
---

Last week I bought an [ATmega8][] [microcontroller][]. I plan to use it to build an arcade [USB Joystick](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) ([Wayback Machine](http://web.archive.org/web/20071026031301/http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm)), but first I need to understand how it works and how to use it.

This and the following posts are an attempt to document my first contact with this microcontroller and to describe all needed hardware and software so you can start using a microcontroller too.


{% include first-contact-with-atmega8-navigation.html %}

## What is a microcontroller?

A [microcontroller][] is a simplified [CPU][], plus some amount of [RAM][], plus some amount of [(re)programmable ROM][ROM], plus some [I/O ports][IO] (including some analog I/O ports), and all of this in a single small [chip][].

Microcontrollers are used in many electronic devices, including microwave ovens and washing machines. They are simple enough, chep enough and useful enough to be used in many [DIY (do it yourself)][DIY] projects. They usually can run at a [clock rate][clock] of a few MHz.

## What is ATmega8?

[ATmega8][] is a microcontroller from [Atmel AVR family][Atmel AVR]. Like (all?) other microcontrollers from that family, it has an [8-bit][] [RISC][] CPU core. Both [ATmega8][] and [ATmega16][] are very popular and inexpensive microcontrollers.

The very popular [Arduino][] project uses [ATmega16][], but has an [ATmega8][] version. [Make Magazine](http://www.makezine.com/) often features some projects using AVR microcontrollers (such as [SpokePOV](http://www.instructables.com/id/SpokePOV%3a-LED-Bike-Wheel-Images/), [The Brain Machine](http://makezine.com/10/brainwave/) and [Do you know how to use and ARRR-duino yet?](http://www.makezine.com/blog/archive/2007/09/its_the_end_of_the_weeken.html)).

[Atmel][] company provides some software tools to work with AVR microcontrollers, but there are also enough free software tools for that.

### Why ATmega8 and not ATtiny or some other model?

There are many [AVR models](http://www.avrfreaks.net/index.php?module=FreaksDevices) ([Wayback Machine](http://web.archive.org/web/20070630224244/http://www.avrfreaks.net/index.php?module=Freaks%20Devices&func=viewDev)). ATtiny, in special, tend to be smaller and to have less memory and fewer I/O pins. I really don't know too much about them (or any other AVR microcontroller), but there is one big reason why I've choosen [ATmega8][]: [Cerne-Tec][] (the place where I bought the microcontroller) [only has two AVR models](http://www.cerne-tec.com.br/avr.htm): [ATmega8][] and [ATmega16][].

### Why ATmega8 and not ATmega16?

There are two main reasons why I've choosen [ATmega8][] over [ATmega16][]: it's cheaper and it's the microcontroller used in [the project I want to build](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) ([Wayback Machine](http://web.archive.org/web/20071026031301/http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm)) sometime soon.

## Before you continue…

I don't have much experience with electronics (yet), so please don't think everything here is 100% correct (actually, if something is wrong, please tell me!). If you are not careful enough, you may damage the microcontroller or even the USB port or the parallel port from your computer.

I use [Gentoo/Linux](http://www.gentoo.org/) system on x86 arch. I don't have access to Windows, Mac or BSD computers, so I don't know exactly what you must do on those systems.

This post is intended to be a very quick introduction to [ATmega8][] microcontroller. This post (and probably future posts about the same subject) can be viewed as crash course about [ATmega8][].

In this post I'm going to assume you have some very basic electronics background: you know what are [DC][], [Vcc][] and [GND][]; you can recognize a [resistor][], a [capacitor][], a [LED][] and other components; you know how to solder and how to use a multimeter. I'm also going to assume you can use your computer, whatever the system is, but I'm going to focus on Linux. Finally, I'm going to assume you can understand [C programming][], [Makefile][] and [assembly][].

Want to learn more about basic electronics skills?

* [Skill Set: Soldering](http://makezine.com/2011/01/06/skill-set-soldering/), [Primer — Soldering and Desoldering](http://makezine.com/projects/make-01/primer-soldering-and-desoldering/), [Soldering Tutorial – Make Video Podcast](http://makezine.com/2007/01/05/soldering-tutorial-make-v/) and [MAKE presents: The Multimeter](http://makezine.com/2011/01/26/make-presents-the-multimeter/) ([on YouTube](http://www.youtube.com/watch?v=BW3Wj7UD-_s)) from [MAKE](http://makezine.com/).
* [Soldering Tutorial](http://www.ladyada.net/learn/soldering/) and [Multimeters](http://learn.adafruit.com/multimeters/) from [ladyada.net](http://www.ladyada.net) and [Adafruit](http://learn.adafruit.com/).
* [How To Use A Multimeter](http://blip.tv/make/how-to-use-a-multimeter-142363) ([also available on YouTube](http://www.youtube.com/watch?v=KzjMIcER4EU)), [Learn How To Solder - Skill Building Workshop](http://blip.tv/make/learn-how-to-solder-skill-building-workshop-130343) by Bre Pettis and Joe Grand.
* [How to Use a Multimeter](http://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/all) and [How to Solder - Through-hole Soldering](http://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering/all) from [SparkFun Electronics](http://learn.sparkfun.com/)
* [Breadboards & Perfboards](http://www.youtube.com/watch?v=w0c3t0fJhXU), [Multimeters](http://www.youtube.com/watch?v=rPGoMbVSUu8) and [Soldering](http://www.youtube.com/watch?v=QKbJxytERvg) from [Collin's Lab (by Adafruit Industries)](http://www.youtube.com/playlist?list=PLjF7R1fz_OOU08_hRcayfVZSmTpBCGJbL). See also [Collin's Lab (by MAKE)](http://www.youtube.com/playlist?list=PLDE23FAC8A681FA46) and [Circuit Skills by Collin Cunningham (by MAKE)](http://www.youtube.com/playlist?list=PL736ED63818F361CB).

## Objectives

The main objectives in this post are:

* to make the microcontroller **work**
* to make it work using my **Linux** system (without the need of Windows or any proprietary software)
* the total cost of components must be low (the project must be as **cheap** as possible)
* it must be **simple**

Fortunately, all objectives were met.

## What you need

### Hardware

_**Update on 2011-08-10:** This list is obsolete. It has been left here for historical reasons._

* 1 × ATmega8
* 1 × [28-pin socket](http://en.wikipedia.org/wiki/Dual_in-line_package) (optional)
* 1 × USB-B connector (optional)
* 1 × [DB-25 male connector](http://en.wikipedia.org/wiki/D-subminiature) (plus case)
* 1 × 220 Ω resistor
* 3 × 330 Ω resistors
* about 1 meter of cable (with 5 wires or more)
* a pair of male/female connectors with 5 pins or more
* 1 × [breadboard][] (AKA [protoboard][])
* many short wires
* some LEDs and resistors
* [basic electronic tools](http://learn.adafruit.com/minipov3/preparation): soldering iron, solder, wire cutter, wire stripper (with practice, a pair of scissors can be used to strip wires), pliers, helping hands [(1)](http://www.instructables.com/id/Build-a-Pair-of-Helping-Hands/) [(2)](http://www.instructables.com/id/make-your-_helping-hands_-100x-more-useful-for-sol/)…

For the final version of any project, consider either making a [PCB][] or using a [stripboard][]. The project from this post, however, is just for learning the basics and, thus, won't generate anything useful at the end (except knowledge).

### Software

* A compiler: [avr-gcc][avr-libc] or [tavrasm][] ([Wayback Machine](http://web.archive.org/web/20070929162857/http://www.tavrasm.org/))
* A programmer: [avrdude][] or [uisp](http://www.nongnu.org/uisp/) ([Wayback Machine](http://web.archive.org/web/20071021021038/http://www.nongnu.org/uisp/)) (or maybe [PonyProg][] ([Wayback Machine](http://web.archive.org/web/20071026014723/http://www.lancos.com/prog.html)), but I haven't tried it)
* `ppdev` Linux kernel module (_Device Drivers → Character devices → Support for user-space parallel port device drivers_) (_**Update on 2011-08-10:** This is not needed if you don't use a parallel port programmer._)
* [giveio](http://web.mit.edu/6.115/www/pic.shtml) ([Wayback Machine](http://web.archive.org/web/20071031044855/http://web.mit.edu/6.115/www/pic.shtml)) ([direct download](http://web.mit.edu/6.115/www/miscfiles/giveio.zip)) (only for Windows, I don't know how this works nor how to install it)

Installing them on [Gentoo](http://www.gentoo.org/):

    emerge -av crossdev tavrasm avrdude uisp
    crossdev -t avr

If you use a parallel port programmer, run `modprobe ppdev` and add your user (your ordinary user, not the root) to the `lp` group, or instead change the permissions of `/dev/parport0`.

## Total cost

I already had the [breadboard][], some resistors, some LEDs and some wires. The other components I bought at [Cerne-Tec][] (I went to their physical office in Rio de Janeiro). The prices here are in Brazillian Reais (R$). Today, US$ 1.00 = R$ 1.78.

_**Update on 2011-08-10:** This shopping list was meant for building a parallel port programmer. If you don't build one, then this list has no use for you. It has been left here for historical reasons._

* R$ 9.90 - 1 × ATmega8
* R$ 1.00 - 1 × 28-pin socket
* R$ 4.00 - 1 × USB-B connector
* R$ 4.50 - 1 × DB-25 male connector (plus case)
* R$ 0.20 - 1 × 220 Ω resistor
* R$ 0.60 - 3 × 330 Ω resistors
* R$ 2.00 - about 1 meter of cable (with 5-wires or more)
* R$ 1.50 - a pair of male/female connectors with 5 pins or more
* **R$ 23.70 - Subtotal (US$ 13.30)**
* R$ 4.60 - 2 × subway tickets for transportation
* R$ 28.30 - Total (US$ 15.90)

The [ATmega16][] was priced at R$ 24.90, which is a bit more than the total cost of all these components. There was also a large [stripboard](http://en.wikipedia.org/wiki/Stripboard) available for sale at around R$ 20.00 ~ R$ 25.00, which is almost the price of all these componentes together. Since I don't want to double this project cost, I'm using the breadboard I already have for now.

**Note:** There is no guarantee the prices will be the same at the time you go buy your components. I'm not affiliated with Cerne-Tec. The prices listed here are just for illustration.

**Update on 2007-10-26:** I found a small stripboard (about the exact size I need, maybe just a bit larger) for sale at R$ 2.50 at an electronics store near my house. I haven't bought it yet, but I'm probably going to.

**Update on 2007-12-29:** The USB-B connector turned out to not be needed for these experiments and was substituted by a simple USB cable (priced at R$ 2.79, or US$ 1.57). However, I know I'm going to use it sometime in future, in other project. (_**Update on 2011-08-10:** It turns out I've never used this USB-B connector, and I don't think I will ever use it._)

**Update on 2014-06-12:** If you live in São Paulo, or if you want to order online, you can try buying [AVR microcontrollers](http://loja.multcomercial.com.br/ecommerce_site/categoria_4741-4769-4809_4689_Componentes-Eletronicos-ATMEGAxx) at [Mult Comercial](http://www.multcomercial.com.br/).

## Overall plan of this project

Since I wanted to learn how to use ATmega8, I wanted to make a simple “[Hello, world](http://en.wikipedia.org/wiki/Hello_world_program)” program and put it on the microcontroller. Well, my microcontroller does not have a terminal, a screen or an LCD to print something, so the “Hello, world” is going to be just some blinking LEDs. Also I need something to write the program into the microcontroller, so I need to build such tool.

So, these are the steps in this project:

1. Build a simple, cheap and working parallel port AVR Programmer ([part 2][])
2. Build and/or buy a simple, cheap and working USB port AVR Programmer ([part 2.1][]) _(added at 2011-08-10)_
3. Write a simple “Hello, world” for the microcontroller ([part 3][])
4. Compile the “Hello, world” ([part 3][])
5. Mount the microcontroller on the breadboard ([part 4][])
6. Use the AVR Programmer to write the "Hello, world" to the microcontroller ([part 4][])
7. Be happy and watch the blinking LEDs! ([part 4][])

See you at the [next part][part 2]!

**Update on 2008-02-02:** I've uploaded a [video of this project at YouTube](http://www.youtube.com/watch?v=V7ESjm2bG-A). Everybody loves videos, so check it out!

**Update on 2011-08-10:** Parallel ports are from the past, and nobody uses them anymore. Thus I've revisited this series of posts and added [part 2.1][], that shows how I built USBasp. It also has a [video](http://www.youtube.com/watch?v=sr0B-5Bhxdg).

**Update on 2011-08-11:** The source-code for this "blinking LEDs" firmware (see [part 3][]) is now available at: <https://github.com/denilsonsa/atmega8-blinking-leds>

{% include first-contact-with-atmega8-navigation.html %}

[Atmel]: http://www.atmel.com/
[ATmega8]: http://www.atmel.com/devices/ATMEGA8.aspx
[ATmega16]: http://www.atmel.com/devices/ATMEGA16.aspx
[Arduino]: http://www.arduino.cc/
[Cerne-Tec]: http://www.cerne-tec.com.br/
[avr-libc]: http://www.nongnu.org/avr-libc/
[tavrasm]: http://www.tavrasm.org/
[avrdude]: http://www.nongnu.org/avrdude/
[uisp]: http://www.nongnu.org/uisp/
[PonyProg]: http://www.lancos.com/prog.html
[Atmel AVR]: http://en.wikipedia.org/wiki/Atmel_AVR
[microcontroller]: http://en.wikipedia.org/wiki/Microcontroller
[CPU]: http://en.wikipedia.org/wiki/CPU
[RAM]: http://en.wikipedia.org/wiki/RAM
[ROM]: http://en.wikipedia.org/wiki/Read-only_memory
[IO]: http://en.wikipedia.org/wiki/Input/output
[chip]: http://en.wikipedia.org/wiki/Integrated_circuit
[clock]: http://en.wikipedia.org/wiki/Clock_signal
[DIY]: http://en.wikipedia.org/wiki/Do_it_yourself
[8-bit]: http://en.wikipedia.org/wiki/8-bit
[RISC]: http://en.wikipedia.org/wiki/Reduced_instruction_set_computer
[DC]: http://en.wikipedia.org/wiki/Direct_current
[Vcc]: http://en.wikipedia.org/wiki/IC_power_supply_pin
[GND]: http://en.wikipedia.org/wiki/Ground_(electricity)
[resistor]: http://en.wikipedia.org/wiki/Resistor
[capacitor]: http://en.wikipedia.org/wiki/Capacitor
[LED]: http://en.wikipedia.org/wiki/Light-emitting_diode
[C programming]: http://en.wikipedia.org/wiki/C_(programming_language)
[Makefile]: http://en.wikipedia.org/wiki/Make_(software)
[assembly]: http://en.wikipedia.org/wiki/Assembly_language
[breadboard]: http://en.wikipedia.org/wiki/Breadboard
[protoboard]: http://en.wikipedia.org/wiki/Protoboard
[stripboard]: http://en.wikipedia.org/wiki/Stripboard
[PCB]: http://en.wikipedia.org/wiki/Printed_circuit_board
[part 1]: {% post_url 2007-10-25-first-contact-with-atmega8-microcontroller-part-1 %}
[part 2]: {% post_url 2007-10-26-first-contact-with-atmega8-microcontroller-part-2 %}
[part 2.1]: {% post_url 2011-08-10-first-contact-with-atmega8-microcontroller-part-2-1 %}
[part 3]: {% post_url 2007-11-02-first-contact-with-atmega8-microcontroller-part-3 %}
[part 4]: {% post_url 2008-02-02-first-contact-with-atmega8-microcontroller-part-4 %}
