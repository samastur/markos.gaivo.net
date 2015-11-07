Title: Firefox and defer="defer"
Date: 2006-03-04 17:19
Author: markos
Category: General development, Web
Slug: firefox-and-deferdefer
Status: published
Id: 132

<html>
 <body>
  <div>
   <p>
    If you’re sitting in the wrong part of the world, then Google might be inaccessible to you right now. That would be only a minor annoyance, if the same wasn’t true also for Google Analytics.
   </p>
   <p>
    It’s remarkable how many sites (including this one) use it and are right now more or less inaccessible to every poor soul suffering from Google blackout. That’s because browser can’t tell if external Javascript will use a method like
    <em>
     document.write
    </em>
    and therefore blocks rendering until the code is loaded or it timeouts waiting for it.
   </p>
   <p>
    There should be a workaround for times like this and according to HTML4 specification there is
    <a href="http://www.w3.org/TR/1999/REC-html401-19991224/interact/scripts.html#adef-defer">
     one
    </a>
    . By using
    <em>
     defer=”defer”
    </em>
    we can signal to the browser that it can safely proceed rendering the page, because we won’t be using any dangerous methods in our Javascript files.
   </p>
   <p>
    However, it sadly doesn’t work everywhere. It works in Internet Explorer, but fails in Firefox and Safari. And that simply sucks.
   </p>
  </div>
 </body>
</html>