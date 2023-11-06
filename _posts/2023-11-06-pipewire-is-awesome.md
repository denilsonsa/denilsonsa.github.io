---
layout: post
title: PipeWire is awesome!
lang: en
tags: [Linux]
---

Modern Linux distros are switching from [PulseAudio][] to [PipeWire][], and I have to say: PipeWire is great!


But what is PipeWire? It is a [sound server][] that tries to combine most of
the features from both [JACK][] and [PulseAudio][], while also providing
backwards-compatible APIs. Historically, professional audio applications on
Linux were targeting the JACK sound server, while most applications for general
users were using either PulseAudio or ALSA. With PipeWire, both kinds of
applications can now talk to each other.

Confused? Well, there is a lot to unpack in the previous paragraph. Let's
understand each piece, one-by-one.

## Sound drivers and low-level APIs

Before 2003 or 2004, the Linux kernel used [OSS (Open Sound System)][OSS]
(version 3) as the way to expose the sound card to user applications. It had
several limitations, and it was replaced by [ALSA][] in kernel version 2.6,
when the OSS license became proprietary. Some people argue that those
limitations were restricted to the (old) OSS implementation in the Linux
itself, and they were not inherent restrictions of the OSS interface. In fact,
OSS continued to evolve (to version 4) and is still being used in a few other
operating systems, such as Solaris. OSSv4 later added an open-source license as
well.

Unfortunately, due to these licensing issues, there is no unified API for audio
across Unix-based systems, and each system has their own native APIs. Although
OSSv4 can be installed on some operating systems, and on some systems there is
an OSS compatibility API, I believe in general the world has moved on. It
sounds like (pun intended) using OSS nowadays requires a lot of extra work on
any system.

In practice, many applications use some kind of library that abstracts the
low-level API calls, and thus the library can support different APIs on
different systems. So, for the general end-user, the choice of the low-level
APIs doesn't matter.

## Sound servers

But, in the early days, the choice of the low-level sound APIs was very
important. OSS in Linux didn't have support for mixing multiple sounds, and
even plain ALSA didn't have support either. Well, ALSA provided a module for
software-based mixing, and even hardware-based mixing if the sound card
supported that; but such features had to be properly configured. Otherwise, the
out-of-the-box experience was the lack of any mixing.

What does it mean? Well, when the user has two applications producing audio at
the same time, "mixing" would allow both sounds to be played simultaneously on
the same sound card (and thus on the same set of speakers or headphones).
Without mixing, then the first application to start using the sound card would
be the only application in the system that would be able to produce any audio.
(Until that application released the sound card, or when that application was
closed.) The second application would either be completely silent, or just hang
while waiting for the sound card to be available again.

As a side note, it is worth mentioning that [BeOS][] was an operating system
designed from scratch to support many multimedia applications and many other
modern features (when compared to other operating systems at that time). So,
yes, BeOS had native support for audio mixing one decade before Linux had it.

Back to Linux, in order to overcome the limitations of the low-level APIs,
several sound servers were written. A [sound server][] is an application that
runs in the background (AKA [daemon][]) and that positions itself as a layer
between the end-user applications and the low-level audio APIs, providing
additional features. The most important feature was mixing. In other words, a
sound server would receive audio from multiple clients (i.e. applications),
would mix it together, and would send a single audio stream to the sound card
(via either ALSA or OSS low-level APIs).

With the help of a sound server, the end-users could finally have music
playing on their Linux systems while at the same time hearing the notification
sounds for incoming e-mail or incoming messages. It would work, regardless of
the low-level API (OSS or ALSA), and regardless of hardware support.

## PulseAudio

Initially, there were multiple sound servers, each one incompatible with each
other. Folks at KDE created [aRts][], which was used in KDE 2 and in KDE 3.
Meanwhile, Enlightenment enthusiasts and GNOME users were using [ESD][]. But
anyone using any window manager and any desktop environment could run any of
sound server, or no sound server at all.

Among those, one sound server emerged as the de facto standard after several
years: [PulseAudio][]. Linux distros started shipping PulseAudio by default on
any desktop environment. In fact, PulseAudio is also available on a few other
operating systems besides Linux. (But I don't know if it is installed by
default on those systems.)

PulseAudio has many desirable features, though some of these were also present
on other sound servers:

* Audio mixing, multiple applications (clients) can play sounds simultaneously.
* Per-application volume control.
* Support for multiple sound cards.
* Support for hot-pluggable devices (such as USB sound cards or Bluetooth
  headsets).
* Audio re-routing to different devices (i.e. switching between speakers and
  headsets without restarting client applications).
* Compatibility layers for other APIs, supporting applications written for
  ALSA, aRts, ESD and even OSS.
* Network audio support (stream audio over the network).
* etc.

Like mentioned, these features are not exclusive to PulseAudio, some of the
other sound servers already supported some of those features. And, of course, a
few features are dependent on the low-level support (such as hot-pluggable
devices). But the main feature of PulseAudio was the broad adoption across most
Linux distributions, making it the de facto standard, instead of the very
fragmented software landscape of the past.

The compatibility layers helped with the adoption, meaning that software
written before PulseAudio (or without native PulseAudio support) would still
work just fine with the PulseAudio sound server. For instance, a new virtual
ALSA device would be created for PulseAudio, so that any application using ALSA
directly could use this virtual device, and the audio would be mixed and routed
by PulseAudio (which would then use ALSA to access the real hardware device).

For the general end-user, PulseAudio was the chosen solution. Chosen by
maintainers of the distros, and chosen by the developers of the desktop
environments. Supporting most use-cases and working in the background while the
user uses the computer. Not a perfect solution, but good enough.

## Professional use-cases

Except for the cases where it wasn't good enough. Although great for the
general end-user, professional audio users needed more features beyond what
PulseAudio could provide.

Professional users may have multiple sound cards in their systems. Maybe not
just internal sound cards connected to the motherboard, but also USB sound
devices. And such hardware may even provide several input channels and several
output channels.

You can imagine a single sound device that can accept the input from multiple
microphones. If those are professional microphones, they use [XLR][] connectors
instead of consumer-style 3.5mm jacks, requiring a dedicated box that is able
to provide [phantom power][] and handle [balanced audio][]. You can also
imagine several [line in / line out][line out] connectors. Let's not forget the
[MIDI][] ports. These are many more ports (and channels) than the basic onboard
sound from most computers.

There are many use-cases beyond what the general user needs. These use-cases
need professional gear (professional hardware), and also proper
professional-grade software. Here a few examples:

* A podcast host doing interviews with two (or more) microphones, one for the
  host and another for the guest. The audio must be simultaneously recorded in
  separate tracks for later editing.
* A band with multiple instruments. The guitar is connected to a distortion
  pedal that is connected to line in. The drums and the vocals are recorded
  from different microphones. The keyboard synthesizer can simultaneously
  generate analog audio and MIDI events, and both can be recorded
  simultaneously.
* A USB MIDI keyboard can be connected to the computer, which is then connected
  to a non-USB MIDI synthesizer, which is then connected back to the computer
  to record the synthesized audio.
* A MIDI controller providing many knobs and sliders is connected to the
  computer, and is able to control several volume levels and effects.

For these use-cases, PulseAudio is not enough. We need something else.

<!--

There are many different kinds of audio gear. Some of them analog (using 3.5mm
or 6.35mm or RCA jack or XLR cable), some of them digital (using MIDI DIN
connector). Some sound cards are plugged directly to the motherboards, some
sound cards are part of the on-board chipset, some sound devices are connected
over USB (and even some over Bluetooth, usually with lower quality). Some
analog cables transfer a single channel (mono audio), some cables transfer two
channels (stereo audio).

-->

## JACK

[JACK][] is a sound server written for professional audio. It aims to provide
low-latency audio and a way to freely interconnect applications.

When working with audio, latency must be kept as low as possible. You can't
work efficiently with audio if everything is delayed. [You can't even talk
properly if you are hearing your own voice with a delay][sanduiche]. As more
layers are added between the audio generation and the audio playback, it
becomes more difficult to achieve low latency. Thus, it's important to consider
latency when designing a sound server aimed at professional audio.

How about interconnecting applications? That's an unique feature of JACK.

With JACK, you have a list of audio sinks (things that consume audio) and a
list of audio sources (things that produce audio), and you have the ability to
interconnect them according to your needs. Let's look at some examples:

* You can connect your microphone (source) to an audio recorder application
  (sink), to record the audio straight from the microphone. (This is such a
  simple case that can be achieved on any sound server.)
* You can connect your microphone to an application that equalizes or distorts
  the audio. The processed audio is then connected to a recorder.
* You can have a mixing app that consumes from multiple sources, provides an UI
  to mix them together with varying effects, and outputs as another source to
  be consumed by other application. (Or to be played by the speakers.)
* You can have a [DAW][] application that records audio simultaneously from
  multiple devices. Each device is recorded to a different track, and each
  track can have its own equalization settings.

If you imagine each application as a little box with one or more input and
output connectors, and you have a bunch of audio cables with jack plugs at each
end, then you can understand the JACK sound server as a [patchbay][] that
allows you to freely connect those boxes and freely rewire them from a single
location.

Even though you can use each application settings screen to try to connect each
sink/source, this is usually cumbersome, as each application has a different
interface. In fact, some applications don't even try to provide such interface.
Thus, it's better to use a nice tool like [qjackctl][] to re-route all the
audio at one single interface. Do you want to connect one application to
another? Just click and drag in that tool and they're now connected.

And there is more! JACK also allows interconnection of MIDI applications. Thus,
you can have a virtual MIDI keyboard (that generates MIDI events) connected to
a software synthesizer (that generates audio based on MIDI events). And, of
course, connect hardware MIDI inputs and outputs to applications.

Although JACK is a great solution for professional audio users, it requires a
non-trivial amount of setup. Out-of-the-box it only supports applications
written for the JACK API, and even then it usually requires the user to connect
the application to the appropriate sources and sinks. It is possible to make
[JACK interact with applications written for
ALSA](https://jackaudio.org/faq/routing_alsa.html), but that requires
additional setup. [Running JACK alongside
PulseAudio](https://jackaudio.org/faq/pulseaudio_and_jack.html) is not easy,
and many times not possible. 

While JACK became the de facto standard for professional Linux audio, it never
became mainstream, general users don't benefit from it, and the most popular
distros never had JACK installed by default.

## PipeWire

For many years, JACK and PulseAudio were the de facto standards for sound
servers in Linux, but each one aiming to a different kind of user.

Then, after years in development, PipeWire started being shipped as the default
sound server in Linux distributions from 2021 onwards. We are near the end of
2023, [PipeWire version 1.0 is still a release
candidate](https://gitlab.freedesktop.org/pipewire/pipewire/-/releases/0.3.84),
but more and more distros are replacing PulseAudio with PipeWire.

But why PipeWire? What makes it different than the other sound servers? Well,
maybe the answer isn't in the differences, but in the similarities.

PipeWire is a sound server that is compatible with PulseAudio clients. All
those applications written to work with PulseAudio (e.g. that mixer control
panel in your favorite desktop environment) will continue working just fine
with PipeWire. Just like what had happened during the PulseAudio adoption, the
backwards-compatibility layers of PipeWire are making the transition very
smooth. The general end-user doesn't care which sound server is running (and
doesn't even care about the existence of a sound server), and hopefully those
users aren't even noticing the difference.

However, PipeWire isn't just a replacement for PulseAudio. It's also a
replacement for JACK. PipeWire provides APIs compatible with JACK, so JACK
applications can continue working just fine. What's more, PipeWire allows
connecting JACK and non-JACK applications together! There is no longer a split
between the applications, now both professional applications and normal
applications can be used together.

Just like JACK, PipeWire also includes MIDI routing support.

However, unlike any of the other pieces of software mentioned here, PipeWire
aims to also support video streams. This would allow, for the first time, to
easily route video streams between applications. Unfortunately, very few
applications support it as of today. Still, that's an amazing objective.

The older [qjackctl][] tool was used as the basis for the new [qpwgraph][], a
simple tool for managing the PipeWire graph of connections.


## PipeWire examples

Let's look at some examples. These are screenshots of [qpwgraph][] 0.5.3 on
Manjaro Linux, which is running PipeWire 0.3.81. These examples can be
replicated on any modern Linux distro running PipeWire, even on [Valve's Steam
Deck](https://www.steamdeck.com/). You may need to [install
qpwgrpah](https://pkgs.org/search/?q=qpwgraph), which is easy to do (and
[it's even available on Flathub](https://flathub.org/apps/org.rncbc.qpwgraph)).

If for some reason you don't want to use or you can't use qpwgraph, you can try
using [Helvum](https://gitlab.freedesktop.org/pipewire/helvum) or even the
command-line tool [pw-link](https://docs.pipewire.org/page_man_pw_link_1.html).
But personally I find qpwgraph the simplest, the most intuitive, and the most
powerful of those.

Let's start with a simple example. Just like most sound servers, PipeWire can
easily mix multiple audio streams onto a single audio sink (in this case, the
headphones). This is the most basic use-case, something all users expect in any
modern system.

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-3-apps-playing.png"><img src="{{ site.baseurl }}/blog/images/pipewire-3-apps-playing.png" alt="qpwgraph showing three applications (Firefox, VLC, Kwave) playing audio simultaneously into the headphones."></a>
</figure>

Likewise, PipeWire allows the microphone to be used simultaneously by multiple
recording applications. In this case, I'm recording some audio using [Kwave][]
while also viewing a real-time spectrogram of the audio using [Friture][].

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-kwave-friture.png"><img src="{{ site.baseurl }}/blog/images/pipewire-kwave-friture.png" alt="qpwgraph showing two applications (KWave and Friture) capturing audio from a single microphone source."></a>
</figure>

If you want, you can route one application to play on the left channel, and the
other application to play on the right channel. For instance, in this case I'm
playing a recording from [Kwave][] on my left ear while listening to [VLC][] on
my right ear. Why would you want that? Maybe you have two similar audio files
and you want to simultaneously listen to both, trying to pick up their
differences.

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-kwave-left-vlc-right.png"><img src="{{ site.baseurl }}/blog/images/pipewire-kwave-left-vlc-right.png" alt="qpwgraph showing two applications (Kwave and VLC), one playing on the left ear while the other plays on the right ear."></a>
</figure>

And you can also do that with the microphone. You can easily listen to your own
microphone by connecting it directly to your headphones. In this case, I'm
mixing the stereo [Kwave][] output to be played as mono on my left ear, while
listening to the microphone on my right ear. But I could instead have mixed the
stereo microphone input with the stereo application output, just like the first
example. Unlike the dedicated headphone jack on professional microphones, this
isn't zero-latency; but it is trivial to setup and is as low latency as you can
get. (You can probably fine-tune some PipeWire parameters to achieve lower
latency, but doing so is left as an exercise to the reader.)

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-kwave-left-mic-right.png"><img src="{{ site.baseurl }}/blog/images/pipewire-kwave-left-mic-right.png" alt="qpwgraph showing one application (Kwave) playing on the left ear while the microphone audio is being fed to the right ear."></a>
</figure>

If you have a fine microphone and a good set of amplified speakers, you can
just connect the two together for a trivial way to amplify your voice. Just
watch out for [audio feedback](https://en.wikipedia.org/wiki/Audio_feedback).

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-mic-to-hdmi.png"><img src="{{ site.baseurl }}/blog/images/pipewire-mic-to-hdmi.png" alt="qpwgraph showing a USB microphone being connected directly to the HDMI output."></a>
</figure>

How about playing with a MIDI synthesizer? [amsynth][] is an application that
produces sound (i.e. a synthesizer) based on the received MIDI events. If you
have a MIDI keyboard, you can connect it to the application. If you don't have
one, you can use another application as the keyboard, such as [VMPK][].

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-midi-amsynth.png"><img src="{{ site.baseurl }}/blog/images/pipewire-midi-amsynth.png" alt="qpwgraph with amsynth playing synthesized audio to the headphones. It's using JACK to receive MIDI events from VMPK."></a>
</figure>

PipeWire supports MIDI routing for JACK clients (shown as red color), and also
MIDI routing for any application trying to use ALSA (shwon as purple color).
Either way can be freely re-routed (among ports of the same type), and they
both work fine.

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-alsa-midi-amsynth.png"><img src="{{ site.baseurl }}/blog/images/pipewire-alsa-midi-amsynth.png" alt="qpwgraph with amsynth playing synthesized audio to the headphones. It's using ALSA to receive MIDI events from VMPK."></a>
</figure>

Finally, we have here a slightly more complicated example. We have both
[VMPK][] and [Mamba][] as virtual MIDI keyboards. The [amsynth][] synthesizer
is receiving MIDI events from one of the virtual keyboards and playing audio to
the headphones. Its audio is also being monitored through
[x42-spectr](https://x42-plugins.com/x42/x42-spectra) spectrogram. Meanwhile,
the other MIDI keyboard is sending MIDI events to the [ZynAddSubFX][]
synthesizer, together with the
[x42-stepseq](https://x42-plugins.com/x42/x42-stepseq-8x8) sequencer. The audio
output of that synthesizer is being filtered through [an
equalizer](https://x42-plugins.com/x42/x42-eq) before being mixed onto the
headphones.

<figure class="singleimage">
<a href="{{ site.baseurl }}/blog/images/pipewire-a-lot-of-stuff.png"><img src="{{ site.baseurl }}/blog/images/pipewire-a-lot-of-stuff.png" alt=""></a>
</figure>

PipeWire isn't perfect. For sure there are bugs. For sure the latency can be
reduced with enough tinkering and fine-tuning (and even changing some Linux
kernel configuration). Although video routing is one of the project objectives,
I personally couldn't make it work. (Truth to be told, video is a whole
different beast when compared to audio.)

Still, the amount of possibilities unlocked by PipeWire (together with a tool
like qpwgraph) is amazing. And all of that available on consumer hardware.

Do you want some more ideas?

* You can play some music during a video call, and route that music to the
  video call application so the other participants can hear it. Or, rather,
  route it exclusively to your headphones.
* You can apply some live filters to your microphone during a video call.
* You can play a kids show on a window at the corner of your screen, with its
  audio going to the speakers, while you listen to your choice of music at your
  headphones.
* You can configure network audio (again, left as an exercise to the reader),
  so that you can have the microphone of one device in one room, while the
  speakers are in another room. In other words, a very hacky [baby
  monitor](https://en.wikipedia.org/wiki/Baby_monitor).

## Conclusion

This article is supposed to be an overview of the history of audio on Linux,
helping to understand how we reached to PipeWire and why it is awesome. I'm
overlooking many of the details, and I may have made a few mistakes. (Feel free
to contact me with corrections in such case.)

I hope this article can be used as an introduction for people who never knew
the intricacies of (Linux) audio. I hope it is also inspiring for all the
multimedia possibilities now available on PipeWire, most of those were formerly
only available to people who went through the trouble of obscure settings and
hours of trial-and-error.

Now, stop just playing audio and go have fun playing with audio!


[ALSA]: https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture
[amsynth]: https://amsynth.github.io/
[aRts]: https://en.wikipedia.org/wiki/ARts
[balanced audio]: https://en.wikipedia.org/wiki/Balanced_audio
[BeOS]: https://en.wikipedia.org/wiki/BeOS
[daemon]: https://en.wikipedia.org/wiki/Daemon_(computing)
[DAW]: https://en.wikipedia.org/wiki/Digital_audio_workstation
[ESD]: https://en.wikipedia.org/wiki/Enlightened_Sound_Daemon
[Friture]: https://friture.org/
[JACK]: https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit
[Kwave]: https://apps.kde.org/kwave/
[line out]: https://en.wikipedia.org/wiki/Line_level#Line_out
[Mamba]: https://github.com/brummer10/Mamba
[MIDI]: https://en.wikipedia.org/wiki/MIDI
[OSS]: https://en.wikipedia.org/wiki/Open_Sound_System
[patchbay]: https://en.wikipedia.org/wiki/Patchbay
[phantom power]: https://en.wikipedia.org/wiki/Phantom_power
[PipeWire]: https://en.wikipedia.org/wiki/PipeWire
[PulseAudio]: https://en.wikipedia.org/wiki/PulseAudio
[qjackctl]: https://qjackctl.sourceforge.io/qjackctl-screenshots.html
[qpwgraph]: https://gitlab.freedesktop.org/rncbc/qpwgraph
[repo]: https://gitlab.freedesktop.org/pipewire/pipewire
[sanduiche]: https://youtu.be/pmn-dbBpglU?t=45
[sound server]: https://en.wikipedia.org/wiki/Sound_server
[VLC]: https://www.videolan.org/
[VMPK]: https://vmpk.sourceforge.io/
[XLR]: https://en.wikipedia.org/wiki/XLR_connector
[ZynAddSubFX]: https://zynaddsubfx.sourceforge.io/
