Title: Look ma', HTML too
Date: 2005-12-11 23:08
Author: markos
Category: Javascript, UI, Web
Slug: look-ma-html-too

This is a second post in hopefully a very short series dedicated to
javascript internationalization. If you want, you can read the first one
[here](http://markos.gaivo.net/blog/?p=90).

We left off with two supporting functions for striping whitespace and a
simple function for translation lookup. Today I added another two
functions, one for translating HTML elements and the other for resolving
a problem with HTML entities. You can find new javascript
[here](http://markos.gaivo.net/examples/js_i18n/2/translate.js) and a
demo [here](http://markos.gaivo.net/examples/js_i18n/2/index.html).

*translateNodes* searches for elements with class name i18n, picks up
their text content and translates it, if it can find it in translation
dictionary. Sometimes it can't, because what javascript actually sees is
a real utf-8 encoded string, where X/HTML entities have been replaced
with characters they represent. If this is not true also for source
string in dictionary, then there's a mismatch.

That's why there's *toEntity* function which translates all non-ASCII
characters in given string to their entity representation. When
*translateNodes* fails to find translation, it uses *toEntity* to get a
possibly different representation and tries again.

This way you can use entities, which are the only real cross-browser way
to describe non-ASCII chars and translations still work. There's a
downside though. Your translation source string must either have all
non-ASII characters represented as HTML entities or none of them.
Otherwise translation will fail for obvious reasons.

There are planned limitations (like building a system that handles only
utf-8 text) and unplanned ones. I still don't do anything special for
strings with significant whitespace (like content of a *pre* tag) and
probably should.

Do nothing = I break it.

It would be nice, if I started to pack this functionality in a more
sensible form and build tools that make handling of the whole thing
easier.

Next week, which starts in an hour or so, seems perfect time for that.

Update: Follow up [here](http://markos.gaivo.net/blog/?p=100).

