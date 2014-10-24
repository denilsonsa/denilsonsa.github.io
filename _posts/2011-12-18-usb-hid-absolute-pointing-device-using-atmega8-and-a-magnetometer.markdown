---
layout: post
title: USB HID absolute pointing device using ATmega8 and a magnetometer
lang: en
tag:
- ATmega8
- AVR
- Hardware
- Microcontroller
- Programming
- Python
- USB
---

In last November, I finally finished my college! I've got a Bachelor's Degree in Computer Science by UFRJ (_Universidade Federal do Rio de Janeiro_).

And for my senior project (or final graduating project, or _TCC - Trabalho de Conclusão de Curso_, or _PFC - Projeto Final de Curso_) I chose to build a USB device that could control the mouse pointer, using an AVR ATmega8 microcontroller and a magnetometer.


A magnetometer is a digital compass, something that can measure the magnetic field (in three dimensions). The idea is that the user holds the magnetometer and moves it around (actually, only the rotation is considered). When the magnetometer orientation changes, the measured 3D vector of the magnetic field also changes. Based on this vector, the microcontroller applies some math and moves the mouse pointer to some position at the screen.

In a nutshell, the device behaves like a [Wiimote](http://en.wikipedia.org/wiki/Wii_Remote), but using a completely different technology. You just point the device to some direction, and the mouse pointer is moved to that position.

Since the microcontroller implements the [USB HID](http://en.wikipedia.org/wiki/USB_human_interface_device_class) class (using [V-USB firmware-only USB implementation, by OBJECTIVE DEVELOPMENT Software GmbH](http://www.obdev.at/products/vusb/index.html) ([Wayback Machine](http://web.archive.org/web/20101225062142/http://www.obdev.at/products/vusb/index.html))), it works straight away on any operating system without requiring any special driver. It has been successfully tested on Linux, Mac OS X and Windows. It was also tested on one Android device, but it did not support an absolute pointing device.

Links:

* **[Full source-code at BitBucket](https://bitbucket.org/denilsonsa/atmega8-magnetometer-usb-mouse)**
* **[Full source-code at GitHub](https://github.com/denilsonsa/atmega8-magnetometer-usb-mouse)**
* [Photos at Picasa](https://picasaweb.google.com/denilsonsa/Atmega8MagnetometerUsbMouse)
* [Videos at YouTube](https://www.youtube.com/playlist?list=PLA37C87EEDE5EC88C)

Videos:

[Dispositivo apontador com interface USB usando magnetômetro](https://www.youtube.com/watch?v=lBZV_GAg8yw) (English subtitles available)

<figure class="singleimage youtube">
{% include youtube.html video="lBZV_GAg8yw" cc=1 annotations=0 %}
</figure>

[Moving the mouse pointer using head movements](https://www.youtube.com/watch?v=1nuw9zsZtk4)

<figure class="singleimage youtube">
{% include youtube.html video="1nuw9zsZtk4" annotations=1 %}
</figure>

[USB Absolute Pointing Device implemented in ATmega8 using Magnetometer](https://www.youtube.com/watch?v=nZLTwfAJmrE) (work-in-progress video)

<figure class="singleimage youtube">
{% include youtube.html video="nZLTwfAJmrE" %}
</figure>

This project was challenging and very rewarding. It feels good to see it working after so many weeks staying awake during the night developing and debugging it.

Trivia: the idea for this project was inspired by Marcin Wichary speak/demonstration at [Google I/O 2011: The Secrets of Google Pac-Man: A Game Show](https://www.youtube.com/watch?v=ttavBa4giPc#t=2m46s)

<figure class="singleimage youtube">
{% include youtube.html video="ttavBa4giPc" extra_params="&amp;start=166&amp;end=290" %}
</figure>

