Title: sgmllib.py parser woes
Date: 2006-03-28 20:51
Author: markos
Category: Python
Slug: sgmllibpy-parser-woes
Status: published
Id: 142

<html>
 <body>
  <div>
   <p>
    Does anybody have problems with sgmllib.py?
   </p>
   <p>
    After I spent way too much time hunting a bug in my code, I gave up, read the
    <em>
     goahead
    </em>
    function in
    <em>
     sgmllib.py
    </em>
    and I’m certain now that its parser is broken.
   </p>
   <p>
    Let’s say you’re handling a web page with inline Javascript code which also includes HTML tags. Even if you use a
    <em>
     setliteral
    </em>
    method to skip processing data inside
    <em>
     &lt;script&gt;
    </em>
    tags,
    <em>
     sgmllib.py
    </em>
    will start doing so when it encounters first &lt;/. It interprets this as a start of an end tag and tries  to close it. Even though code handles cases of known and unknown tags, it fails to do the right thing because it simply doesn’t expect a scenario where this isn’t a tag at all.
   </p>
   <p>
    The other possibility is that I’m simply a dolt who should do stuff like this only when rested. By the way, where’s the proper place to make an ass out of myself complaining about standard library?
   </p>
  </div>
 </body>
</html>