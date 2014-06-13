---
layout: post
title: First contact with ATmega8 microcontroller - part 2
lang: en
tag:
- AVR
- ATmega8
- Microcontroller
- Hardware
---

In this second part, I'm going to build an AVR programmer to be connected to the PC's parallel port. I'm trying to summarize here all information I found spread all over the web. I believe this post is worth reading even if you don't have a parallel port, as it describes how AVR programming works.


{% include first-contact-with-atmega8-navigation.html %}

## What is an AVR ISP Programmer?

[ATmega8][] (as well as many other microcontrollers) has a feature called [ISP (In-System Programming)][ISP], which means they can be programmed while still connected to the final circuit. You do this by sending electric signals to the microcontroller; there is no need for UV light, like many chips from the last century. In other words, it means that it is very easy to program the microcontroller.

By _programming the microncontroller_ I mean writing a new [firmware][] on it. And the firmware is the software you are going to write to be run inside the microcontroller.

## Available AVR Programmers

There are many types of AVR Programmers available for sale everywhere. Most of them are somewhat expensive. Some of them use the [parallel port][], others use the [serial port][] and others use a [USB port][USB]. Some may require external power supply.

At [Cerne-Tec](http://www.cerne-tec.com.br/) (the place where I bought ATmega8), they sell a programmer for R$ 89.90 (about US$ 50.50), which is nine times the price of the microcontroller itself! I really don't know what kind of special features it has, but I won't spend so much money if I can build a working one for R$ 8.80 (maybe even less, if you happen to have some components). For [DIY projects][DIY], it's more than enough.

## How AVR Programming works

ATmega8 (and probably other AVR microcontrollers too) has two methods of programming: parallel programming and serial programming. The former uses 17 pins (plus 3 for Vcc and GND) to send all data and control commands [in parallel](http://en.wikipedia.org/wiki/Parallel_communication). The latter uses just 4 pins (plus 3 for Vcc and GND) and send commands and data [in serial](http://en.wikipedia.org/wiki/Serial_communication). This means that serial programming requires less wires and may use a smaller connector. In addition, serial programming looks simpler than parallel programming (4 pages versus 11 pages at [ATmega8 datasheet][]).

Serial programming uses almost the same pins as the [SPI (Serial Peripheral Interface)](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus); the SS (Slave Select) pin is not used. It works by sending a RESET signal at the RESET pin, which will… huh… reset the microcontroller and enter the serial programming mode. Then, the commands are sent at the MOSI (Master Output, Slave Input) pin and the [clock signal][clock] is sent at the SCK (Serial Clock) pin. Data sent from the microcontroller back to the programmer (or to the computer) goes through the MISO (Master Input, Slave Output) pin. And that's all you need to know! (refer to _Serial Programming_ section at [ATmega8 datasheet][], pages 230-233)

## The AVR ISP Parallel Port Programmer

You must be asking to yourself: _Why did this guy describe the serial programming method if we are going to use the parallel port?_ The answer is simple: we are going to use the PC parallel port to transfer serial data to the microcontroller serial pins. This works very well because the complicated (well, not so complicated) logic of sending the required bits at the exact time and the exact order is done by software. The parallel port will just receive some bytes (which are just a couple of bits together) and set the respective pins high or low, which will be directly (except by resistors) connected to the microcontroller pins. This means the parallel port programmer dongle is the cheapest programming hardware you can build: it has just the connectors, the wires and some resistors.

While searching the web for instructions about how to build it, I found many sites with different ways of connecting the parallel port pins. This made me confused about which one I should try to build, and which one would work. After looking at `/etc/avrdude.conf` file, I understood that all of them (or at least most of them) will work, even though they are different. You just need to select the correct programmer type in your programmer software (be it [avrdude][], [uisp][] ([Wayback Machine](http://web.archive.org/web/20071021021038/http://www.nongnu.org/uisp/)) or even [PonyProg][] ([Wayback Machine](http://web.archive.org/web/20071026014723/http://www.lancos.com/prog.html))).

I found basically 3 different schematics almost everywhere. Unfortunately, not all of them looked similar at first sight, and also not all of them had a name describing what type of parallel port programmer it was. Fortunately for you, I'm going to list here these three schematics with their respective names.

The schematic diagrams below were drawn by me using [Inkscape](http://www.inkscape.org/). I release these images as public domain, but I would love to be credited if you use them. Note: these circuits are not my creation.

### bsd

The first one is called `bsd`, probably because it was originally available at _AVRPROG_ program for FreeBSD. (Well, I'm not sure if this is true, but it's the best explanation I have to give you.) This program was later renamed to _AVRDUDE_ to avoid confusion with Atmel's _AVRPROG.EXE_. You can find a description of this parallel port programmer at [AVRDUDE old homepage](http://www.bsdhome.com/avrdude/) ([Wayback Machine](http://web.archive.org/web/20071015042041/http://www.bsdhome.com/avrdude/)).

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/AVR-bsd.png" alt="Diagram for AVR parallel port ISP, model 'bsd'.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/AVR-bsd-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/AVR-bsd.svg">SVG version</a>)
</figcaption>
</figure>

### dapa

The second one is called `dapa`, which means _Direct AVR Parallel Access cable_. This one is described at `uisp-parport-connect.txt` file from [uisp][] ([Wayback Machine](http://web.archive.org/web/20071021021038/http://www.nongnu.org/uisp/)). It is also found at [Arduino's ParallelProgrammer page](http://www.arduino.cc/en/Hacking/ParallelProgrammer) ([Wayback Machine](http://web.archive.org/web/20071025052338/http://www.arduino.cc/en/Hacking/ParallelProgrammer)) and at [LinuxFocus 352 article](http://www.linuxfocus.org/English/November2004/article352.shtml) ([Wayback Machine](http://web.archive.org/web/20071029080245/http://www.linuxfocus.org/English/November2004/article352.shtml)).

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/AVR-dapa.png" alt="Diagram for AVR parallel port ISP, model 'dapa'.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/AVR-dapa-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/AVR-dapa.svg">SVG version</a>)
</figcaption>
</figure>

### stk200

The third one is called `stk200`, because it behaves like the _STK200 AVR Starter Kit_. It is the schematic used by [How To...Build A DIY USB Joystick](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) ([Wayback Machine](http://web.archive.org/web/20071026031301/http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm)) project and is also available at [a personal homepage address found at #avr channel topic](http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/) ([Wayback Machine](http://web.archive.org/web/20071229042911/http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/)) on [FreeNode](http://en.wikipedia.org/wiki/Freenode).

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/AVR-stk200.png" alt="Diagram for AVR parallel port ISP, model 'stk200'.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/AVR-stk200-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/AVR-stk200.svg">SVG version</a>)
</figcaption>
</figure>

### Other similar designs

While writing this post I also found [another design](http://www.ladyada.net/make/spokepov/makeparrdongle.html) ([Wayback Machine](http://web.archive.org/web/20071011202509/http://www.ladyada.net/make/spokepov/makeparrdongle.html)). It's the one used by [SpokePOV](http://www.ladyada.net/make/spokepov/) ([Wayback Machine](http://web.archive.org/web/20071014050832/http://ladyada.net/make/spokepov)) project. <s>There is [a kit available for sale](http://www.adafruit.com/index.php?main_page=index&cPath=16) ([Wayback Machine](http://web.archive.org/web/20071012020148/http://www.adafruit.com/index.php?main_page=index&cPath=16)).</s> It works like the [DT006 AVR Development Board (the little rAVeR programmer)](http://www.dontronics.com/dt006.html) ([Wayback Machine](http://web.archive.org/web/20071018031445/http://www.dontronics.com/dt006.html)) and is recognized by avrdude and uisp as `dt006`. Sorry, I don't have the schematic diagram for this one, but don't you think that 3 different schematics are more than enough?

## Notes about the parallel port dongles

The first thing to be noted is the absence of a Vcc line. This happens because the parallel port can't supply enough power. This implies that the microcontroller must be powered by something else (like the USB port or batteries) while using these dongles.

You can also see I've connected 8 pins to the GND wire. I did that because the parallel port has 8 GND pins, but you are not required to solder all of them together. You can use just one GND pin and it shoud be enough.

Another thing to be noted are the resistors. I've not specified their values because each site used different values (and sometimes the same site used different values). The `stk200` schematic from [How To...Build A DIY USB Joystick](http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm) ([Wayback Machine](http://web.archive.org/web/20071026031301/http://www.flightsim.com/cgi/kds?$=main/howto/mind.htm)) ([direct link to the image](http://www.flightsim.com/howto/mind/avrisp.gif) ([Wayback Machine](http://web.archive.org/web/20111206023811/http://flightsim.com/howto/mind/avrisp.gif))) uses 4 resistors of 330 Ω each, one for each line (of course, GND is not included). On the other hand, this [personal homepage](http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html) ([Wayback Machine](http://web.archive.org/web/20071229042911/http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html)) tells us to use 4 × 220 Ω, but also hosts an image that shows one 100 Ω resistor for the MISO line and 3 × 330 Ω for the other lines.

Both [Arduino's ParallelProgrammer page](http://www.arduino.cc/en/Hacking/ParallelProgrammer) ([Wayback Machine](http://web.archive.org/web/20071025052338/http://www.arduino.cc/en/Hacking/ParallelProgrammer)) and [LinuxFocus 352 article](http://www.linuxfocus.org/English/November2004/article352.shtml) ([Wayback Machine](http://web.archive.org/web/20071029080245/http://www.linuxfocus.org/English/November2004/article352.shtml)) use the `dapa` schematic and both use the same values for resistors: 220 Ω for the MISO line, 470 Ω for the SCK and the MOSI lines, no resistor for the RESET line. In addition, the [LinuxFocus 352 article](http://www.linuxfocus.org/English/November2004/article352.shtml) ([Wayback Machine](http://web.archive.org/web/20071029080245/http://www.linuxfocus.org/English/November2004/article352.shtml)) says the cable should not be longer than 70 cm.

The [old AVRDUDE homepage](http://www.bsdhome.com/avrdude/) ([Wayback Machine](http://web.archive.org/web/20071015042041/http://www.bsdhome.com/avrdude/)) does not even give many details about this: _“Be sure and include series resistors between the signal wires and the parallel port. 1K resistors should work fine and may save your parallel port from damage in case of mis-wiring or some other mishap.”_

Finally, the [dongle used in SpokePOV project](http://www.ladyada.net/make/spokepov/makeparrdongle.html) ([Wayback Machine](http://web.archive.org/web/20071011202509/http://www.ladyada.net/make/spokepov/makeparrdongle.html)), which works as `dt006`, uses 3 × 1K Ω and one 47 Ω.

My conclusion about this: put some resistors and avoid too long cables. I've used a 220 Ω resistor for the MISO line and 3 × 330 Ω resistors for the other lines. My cable is 1 meter long.

If you run into problems, read [this post at AVR Freaks forum](http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=36591) ([Wayback Machine](http://web.archive.org/web/20080108163849/http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=36591)) and try shortening the cable length, or try using one of the other (a little more expensive) programmers listed below.

## My parallel port AVR programmer

From all possible dongles above (and below), you just have to choose one to build. All of above are very similar to each other, and all of them should work on both [avrdude][] and [uisp][] ([Wayback Machine](http://web.archive.org/web/20071021021038/http://www.nongnu.org/uisp/)) (and both programs are available on multiple platforms).

I've choosen to build the `bsd` one. I got a flat cable with 14 wires, but since I needed only 6 (actually, only 5), I've split the cable. To make sure the wires wouldn't short-circuit inside the DB-25 case and to make everything inside the case less likely to break, I've applied an amount of [hot glue](http://en.wikipedia.org/wiki/Hot_glue) after I finished with the soldering. If you look at the photos, the dongle looks a bit messy and ugly, but since that hot-glued part will be hidden inside the DB-25 case, no problem!

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00476.jpg" alt="The inside of my parallel port programmer, showing 4 resistors soldered to the DB-25 connector and some hot glue.">
</figure>

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00477.jpg" alt="The inside of my parallel port programmer, showing a bulk of hot glue next to the DB-25 connector.">
</figure>

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00478.jpg" alt="My parallel port programmer, showing the DB-25 connector (to the PC parallel port) and a non-standard 6-pin connector (to the microcontroller circuit).">
</figure>

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00485.jpg" alt="A picture of my finished parallel port programmer, with a black case around the DB-25 connector, hiding the the resistors and the hot glue blob. The flat cable has a black mark over the wire 1.">
</figure>

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00486.jpg" alt="Another angle of the previous picture.">
</figure>

I've not used any standard AVR connector for this project, but I will, if I build another programmer. Things will be easier in future if you use the standard 6-pin plug (or the 10-pin, but I prefer the 6-pin one), just in case you happen to use another programmer with your project, or your programmer with another project.

**Update on 2008-12-02:** [Originally, the 6-pin pinout in this blog was wrong.]({{ site.url }}/blog/2008-12-01/first-contact-with-atmega8-microcontroller-correction) It has been fixed, so the pinout below is correct.

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/AVR-ISP-connectors.png" alt="Diagram for AVR ISP 6-pin and 10-pin connectors.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/AVR-ISP-connectors-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/AVR-ISP-connectors.svg">SVG version</a>)
</figcaption>
</figure>

Even though I have not used the standard connector, I kept the same wire order as the 6-pin one. Then, I tried to use the following pen to mark the wire 1 as black:

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/DSC00487.jpg" alt="Pen used to paint the wire 1 of the flat cable.">
</figure>

Unfortunately, it was not a good choice, because the painted portion of that cable now leaves a black stain everywhere it touches.

The photos above were taken using a [SonyEricsson K750i phone](http://en.wikipedia.org/wiki/Sony_Ericsson_K750) at full resolution (2 megapixels). Then, I used [Gimp](http://www.gimp.org/) to scale down the images after applying _Layer → Colors → Auto → White Balance_.

## Other DIY AVR Programmers

**Update at 2011-08-10:** This section is now somewhat obsolete, as I've just written [part 2.1][], which deals with _USBasp_ programmer. If you prefer, skip the rest of this post and go directly to [part 2.1][].

### Buffered parallel port

[That personal homepage address found at #avr channel topic](http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html) ([Wayback Machine](http://web.archive.org/web/20071229042911/http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html)) has a link to a [PDF schematic diagram](http://eds.dyndns.org:81/~ircjunk/avr/programmer/avrprog.pdf) ([local mirror]({{ site.url }}/blog/images/avr/avrprog.pdf)) (**Update on 2008-12-02:** be careful, [the pinout in this PDF is wrong]({{ site.url }}/blog/2008-12-01/first-contact-with-atmega8-microcontroller-correction)) that describes how to build a buffered parallel port dongle. It uses one 100K [pull-up resistor](http://en.wikipedia.org/wiki/Pull-up_resistor), one 0.1µF [decoupling capacitor](http://en.wikipedia.org/wiki/Decoupling_capacitor), and a 74HC244 buffer chip. A similar diagram can be found [elsewhere on the web](http://wiredworld.tripod.com/tronics/atmel_isp.html) ([Wayback Machine](http://web.archive.org/web/20071024175932/http://wiredworld.tripod.com/tronics/atmel_isp.html)).

I'm not sure, but as I understood the schematics, this dongle will get the needed Vcc from the microcontroller connector.

### Serial port

The [MiniPOV3](http://www.ladyada.net/make/minipov3/index.html) ([Wayback Machine](http://web.archive.org/web/20071012232209/http://www.ladyada.net/make/minipov3/index.html)) DIY project uses a serial port to program the chip. This works in a similar way to the parallel port programming, but requires some diodes too. You can see [the schematic diagram](http://www.ladyada.net/images/minipov3/minipov3schem.png) ([Wayback Machine](http://web.archive.org/web/20100612041806/http://ladyada.net/images/minipov3/minipov3schem.png)) at [Design link](http://www.ladyada.net/make/minipov3/hardware.html) ([Wayback Machine](http://web.archive.org/web/20071012232204/http://www.ladyada.net/make/minipov3/hardware.html)). You can also see [a page dedicated to the serial dongle](http://www.ladyada.net/make/spokepov/makeserialdongle.html) ([Wayback Machine](http://web.archive.org/web/20071013130827/http://ladyada.net/make/spokepov/makeserialdongle.html)) at [SpokePOV](http://www.ladyada.net/make/spokepov/) ([Wayback Machine](http://web.archive.org/web/20071014050832/http://ladyada.net/make/spokepov)) project.

Personally, I don't see enough good reasons to use the serial port over the parallel port. The only good reason is the size (a serial port is about half of the size of a parallel port). However, I guess that, if a PC does not have a parallel port, most likely it won't have a serial port either. In addition, the serial port programmer requires a few more componentes (3 diodes). Finally, it uses a method called “bitbanging”. I don't like this name, it sounds too hackish and cheap for me.

### USB port

There is a so-called [inexpensive USB AVR programmer](http://www.ladyada.net/make/usbtinyisp/index.html) ([Wayback Machine](http://web.archive.org/web/20071019054156/http://www.ladyada.net/make/usbtinyisp/index.html)). You can [buy the kit](http://www.adafruit.com/index.php?main_page=index&cPath=16) ([Wayback Machine](http://web.archive.org/web/20071012020148/http://www.adafruit.com/index.php?main_page=index&cPath=16)) with all needed components for US$ 22.00, or you can use the instructions and find or buy the components by your own.

This programmer is more complex. It uses an AVR microcontroller and some [tri-state buffers](http://en.wikipedia.org/wiki/Tri-state_buffer). It will be difficult (or impossible, or at least ugly and messy) to build this without a [PCB][] or a [stripboard][]. It also has two LEDs (one red and one green) to display the current status. If you buy the kit, this programmer looks pretty neat because of the case and the LEDs.

This programmer is also good because it can use the USB to give enough power to the microcontroller being programmed, avoiding the need of external power supply, unlike the parallel/serial programmers.

In my opinion, if your PC has neither the parallel port nor the serial port, but has at least one available USB port, and you don't want to buy a USB-to-Serial or a USB-to-Parallel adapter, then this is the programmer you should build (_I've changed my mind, see the update below_).

On the other hand, there are some disadvantages with this project. The first one is the price (US$ 22.00 versus US$ 7.50 for the parallel/serial dongle kit at [the same site](http://www.adafruit.com/index.php?main_page=index&cPath=16) ([Wayback Machine](http://web.archive.org/web/20071012020148/http://www.adafruit.com/index.php?main_page=index&cPath=16))). The second one is the need for a USB A-B cable. Of course you must have at least one of this cable lying around somewhere (or at least one connecting your printer or scanner), but the parallel/serial programmers don't need any extra cable. Ok, I know this is easy to fix. Just get a cable, cut one of the connectors and solder the cable to the dongle.

Another disadvantage is the buggy libusb on 64-bit architectures, as you can read on [FAQ](http://www.ladyada.net/make/usbtinyisp/faq.html) ([Wayback Machine](http://web.archive.org/web/20071026042110/http://www.ladyada.net/make/usbtinyisp/faq.html)). It also looks like you need to be root to use libusb and this device (but I'm not sure), while it's not needed with parallel/serial programmers (I need to get root once to change permissions of the /dev/something device or to add my ordinary user to some group).

Yet another disadvantage is the difficulty to build this dongle without buying the kit. You must buy two chips and a [PCB][] or a [stripboard][] and solder everything together. The buffer chip should be easy to find (but I don't know if it really is). The ATTINY2313-20PU chip, however, might not be so easy. I found ATmega8 and ATmega16 at [Cerne-Tec](http://www.cerne-tec.com.br/) (which is located in Rio de Janeiro, where I live), but only these two models are sold there, they don't sell ATtiny. Probably I can replace the ATtiny with ATmega, but it will probably make the project a bit more expensive. Finally, whenever you get the microcontroller, you still need to program it with the USBtinyISP firmware, but how? (the “chicken & egg” problem) Well, you can use someone else's programmer, or you can just use a serial or parallel programmer. But, in the latter case, why don't you just use that programmer for everything else?

**Update at 2008-01-03:** I've just found another USB ISP programmer. It's called [USBasp](http://www.fischl.de/usbasp/) ([Wayback Machine](http://web.archive.org/web/20080105030005/http://www.fischl.de/usbasp/)). _“It simply consists of an ATMega48 or an ATMega8 and a couple of passive components. The programmer uses a firmware-only USB driver, no special USB controller is needed.”_ After reading this, I've changed my mind. If I ever need to use an AVR programmer on a PC without parallel port, I will build this one.

I've read at [a page with instructions about USBasp](http://www.scienceprog.com/building-and-installing-usbasp-usb-programmer-of-avr-microcontrollers/) ([Wayback Machine](http://web.archive.org/web/20080103013932/http://www.scienceprog.com/building-and-installing-usbasp-usb-programmer-of-avr-microcontrollers/)) that you should connect the programmer to a port on the computer, avoiding [USB hubs](http://en.wikipedia.org/wiki/USB_hub). I'm not sure if this is the case of other USB programmers, but since nowadays computers fortunately have many USB ports, I hope this won't be a problem.

**Update at 2011-08-10:** I've bought a USBasp, and I've also built one on a breadboard. Everything is described in detail at [part 2.1][].

## Other links

* [PC parallel LPT port pinout (SPP)](http://pinouts.ru/ParallelPorts/ParallelPC_pinout.shtml) ([Wayback Machine](http://web.archive.org/web/20071013122024/http://pinouts.ru/ParallelPorts/ParallelPC_pinout.shtml))
* [ECP Parallel LPT port (IEEE-1284A) pinout](http://pinouts.ru/ParallelPorts/ParallelECP_pinout.shtml) ([Wayback Machine](http://web.archive.org/web/20071011022120/http://pinouts.ru/ParallelPorts/ParallelECP_pinout.shtml))
* [Information about using AVR ISP programmers](http://elm-chan.org/works/avrx/report_e.html)

{% include first-contact-with-atmega8-navigation.html %}

[ATmega8]: http://www.atmel.com/devices/ATMEGA8.aspx
[ATmega8 datasheet]: http://www.atmel.com/Images/Atmel-2486-8-bit-AVR-microcontroller-ATmega8_L_datasheet.pdf
[avrdude]: http://www.nongnu.org/avrdude/
[uisp]: http://www.nongnu.org/uisp/
[PonyProg]: http://www.lancos.com/prog.html
[ISP]: http://en.wikipedia.org/wiki/In-System_Programming
[firmware]: http://en.wikipedia.org/wiki/Firmware
[parallel port]: http://en.wikipedia.org/wiki/Parallel_port
[serial port]: http://en.wikipedia.org/wiki/Serial_port
[USB]: http://en.wikipedia.org/wiki/Universal_Serial_Bus
[DIY]: http://en.wikipedia.org/wiki/Do_it_yourself
[clock]: http://en.wikipedia.org/wiki/Clock_signal
[PCB]: http://en.wikipedia.org/wiki/Printed_circuit_board
[stripboard]: http://en.wikipedia.org/wiki/Stripboard
[part 2.1]: {{ site.url }}/blog/2011-08-10/first-contact-with-atmega8-microcontroller-part-2-1
