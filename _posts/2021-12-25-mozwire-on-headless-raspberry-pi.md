---
layout: post
title: How to use MozWire on a headless Raspberry Pi
lang: en
tags: []
---

In this post, I'm sharing some notes on how to get [Mozilla VPN][] running on a headless Raspberry Pi. In fact, these instructions generate the necessary [WireGuard][] configuration files that can be used on any device, even those not supported by the [official Mozilla VPN GUI application][app].


## Introduction

Sometime in 2020, Mozilla launched their own VPN service on just six countries. On the following year, they expanded to more countries. Mozilla isn't running the infrastructure, but instead relying on [Mullvad VPN][], and using the [WireGuard][] protocol behind the user-friendly GUI application.

I wanted to give it a try. However, the Raspberry Pi 4 device I'm using isn't connected to any display, so I can't run their [official GUI application][app]. Additionally, although they have an official Android app, that app is not available for Android TVs. Well, I can download it and side-load it to the Android TV, but the app was designed only for phones with touch screens, and it's unusable with a remote control. That means I need to connect a mouse to the Android TV just to use the Mozilla VPN app.

I had to find an alternative… and I found [MozWire][]: an unofficial cross-platform command-line client for Mozilla VPN.

In this post, I'm writing down some simple straight-to-the-point instructions on how to use this unofficial tool to generate WireGuard configuration files (for use in other devices). These instructions worked for me at least once. These instructions may not work for you, and they may as well be obsolete by the time you're reading this post. These instructions assume a certain level of familiarity with Linux, shell, WireGuard, HTTP and network. Good luck!

[Mozilla VPN]: https://www.mozilla.org/products/vpn/
[app]: https://www.mozilla.org/en-US/products/vpn/download/
[MozWire]: https://github.com/NilsIrl/MozWire/
[WireGuard]: https://en.wikipedia.org/wiki/WireGuard
[Mullvad VPN]: https://mullvad.net

## Step 1: Building MozWire

As [described in the README.md](https://github.com/NilsIrl/MozWire/#installation):

    git clone (or git pull)
    cargo build

The [AUR PKGBUILD](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=mozwire) has a slightly different command:

    cargo build --release --locked --all-features --target-dir=target

I don't know the difference.

The final binary will be available as `./target/debug/mozwire` (or similar)

## Step 2: Running MozWire

Remember to first go to the correct directory:

    cd ./target/*/
    ./mozwire --help

### Getting a token

Since this Raspberry Pi is headless, we can't open a browser. We have work around that.

1. Run: `./mozwire --no-browser --print-token`
2. Copy-paste the URL and open it in a browser (in another machine).
3. Open the browser dev tools, and open the Network tab.
4. Proceed to sign in and complete the authorization flow.
5. At the page that says *“Please return to the Mozilla VPN app to complete setup.”*, look at the Network tab in the browser dev tools. Look for a request that looks like `?code=…`. It is a request going to localhost (`127.0.0.1`), but since we are running the browser in a different machine, this request fails.
6. Right-click on that request and select *Copy as cURL (bash)*.
7. Go back to the Raspberry Pi, in another shell, and paste the command you just copied.
8. The command you ran at step 1 should now finish and it should print a string of about 296 characters.
9. Copy that string, and run: `export MOZ_TOKEN='paste that string here'`

The `./mozwire` tool either accepts a `--token` parameter, or it looks at the `MOZ_TOKEN` environment variable.

### Renewing the token

Sometimes, the token expires. To renew it:

1. Run: `unset MOZ_TOKEN`
2. Redo all the steps above to get a new token.

### Listing the registered devices

The Mozilla VPN has a limit of 5 devices. You can use:

    ./mozwire device list

See also:

    ./mozwire device --help

### Listing all the available servers

Simple:

    ./mozwire relay list

The list is very long, you might want to pipe it to some tool (`| less` or `| vim -`).

### Generating WireGuard configuration files

As an example, this command will generate all files for all UK servers:

    ./mozwire relay save --name Manual-MozWire -n 0 -o ~/path-where-the-config-files-will-be-saved '^gb'

Let's understand it:

* `relay save` will save configuration files.
* `--name …` is the device name. (See also the list of registered devices.)
* `-n 0` means to generate an unlimited amount of configuration files. (By default, `-n 1` will generate only one file.)
* `-o …` is the directory to save the configuration files. They will be overwritten without questions.
* `'^gb'` is the regex to filter which servers are desired. (See also the list of available servers.)
* `--privkey …` can specify a previously created device private key.

Once you have those configuration files, you can use them with your WireGuard configuration. Or you can view the contents of those files and manually copy those settings to another device. Well, configuring WireGuard is outside of the scope of this blog post; if you got to this paragraph, you probably know how to configure WireGuard yourself.
