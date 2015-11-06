Title: Auto-grow TEXTAREA
Date: 2006-07-31 13:58
Author: markos
Category: Javascript, UI, Web
Slug: auto-grow-textarea

***Update 6.8.2009:** This post is old and somewhat obsolete, but has
been kept alive by commentators. Hence I posted an updated version of
the script in comments.*

[Fry](http://friedcellcollective.net/outbreak/) recently mentioned a
TEXTAREA improvement he found. As you type your text in the box, it
grows in length as needed to avoid having to deal with scroll bars.

I liked the idea and went to create my own version. Making it work in
Internet Explorer and Firefox was literally a matter of seconds. All you
really need to do is compare elements *clientHeight* with its
*scrollHeight* on key presses and increment *rows* attribute when former
is smaller than later.

But supporting Opera and Safari has proven to be an insurmountable task
for now. They simply don't seem to update any property that could
reliably be used for measuring the height of the text (but would love to
be proven wrong).

You can try a
[demo](http://markos.gaivo.net/examples/growtextarea/index.html), which
also doubles as a test environment for reading interesting attributes on
the fly (updates are done with mouse over input box).

Random bits of observation:

-   *scrollHeight* is always bigger than *clientHeight* in Opera. Hence
    the need to ignore it using its unique fingerprint.
-   I didn't try to work out the length of the text by trying to count
    the number of lines (using *\\n*) and the length of each of them.
    Proportional fonts prevent any such reasonable guess.
-   I didn't try to limit the growth of the box to the boundaries of the
    screen. I find page scroll bars the least annoying when scroll bars
    can't be avoided. It's a personal choice though.

