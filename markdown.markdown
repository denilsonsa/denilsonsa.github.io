---
layout: default
---

# Header 1 {#header1}

## Header 2 {#header2}

### Header 3 {#header3}

#### Header 4 {#header4}

##### Header 5 {#header5}

###### Header 6 {#header6}

Text with *asterisk* **two asterisks** 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" _underline_ __two underlines__ `backtick` ``two backticks`` ~tilde~ ~~two tildes~~ middle_under_line two -- three --- dots ... 1/2 1/4 3/4 http://example.com/ [example] <http://example.com> denilsonsa@gmail.com <denilsonsa@gmail.com>

> Blockquote text with *asterisk* **two asterisks** 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" _underline_ __two underlines__ `backtick` ``two backticks`` ~tilde~ ~~two tildes~~ middle_under_line two -- three --- dots ... 1/2 1/4 3/4 http://example.com/ [example] <http://example.com> denilsonsa@gmail.com <denilsonsa@gmail.com>

    Preformatted text with *asterisk* **two asterisks** 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" _underline_ __two underlines__ `backtick` ``two backticks`` ~tilde~ ~~two tildes~~ middle_under_line two -- three --- dots ... 1/2 1/4 3/4 http://example.com/ [example] <http://example.com> denilsonsa@gmail.com <denilsonsa@gmail.com>

* List
    * List
* List
    1. List
    # List

```python
import this
f = lambda x: str(x)
print(','.join(f(i) for i in range(10)))
```

{% highlight python %}
import this
f = lambda x: str(x)
print(','.join(f(i) for i in range(10)))
{% endhighlight %}

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

## Table of contents

* Foobar
{:toc}

---

***

___

## redcarpet

* Does not support `{#id}` syntax.
* Adds IDs to the headers.
* Converts two single quotes into a double-quote (but buggy).
* Converts quotes into angled quotes (buggy on consecutive quotes).
* Converts multiple hyphens into dashes.
* Two tildes `~~` to strike-through.
* Auto-links plain links and also supports `<` and `>`.
* Links support title text.
* Supports tables.
* Supports syntax highlighting.
* Does not support TOC.

## kramdown

* Supports `{#id}` syntax.
* Adds IDs to the headers.
* Keeps two single quotes separate.
* Converts quotes into angled quotes.
* Converts multiple hyphens into dashes.
* Does not support strike-through.
* Auto-linking requires `<` and `>`.
* Links support title text.
* Supports tables.
* Requires `coderay` gem for syntax highlighting.
    * But it embeds line numbers, making it impossible to correctly copy-paste the code.
    * But it hard-codes the colors.
* Supports TOC.
* [Always obfuscates e-mail links using HTML entities](https://github.com/gettalong/kramdown/blob/REL_1_10_0/lib/kramdown/converter/html.rb#L243).

[example]: http://example.com/ "Example link"
