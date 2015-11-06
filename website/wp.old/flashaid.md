Title: FlashAid
Date: 2006-07-04 11:21
Author: markos
Category: Javascript, UI, Web
Slug: flashaid

Ever since I listened to Andy Clarke's talk at @media, I've been
convinced that what we're missing is a simple way to distinguish between
visitors which need accessible version of the site and those who would
prefer to use a non-accessible version.

I still think that by and large sites should be made accessible to
everyone and done so completely. But just as Braille signs are used only
by those who need them, there's no reason why everyone should be using
the same user interface when not doing so can be beneficial.

Those who've been dabbling with Javascript and AJAX for a while have
probably noticed that it can be very difficult if often not impossible
to make every piece of interface accessible. A common approach was to
add javascript as a layer on top of an accessible website, which could
be turned off when necessary. I find this a rather blunt instrument,
since all or nothing approach removes even pieces that may be useful and
accessible. Yet, there didn't seem to be a better way.

Accessibility preference would ideally be provided by a browser in a way
that can be picked up with Javascript (environment variable?), but
lacking that, I was looking for a way to signal such preference through
user defined CSS. My idea was to define a syntactically valid, but
normally not used combination of a page element, CSS property and its
value that could be interpreted as a switch for accessible version of
the site.

Well, now [there's](http://osflash.org/flashaid) another way to learn if
screen reader is used
([via](http://domscripting.com/blog/display/77#comment-container) Jeremy
Keith), which uses Flash 8 and its JS-Flash bridge to read if such a
device is present. Obviously its use is not universal, but it covers
scenario that troubles me most.

Still a real fix would be a better support from user agents. It doesn't
seem to be that hard to add an environment variable and a preference
switch, so is there some other reason why it hasn't happened yet?

