---
layout: post
title: devcon.exe for Windows (and F.E.A.R. games)
lang: en
tags:
- Windows
---

`devcon.exe` is a command-line tool alternative to the Windows Device Manager.


Version 5.2.3718.0, released on 2003-01-29, modification date from 2002-11-15, can be downloaded from [Q311272](https://support.microsoft.com/en-us/kb/311272). Only available on *ia64* and *x86* architectures. It is very old, designed to work on Windows up to version 2003. Don't waste time trying this version.

Version 6.1.7600.16385, modification date from 2010-02-08, is inside `setuptools_x86fre.msi` and `setuptools_x86fre_cab001.cab` (or `setuptools_x64fre.msi` and `setuptools_x64fre_cab001.cab`), which can be found inside `GRMWDK_EN_7600_1.ISO`, which is the [*WDK 7.1.0* (Windows Driver Kit)](https://msdn.microsoft.com/en-US/windows/hardware/hh852365) that [can be downloaded from Microsoft](https://www.microsoft.com/en-us/download/confirmation.aspx?id=11800). This version should be compatible with Windows 7. To save you trouble, I'm also making it available for download: [devcon_x86.exe]({{ site.url }}/blog/files/devcon_6.1.7600.16385_x86.exe) and [devcon_amd64.exe]({{ site.url }}/blog/files/devcon_6.1.7600.16385_amd64.exe).

Source-code is available at [Microsoft's repository on GitHub](https://github.com/Microsoft/Windows-driver-samples/tree/master/setup/devcon).

### Links regarding `devcon.exe`

* <http://social.technet.microsoft.com/wiki/contents/articles/182.how-to-obtain-the-current-version-of-device-console-utility-devcon-exe.aspx>
* <https://answers.microsoft.com/en-us/windows/forum/windows_7-hardware/devcon-not-working-correctly-in-windows-7/9abcc12c-d7db-4249-aec4-fc4ff0ea6ee8#ThreadAnswers>
* <https://superuser.com/questions/305685/devcon-exe-not-working-in-windows7-x64>
* <http://9b5.org/2011/10/getting-devcon-exe-onto-and-working-with-windows-7/>
* <http://techlikes.com/2010/09/25/devcon-problem-in-windows-7-solved.html>

## F.E.A.R. games

[*F.E.A.R.* games have an issue with Logitech USB devices](http://pcgamingwiki.com/wiki/F.E.A.R.#FPS_problems). The only known workaround is to disable them at Device Maanager.

Igor Duarte Cardoso posted [a `.bat` script to automatically disable and re-enable Logitech devices](https://github.com/igordcard/igordcard/blob/master/_downloads/run_fear.bat), which was later [edited by zacr0 to support the Steam version](https://gist.github.com/anonymous/43ac3eed100d46b04aee). The script is copied down below:

```bat
@echo off

:: Disable all Logitech HID devices.
devcon.exe disable HID\VID_046D*
:: The previous command disables too much and the mouse may stop working, but this line fixes it.
devcon.exe enable HID_DEVICE_SYSTEM_MOUSE

:: Uncomment one of the following lines:
::pause
::FEAR.EXE
::FEARMP.EXE
::start steam://rungameid/21090
::start steam://rungameid/21110
::start steam://rungameid/21120

:: Enable everything back.
devcon.exe enable HID\VID_046D*
```

### Does it work?

Unfortunately, it does not work for me. Running the script gives me:

```
D:\>devcon_amd64.exe disable HID\VID_046D*
HID\VID_046D&PID_C062\8&A7583A8&0&0000                      : Disabled
1 device(s) disabled.

D:\>devcon_amd64.exe enable HID_DEVICE_SYSTEM_MOUSE
HID\VID_045E&PID_0745&MI_01&COL01\9&283EC78A&0&0000         : Enabled
HID\WACOMVIRTUALHID&COL03\1&4784345&0&0002                  : Enabled
HID\VID_046D&PID_C062\8&A7583A8&0&0000                      : Enabled
HID\VID_056A&PID_0016&COL01\8&15A54371&0&0000               : Enabled
4 device(s) are enabled.
```

We can clearly see the [Logitech LS1 mouse](http://support.logitech.com/product/ls1-laser-mouse) being disabled on the first command, and then re-enabled on the second command.

My advice? Don't buy *F.E.A.R.* games.

### Links regarding the issue with F.E.A.R. games

* <https://gist.github.com/anonymous/43ac3eed100d46b04aee>
* <https://github.com/igordcard/igordcard/blob/master/_downloads/run_fear.bat>
* <http://igordcard.blogspot.com.br/2013/01/sudden-fps-drop-in-fear-logitech.html>
* <http://pcgamingwiki.com/wiki/F.E.A.R.#FPS_problems>
* <https://www.gog.com/forum/fear_series/terrible_performance>
* <http://forums.steampowered.com/forums/showthread.php?t=1279444>
* <https://forums.logitech.com/t5/Mice-Hardware/G5-G7-G15-FEAR-Solved-F-E-A-R/td-p/23474>
* <http://steamcommunity.com/app/21090/discussions/0/864951657825089435/>
* <http://forums.guru3d.com/showpost.php?p=3668045&postcount=12>

