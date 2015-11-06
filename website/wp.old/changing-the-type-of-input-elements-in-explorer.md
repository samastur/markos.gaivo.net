Title: Changing the type of INPUT elements in Explorer
Date: 2006-07-09 21:42
Author: markos
Category: Javascript
Slug: changing-the-type-of-input-elements-in-explorer

Building XHTML using DOM methods is annoying as it is without strange
errors making things worse. Today I stumbled on a new problem when
testing improved organizer in Internet Explorer.

If you are creating INPUT elements with non-default types (that is other
than text input), then you have to change their type BEFORE you attach
them to document tree. Otherwise Explorer might complain.

I haven't had time to test this sufficiently and frankly I'd rather do
something else on Sunday evening, so there might be some cases where
above doesn't hold true. But if you find yourself looking at such an
error, it doesn't hurt to try my remedy.

