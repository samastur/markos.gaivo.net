Title: Solving javascript i18n as work in progress
Date: 2005-12-08 14:11
Author: markos
Category: Javascript, Web
Slug: solving-javascript-i18n-as-work-in-progress
Status: published
Id: 90

<div>
 <p>
  A while ago I was moaning about a sad state of javascript i18n tools. When I finally started working on it, I faced a dilemma.
 </p>
 <p>
  Should I wait until it’s finished and then reveal it like Moses to chosen people? Look guys what I etched with a toothpick during my lunch time break! You know, I was waiting for my Crème Brûlée and had to kill those few pesky minutes.
 </p>
 <p>
  Or should I choose a more honest approach, showing steps and missteps between embarrassing first version and hopefully usable last?
 </p>
 <p>
  Well, there’s nothing better than public humiliation to instill some humility so let’s see what is behind the door number two.
 </p>
 <p>
  The goal is still the same. Develop a short and relatively fast library that allows you to translate javascript code and HTML content and to do so with as little fuss as possible and with a clear separation between HTML, javascript and translations, but without breaking pages in case translation doesn’t exist yet.
 </p>
 <p>
  And
  <a href="http://markos.gaivo.net/examples/js_i18n/1/translate.js" title="Translation functions">
   here’s
  </a>
  my humble start together with a
  <a href="http://markos.gaivo.net/examples/js_i18n/1/index.html" title="Link to demonstration page">
   simple demo
  </a>
  . Three functions, two of them a support needed later on. stripStr and stripStrML just strip whitespace at the start and end of string with stripStrML doing it on every line of a given string. We’ll need this later on so we can find strings to translate even if they are enclosed in whitespace to make source display more pretty.
 </p>
 <p>
  Then there’s a function called _, which takes a string and translates it if javascript object i18nDict exists and has this string as an attribute with a non empty value. Otherwise it just returns the same string, so it doesn’t break page even if translation doesn’t exist in
  <a href="http://markos.gaivo.net/examples/js_i18n/1/i18n.js" title="Translation dictionary">
   translation object
  </a>
  . It’s what is usually called a proof of concept prototype.
 </p>
 <p>
  That’s it for today. I’ll try to post updates every couple of days or so, if progress warrants it.
 </p>
 <p>
  Update: Follow up
  <a href="look-ma-html-too.html">
   here
  </a>
  and
  <a href="news-at-seven-javascript-i18n-that-almost-doesnt-suck.html">
   here
  </a>
  .
 </p>
</div>
