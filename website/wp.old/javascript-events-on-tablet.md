Title: Javascript events on tablet
Date: 2007-12-16 18:14
Author: markos
Category: Javascript, Web
Slug: javascript-events-on-tablet

I've been curious about interface possibilities and limitations of
non-desktop environments like my Nokia tablet for a while, especially as
they pertain to web. Pen on a touchscreen obviously doesn't have to
leave a "trail" of traversal like a mouse does. You also don't have
several mouse buttons at your disposal.

So I made a simple [test
page](http://markos.gaivo.net/examples/jsenvtest.html) to see how some
of more interesting events get caught.

The result on my 770 was quite disappointing while also expected. I'll
summarize it for those who don't have a tablet. Touching a screen
generates *mousemove* event and sometimes *mouseover*, but you never get
a *mouseout* event. If touched briefly enough, it'll also generate
*mousedown*, *mouseup* and *click* event in this order.

You won't get a *mousedown* and *mouseup* events until *click*. If you
keep pressing the screen without moving, you'll get a context menu, but
I found no way to get to *mousedown* on its own. This means it's
impossible to create a "natural" drag and drop, which isn't surprising,
since same movement is already taken by browser for scrolling.

My test was limited to Nokia 770 tablet, but I doubt results would be
much different elsewhere (Fry, can you check your tablet?). It would
also be interesting to see what iPhone does, but since I don't have it
either, I can't tell.

Still I'll need to rethink a widget for website I'm working on and keep
this in mind for my next year project.

