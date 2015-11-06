Title: Javascript slider
Date: 2005-10-08 15:27
Author: markos
Category: Javascript
Slug: javascript-slider

I think HTML forms are probably the least well designed part of X/HTML
specifications and at least [some
people](http://www.whatwg.org/ "Link to WHATWG") agree. They were fine
when they came out, but time has moved on and form elements just didn't
follow. There are too many things wrong with them, but personally I
mostly miss a good control for date handling and a slider.

So [here's](/examples/slider/index.html "Slider example") my take on a
slider, implemented with javascript. You can also download this example
packed in [a zip](/examples/slider.zip).

It works at least in all major browsers, but I don't consider it
finished. However, since I haven't found the time to finish it and I
don't think I will any time soon, I've decided to publish it anyway. It
may be useful to somebody.

It's fairly easy to use, if you can live with its limitations. You can
create a horizontal or vertical slider. I believe example is
self-explanatory, but if you find it difficult to use, please let me
know and I'll help.

Couple of things to remember. Code expects to find an image of button in
subdirectory *img* and it shouldn't be bigger than this one. If you need
a different size, just correct javascript.

Also *addEvent* and *delEvent* functions in *slider.js* should be
replaced with something more robust, when
[ppk's](http://www.quirksmode.org/blog/ "PPK's blog") team declares a
winner.

