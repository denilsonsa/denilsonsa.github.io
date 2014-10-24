---
layout: post
title: First contact with ATmega8 microcontroller - correction
lang: en
tags:
- AVR
- ATmega8
- Microcontroller
- Hardware
---

At [part 2][] of this series of posts, **I've posted the wrong pinout for 6-pin ISP connector**.


Thanks goes to Stig Hornang, who e-mailed me a few days ago. He said he spent two hours until he figured out it was wrong. Sorry about your time, Stig, but thank you very much for pointing it out!

I copied the wrong pinout from [a PDF](http://eds.dyndns.org:81/~ircjunk/avr/programmer/avrprog.pdf) ([local mirror]({{ site.url }}/blog/images/avr/avrprog.pdf)) [that I found at some personal homepage](http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html) ([Wayback Machine](http://web.archive.org/web/20071229042911/http://eds.dyndns.org:81/~ircjunk/avr/avrstarter/avrstarter.html)). I should have copied it from official documents from [Atmel](http://www.atmel.com/), like the [AVR ISP In-System Programmer](http://www.atmel.com/dyn/Products/tools_card.asp?tool_id=2726) ([Wayback Machine](http://web.archive.org/web/20081203011048/http://www.atmel.com/dyn/Products/tools_card.asp?tool_id=2726)) [Schematics](http://www.atmel.com/dyn/resources/prod_documents/Avrisp_Sch.pdf) or the [User Guide](http://www.atmel.com/dyn/resources/prod_documents/AVRISP.chm) ([PDF version](http://www.equinox-tech.com/downloads/atmel/avr%20tools/avrisp/AVRISP_User_Guide.pdf)), or even the [AVRISP mkII In-System Programmer](http://www.atmel.com/tools/AVRISPMKII.aspx) [User Guide](http://www.atmel.no/webdoc/avrispmkii/avrispmkii.section.zgf_vsd_lc.html). What's more, even [this page](http://elm-chan.org/works/avrx/report_e.html) has the correct pinout.

Here is the fixed version:

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/avr/AVR-ISP-connectors-whatwaswrong.png" alt="Diagram for AVR ISP 6-pin and 10-pin connectors, highlighting my mistakes and the correct pinout.">
<figcaption>
(<a href="{{ site.url }}/blog/images/avr/AVR-ISP-connectors-whatwaswrong-hi.png">PNG version</a>,
<a href="{{ site.url }}/blog/images/avr/AVR-ISP-connectors-whatwaswrong.svg">SVG version</a>)
</figcaption>
</figure>

I've already updated the previous posts with the correct pinout.

Sorry for this mistake, and thank you all for making this series of posts so successful.

{% include first-contact-with-atmega8-navigation.html %}

[part 2]: {% post_url 2007-10-26-first-contact-with-atmega8-microcontroller-part-2 %}
