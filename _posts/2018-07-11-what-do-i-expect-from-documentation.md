---
layout: post
title: What do I expect from documentation?
lang: en
tags: []
---

Based on my experience looking/installing/running/modifying open-source projects at my own computer, and my experience working on code at my employer, I came up with the following expectations for a README file for any project:


* **Project name**, obviously.
* **Project purpose**.
    * What is the problem it tries to solve?
    * Who should use this project?
    * Why would people use this project?
* **Project overview**.
    * What does this project do?
    * How does this project work?
    * What are the expected inputs and outputs?
    * If this project is part of a larger pipeline or a larger system, where does this project fit in the overall picture?
* **Setup instructions**.
    * How do I setup the project to get it up and running?
    * What are the dependencies of this project?
    * What are the assumptions about the environment this project is running?
    * If it is a web service or site, where can I view it? In production? In dev?
    * If it is a script, how should I run it? I hope it has built-in support for `--help`.
* **Code overview**.
    * **Where** is the code?
        * This is simpler on external/isolated projects, because everything inside the same repository belongs to the project, and everything outside doesn't.
        * Inside my employer repositories, this is not straightforward, and needs to be explained. What directories inside which repositories are relevant to this project?
    * **How is the code organized**?
        * What is the purpose of each directory or file?
        * Just an overview, so that I know what and where is the front-end code, the back-end code, the HTTP endpoints, the database modules, the configuration files...
    * How does the different pieces of **code interact**?
        * An brief overview of code interaction can help building a mental picture of the execution and data flows.
    * What are the relevant **databases and tables**?
    * What are the relevant **metrics and dashboards**?
    * Where to **find the documentation**?
        * The documentation should be close to the code. That way, the documentation is easy to find, and can be kept up-to-date together with the code. That's why a README file is a good solution.
        * If a project is spread over many directories, having a README on each one that points to the main documentation can be very helpful.
        * If the main documentation is somewhere else, there should be a README (or code comments) pointing to the main documentation.
        * Having comments on database tables and columns can also be very helpful.
* **Authors**.
    * **Who** created it?
    * How to contact them?
* **History**.
    * **When** was it created?
    * What were the **major changes**? (AKA change log, what's new, release notes...)
    * A brief history of the project can help understanding some legacy code and some technical decisions.

## Why all of this?

Imagine someone who never heard about your project finds either your project or some piece of code. Either by accident, or because they need to fix/maintain something. Or maybe the project changed ownership.

How would such person get to know what to do? What if that person is you?

## Too high expectations?

Not all answers have to be written, some can be implied.

I just want to be able to answer those questions after finding a project.

Some technical details can be understood by just reading the code... But that is only possible if the developer knows *what code* to read, and *where* it is.

But maybe my expectations are too high? Do you have a different opinion than me? I can compromise and settle to being able to answer the majority of those questions.

I think I should review the documentation of [my side projects](https://github.com/denilsonsa?tab=repositories), I'm pretty sure many of them are lacking enough answers. However, smaller projects are easier to understand; the bigger the project is, the more it needs good documentation.
