Title: Auto-grow TEXTAREA
Date: 2006-07-31 13:58
Author: markos
Category: Javascript, UI, Web
Slug: auto-grow-textarea
Status: published
Id: 198

<html>
 <body>
  <div>
   <p>
    <em>
     <strong>
      Update 6.8.2009:
     </strong>
     This post is old and somewhat obsolete, but has been kept alive by commentators. Hence I posted an updated version of the script in comments.
    </em>
   </p>
   <p>
    <a href="http://friedcellcollective.net/outbreak/">
     Fry
    </a>
    recently mentioned a TEXTAREA improvement he found. As you type your text in the box, it grows in length as needed to avoid having to deal with scroll bars.
   </p>
   <p>
    I liked the idea and went to create my own version. Making it work in Internet Explorer and Firefox was literally a matter of seconds. All you really need to do is compare elements
    <em>
     clientHeight
    </em>
    with its
    <em>
     scrollHeight
    </em>
    on key presses and increment
    <em>
     rows
    </em>
    attribute when former is smaller than later.
   </p>
   <p>
    But supporting Opera and Safari has proven to be an insurmountable task for now. They simply don’t seem to update any property that could reliably be used for measuring the height of the text (but would love to be proven wrong).
   </p>
   <p>
    You can try a
    <a href="http://markos.gaivo.net/examples/growtextarea/index.html">
     demo
    </a>
    , which also doubles as a test environment for reading interesting attributes on the fly (updates are done with mouse over input box).
   </p>
   <p>
    Random bits of observation:
   </p>
   <ul>
    <li>
     <em>
      scrollHeight
     </em>
     is always bigger than
     <em>
      clientHeight
     </em>
     in Opera. Hence the need to ignore it using its unique fingerprint.
    </li>
    <li>
     I didn’t try to work out the length of the text by trying to count the number of lines (using
     <em>
      \n
     </em>
     ) and the length of each of them. Proportional fonts prevent any such reasonable guess.
    </li>
    <li>
     I didn’t try to limit the growth of the box to the boundaries of the screen. I find page scroll bars the least annoying when scroll bars can’t be avoided. It’s a personal choice though.
    </li>
   </ul>
  </div>
 </body>
</html>