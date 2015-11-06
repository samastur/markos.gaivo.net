Title: Google Gears Goodies
Date: 2007-05-31 15:00
Author: markos
Category: Javascript, Web
Slug: google-gears-goodies

It's an expected fact of a geek life that interesting technologies and
gadgets appear when you don't have either means or time to play with
them. No surprise then that [Google
Gears](http://code.google.com/apis/gears/index.html) was announced
exactly at such a time for me. As you've probably read elsewhere, Google
Gears is a browser extension for Firefox and Internet Explorer (with
Safari coming up) which lets developers create web applications that can
also run offline on Windows, Mac OS X and Linux.

Google isn't the first company doing something like this. Adobe has
Apollo, Microsoft is working on its own thing, Mozilla added support for
offline storage in version 2 of the fox and there are some less well
known attempts like Dojo's. What makes it special are few things.

First, unlike Apollo or Firefox, it's not a special environment and it's
as cross-browser and cross-platform as it gets these days. Google is
also trying to build an industry support for this and Adobe already
[announced](http://shebanation.com/2007/05/30/google-gears/) it will
support Gears API in Apollo. Same has [already been
done](http://ajaxian.com/archives/audible-ajax-episode-21-dojo-offline-on-google-gears)
by Dojo Toolkit. There's also [an
intention](http://erik.eae.net/archives/2007/05/30/19.06.10/#comments)
to make it an open standard by submitting proposal to WHATWG/W3C (and
hopefully them accepting it).

Personally, I can't wait to play with WorkerPool API (which seems to be
overlooked in all the excitement). Having a possibility of running
time-intensive operations in a background without the fear of triggering
"unresponsive script" dialog is a wish come true. Even though you can't
access objects *document* and *window* (and hence any part of the DOM).
Reason for this is that background scripts don't share any execution
state and hence can't all access unique objects like aforementioned
ones.

This might limit usefulness of the API somewhat, but there are still
plenty of uses that come to my mind. What also comes to my mind is a
problem, that isn't really technological. Web applications gave
impression to public of being fairly safe to use even on public
computers (which isn't really true) and I fear many won't understand
that new tools may now store private data where they don't expect or
want them to.

