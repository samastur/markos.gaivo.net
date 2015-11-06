Title: The callee is not available
Date: 2006-05-24 13:38
Author: markos
Category: Javascript
Slug: the-callee-is-not-available
Status: published
Id: 173

<html>
 <body>
  <div>
   <p>
    Sometimes you get this feeling of really mastering a technology. As if nothing can surprise you and you’ve seen it all. If you’re lucky, you’ll get a message like this before you become too cocky:
   </p>
   <blockquote>
    <p>
     Error: The callee (server [not server application]) is not available and disappeared; all connections are invalid. The call did not execute.
    </p>
   </blockquote>
   <p>
    Do you know what it means? Neither did I, but somebody else
    <a href="http://www.thescripts.com/forum/post297987-2.html">
     did
    </a>
    :
   </p>
   <blockquote>
    <p>
     It occurs in the context of pages using javascript to generate page
     <br/>
     content and communicate between windows, one of which windows is closed.
    </p>
    <p>
     Possibly
     <br/>
     * page A pops up page B in the link and page B wants to communicate with
     <br/>
     page A, but page A has been closed (possibly by you or a popup killer?), or
     <br/>
     * Internet Explorer has become totally confused and it will work in
     <br/>
     another browser, or
     <br/>
     * poor page design.
    </p>
   </blockquote>
   <p>
    Or in my case forgetting Javascript passes references when assigning objects which become null, if referenced object was stored in now defunct window. The problematic browser in question was of course Internet Explorer.
   </p>
  </div>
 </body>
</html>