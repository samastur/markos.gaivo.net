Title: Building FAQ from wiki pages
Date: 2005-11-22 17:17
Author: markos
Category: Company, Python, Web
Slug: building-faq-from-wiki-pages

We use [MoinMoin](http://moinmoin.wikiwikiweb.de/ "MoinMoin's homepage")
for all our documentation needs, since it simplifies almost all related
tasks. It's nice when everything is available at one place through a
familiar and easy to use interface.

This is why I also wanted to use it to build a FAQ for our site, which
is more needed with each day. There's an abundance of software for
building and managing such documents, but I haven't found anything that
would match our needs. Apart from using wiki pages as the source of
wisdom, I also wanted:

1.  A good and fairly easy integration with our site (but not
    automatic).
2.  A very malleable solution, where it would be easy to change FAQ
    organization as requirements change.

At the end I decided to build our own thing using [Beautiful
Soup](http://www.crummy.com/software/BeautifulSoup/index.html), a python
package I raved about a while ago. Since we wanted each question to have
a permanent link that could be bookmarked, we had to give them an
identifier that wouldn't change even if we rephrased the question or
changed the answer. The simplest way was to assign a unique number to
each question as it can be seen on a [sample FAQ
page](http://markos.gaivo.net/examples/samplefaq/faq.html). This way
it's easy to add and remove questions as long as you can count.

MoinMoin produces very sensible HTML that is easy to work with.
[Here's](http://markos.gaivo.net/examples/samplefaq/faq.py) a proof of
concept module that extracts information from a page like the sample one
and packs it in a dictionary with identifiers as keys and a list *[
question, answer ]* as value.

It's not something very useful on its own, but I think it's a nice
example of what can be done quickly with existing tools like MoinMoin
and BeautifulSoup.

Notes: In principle there's no need to use MoinMoin as long as produced
HTML fits following assumptions:

1.  FAQ is stored inside a *div* element with *id* set to *content*.
2.  Questions are inside a heading element which also acts as a
    delimiter between them.
3.  Identifiers are integers.

If it doesn't, you'll need to change code a bit.

