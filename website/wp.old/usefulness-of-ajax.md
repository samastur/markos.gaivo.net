Title: Usefulness of AJAX
Date: 2006-05-13 07:53
Author: markos
Category: Javascript, Web
Slug: usefulness-of-ajax

At least one participant of our recent
[workshop](http://markos.gaivo.net/blog/?p=150 "Previous announcement of AJAX workshop")
was under impression that I'm an AJAX advocate. It's certainly a
reasonable and not completely wrong conclusion. However, it seems I
failed in limited time available to explain my perspective.

As any other useful tool AJAX has its advantages, but it can also create
problems when used inappropriately. I won't dwell on advantages. More
than enough has already been said about them. There are three important
aspects that still don't get enough attention and bear repeating.

**Write unobtrusive and degradable Javascript.** It's really not that
hard with a bit of planning and it makes things easier in the long run.
It's easier to find, fix and change code when it's cleanly separated
from HTML and CSS. I'd expect everyone learned this lesson by now from
PHP. Also, creating HTML version first and then carefully improving it
with use of Javascript/AJAX can get us maximum reach without sacrificing
flexibility.

**Pay attention to usability.** This one is much harder to get right,
but if nothing else, you should have in mind at least next three
advices. Show a progress indicator when doing something that might take
more than a second. Put action trigger as close as possible to the part
of a page it will change, so user has a good chance of noticing it and
whenever possible assist them with change indicators like [yellow
fade-in](http://www.axentric.com/posts/default/7 "Example of yellow fade-in").

**Accessibility shouldn't be forgotten either.** This is probably [the
hardest
problem](http://domscripting.com/blog/display/64 "Accessibility problems with DOM manipulation")
to tackle. It's the most important reason (but not the only one) why I
try to use Javascript/AJAX only when benefits of doing so significantly
outweigh the problems it might cause.

Everyone makes mistakes and I certainly have. I'm sure they weren't last
ones either, but we can all strive for better.

