Title: Javascript enabled spiders
Date: 2006-04-07 17:23
Author: markos
Category: Javascript, Web
Slug: javascript-enabled-spiders

One of more popular javascript scripts I've written is a simple function
that hides an email address from spiders by constructing a mailto link
on page load. So far it has worked quite well.

Lately I started to have my doubts about this approach though. There was
[a series of
articles](http://www.google.com/search?hl=en&q=mozilla+google+spider&btnG=Google+Search)
a while ago about Google's new Mozilla-based spider that I didn't take
too seriously at the time. However, even if not true then, it's still
only a matter of time before a spider like this will show up. The new
found popularity of AJAX/Javascript simply guarantees that, since search
engines can't and won't give up indexing content hidden behind fancy
scripts.

Which means that my script will stop working in not so distant future as
will all email obfuscating scripts out there. If it can be seen by a
human, then it will be seen by a spider. So is there a way to publish my
email address without it becoming public through search engines indexes,
which is where most spammers seem to get our emails?

I could write a robots.txt file, which would exempt my contact page from
being indexed at all. But this is a rather crude approach, since it
means nothing on that page will get indexed. I could move email
information to a separate page to let other contact data get indexed,
but this is hardly any nicer.

What I'd really want is to be able to tell to search engines that only a
part of my document is off limits. I don't think there's currently a way
to do this, but if anyone has an idea how to do it, I'd really like to
hear it.

**Update:** I think all efforts, including mine, to prevent spammers
from collecting published addresses are ultimately doomed. The basic
premise of all such approaches is to cloak an address in a way that
spider can't see it or can't recognize it if it does. By basing spider
on something like Mozilla, there won't be any difference between what
spider sees and what user does. There's a similar problem with
recognition. As spiders gets smarter, as they invariably do, you'll be
getting ever growing overlap between smartest spiders and stupidest
users until it's big enough to be unacceptable.

So we'll either put up contact forms or I hope move to defending our
inboxes with smart spam filters (those who haven't yet).

