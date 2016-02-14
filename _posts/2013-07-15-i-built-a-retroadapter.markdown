---
layout: post
title: I built a RetroAdapter
tags:
- AVR
- ATmega8
- Hardware
- Microcontroller
- USB
---

A few weeks ago, I did what I wanted to do for a long time: I built my own [RetroAdapter][] ([Wayback Machine][RetroAdapterWBM]).


[RetroAdapter][] ([Wayback Machine][RetroAdapterWBM]) is an open-source project that uses an 8-bit AVR microcontroller (ATmega8 or ATmega168) to convert gamepads for old console video-games to USB. The list of compatible game controllers is huge, ranging from [Atari 2600](http://en.wikipedia.org/wiki/Atari_2600_hardware#Controllers) to [SEGA Dreamcast](http://en.wikipedia.org/wiki/Dreamcast#Accessories) and [Nintendo GameCube](http://en.wikipedia.org/wiki/GameCube#Controller). However, I'm only interested in one kind of gamepad: [SEGA Mega Drive 6-button controller](http://en.wikipedia.org/wiki/Sega_Genesis#Peripherals).

Parts list:

* 1 × ATmega8 (or ATmega168, or similar) microcontroller
* 1 × 10K Ω resistor
* 1 × 1K5 Ω resistor
* 2 × 68 Ω resistors (in fact, [any value between 30 and 100 Ω should work](http://forums.obdev.at/viewtopic.php?f=8&t=333) ([Wayback Machine](https://web.archive.org/web/20130616160938/http://forums.obdev.at/viewtopic.php?f=8&t=333)))
* 2 × 3V6 zener diodes
* 1 × 12MHz crystal (other frequencies supported by [V-USB](http://www.obdev.at/products/vusb/) ([Wayback Machine](https://web.archive.org/web/20130709064854/http://www.obdev.at/products/vusb/index.html)) might also work)
* 2 × 22pF capacitors
* 1 × 10µF capacitor
* 1 × 100nF capacitor
* 2 × [male DE9 connectors](http://en.wikipedia.org/wiki/D-subminiature) (if you want to build a full-featured RetroAdapter, you need one DE9 and one DA15 instead)
* USB cable
* 6-pin or 10-pin header for using the ICSP
* Lots of wire, a board to mount the circuit, a socket for the microcontroller
* A box to put the circuit inside and to mount the two connectors

## The circuit

This is the schematic diagram for [RetroAdapter V2][RetroAdapter] ([Wayback Machine][RetroAdapterWBM]) (based on [the original schematic](http://denki.world3.net/img/retro/schematic_w.png) ([Wayback Machine](https://web.archive.org/web/20150927151939/http://denki.world3.net/img/retro/schematic_w.png))):

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/retroadapter_atmega8.png" alt="Schematic diagram for RetroAdapter V2 circuit.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/retroadapter_atmega8-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/retroadapter_atmega8.svg">SVG version</a>)
</figcaption>
</figure>

Since I'm only interested in SEGA Mega Drive gamepads, I can simplify the circuit

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/retroadapter_atmega8_dual_megadrive.png" alt="Schematic diagram for RetroAdapter V2 circuit restricted to SEGA Mega Drive gamepads.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/retroadapter_atmega8_dual_megadrive-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/retroadapter_atmega8_dual_megadrive.svg">SVG version</a>)
</figcaption>
</figure>

Note: The colors for Player 1 and Player 2 connections in the diagram were chosen to be the exact same colors as Sonic and Tails.

## The hardware

Here is a picture of the finished circuit board (sorry, I didn't take any picture of the solder side):

<figure class="singleimage polaroid">
<img src="{{ site.url }}/blog/images/avr/retroadapter_circuit_1.jpg" alt="Picture of the finished circuit board with all components and wires soldered.">
</figure>

There are a few things I want to highlight at the previous picture:

* The 22pF capacitors are required by the ATmega8 datasheet, but my circuit worked well even without them.
* The 10µF (or 4.7µF) and 100nF capacitors are standard [decoupling capacitors](http://electronics.stackexchange.com/q/2272) ([Wayback Machine](https://web.archive.org/web/20130507071546/http://electronics.stackexchange.com/questions/2272/what-is-a-decoupling-capacitor-and-how-do-i-know-if-i-need-one)), and they are also missing from the finished circuit. I probably should have added them for increased stability.
* At the bottom-left, I've added a 6-pin header for [in-circuit serial programming (ICSP)]({% post_url 2011-08-10-first-contact-with-atmega8-microcontroller-part-2-1 %}).
* At the top-right, I've added a 4-pin header for the USB cable. If someday my current USB cable breaks, I can easily replace it without resoldering the board.
* The holes at top-left are arbitrary, I drilled them years ago. Still, I used one of those holes to attach the board to the plastic box with a screw. I had to drill another hole at bottom-right (not pictured) to attach a second screw.

While soldering all the pieces together, I used a [multimeter](http://en.wikipedia.org/wiki/Multimeter) to make sure everything was soldered correctly. Fortunately, I've managed to solder everything without any mistakes, and the board worked on the first try (woohoo!).

## The firmware

After the board was ready, I went to my Gentoo Linux machine to prepare the firmware. It took a bit longer than expected, it was not really trivial, but it wasn't too difficult either.

I had to adapt the `Makefile`, remove the code that used `PCICR` register (it is only available on newer AVR microncontrollers, it is not available on ATmega8), update the [V-USB](http://www.obdev.at/products/vusb/) ([Wayback Machine](https://web.archive.org/web/20130709064854/http://www.obdev.at/products/vusb/index.html)) driver to a newer version (to fix an error related to `SIG_INTERRUPT0` being renamed to `INT0_vect` in newer compiler versions), and remove support for Amiga mouse and analogue BBC controllers (some compiler errors that I didn't bother to fix, as I won't ever use those controllers). After these changes, the firmware size was around 7KB. Yes, it fits into ATmega8's 8KB ROM, but it won't fit into the 6KB limit if I decide to also use a bootloader. So I continued disabling other modules that I won't ever use (PC-Engine, PC-FX, 3DO, Atari driving, SNES mouse…). Great! The firmware is now under 6KB.

Then, I had to hard-code support for SEGA Mega Drive controllers on the DB15 port. In the original RetroAdapter design, the DB15-to-DB9 adapter would pull pins `PC3` and `PC4` to `VCC`, and pull pin `PC5` to `GND`. This combination is read by the firmware through a sequence of `if` statements and is used to detect that the controller on the DB15 port is a second Mega Drive controller. Since I'm not using a DB15 port, and also I didn't want to hard-wire those pins to specific logic values in the circuit (instead, I left those pins unconnected), I had to override this detection logic via software. Basically, I [hard-coded those `if` statements](https://bitbucket.org/denilsonsa/retroadapter/commits/8d4558500f1d29c281a4cd2d8de18fcb4b5e5b9a) to always run the Mega Drive controller branch.

After all these changes, it was time to write the firmware into the microntroller and test the device… And it works! On the first try! Amazing! Congratulations to Paul Qureshi for creating this project!

But it still had two small but annoying bugs: the <kbd>Start</kbd> and <kbd>Mode</kbd> buttons were mapped to the same button on the second Mega Drive controller, and the <kbd>Start</kbd>/<kbd>Mode</kbd> button mapping was different between the first and the second virtual USB joysticks. Both were [trivial to fix](https://bitbucket.org/denilsonsa/retroadapter/commits/822507e3a888d9c52ab78bb1aadf8c19bc4f1f8d).

Finally, the icing on the cake, I wanted to add the bootloader to my device, so would be able to update the firmware without requiring any extra device. It turned out to be harder than I thought, but in the end I've managed to use an [updated version of USBaspLoader](https://github.com/baerwolf/USBaspLoader/commit/2ee56517b777f82220a08b1ec5b2b00e2694433f) as the bootloader. Now, if I connect my RetroAdapter to a computer while holding the B button from any Mega Drive controller, it will boot into USBaspLoader mode, allowing firmware updates.

The final firmware with all my modifications is available as a [hg repository at BitBucket](https://bitbucket.org/denilsonsa/retroadapter/).

## The finished product

After everything was working correctly, I bought a plastic box to hold the circuit. I also had to buy some screws, some nuts and some washers. I used a cheap soldering iron (that I won't use for soldering electronic components) to melt holes in the plastic box, and I enlarged and smoothed those holes using some [files][].

This adapter works on both Linux, Windows and Android. Yes, I can connect it to a Android smartphone and use a SEGA Mega Drive joystick to control the Android device. How awesome is that? And it should also work on Mac, but I couldn't test it because I don't have one.

<figure class="singleimage polaroid">
<a href="{{ site.url }}/blog/images/avr/retroadapter_box_1-hi.jpg"><img src="{{ site.url }}/blog/images/avr/retroadapter_box_1-lo.jpg" alt="Picture of the plastic box with the circuit board screwed inside, the two DE9 connectors, and the USB cable."></a>
</figure>

<figure class="singleimage polaroid">
<a href="{{ site.url }}/blog/images/avr/retroadapter_box_2-hi.jpg"><img src="{{ site.url }}/blog/images/avr/retroadapter_box_2-lo.jpg" alt="Another picture of the plastic box with all the components."></a>
</figure>

<figure class="singleimage polaroid">
<a href="{{ site.url }}/blog/images/avr/retroadapter_box_3-hi.jpg"><img src="{{ site.url }}/blog/images/avr/retroadapter_box_3-lo.jpg" alt="Picture of the finished box, already closed. We can see the USB cable and one of the DE9 connectors."></a>
</figure>

<figure class="singleimage polaroid">
<a href="{{ site.url }}/blog/images/avr/retroadapter_box_4-hi.jpg"><img src="{{ site.url }}/blog/images/avr/retroadapter_box_4-lo.jpg" alt="Picture of the finished box with two SEGA Mega Drive controllers connected to it."></a>
</figure>

## See also

* [Retro Adapter homepage][RetroAdapter] ([Wayback Machine][RetroAdapterWBM])
* [Retro Adapter connections pinout](https://docs.google.com/spreadsheet/ccc?key=0Aho3omeSKZ7AdFJPWEFVOEpNX3lOTjdYcVFoX3pfS1E)
* [My modified version of the firmware](https://bitbucket.org/denilsonsa/retroadapter/)
* [First contact with ATmega8 microcontroller]({% post_url 2007-10-25-first-contact-with-atmega8-microcontroller-part-1 %}), a multi-part series of posts where I explain how to work with AVR microcontrollers

[RetroAdapter]: http://denki.world3.net/retro_v2.html
[RetroAdapterWBM]: https://web.archive.org/web/20130517141051/http://denki.world3.net/retro_v2.html
[files]: https://en.wikipedia.org/wiki/File_(tool)
