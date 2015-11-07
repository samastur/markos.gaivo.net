Title: Look ma', HTML too
Date: 2005-12-11 23:08
Author: markos
Category: Javascript, UI, Web
Slug: look-ma-html-too
Status: published
Id: 93

<html>
 <body>
  <div>
   <p>
    This is a second post in hopefully a very short series dedicated to javascript internationalization. If you want, you can read the first one
    <a href="solving-javascript-i18n-as-work-in-progress.html">
     here
    </a>
    .
   </p>
   <p>
    We left off with two supporting functions for striping whitespace and a simple function for translation lookup. Today I added another two functions, one for translating HTML elements and the other for resolving a problem with HTML entities. You can find new javascript
    <a href="http://markos.gaivo.net/examples/js_i18n/2/translate.js">
     here
    </a>
    and a demo
    <a href="http://markos.gaivo.net/examples/js_i18n/2/index.html">
     here
    </a>
    .
   </p>
   <p>
    <em>
     translateNodes
    </em>
    searches for elements with class name i18n, picks up their text content and translates it, if it can find it in translation dictionary. Sometimes it can’t, because what javascript actually sees is a real utf-8 encoded string, where X/HTML entities have been replaced with characters they represent. If this is not true also for source string in dictionary, then there’s a mismatch.
   </p>
   <p>
    That’s why there’s
    <em>
     toEntity
    </em>
    function which translates all non-ASCII characters in given string to their entity representation. When
    <em>
     translateNodes
    </em>
    fails to find translation, it uses
    <em>
     toEntity
    </em>
    to get a possibly different representation and tries again.
   </p>
   <p>
    This way you can use entities, which are the only real cross-browser way to describe non-ASCII chars and translations still work. There’s a downside though. Your translation source string must either have all non-ASII characters represented as HTML entities or none of them. Otherwise translation will fail for obvious reasons.
   </p>
   <p>
    There are planned limitations (like building a system that handles only utf-8 text) and unplanned ones. I still don’t do anything special for strings with significant whitespace (like content of a
    <em>
     pre
    </em>
    tag) and probably should.
   </p>
   <p>
    Do nothing = I break it.
   </p>
   <p>
    It would be nice, if I started to pack this functionality in a more sensible form and build tools that make handling of the whole thing easier.
   </p>
   <p>
    Next week, which starts in an hour or so, seems perfect time for that.
   </p>
   <p>
    Update: Follow up
    <a href="news-at-seven-javascript-i18n-that-almost-doesnt-suck.html">
     here
    </a>
    .
   </p>
  </div>
 </body>
</html>