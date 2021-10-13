---
layout: post
title: Getting rid of Disqus
lang: en
tags: []
---

I'm removing [Disqus][] from my website. Why? Well, keep reading…


## History

[I started blogging in 2005][first] ([Wayback Machine][firstarc]). I wrote posts about my experience with [Gentoo Linux][gentoo], and posts about whatever subject I wanted to write and I wanted to share. Back then, I either had a [56K dial-up modem][modem] or had just upgraded to [256kbps ADSL][adsl]. Facebook wasn't popular yet, laptops weren't popular yet, modern touch-screen smartphones didn't exist yet, and neither did sites like Twitter and Stack Overflow. Back then, blogs and forums were the most common way that users would share stuff.

At that time, I was using the [Opera browser][opera], and it was good. It had its own rendering engine, it was lightweight, it was powerful. The company behind the browser had also launched [My Opera][], a community-focused website that provided forums and blogs and photo albums. Essentially, that was a social website. I started my own blog in there. And I kept going on that platform ([Wayback Machine][blogarc]) until they decided to shut it down in 2014 ([Wayback Machine][shutdown]).

Some time later, I moved my blog to my own domain, hosted on [GitHub Pages][ghpages] and powered by the static website generator [Jekyll][]. It was a new paradigm for me, but also a very compelling one: I can have full control of the pages, I can easily write posts in [Markdown][] instead of HTML, I can have the full history of changes in [the git repository][git], and I have the freedom to host the website anywhere (since it is made of just static files, it is extremely easy to host).

But if the website is static, how can people leave comments? Well, the short answer is: they can't. Since there is no server-side processing, there is no way to handle comments. Unless… well, unless I use a third-party service to include comments on each page. And that's precisely what [Disqus][] does. The website author includes the Disqus script into the page, and that service will take care of comments. Sounds like a good idea.

## Reality

In practice, however, Disqus is not as useful. Back in My Opera days, somehow people discovered my blog organically, probably through My Opera itself. I used to receive a few comments on almost every post, and some of them were very relevant to the content. Now, with my own domain, I don't have any free publicity. People rarely discover my blog (and I'm neither posting as often, nor promoting it myself), and even fewer people comment.

In fact, in the past year(s), I received exactly one comment on my blog.

The lack of comments isn't enough reason to remove Disqus. But I really expected to receive some notification whenever I got any comment. But I didn't. And it seems Disqus doesn't have this feature.

Let me say it again: I, as the site owner, can put Disqus system on my pages, but I cannot automatically receive notifications about new comments. There is no such feature. And, given the lack of activity on my blog, I need to receive notifications, otherwise I won't know about it.

Even the Disqus admin dashboard is confusing and lacking. I couldn't see the list of recent comments on my site. Even after several minutes searching through the Disqus admin interface, I still couldn't find the comments. I only know about that single comment because the author also contacted me through another service.

## Future

So, there is no reason to keep that third-party service on my website, given the extremely low usage, and given it simply doesn't have the features I expect.

Plus, given the [recent European Union rules regarding cookies and privacy][cookies], it's a good idea to get rid of this service that tracks users across websites. (Sidenote: I still keep the analytics system on the website, although I almost never look at it. So… There is still room for improvement. I may end up replacing it with [GoatCounter][goat] in the future.)

So, that's why, starting today, I'm getting rid of Disqus from my website. Goodbye! It won't be missed!


[Disqus]: https://en.wikipedia.org/wiki/Disqus
[gentoo]: https://www.gentoo.org/
[My Opera]: https://en.wikipedia.org/wiki/My_Opera
[shutdown]: https://web.archive.org/web/20131031211626/http://my.opera.com/chooseopera/blog/2013/10/31/important-announcement-about-your-my-opera-account
[opera]: https://en.wikipedia.org/wiki/Opera_(web_browser)
[modem]: https://en.wikipedia.org/wiki/Dial-up_Internet_access
[adsl]: https://en.wikipedia.org/wiki/Asymmetric_digital_subscriber_line
[firstarc]: https://web.archive.org/web/20070309144911/http://my.opera.com/CrazyTerabyte/blog/show.dml/51899
[first]: {% post_url 2005-10-27-gentoo-install-part-1 %}
[blogarc]: https://web.archive.org/web/20140210064853/http://my.opera.com/CrazyTerabyte/blog/
[ghpages]: https://en.wikipedia.org/wiki/GitHub_Pages
[jekyll]: https://en.wikipedia.org/wiki/Jekyll_(software)
[markdown]: https://en.wikipedia.org/wiki/Markdown
[git]: https://github.com/denilsonsa/denilsonsa.github.io
[cookies]: https://en.wikipedia.org/wiki/HTTP_cookie#EU_cookie_directive
[goat]: https://www.goatcounter.com/
