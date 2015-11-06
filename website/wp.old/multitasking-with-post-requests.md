Title: Multitasking with POST requests?
Date: 2005-12-15 20:34
Author: markos
Category: Javascript, UI, Web
Slug: multitasking-with-post-requests

I have a kinky wish. I'd like to submit a web form that wouldn't get
canceled if I clicked another link before its completion.

Browsers normally don't work like this. They interpret subsequent clicks
on active elements as a change of heart on user's part and cancel
previous clicks in favor of last one. Most of the time this is exactly
what you'd want and expect.

However, sometimes it isn't. I'd like to open a new window for upload
progress bar and release the old one so users can continue working
without waiting for upload to finish. I suspect it can't be done though.

Has anyone had more luck with this?

