Title: Tags
Date: 2006-02-08 18:01
Author: markos
Category: General development, UI, Web
Slug: tags-use

Tags are increasingly popular and rightfully so. I've built my share of
applications with their own taxonomies and I'm certain they simply don't
work. They sort of work if they were built for specialized needs and are
used only by trained, disciplined people with excellent organizational
skills.

Which means almost never.

Tags (aka folksonomies) are messy. There's no real system, any bozo can
attach whatever it wants and you'd be a fool to blindly trust any
specific tag. They are the worst possible system apart from everything
else we tried so far.

That's why we decided to implement them in Marela. Language used on
Marela is Slovene and that led to slightly different design that
commonly found elsewhere.

We decided to treat multiple words separated with spaces as one tag and
use commas as a delimiters between different tags. First reason for this
is that tagging something like *New Zealand* becomes more natural. The
other was that in Slovene compound words like handbag are very often
separate words. For example, handbag would be *ro??na torbica*.

Another problem, which we haven't tackled yet, but probably will have
to, is that Slovene is [a complicated
language](http://en.wikipedia.org/wiki/Slovene_grammar "Short description on Wikipedia")
in ways that make tagging a nasty problem. There are six cases, but
nominative is usually used. Still three different grammatical numbers
(singular, dual and plural) together with three different genders
(masculine, feminine and neutral) leave multiple options for the same
thing. If you were looking for *blue* objects, you'd need to search at
least for tags *modra*, *modro*, *modri* and *modre*. Right now you have
to do this manually.

And then there are problems that plaque other tagging systems as well.
Most common of them are misspelled words, like *Wein* instead of *Wien*
for Vienna.

All these lead to a fairly flat tag space with a ratio of 5.6 between
all tags and unique ones. I'm not sure how it would change if we treated
spaces differently or even what is a common ratio for other languages
and other applications. I'm guessing it wouldn't change the ratio too
much because of noun cases, but it remains to be investigated.

So, why does it matter?

Well, that's a matter for another post, which I'll probably write
tomorrow.

