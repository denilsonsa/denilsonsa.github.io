---
layout: post
title: Sample styling
lang: en
tags:
- Linux
- Rio de Janeiro
- X.org
- Nvidia
- fun
- Open Source
---

This is a sample page with all available elements, with many of them combined. This page is helpful while testing CSS.


# Headers

It is worth noting that setting an ID (using `{#header_id}` syntax) is only available in `kramdown`, and it is not available in `redcarpet`.

# Header 1 {#header1}

## Header 2 {#header2}

### Header 3 {#header3}

#### Header 4 {#header4}

##### Header 5 {#header5}

###### Header 6 {#header6}


# Inline and block styling

Text with *asterisk* **two asterisks** _underline_ __two underlines__ ~tilde~ ~~two tildes~~ middle_under_line `backtick` ``two backticks``.

Characters such as 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" two dashes -- three dashes --- three dots ... two--three---dashes three...dots.

Links such as http://example.com/ <http://example.com> [example] or [example][] denilsonsa@gmail.com <denilsonsa@gmail.com>


> Text with *asterisk* **two asterisks** _underline_ __two underlines__ ~tilde~ ~~two tildes~~ middle_under_line `backtick` ``two backticks``.

> Characters such as 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" two dashes -- three dashes --- three dots ... two--three---dashes three...dots.

> Links such as http://example.com/ <http://example.com> [example] [example][] denilsonsa@gmail.com <denilsonsa@gmail.com>


    Text with *asterisk* **two asterisks** _underline_ __two underlines__ ~tilde~ ~~two tildes~~ middle_under_line `backtick` ``two backticks``.

    Characters such as 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" two dashes -- three dashes --- three dots ... two--three---dashes three...dots.

    Links such as http://example.com/ <http://example.com> [example] [example][] denilsonsa@gmail.com <denilsonsa@gmail.com>


* Text with *asterisk* **two asterisks** _underline_ __two underlines__ ~tilde~ ~~two tildes~~ middle_under_line `backtick` ``two backticks``.

* Characters such as 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" two dashes -- three dashes --- three dots ... two--three---dashes three...dots.

* Links such as http://example.com/ <http://example.com> [example] or [example][] denilsonsa@gmail.com <denilsonsa@gmail.com>


1. Text with *asterisk* **two asterisks** _underline_ __two underlines__ ~tilde~ ~~two tildes~~ middle_under_line `backtick` ``two backticks``.

1. Characters such as 'quotes' ''two quotes'' "double-quotes" ""two double-quotes"" two dashes -- three dashes --- three dots ... two--three---dashes three...dots.

1. Links such as http://example.com/ <http://example.com> [example] or [example][] denilsonsa@gmail.com <denilsonsa@gmail.com>


# Blocks and inter-block margin

Paragragh

> Blockquote

Paragragh

> Blockquote

<!-- -->

> Blockquote

    Preformatted

Paragragh

    Preformatted

<!-- -->

    Preformatted

> Blockquote


# Lists

* No blank lines.
* No blank lines.
* No blank lines.

* With blank lines.

* With blank lines.

* With blank lines.

* Multiple paragraphs

    Multiple paragraphs (requires 4-spaces)

    Multiple paragraphs (requires 4-spaces)

* List 1
    * List 2
        * List 3
            * List 4
                * List 5
                    * List 6
                        * List 7
* List 1

1. List 1
    1. List 2
        1. List 3
            1. List 4
                1. List 5
                    1. List 6
                        1. List 7

1. List 1
    * List 2
        1. List 3
            * List 4
                1. List 5


# Blocks next to headers and lists

Paragragh

* List

Paragragh

* List

## Header 2

* List

> Blockquote

* List

    Preformatted

* List

## Header 2

> Blockquote

## Header 2

    Preformatted

## Header 2


# Nesting blocks and lists

> Blockquote 1

>> Blockquote 2

>>> Blockquote 3

>>>> Blockquote 4

>>>>> Blockquote 5

>>>>>> Blockquote 6

* List 1

    > Blockquote inside list 1

* List 1

        Preformatted inside list 1

* List 1
    1. List 2

        > Blockquote inside list 2
    1. List 2 (if there is a blank line before this line, it will become Preformatted instead)
* List 1
    1. List 2

            Preformatted inside list 2
    1. List 2 (if there is a blank line before this line, it will become Preformatted instead)
* List 1

> Blockquote 1

>     Preformatted inside Blockquote requires 5 spaces
>     ("> " because of Blockquote, and 4 spaces for Preformatted)


# Horizontal rules

Paragragh

***

___

---

Paragragh


# Tables

| Tables   | Are           | Cool  |
| -------- |:-------------:| -----:|
| col 3 is | right-aligned | $1600 |
| col 2 is | centered      |   $12 |
| col 1 is | left-aligned  |    $1 |


# Liquid tags in preformatted text

Without escaping:

    {% if true %} {{ page.title }} {% endif %}

```
{% if true %} {{ page.title }} {% endif %}
```

{% highlight liquid %}
{% if true %} {{ page.title }} {% endif %}
{% endhighlight %}

Using `{{"{% raw "}}%}`:

    {% raw %}
    {% if true %} {{ page.title }} {% endif %}
    {% endraw %}

{% raw %}
{% if true %} {{ page.title }} {% endif %}
{% endraw %}

```
{% raw %}
{% if true %} {{ page.title }} {% endif %}
{% endraw %}
```

{% highlight liquid %}
{% raw %}
{% if true %} {{ page.title }} {% endif %}
{% endraw %}
{% endhighlight %}

Using lots of curly braces:

    {{"{% if true "}}%} {{"{{ page.title "}}}} {{"{% endif "}}%}

```
{{"{% if true "}}%} {{"{{ page.title "}}}} {{"{% endif "}}%}
```

{% highlight liquid %}
{{"{% if true "}}%} {{"{{ page.title "}}}} {{"{% endif "}}%}
{% endhighlight %}

See also: http://tesoriere.com/2010/08/25/liquid-code-in-a-liquid-template-with-jekyll/

# Syntax highlighting

```python
import this  # Using ```python
f = lambda x: str(x)
print(','.join(f(i) for i in range(10)))
```

{% highlight python %}
import this  # Using highlight python
f = lambda x: str(x)
print(','.join(f(i) for i in range(10)))
{% endhighlight %}


```cpp
# include <iostream>
int main(int argc, char *argv[]) {
    std::cout << "Using ```cpp" << std::endl;
    return 0;
}
```

{% highlight cpp %}
# include <iostream>
int main(int argc, char *argv[]) {
    std::cout << "Using highlight cpp" << std::endl;
    return 0;
}
{% endhighlight %}


```c++
# include <iostream>
int main(int argc, char *argv[]) {
    std::cout << "Using ```c++" << std::endl;
    return 0;
}
```

{% highlight c++ %}
# include <iostream>
int main(int argc, char *argv[]) {
    std::cout << "Using highlight c++" << std::endl;
    return 0;
}
{% endhighlight %}


```c
#include <stdio.h>
int main(int argc, char *argv[]) {
    puts("Using ```c");
    return 0;
}
```

{% highlight c %}
#include <stdio.h>
int main(int argc, char *argv[]) {
    puts("Using highlight c");
    return 0;
}
{% endhighlight %}


# Pictures

Lorem ipsum dolor sit amet. Ipsum. Aenean laoreet posuere orci. Etiam id nisl.
Suspendisse volutpat elit molestie orci. Suspendisse vel augue at felis
tincidunt sollicitudin.

<figure class="floatright">
<img src="{{ site.url }}/blog/images/k750i_main_menu.jpg" alt="">
<figcaption>
Figure caption here.
</figcaption>
</figure>

Sit amet ante. Mauris ac nibh eget risus volutpat tempor. Praesent volutpat
sollicitudin dui. Sed in tellus id urna viverra commodo. Vestibulum enim felis,
interdum non, sollicitudin in, posuere a, sem. Cras nibh.

<figure class="floatright">
<img src="{{ site.url }}/blog/images/hard_drive_adapter_screws.jpg" alt="">
</figure>

Vestibulum ac lacus. Vivamus porttitor, massa ut hendrerit bibendum, metus
augue aliquet turpis, vitae pellentesque velit est vitae metus. Duis eros enim,
fermentum at, sagittis id, lacinia eget, tellus. Nunc consequat pede et nulla.
Donec nibh. Pellentesque cursus orci vitae urna. Cum sociis natoque penatibus
et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque risus
turpis, aliquet ac, accumsan vel, iaculis eget, enim. Pellentesque nibh neque,
malesuada id, tempor vel, aliquet ut, eros. In hac habitasse platea dictumst.
Integer neque purus, congue sed, mattis sed, vulputate ac, pede. Donec
vestibulum purus non tortor. Integer at nunc.

<figure class="singleimage">
<img src="{{ site.url }}/blog/images/hard_drive_adapter_screws.jpg" alt="">
<figcaption>
Figure caption here. Maecenas sed nibh non lacus tempor faucibus. In hac
habitasse platea dictumst.
</figcaption>
</figure>

Etiam facilisis. Nam suscipit. Ut consectetuer leo vehicula augue. Aliquam
cursus. Integer pharetra rhoncus massa. Cras et ligula vel quam tristique
commodo. Sed est lectus, mollis quis, lacinia id, sollicitudin nec, eros.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
cubilia Curae; Morbi urna dui, fermentum quis, feugiat imperdiet, imperdiet id.


<!-- Comments in Markdown: https://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax -->

[example]: http://example.com/ "Example link"
[//]: # ( vi:et:sw=4:ts=4 )
