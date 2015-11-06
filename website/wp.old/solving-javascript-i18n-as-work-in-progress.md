Title: Solving javascript i18n as work in progress
Date: 2005-12-08 14:11
Author: markos
Category: Javascript, Web
Slug: solving-javascript-i18n-as-work-in-progress

A while ago I was moaning about a sad state of javascript i18n tools.
When I finally started working on it, I faced a dilemma.

Should I wait until it's finished and then reveal it like Moses to
chosen people? Look guys what I etched with a toothpick during my lunch
time break! You know, I was waiting for my Crème Brûlée and had to kill
those few pesky minutes.

Or should I choose a more honest approach, showing steps and missteps
between embarrassing first version and hopefully usable last?

Well, there's nothing better than public humiliation to instill some
humility so let's see what is behind the door number two.

The goal is still the same. Develop a short and relatively fast library
that allows you to translate javascript code and HTML content and to do
so with as little fuss as possible and with a clear separation between
HTML, javascript and translations, but without breaking pages in case
translation doesn't exist yet.

And
[here's](http://markos.gaivo.net/examples/js_i18n/1/translate.js "Translation functions")
my humble start together with a [simple
demo](http://markos.gaivo.net/examples/js_i18n/1/index.html "Link to demonstration page").
Three functions, two of them a support needed later on. stripStr and
stripStrML just strip whitespace at the start and end of string with
stripStrML doing it on every line of a given string. We'll need this
later on so we can find strings to translate even if they are enclosed
in whitespace to make source display more pretty.

Then there's a function called \_, which takes a string and translates
it if javascript object i18nDict exists and has this string as an
attribute with a non empty value. Otherwise it just returns the same
string, so it doesn't break page even if translation doesn't exist in
[translation
object](http://markos.gaivo.net/examples/js_i18n/1/i18n.js "Translation dictionary").
It's what is usually called a proof of concept prototype.

That's it for today. I'll try to post updates every couple of days or
so, if progress warrants it.

Update: Follow up [here](http://markos.gaivo.net/blog/?p=93) and
[here](http://markos.gaivo.net/blog/?p=100).

