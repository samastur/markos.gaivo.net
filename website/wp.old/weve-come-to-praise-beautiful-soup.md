Title: We've come to praise Beautiful Soup
Date: 2005-08-31 19:44
Author: markos
Category: Python, Web
Slug: weve-come-to-praise-beautiful-soup

So, I've been working on this project for some time now, where I'd take
user supplied HTML templates and transformed them into new templates,
that our system can actually use.

I needed to mangle and change them, but I also didn't want to require
from users things like well-formedness and other stuff that makes sense
only to web developers (and sadly not even to all of them). Mainly, I
want this stuff to be used by everyone, even those with retarded web
editors and if it's good enough to be displayed in their browsers, it
ought to be good enough for me.

This decision was made a lot easier, when I discovered [Beautiful
Soup](http://www.crummy.com/software/BeautifulSoup/index.html "Homepage of Beautiful Soup python module").
It's a python module that makes screen-scraping much easier, but what is
even more cool, is that it makes changing documents, even those with bad
markup, extremely easy.

If you are a python developer, who needs to extract information from or
possibly change documents with bad markup, this is the module to use. It
will save you time, keep you sane and make you rich. Well, two out of
three ain't bad either.

*Update: Beautiful Soup has [issues](http://markos.gaivo.net/blog/?p=18)
with Javascript code included in HTML.*

