Title: Beloved python filter
Date: 2005-12-17 23:07
Author: markos
Category: Python
Slug: beloved-python-filter

Is it just me or does anybody else find it easier to write:

`elmList = filter( len, elmList )`

then

`elmList = [ x for x in elmList if len(x) ]`

I don't know why, but if I want to use the second form, I always have to
look it up
[somewhere](http://www.artima.com/weblogs/viewpost.jsp?thread=98196). I
know *filter* and friends are frowned upon, but I can't stop liking
them.

