Title: Self-referencing page links
Date: 2008-12-27 18:23
Author: markos
Category: Javascript, UI, Web
Slug: self-referencing-page-links

There's an HTML pattern that has been bugging me for a while even though
I'm guilty of using it too. It's even present on page you are reading
right now.

Almost every page has a navigation bar and chances are that strip is
presented as some kind of a list of links. Just as it should be. What
bothers me is that when you actually are on page listed in navigation,
its navigation item will [still
contain](http://www.alistapart.com/articles/ "An example of this pattern")
a link to it.

This reference to itself is like having a door in a room which leads you
back in. Not very useful and certainly misleading.

Better approach is to simply not have a link when that link would point
to page itself. Such HTML is also more semantic, since it's clear which
item was selected and where we are even without a style sheet.

When discussing this observation it was pointed out to me that with
proliferation of Javascript and AJAX you might want to give your
visitors a way to bring a page to a known state by reloading it. I think
this is more than adequately solved by reload button that every browser
has and most users know, but if you find having a link a better
solution, why not try a compromise. Just add the missing link with
Javascript in spirit of [this
demo](http://markos.gaivo.net/examples/html_pattern/link.html).

This way you won't polute content markup with behavior that should sit
on top of it.

