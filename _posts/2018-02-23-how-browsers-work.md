---
layout: post
title: How browsers work
lang: en
tags: []
---

This is a very concise introduction to how browsers work, aimed to let people understand what is a web browser, what are the main technologies involved in the browser, and how it all fits together.


It was originally written by me (Denilson Sá Maia) in February 2018, with some help from [Alex Badarin](https://github.com/lyzzard). It was supposed to be turned into a talk/training for new (full-stack) developers at Booking.com, but we never went forward with the training. That also explains why this text is written in a format full of bullet points with very succinct descriptions: it was supposed to be converted into slides accompanied by a instructor explaining all the details and doing live demos.

Still, I believe this overview can be useful for people just starting on web development, or people who are just curious to how things work behind the scenes.

## Chapter 1: Introduction

### What is a browser?

* HTML viewer
    * (and CSS, and DOM)
* Image viewer
    * PNG, JPEG, GIF, SVG, WebP…
    * (and multimedia viewer: audio and video)
* JavaScript interpreter
* (implements) HTTP protocol
    * (and HTTPS)
    * (and FTP, and …)

### What is a browser? (part 2)

* An application that implements several specifications
    * HTTP, HTTPS, FTP
    * HTML, CSS, DOM
    * JavaScript (ECMAScript)
    * PNG, JPEG, GIF, SVG, WebP…

### But why? What is the purpose of a browser?

* Fetch and display documents
* But…
    * How to fetch documents?
    * How to display them?

## Chapter 2: HTTP protocol

### What is HTTP?

* Hypertext Transfer Protocol
* It's how browsers fetch documents (and resources)
* It's built on top of TCP

### What is TCP?

* Transmission Control Protocol
* Bi-directional socket between a client and a server
    * Whatever is written in one side of the socket gets transmitted to the other side
* It's built on top of IP

### What is TCP? (part 2)

* IP `:` port
    * IP (Internet Protocol) is the way to address a machine on the Internet
    * Port is the way to address a certain service (application) on the machine
    * The server listens to an IP address and to a port
    * The client connects to that IP address and to that port
* IP addresses look like this:
    * 5.57.16.220 (IPv4)
    * 2a00:1450:400e:807::200e (IPv6)
* Some port numbers are standard
    * 80 for HTTP
    * 443 for HTTPS
* [idea: live `netcat` demo]
* But how to find the IP address of a host?

### How to resolve names?

* DNS
    * Domain Name Server
* Resolves hostnames (i.e. domain names) to IP addresses
* [idea: output of `dig booking.com` or `dig AAAA google.com` or `nslookup booking.com`]

### Recap

* We now know how to find the IP of a server
    * DNS
* We now know how to connect to a server
    * TCP (or TCP/IP)
* But how do we "talk" to the server?
    * HTTP

### HTTP is simple

* Client sends:
    * `GET /example.html HTTP/1.1`
    * `Host: www.example.com`
* Server responds:
    * `HTTP/1.1 200 OK`
    * (empty line)
    * `<html> … </html>`
* [idea: live `netcat` or `telnet` demo]
    * Can be `netcat` as both client and as server

### HTTP is extensible

* Request headers
    * `Accept-Language:`
    * `Accept:`
        * json, html, text
    * …
* Response headers
    * `Content-Length:`
    * `Content-Type:`
    * …

### HTTP is stateless

* Cookies can hold state
* Cookies are small
    * A random identifier is stored in the cookie, but the user data is kept on a server database
* Cookies are sent as `Cookie:` header on all requests to the same domain
* Cookies can be set by `Set-Cookie:` header on responses

### HTTP methods (verbs)

* GET
    * Most common, used to load most resources, should not cause side-effects
* POST
    * Usually for user-submitted forms
* HEAD
* PUT
* DELETE

### HTTP status codes

* 2xx
    * When things go well
    * 200 OK
* 3xx
    * Redirections: server tells the client to look elsewhere
    * 301 Moved Permanently
    * 302 Found (Moved Temporarily)
* 4xx
    * Client errors
    * 400 Bad Request
    * 404 Not Found
* 5xx
    * Server errors
    * 500 Internal Server Error

### How about HTTPS?

* Adds encryption layer to HTTP
* Behaves just like HTTP

### Recap

* We know now how to communicate with the server using HTTP
* Now we need to display the content to the user

## Chapter 3: HTML

### HTML

* It is a way to describe a document
    * structured document
        * as a tree

### HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My page</title>
  </head>
  <body>
    <p>Hello! Do you like <em>animals</em>?</p>
    <ul>
      <li>cats</li>
      <li>dogs</li>
      <li>bunnies</li>
    </ul>
  </body>
</html>
```

* html
    * head
        * meta
        * title
            * "My page"
    * body
        * p
            * "Hello! Do you like"
            * em
                * "animals"
            * "?"
        * ul
            * li
                * "cats"
            * li
                * "dogs"
            * li
                * "bunnies"

Observe how some nodes are element nodes, and others are text nodes. (And there are a few other node types as well.)

[note: Mention here: "please please please always use a proper `DOCTYPE` to avoid nasty bugs later on"]

### Do you like acronyms?

* HTML
    * SGML
    * XML
    * XHTML
* CSS
* DOM

HTML syntax was designed alongside SGML, was supposed to be compatible with SGML, but it is slightly different. XML syntax is a simpler than SGML. XHTML was an HTML dialect using the stricter XML syntax, but no one uses it anymore.

### Too boring, I demand pictures!

```html
<li><img src="kitten.png" alt=""> cats</li>
```

* ul
    * li
        * img
        * "cats"

### How does the browser fetch the picture?

* Browser sends `GET /page` to `domain.com`
* Parses the returned HTML
* Sees `<img src="…">`
* Sends `GET /kitten.png` to `domain.com`

### Optimization details

* Reusing the same TCP connection
* Doing simultaneous parallel TCP connections
    * But there's a limit, so websites usually bundle together some resources into a single file
* HTTP/2 (SPDY)
    * [TODO: briefly explain in one sentence what's new]
* HTTP/3 (over QUIC)
* Still the same HTTP

### All external content creates new HTTP requests

* Media
    * Image
    * Audio
    * Video
* CSS
    * `<link rel="stylesheet" href="…">`
* JS
    * `<script src="…">`
* frames/iframes

### Recap

* Now we know:
    * How to communicate with a server
        * HTTP
    * How to markup text
        * HTML
    * How to include external content
        * Kitten pictures!
* What's next?
    * How to make it pretty!

## Chapter 4: CSS

### CSS

* Cascading Style Sheets
    * Wait, what?

### CSS

* A set of properties (and their default values)
    * e.g. `color`, `font-size`
    * All elements have all properties with some default values
* A set of rules that
    * Select a subset of elements
        * "Selector"
    * Set values to some properties
        * Declaration block

```css
selector {
  property: value;
}

selector1, selector2 {
  p1: v1;
  p2: v2;
}
```

### HTML elements have their own default values

* depends on the browser and user settings
* e.g. `h1` → `font-size`

### CSS example 1

```html
<p>Hello! Do you like <em>animals</em>?</p>
<ul>
  <li>a <em>cute</em> cat</li>
  <li>a dog</li>
</ul>
```

[note: show both the HTML source-code and the DOM tree and the CSS code; maybe show the result without CSS and then apply the CSS]

```css
li { color: blue; }
```

We should point out how the `<em>` inside `<li>` became blue — talk about inheritance: by default some properties are inherited (e.g. `color`), others aren't (e.g. `border`):

```css
li { color: inherit; } /* by default */

body { color: black; } /* by default */
```

### CSS example 2

```css
em { color: red; }
li { color: blue; }
```

* Point out that the `<em>` became red
* But `li` came later!
    * But it doesn't match the `em`

### Selectors

* How can we select elements?

* `tagName`
    * `a`
    * `em`
    * `body`
* `#id`
    * `#searchresults-count`
* `.className`
    * `.hotel-card`
* `[attr]`
    * `[required]` [note: pick a different example]
* `[attr="..."]`
    * `[type="checkbox"]`
* `[attr*="..."]`
    * ...
* `:pseudo-class`
    * `:hover`
    * `:focus`
    * `:first-child`
    * `:invalid`
    * `:nth-child(odd)` `:nth-child(even)`
* `*`

### Combining selectors (same element)

* They can also be combined:
    * `tag#id`
    * `tag.class`
    * `tag[attr]`
    * `tag:pseudo-class`
    * `tag#id.class[attr]:pseudo-class`
    * `tag:pseudo-class[attr].class#id`
        * The tagname (if present) must be the first one
        * Otherwise, the order does not matter
* [note: show them one by one, and explain the meaning of each one]

### Combining selectors (multiple elements)

* `A, B` (one or another)
* `A B` (descendant)
* `A > B` (child)
* `A + B` (next sibling)
* `A ~ B` (following sibling)
* [note: add real-world examples, and explain each one]
* <http://gallery.theopalgroup.com/selectoracle/>

### CSS example 3

```css
li em { color: yellow; }
em { color: red; }
li { color: blue; }
```

* Ask the audience: What should be the colors?

* Look at the first `<em>`: which rules match?
    * Only one
* Second `<em>`?
    * Two rules
        * How to resolve it? (specificity)

### Specificity

* `li em` is more specific than `em`
    * But why?
* Count how many `#id` selectors
    * if tied, count how many classes, pseudo-classes, attributes
        * if tied, count how many elements (and pseudo-elements) [Note: we should probably omit pseudo-elements from here, but leave a note in the written material]
            * if still tied, the later declaration wins
* As a special case, `style="…"` has the maximum possible specificity
* <https://specificity.keegan.st/>
* Reference:
    * <https://www.w3.org/TR/selectors/#specificity>
    * <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>

### CSS BEM / SASS / etc

(include examples of what problem they try to solve)

### Recap

* With CSS we can
    * write rules
    * that apply some values
    * to visual properties
    * to a subset of elements

### CSS box model

[Note: we need several examples in this and in the following sections]

[Need to make this interactive — consider live CSS editors.]

margin/border/padding/content

### CSS layout

* Normal flow
    * p
        * ul
            * li
            * li
            * li
* One after another vertically with full width
    * `display: block`

### CSS layout: inline

`<em>` example (`display: inline`)

Block elements have several anonymous inline boxes.

### CSS inline-block

Cannot be broken

Behaves like images or any replaced element (`img`, `object`, `iframe`, `input`, …).

### CSS removing from normal flow

* `float`
    * `left`
    * `right`
* `clear`
    * `left`
    * `right`
    * `both`
* `position`
    * `absolute`
    * `fixed`

### CSS display: flex

…

### DOCTYPE

* Please use `<!DOCTYPE html>`
    * AKA the HTML5 DOCTYPE
* Due to historical reasons of backwards compatibility, browsers render pages differently (replicating old browser bugs) if there is no DOCTYPE. This is called "quirks mode".

### Recap

* Now we know:
    * How to communicate with a server
        * HTTP
    * How to markup text
        * HTML
    * How to make it pretty
        * CSS
* What's next?
    * How to make it interactive!

## Chapter 5: forms and JavaScript

### Server-side interaction

* Forms can be used to send data to the server.
* Examples: [note: we need live examples/demos]
    * `<form method="GET">`
        * For a search box
    * `<form method="POST">`
        * For the comments section

### How to handle user logins?

* `<form method="POST"> <input type="text"> <input type="password">`
* The server checks the credentials.
    * If valid, server sets a cookie to a unique id.
* On all future requests:
    * The client sends the cookie
    * The server checks if the cookie id is valid

### More interaction?

* That's fine for simple interactions.
* That's fine for 1990s
* How to make the page MORE interactive?

### JavaScript

* Introduction to the language
* `"use strict";`
* What is jQuery
* AJAX is just another HTTP request
* DOM — glue between JS and the page

## Conclusion

### What have we learned?

* …

### How to debug?

* Look for "Developer tools" in any browser
    * <https://developer.chrome.com/devtools>
    * <https://developer.mozilla.org/en-US/docs/Tools/Tools_Toolbox>
    * <https://www.mozilla.org/en-US/firefox/developer/> (why? that's an honest question, I wish to learn why!)
    * <https://developer.apple.com/safari/tools/>
    * <https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide>
* [Note: maybe compile a list of shortcuts on how to open devtools on each browser on each system]

### How about mobile debugging?

* [TODO: explain how to do it]
    * built-in simulator in desktop browsers
    * remote debugging

### How to learn more?

* <https://developer.mozilla.org/>
* <https://html.spec.whatwg.org/multipage/>
* <https://caniuse.com/>
* <https://devdocs.io/>
* …

### Live-demo on production website

Open your favorite website in a browser and play with it in dev tools.
