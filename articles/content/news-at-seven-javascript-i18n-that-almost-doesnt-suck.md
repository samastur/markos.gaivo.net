Title: News at seven - javascript i18n that almost doesn't suck
Date: 2005-12-19 19:36
Author: markos
Category: Javascript, UI, Web
Slug: news-at-seven-javascript-i18n-that-almost-doesnt-suck
Status: published
Id: 100

<div>
 <p>
  Holidays are closer with each day and it’s getting harder and harder to concentrate on work, when your mind is occupied with loot coming your way.
 </p>
 <p>
  It’s also a time of the year when web sites are filled with various summations of year left behind and always present guesses about the future. I certainly am not above that and I’ll probably add a line or two of my own in next few days, but I also wanted to finish my little javascript i18n library before the year ends. I don’t want it to turn into a pumpkin at midnight like some girl’s ride back home.
 </p>
 <p>
  You know, sort of a present for everyone as it befits this holiday.
 </p>
 <p>
  Alas, it’s taking longer then planned. So many things to do and so little time. Since trip to Stockholm is just around the corner, I decided to release what I believe by now to be practically usable piece of localization code. If you’re interested just in the goods, then you can see new javascript file
  <a href="http://markos.gaivo.net/examples/js_i18n/3/translate.js" title="Javascript i18n library">
   here
  </a>
  and demo
  <a href="http://markos.gaivo.net/examples/js_i18n/3/index.html" title="Javascript i18n demo">
   here
  </a>
  .
 </p>
 <p>
  There have been few changes since
  <a href="look-ma-html-too.html" title="Previous post on this topic">
   last time
  </a>
  . The whole thing has been objectified, but I kept  few functions (
  <em>
   stripStr
  </em>
  ,
  <em>
   stripStrML
  </em>
  and new one
  <em>
   printf
  </em>
  ) outside of a class, since they’re too general to belong there. Nice thing about new class is that instead of looking for globally defined translation dictionary, it’s initialized with one. This also means you can use more than one translation object or translation dictionary per page, which sounds cool even if not all that useful.
 </p>
 <p>
  I made a small correction to method
  <em>
   toEntity
  </em>
  . A bug was pointed out to me by
  <a href="http://www.opera.com">
   Opera browser
  </a>
  , which is a great browser for testing against standards, if not common sense. I might think it’s OK to fetch a character out of a string with their index value, as you would fetch an element from a list or an object, but I would be wrong. That’s why a string method
  <em>
   charAt
  </em>
  was defined and if working everywhere except in Opera is not good enough for you, then you must use this method. So, I did.
 </p>
 <p>
  I also renamed the function
  <em>
   _
  </em>
  . It’s a nifty name widely used in other languages, but it doesn’t work quite like that when it’s a method in an object.
  <em>
   init.js
  </em>
  demonstrates how you can still use it by defining an anonymous function.
 </p>
 <p>
  This is it for now. I think the library is actually usable, but it’s also lacking few things.
  <em>
   printf
  </em>
  provides now a method of easily stitching  stings together and even using parameters in translations. However, it does require that those parameters are listed in same order as in original text. Better than previously, but still often awkward.
 </p>
 <p>
  What’s missing is also a tool to translate between javascript dictionary/object and a widely used translation format like
  <em>
   GNU’s gettext
  </em>
  . I’m currently working on this and I hope to have something usable ready in next few days.
 </p>
 <p>
  Last but not least, it needs a useful documentation on how to use it and work with it. It will get it.
 </p>
 <p>
  <em>
   Update: It turns out my code might be usable, but it’s certainly not good. Some issues were listed in
  </em>
  <em>
   <a href="revisiting-javascript-i18n.html">
    later
   </a>
  </em>
  <em>
   post and some I discovered just recently. For instance it won’t work if you’re trying to translate text on buttons or if text to be translated includes HTML tags (case of tags is not preserved in DOM tree, which wouldn’t be a problem if Firefox and IE defaulted to the same one).
  </em>
 </p>
</div>
