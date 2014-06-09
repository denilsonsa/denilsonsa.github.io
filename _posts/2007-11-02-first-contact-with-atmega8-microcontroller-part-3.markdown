---
date: 2007-11-02 14:11:00+00:00
excerpt: 'Now, I&#39;m going to leave the hardware parts alone and start working with
  the software. At the end of this part, we will have our <a href="http://en.wikipedia.org/wiki/Firmware"
  rel="nofollow" target="_blank">firmware</a> ready to be written (programmed) into
  the microcontroller. ... '
layout: post
title: First contact with ATmega8 microcontroller - part 3
tag:
- avr
- gentoo
- atmega8
- linux
- microcontroller
---

Now, I'm going to leave the hardware parts alone and start working with the software. At the end of this part, we will have our [firmware](http://en.wikipedia.org/wiki/Firmware) ready to be written (programmed) into the microcontroller. ...

<!-- more -->Go to: [part 1](http://my.opera.com/CrazyTerabyte/blog/2007/10/25/first-contact-with-atmega8-microcontroller-part-1), [part 2](http://my.opera.com/CrazyTerabyte/blog/2007/10/26/first-contact-with-atmega8-microcontroller-part-2), [part 2.1](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1) ([video](http://www.youtube.com/watch?v=sr0B-5Bhxdg)), **part 3**, [part 4](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4) ([video](http://www.youtube.com/watch?v=V7ESjm2bG-A)).

For this part I'm going to write a "[Hello, world](http://en.wikipedia.org/wiki/Hello_world_program)" software for the [ATmega8][] [microcontroller][], which will make 4 [LEDs](http://en.wikipedia.org/wiki/Light-emitting_diode) blink.

I'm going to write it in three different ways. I've choosen to do so in order to learn more and because I might need one or more of these in future. _**Update 2008-02-05:** I found a fourth way and I'm going to describe it too._

**#1: Writing the firmware in C and compiling with avr-gcc**

**Required software**



  * Any text editor
  * avr-gcc

You should already have at least one text editor installed.

When I talk about _avr-gcc_, in fact I talk about a couple of packages: _avr-binutils_, _avr-libc_, _avr-gcc_ and optionally _avr-gdb_. To install them on [Gentoo/Linux](http://www.gentoo.org/), run these commands (as root):



    emerge -av crossdev
    crossdev -t avr


Run **crossdev** without parameters for usage instructions.

Optionally, after above commands, run the following one to add these packages to the world file (_/var/lib/portage/world_):



    emerge --noreplace cross-avr/binutils cross-avr/gcc cross-avr/avr-libc


Optionally, edit _/etc/portage/package.keywords_ and comment out some of the lines added by the _crossdev_ script.
Also, you may want to add the **doc** [USE flag](http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=2) to the _avr-libc_ package at the _/etc/portage/package.use_ file. (then use **avr-man** or **/usr/share/doc/avr-libc-1.4.4/**)

After all of this, you will have a bunch of **avr-*** tools installed on your system:



    avr-addr2line  avr-cpp        avr-gcov       avr-nm         avr-readelf
    avr-ar         avr-gcc        avr-gprof      avr-objcopy    avr-size
    avr-as         avr-gcc-4.2.2  avr-ld         avr-objdump    avr-strings
    avr-c++filt    avr-gccbug     avr-man        avr-ranlib     avr-strip


They are the _AVR versions_ of the standard Unix and GNU/Linux tools. By _AVR versions_ I mean that they work on AVR-related files (AVR sources and binaries).

Optionally, you may choose to build _avr-gcc_ with C++ support (disable the **nocxx** USE flag). I really don't think it is needed, because I think it is not a good idea to use C++ to write programs to a microcontroller and because the stdc++ library is not available for the AVR. [(1)](http://electrons.psychogenic.com/modules/arms/art/3/AVRGCCProgrammingGuide.php#progcpp)

**The C code: hello.c**

Just notice that there are many ways of doing the same thing. This is how I've done it.

_You can download this code and the Makefile to compile it at the end of this post._



    #include <avr/io.h>          // this contains all the IO port definitions
    #include <compat/ina90.h>    // among other things, contains _NOP()

    void wait_some_time()
    {
        // Use this to store the counter at SRAM. This will be slower.
        //volatile unsigned short int t = 0;

        // Use this to store the counter inside registers.
        register unsigned short int t = 0;

        while(++t) _NOP();
    }

    int main()
    {
        DDRC  = 0x0F;  // PC0..PC3 as output
        PORTC = 0x00;  // all PORTC output pins Off

        while(1)
        {
            PORTC ^= 0x01;
            wait_some_time();
            PORTC ^= 0x02;
            wait_some_time();
            PORTC ^= 0x04;
            wait_some_time();
            PORTC ^= 0x08;
            wait_some_time();
        }
        return 0;
    }



**Compiling the C code with avr-gcc**

Basically, all you need is:



    avr-gcc -mmcu=atmega8 -o hello.elf hello.c


You might want to compile in two phases, generating the .o first and then linking it all together with the libc:



    avr-gcc -c -mmcu=atmega8 -o hello.o hello.c
    avr-gcc -mmcu=atmega8 -o hello.elf hello.o


You might also want to add some flags...


  * **-std=c99** This makes gcc use C99 standard when compiling C code. Among other things, this allows //-style comments.
  * **-pipe** This avoids using temporary files and tries to use pipes when passing things from one stage to another. It is a good flag to use anytime you compile anything with GCC.
  * **-Wall** Enables all warnings. Again, it is a good flag to use whenever you develop things with GCC.
  * **-Os** Optimize for size, trying to archieve a faster and smaller code. Maybe you might want to try other flags, like **-O0** (do not optimize) or **-O1** or **-O2**.
  * **-funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums** I'm not very sure why these things might be useful, but many people use them when developing for AVR.
  * **-Wa,-adhlns=hello.lst** GCC will pass this parameter to the assembler. In a nutshell, it will write a _hello.lst_ file containing the generated assembly code. If you compile things in two phases, then this flag should be added to the first one only (when making the .o out of the .c source). Personally, I think this flag is not much useful, because it prints the assembly code before linking with libc and, thus, it is not the final assembly code at the correct positions.

The **-mmcu=atmega8** flag is mandatory. Read the GCC documentation (**man gcc**) to find out all possible values.

If you are on [Gentoo](http://www.gentoo.org/), you will notice that above command actually does not work. It fails with the following message:



    /usr/libexec/gcc/avr/ld: cannot open linker script file ldscripts/avr4.x: No such file or directory


This is a [known bug](http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&p=336170) ([bug #147155](http://bugs.gentoo.org/show_bug.cgi?id=147155)). Fortunately, there is a very easy workaround. Just add **-L/usr/i686-pc-linux-gnu/avr/lib** to the above command (or to the second command, in case you are compiling in two phases).

Finally, after that, you will end up with a nice **hello.elf** file. It is already marked as executable (+x bit), but you can't really run it, because it is an executable for AVR, and not for x86 host (or whatever you are running). In addition, it is not in an appropriate format for passing to the programmer software ([avrdude](http://www.nongnu.org/avrdude/) or [uisp](http://www.nongnu.org/uisp/)). So, basically, that file by itself is useless. The _trick_ is to extract and convert portions of that file to the appropriate formats.

To extract the program data (the one which will be written to the [flash memory](http://en.wikipedia.org/wiki/Flash_memory)), use one of these commands (both should work, just choose one):



    avr-objcopy -R .eeprom -O ihex hello.elf hello.hex
    avr-objcopy -j .text -j .data -O ihex hello.elf hello.hex


To extract the EEPROM data (which, of course, will be written to the [EEPROM memory](http://en.wikipedia.org/wiki/EEPROM)), use:



    avr-objcopy -j .eeprom --change-section-lma .eeprom=0 -O ihex hello.elf hello.eep


I saw someone using the **--set-section-flags=.eeprom="alloc,load"** flag. I don't know why it has been used, and I would appreciate if someone could explain it to me.

After these commands, you will have **hello.hex** and **hello.eep**, which are the data ready to be written to the microcontroller. These files are saved in [Intel Hex format (ihex)](http://www.scienceprog.com/shelling-the-intel-8-bit-hex-file-format/). This format is recognized by most programmer software, including [avrdude](http://www.nongnu.org/avrdude/) and [uisp](http://www.nongnu.org/uisp/).

For this simple "Hello, world" program, there is no data to be written to EEPROM, and the hello.eep file will be empty (well, almost, there will be a line marking the end of file). Even though we won't be using EEPROM in this simple project, it is important to know how to use it for future projects.

There is just one more thing you should know: how to get a nice disassembled version of the final firmware. This is very useful to understand what code the avr-gcc has generated. To do that, just run this command:



    avr-objdump -S hello.elf > hello.lss


You may add the **-d** flag, but it is not needed, since it is implied by **-S**.

You might want to add the **-C** flag, but I haven't noticed any change when using it.

Finally, you may run **avr-objdump -h hello.elf** to see what are the sections available inside this [ELF](http://en.wikipedia.org/wiki/Executable_and_Linkable_Format) file.

**#2: Writing the firmware in assembly and compiling with avr-gcc**

**Required software**



  * Any text editor
  * avr-gcc

You need the exact same environment as the #1. Please refer to above section to instructions about how to install the required software.

**The assembly code: main.S**

Notice: please save with **.S** extension (with upper case S).

_You can download this code and the Makefile to compile it at the end of this post._



    #include <avr/io.h>

    .global main
    main:
        ldi r17, 0x0F    ; This goes to DDRC
        ldi r16, 0x00    ; This goes to PORTC
        out _SFR_IO_ADDR(DDRC), r17
        out _SFR_IO_ADDR(PORTC), r16
        ldi r17, 1
        ldi r18, 2
        ldi r19, 4
        ldi r20, 8

    main_loop:
        rcall wait_some_time
        eor r16, r17
        out _SFR_IO_ADDR(PORTC), r16
        rcall wait_some_time
        eor r16, r18
        out _SFR_IO_ADDR(PORTC), r16
        rcall wait_some_time
        eor r16, r19
        out _SFR_IO_ADDR(PORTC), r16
        rcall wait_some_time
        eor r16, r20
        out _SFR_IO_ADDR(PORTC), r16
        rjmp main_loop


    wait_some_time:
        push r24
        push r25
        ldi r24, 0xFF
        ldi r25, 0xFF
    wait_some_time_loop:
        sbiw r24, 1
        brne wait_some_time_loop
        pop r25
        pop r24
        ret



**Compiling the assembly code with avr-gcc**

Please follow the exact same steps as #1. GCC will automatically detect the **.S** extension as _assembler code which must be preprocessed_. In case this autodetection fails, you may add the **-x assembler-with-cpp** flag.

All the instructions about making an [ELF](http://en.wikipedia.org/wiki/Executable_and_Linkable_Format) file and then converting portions of it to [ihex format](http://www.scienceprog.com/shelling-the-intel-8-bit-hex-file-format/) are the same. Please refer to above section.

**#3: Writing the firmware in assembly and compiling with tavrasm**

**Required software**



  * Any text editor
  * [tavrasm](http://www.tavrasm.org/)

This third method of writing firmware for AVR does not use _avr-gcc_. Instead, it uses [tavrasm](http://www.tavrasm.org/), which is a simple [assembler](http://en.wikipedia.org/wiki/Assembly_language#Assembler) that aims to be compatible with [Atmel]()'s AVR DOS assembler.

[tavrasm](http://www.tavrasm.org/) is very small, simple and easy to use. To install it on [Gentoo/Linux](http://www.gentoo.org/), run:



    emerge -av tavrasm



**The assembly code: hello.asm**

_You can download this code and the Makefile to compile it at the end of this post._



    .device atmega8

    .equ    SPH     =0x3E
    .equ    SPL     =0x3D
    .equ    DDRC    =0x14
    .equ    PORTC   =0x15


    .cseg    ; Start of code segment
    .org 0
        rjmp main

    .org 0x26    ; After the reset/interrupt table
    main:
        ldi r16, 0x5F    ; Setting up the SP (stack pointer)
        ldi r17, 0x04
        out SPL, r16
        out SPH, r17

        ldi r17, 0x0F    ; This goes to DDRC
        ldi r16, 0x00    ; This goes to PORTC
        out DDRC, r17
        out PORTC, r16
        ldi r17, 1
        ldi r18, 2
        ldi r19, 4
        ldi r20, 8

    main_loop:
        rcall wait_some_time
        eor r16, r17
        out PORTC, r16
        rcall wait_some_time
        eor r16, r18
        out PORTC, r16
        rcall wait_some_time
        eor r16, r19
        out PORTC, r16
        rcall wait_some_time
        eor r16, r20
        out PORTC, r16
        rjmp main_loop


    wait_some_time:
        push r24
        push r25
        ldi r24, 0xFF
        ldi r25, 0xFF
    wait_some_time_loop:
        sbiw r24, 1
        brne wait_some_time_loop
        pop r25
        pop r24
        ret



**Compiling the assembly code with tavrasm**

The easiest way:



    tavrasm hello.asm -o hello.hex


The complete way:



    tavrasm hello.asm -o hello.hex -e hello.lst -r hello.eep


This command will compile the **hello.asm** file into **hello.hex** (already in [Intel Hex format](http://www.scienceprog.com/shelling-the-intel-8-bit-hex-file-format/)), will save the EEPROM data to **hello.eep** (also in [Intel Hex format](http://www.scienceprog.com/shelling-the-intel-8-bit-hex-file-format/)) and will save a nice human-readable listing file to **hello.lst** (containing both the hexadecimal dump and the assembly source).

That's it. All done. Simple, isn't it?

**#4: Writing the firmware in assembly and compiling with AVRA** _(new, added in 2008-02-05)_

**Required software**



  * Any text editor
  * [AVRA](http://avra.sourceforge.net/)

This fourth method of writing firmware for AVR also does not use _avr-gcc_. Instead, it uses [AVRA](http://avra.sourceforge.net/), which is also an [assembler](http://en.wikipedia.org/wiki/Assembly_language#Assembler) that aims to be compatible with [Atmel]()'s AVR assembler. The README file says it can easily replace AVRASM32 in Atmel AVR Studio.

To install it on [Gentoo/Linux](http://www.gentoo.org/), run:



    emerge -av avra



**The assembly code: hello.asm**

It compiles the same code as [tavrasm](http://www.tavrasm.org/). Check the code available at #3.

**Compiling the assembly code with AVRA**

To tell the truth, I've not explored [AVRA](http://avra.sourceforge.net/) too much. I've just discovered it and I thought it would be important to update this blog post.

You use it in a way similar to [tavrasm](http://www.tavrasm.org/), but with different command-line parameters. Well, just check the README file, ok?

**Comparison of the 4 methods**

**C with avr-gcc**

**Advantages:**


  * Ability to write code in a high-level language (at least when compared to assembly).
  * Access to avr-libc functions.
  * Optional support for software-based floating point math.
**Disadvantages:**


  * Less control on generated code.

**Assembly with avr-gcc**

**Advantages:**


  * Easy to integrate with C code.
  * Has support for [C preprocessor](http://en.wikipedia.org/wiki/C_preprocessor).
  * Access to avr-libc functions (I'm not sure about this, but I think it's possible).
**May be an advantage or disadvantage:**


  * Must link against avr-libc, which means that avr-gcc adds its own initialization code and some other things.
**Disadvantages:**


  * Ugly sintax for in/out instructions. (example: _out _SFR_IO_ADDR(PORTC), r16_)
  * Not entirely compatible with Atmel's assembler (and, thus, with thousands of codes available at the Internet).

**Assembly with tavrasm or with AVRA**

**Advantages:**


  * Simple and easy to use.
  * Compatible with Atmel's assembler.
  * Full control on generated code.
**Disadvantages:**


  * Impossible (or at least very difficult) to integrate with avr-gcc or with C.

**Download all files used in this post**

_**Update at 2011-08-11: ** All code for this project is now available at: [https://bitbucket.org/denilsonsa/atmega8-blinking-leds](https://bitbucket.org/denilsonsa/atmega8-blinking-leds) (future source-code updates, if any, will be posted there)_

**[Download the atmega8-hello.tar.gz](http://files.myopera.com/CrazyTerabyte/atmega8/atmega8-hello.tar.gz)**

This archive contains:



  * **atmega8-hello/Makefile.tpl** - copied from [Electrons - Standardized AVR Makefile Template](http://electrons.psychogenic.com/modules/arms/art/8/AVRProjectOrganizationStandardizedAVRMakefileTemplate.php).
  * **atmega8-hello/first_hello/hello.c** - The C source code.
  * **atmega8-hello/first_hello/Makefile** - A Makefile I wrote from scratch (copying some commands from other places from the Internet).
  * **atmega8-hello/second_hello/main.S** - The avr-gcc assembly source code.
  * **atmega8-hello/second_hello/Makefile** - A Makefile based on Makefile.tpl.
  * **atmega8-hello/third_hello/hello.asm** - The tavrasm assembly source code.
  * **atmega8-hello/third_hello/Makefile** - A Makefile I wrote from scratch (based on _first_hello/Makefile_).

**Other links**



  * [Electrons - AVR-GCC Programming Guide](http://electrons.psychogenic.com/modules/arms/art/3/AVRGCCProgrammingGuide.php)
  * [Atmel's AVR Assembler User Guide](http://www.atmel.com/atmel/acrobat/doc1022.pdf) - Describes the Atmel's assembler. Very useful to know what assembler directives you may use with [tavrasm](http://www.tavrasm.org/).
  * [Atmel 8-bit AVR Instruction Set](http://www.atmel.com/atmel/acrobat/doc0856.pdf) - The complete and detailed list of all assembly instructions for AVR microcontrollers.
  * [Atmel's ATmega8 datasheet](http://www.atmel.com/atmel/acrobat/doc2486.pdf) - Full description of [ATmega8][].


Go to: [part 1](http://my.opera.com/CrazyTerabyte/blog/2007/10/25/first-contact-with-atmega8-microcontroller-part-1), [part 2](http://my.opera.com/CrazyTerabyte/blog/2007/10/26/first-contact-with-atmega8-microcontroller-part-2), [part 2.1](http://my.opera.com/CrazyTerabyte/blog/2011/08/10/first-contact-with-atmega8-microcontroller-part-2-1) ([video](http://www.youtube.com/watch?v=sr0B-5Bhxdg)), **part 3**, [part 4](http://my.opera.com/CrazyTerabyte/blog/2008/02/02/first-contact-with-atmega8-microcontroller-part-4) ([video](http://www.youtube.com/watch?v=V7ESjm2bG-A)).

[ATmega8]: http://www.atmel.com/dyn/products/product_card.asp?part_id=2004
[microcontroller]: http://en.wikipedia.org/wiki/Microcontroller
