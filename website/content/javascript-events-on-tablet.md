Title: Javascript events on tablet
Date: 2007-12-16 18:14
Author: markos
Category: Javascript, Web
Slug: javascript-events-on-tablet
Status: published
Id: 244

<html>
 <body>
  <div>
   <p>
    I’ve been curious about interface possibilities and limitations of non-desktop environments like my Nokia tablet for a while, especially as they pertain to web. Pen on a touchscreen obviously doesn’t have to leave a “trail” of traversal like a mouse does. You also don’t have several mouse buttons at your disposal.
   </p>
   <p>
    So I made a simple
    <a href="http://markos.gaivo.net/examples/jsenvtest.html">
     test page
    </a>
    to see how some of more interesting events get caught.
   </p>
   <p>
    The result on my 770 was quite disappointing while also expected. I’ll summarize it for those who don’t have a tablet. Touching a screen generates
    <em>
     mousemove
    </em>
    event and sometimes
    <em>
     mouseover
    </em>
    , but you never get a
    <em>
     mouseout
    </em>
    event. If touched briefly enough, it’ll also generate
    <em>
     mousedown
    </em>
    ,
    <em>
     mouseup
    </em>
    and
    <em>
     click
    </em>
    event in this order.
   </p>
   <p>
    You won’t get a
    <em>
     mousedown
    </em>
    and
    <em>
     mouseup
    </em>
    events until
    <em>
     click
    </em>
    . If you keep pressing the screen without moving, you’ll  get a context menu, but I found no way to get to
    <em>
     mousedown
    </em>
    on its own. This means it’s impossible to create a “natural” drag and drop, which isn’t surprising, since same movement is already taken by browser for scrolling.
   </p>
   <p>
    My test was limited to Nokia 770 tablet, but I doubt results would be much different elsewhere (Fry, can you check your tablet?). It would also be interesting to see what iPhone does, but since I don’t have it either, I can’t tell.
   </p>
   <p>
    Still I’ll need to rethink a widget for website I’m working on and keep this in mind for my next year project.
   </p>
  </div>
 </body>
</html>