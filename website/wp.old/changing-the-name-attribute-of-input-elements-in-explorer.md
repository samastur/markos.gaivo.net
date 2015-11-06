Title: Changing the name attribute of INPUT elements in Explorer
Date: 2006-07-10 14:53
Author: markos
Category: Javascript
Slug: changing-the-name-attribute-of-input-elements-in-explorer

Another day, another Internet Explorer problem.

You
[can't](http://msdn.microsoft.com/workshop/author/dhtml/reference/properties/name_2.asp)
set a *name* attribute on elements created with *createElement* method.
You either have to provide the name when executing the method in true
IE-only fashion (see example on linked page) or have to use some other
method of creation like more widely usable but still non-standard
*innerHTML*.

