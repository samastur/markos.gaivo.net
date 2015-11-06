Title: Google ignore
Date: 2006-04-10 13:59
Author: markos
Category: UI, Web
Slug: google-ignore

A few days ago I came to
[recognize](http://markos.gaivo.net/blog/?p=146) that email hiding
technique I use won't work anymore. However I still think it would be a
great idea if I could remove a part of a page from search index, even if
it won't help me hide from spammers in the long run.

What I'd really like is to specify which parts of a page are not its
content and can be safely ignored by search engines. Ignoring it would
also mean absence of those parts from search indexes. Spiders could
still follow links inside those parts, because I can still use
*robots.txt* file if I really want to block their traversal. In effect,
I'd like a more fine-grained approach to blocking, which doesn't force
the layout of my pages to even slightly favor spiders over people.

The way I imagine it would work is by simply applying a class name to
the parts of the page I'd want shielded. I don't care much (yet) if such
class name would need to be specified in robots file or if it would be
some name achieved by a web consensus. As far as I can see both
approaches would work equally well.

The benefit of this would also be better search results. Every now and
then I follow a search hit that fit my query because of a combination of
site content and its navigation. Judging by my logs I'm not the only
deceived soul. So, wouldn't it be nice to be able to tell which parts
are content and which aren't?

