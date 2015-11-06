Title: Lessons from navigation design
Date: 2006-01-31 23:20
Author: markos
Category: General development, UI, Web
Slug: lessons-from-navigation-design

As noted in my previous post, we changed the way image navigation works
on Marela. I already described "philosophical" reason for previous
behavior and in this post I intend to visit other reasons and lessons
learned.

I liked the old behavior because it made every page recognizable and
there were no side effects, no special cases that would require
different handling and make interface bigger. It made under-developed
mathematician in me feel all fuzzy and warm.

What I mean by recognizable is that you could quickly tell where on
Marela you are just by looking at the displayed page. Hence it should be
easy to know how to proceed and what you can do. Very predictable.

Except it didn't matter and nobody cared.

New behavior brought special cases and I'm quite certain we haven't met
all of them yet. Example of one would be navigating through set of
images grouped by a tag and deleting that tag from the current image.
Where does that put you?

The picture obviously can't be a part of that set anymore so its
neighbors can't be from the set either. That's why you fall back to
photo-stream of the author. Except that most people still expect to be
inside of the tag-stream. There wouldn't be much change if we stayed
there, only side-effects would be different. We could only select how to
confuse users, not if.

As it happens, it's not a big deal either. It's confusing at first, but
not for very long, so nobody cares.

What I relearned is that a tight mathematical model without
side-effects, is not necessarily intuitive to human mind. In a way, we
compensate for any small idiosyncrasies in a story our brains write from
what we do. As with any good writing, we have guidelines that make us
write better stories, but at the end it's not they which matter, but the
story itself.

Interface should only help telling it.

