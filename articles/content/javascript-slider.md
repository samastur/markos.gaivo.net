Title: Javascript slider
Date: 2005-10-08 15:27
Author: markos
Category: Javascript
Slug: javascript-slider
Status: published
Id: 38

<div>
 <p>
  I think HTML forms  are probably the least well designed part of X/HTML specifications and at least
  <a href="http://www.whatwg.org/" title="Link to WHATWG">
   some people
  </a>
  agree. They were fine when they came out, but time has moved on and form elements just didn’t follow. There are too many things wrong with them, but personally I mostly miss a good control for date handling and a slider.
 </p>
 <p>
  So
  <a href="/examples/slider/index.html" title="Slider example">
   here’s
  </a>
  my take on a slider, implemented with javascript. You can also download this example packed in
  <a href="/examples/slider.zip">
   a zip
  </a>
  .
 </p>
 <p>
  It works at least in all major browsers, but I don’t consider it finished. However, since I haven’t found the time to finish it and I don’t think I will any time soon, I’ve decided to publish it anyway. It may be useful to somebody.
 </p>
 <p>
  It’s fairly easy to use, if you can live with its limitations. You can create a horizontal or vertical slider. I believe example is self-explanatory, but if you find it difficult to use, please let me know and I’ll help.
 </p>
 <p>
  Couple of things to remember. Code expects to find an image of button in subdirectory
  <em>
   img
  </em>
  and it shouldn’t be bigger than this one. If you need a different size, just correct javascript.
 </p>
 <p>
  Also
  <em>
   addEvent
  </em>
  and
  <em>
   delEvent
  </em>
  functions in
  <em>
   slider.js
  </em>
  should be replaced with something more robust, when
  <a href="http://www.quirksmode.org/blog/" title="PPK's blog">
   ppk’s
  </a>
  team declares a winner.
 </p>
</div>
