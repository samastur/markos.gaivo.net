Title: Simple List Extensions
Date: 2006-04-09 14:05
Author: markos
Category: UI, Web
Slug: simple-list-extensions

I'm not sure how I missed the original announcement of Simple List
Extensions (SLE) for feeds, but better late than never.

SLE is a very simple specification to extend feeds syntax to better
support some common scenarios that weren't covered with original
specifications of RSS and Atom. Previously there was no way to tell feed
readers/aggregators to display feed items in fixed order (e.g. feed with
most popular stories of the day) or delete items not present in feed
anymore (e.g. auction site feed with items matching a query).

SLE also adds support for grouping and filtering of feed items, which
might not be very useful with you average 10-item feed, but will be, if
feeds will indeed become a general mechanism for transporting data and
not only a tool to highlight most recent bunch of updates. In any case,
you can read a very short
[specification](http://msdn.microsoft.com/xml/rss/sle/) or visit [latest
announcement](http://blogs.msdn.com/ie/archive/2006/03/30/565222.aspx)
which includes more explanatory links to why and how they can and
already are used.

By the way, I'm not sure if any reader apart from beta of IE7 already
supports SLE, but I expect that most of them will soon. There's little
reason not to.

