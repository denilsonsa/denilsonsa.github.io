---
layout: post
title: Bulk-editing your Google Contact list
lang: en
tag:
- mobile
- Android
- JavaScript
- programming
- Google
---

Let's say you are a programmer/hacker/geek like me. Let's say you want to edit multiple contacts from your Google contact list (the same one shared by Gmail and Android).

One possible solution (or workaround) is to export all your contacts from [Google Contacts](https://www.google.com/contacts/) into a [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values); import this file into Excel, OpenOffice, Google Spreadsheet, Python, Gvim…; modify the file in that tool; export an updated CSV file from the tool; and finally import it back into Google Contacts. That's way too troublesome, it has too many steps, and I have a feeling that the export-modify-import cycle will lead to trouble (duplicate or messy contacts, maybe). Since I want to avoid trouble, I stayed away from that “solution”.

Wouldn't it be nice if you could write a program to bulk-edit all your contacts? Well, it is possible!


## Google Apps Scripts

Google provides the infrastructure and a lot of APIs to run JavaScript-based code to process data stored inside Google products. You can automate essentially anything. Hardcore Office users can think about Google Apps Scripts as Microsoft Office or OpenOffice macros.

Learn more about Google Apps Scripts at [https://developers.google.com/apps-script/](https://developers.google.com/apps-script/), and start using it right away at [https://script.google.com/](https://script.google.com/).

## Bulk-editing my contact list: adding a ninth digit to mobile numbers

In Brazil, some regions are adding a ninth digit to all mobile numbers. This means everyone needs to go through their contact lists editing all phones from certain region codes. Seems pretty simple, repetitive, boring and time-consuming. It is a great candidate for automation using Google Apps Scripts!

Then I wrote the following code, which is also available on [GitHub Gist](https://gist.github.com/denilsonsa/7165746) and on [Google Apps Scripts](https://script.google.com/d/1Jd3p0m0WS9Jjg1p8ztXDflQkCHZdj6BC36c5ZedgOov3vmRBF_4_pc_Y/edit).

```javascript
function fixNumbers() {
  Logger.log('Starting...');
  var dry_run = true;

  // Numbers from regions 21, 22, 24, 27, 28.
  // Starting with 8 ou 9.
  // Containing exactly 8 digits.
  // Ignoring prefixes, both valid and invalid.
  var re = /\s*(.*2[12478]\)?[- .]?)\b([89](?:[- .]?[0-9]){7})\s*$/;

  var contacts = ContactsApp.getContacts();
  for (var i = 0; i < contacts.length; i++) {
    var contact = contacts[i];
    var phones = contact.getPhones();
    for (var j = 0; j < phones.length; j++) {
      var phone = phones[j];
      var oldnum = phone.getPhoneNumber();
      var match = re.exec(oldnum);
      if (match) {
        var newnum = match[1] + '9' + match[2];
        Logger.log(oldnum + '" -> "' + newnum + '" (' + contact.getFullName() + ')');
        if (!dry_run) {
          phone.setPhoneNumber(newnum);
        }
      }
    }
  }
  Logger.log('Done!');
  return msg;
}
```

As you can see, around 30 lines of very straightforward JavaScript/ECMAScript code: iterate over all phone numbers from all my contacts and update the number based on a [RegEx](https://en.wikipedia.org/wiki/Regular_expression).

Then I wanted to share this solution with other people, and I found out that I could write a UI for this code and deploy it as a web app for anyone to use. And I did it in just one night. From scratch. Without prior knowledge that it was even possible. [I love when this kind of magic happens!](http://my.opera.com/CrazyTerabyte/blog/2010/10/07/how-to-build-a-mobile-app-in-one-hour-from-scratch-with-no-experience)

[The end result is live](https://script.google.com/macros/s/AKfycbzWlGLgZmA0lygkwMLp3p6RrRFIbBfVdKGXaUAcJCJo59R492E/exec), you can try it, and the entire code is around 100 lines (if you ignore the comments and blank lines).
