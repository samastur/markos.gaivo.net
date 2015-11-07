Title: Dreaming about GIL
Date: 2005-10-11 15:38
Author: markos
Category: Python
Slug: dreaming-about-gil
Status: published
Id: 40

<html>
 <body>
  <div>
   <p>
    I’ve been thinking about Python’s global interpreter lock (GIL) again. Since I’m a glutton for punishment and haven’t been crucified in a week, you get to hear about it too.
   </p>
   <p>
    Has anybody thought and wrote about avoiding GIL until you need it? What I mean is creating and using GIL only when you start using code that might not be thread-safe.
   </p>
   <p>
    So, what’s wrong with this idea?
   </p>
   <p>
    Things that come to my mind:
   </p>
   <ul>
    <li>
     garbage collector is not thread-safe
    </li>
    <li>
     majority of interesting modules are not thread-safe, so there would be little ROI
    </li>
    <li>
     dynamic nature of Python means you can’t know in advance if you’ll need GIL and it would a bitch to fall back when you do
    </li>
    <li>
     …
    </li>
   </ul>
   <p>
    I guess it’s just a really stupid idea.
   </p>
  </div>
 </body>
</html>