Title: News at seven - javascript i18n that almost doesn't suck
Date: 2005-12-19 19:36
Author: markos
Category: Javascript, UI, Web
Slug: news-at-seven-javascript-i18n-that-almost-doesnt-suck

Holidays are closer with each day and it's getting harder and harder to
concentrate on work, when your mind is occupied with loot coming your
way.

It's also a time of the year when web sites are filled with various
summations of year left behind and always present guesses about the
future. I certainly am not above that and I'll probably add a line or
two of my own in next few days, but I also wanted to finish my little
javascript i18n library before the year ends. I don't want it to turn
into a pumpkin at midnight like some girl's ride back home.

You know, sort of a present for everyone as it befits this holiday.

Alas, it's taking longer then planned. So many things to do and so
little time. Since trip to Stockholm is just around the corner, I
decided to release what I believe by now to be practically usable piece
of localization code. If you're interested just in the goods, then you
can see new javascript file
[here](http://markos.gaivo.net/examples/js_i18n/3/translate.js "Javascript i18n library")
and demo
[here](http://markos.gaivo.net/examples/js_i18n/3/index.html "Javascript i18n demo").

There have been few changes since [last
time](http://markos.gaivo.net/blog/?p=93 "Previous post on this topic").
The whole thing has been objectified, but I kept few functions
(*stripStr*, *stripStrML* and new one *printf*) outside of a class,
since they're too general to belong there. Nice thing about new class is
that instead of looking for globally defined translation dictionary,
it's initialized with one. This also means you can use more than one
translation object or translation dictionary per page, which sounds cool
even if not all that useful.

I made a small correction to method *toEntity*. A bug was pointed out to
me by [Opera browser](http://www.opera.com), which is a great browser
for testing against standards, if not common sense. I might think it's
OK to fetch a character out of a string with their index value, as you
would fetch an element from a list or an object, but I would be wrong.
That's why a string method *charAt* was defined and if working
everywhere except in Opera is not good enough for you, then you must use
this method. So, I did.

I also renamed the function *\_*. It's a nifty name widely used in other
languages, but it doesn't work quite like that when it's a method in an
object. *init.js* demonstrates how you can still use it by defining an
anonymous function.

This is it for now. I think the library is actually usable, but it's
also lacking few things. *printf* provides now a method of easily
stitching stings together and even using parameters in translations.
However, it does require that those parameters are listed in same order
as in original text. Better than previously, but still often awkward.

What's missing is also a tool to translate between javascript
dictionary/object and a widely used translation format like *GNU's
gettext*. I'm currently working on this and I hope to have something
usable ready in next few days.

Last but not least, it needs a useful documentation on how to use it and
work with it. It will get it.

*Update: It turns out my code might be usable, but it's certainly not
good. Some issues were listed in*
*[later](http://markos.gaivo.net/blog/?p=130)* *post and some I
discovered just recently. For instance it won't work if you're trying to
translate text on buttons or if text to be translated includes HTML tags
(case of tags is not preserved in DOM tree, which wouldn't be a problem
if Firefox and IE defaulted to the same one).*

