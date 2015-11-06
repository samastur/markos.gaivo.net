Title: My OpenData hackday experience
Date: 2011-10-02 20:48
Author: markos
Category: OpenData, Web
Slug: my-opendata-hackday-experience

I attended OpenData hackday previous weekend where we tried to create a
website inspired by
[theyworkforyou.com](http://www.theyworkforyou.com/). We didn't quite
achieve our goal, but a lot was done by everyone and we had fun. At
least I did and I am certain we will release the first version
soon (before the end of October, mark my words).

Not releasing our website still bothered me and I've been thinking about
it since, contemplating what we did right and what I did wrong.﻿ I hope
this rumination can be of use to others who may be thinking about
organizing or attending such an event. If you already have and have some
tips to share or simply disagree with something I said, then please
leave a comment at the bottom.

Planning
--------

It is [important to
finish](http://neoacademic.com/2011/09/22/unfolding-the-ikea-effect-why-we-love-the-things-we-build/ "IKEA effect")
something. Having something at least a bit useful or fun gives everyone
involved a sense of achievement and provides a better motivation for
further work. To avoid problems with too many ideas started and none
finished, we suggested to work only on ideas that have at least 3
volunteers. We also created a wiki where everyone could add their idea
and volunteer for projects they liked.

I think strongly suggesting at least 3 volunteers per project idea had
an effect of ending up with just one idea. Not our intention, nor
necessarily a problem, but it's worth keeping in mind. We all tend to
take the path of least resistance when not really committed to an idea
and joining is easier than finding an idea AND people to help.

However if you do come up with an idea, then here are a few things you
might keep in mind:

**Self-sustaining projects win.** Even with best intentions you will
probably run out of time for your project eventually. So projects that
can be finished or which can be run by a community with few development
and administration resources are less likely to end in failure.

**Strip it to bare essentials**, but keep a list of things you'd like to
add if you had more time or help. I knew that we couldn't build
theyworkforyou in a day, but my planned version was still too grandiose.
I should stop only when removing anything would reduce it to useless.
Another reason for this is that I also often overestimate my free
time -- important for projects that will continue after hackday.

**Check if you have data you need**. First check for completeness, since
missing parts might significantly affect feasibility of your project
(especially if they are needed for a stripped down version). If you plan
to scrap data from a public source (instead of using API or something
you already have), then scrape it well before the event. Site may not be
available when you need it or, as it was our experience, it can be
frustratingly slow. Perception of speed is relative, but downloads can
always go slower than even the pessimist in you would make you
believe. I learned on hackday that I was planning to use
a non-existing data.

**Check the quality of your data,** don't only glance at it. Spend some
time getting to know it and think about how you will clean it up. I knew
our data was in an atrocious state, but I was still widely optimistic.
Luckily [Tomaž](http://www.tablix.org/~avian/blog/ "Tomaž's blog") is a
seasoned data wrangler that can deal with crap input.

**Have a detailed TODO list**. Not only will it give you a better
picture of scope, it also makes it easier to divide work to unexpected
volunteers. Mark what is necessary and what would be nice to have. Also
pay attention to skills needed for finishing each
task. [Gašper](http://www.kiberpipa.org/~hruske/blog/ "Gašper's blog")
put a lot of effort into our to-do list and I haven't. We could
certainly achieve more if it was clearer what needs to be done and if I
could delegate better.

**Have a "roadmap"**. Not every task can be done in parallel so identify
and mark task dependencies. It may also be quicker if multiple
developers extract different information from the same piece of data
then for everyone to wait on one person to extract all.

**Prepare hosting beforehand.** If you plan to host a website, then set
up *and test* at least essential parts before the event. Day passes too
quickly even if you don't waste time setting up the environment.

**Ditto for development environment.** How many people do you think will
or can work on project(s)? Are they all familiar with tools you intend
to use? Do you have adequate resources?

I expected time constraints to prevent us from auditing code for
exploits, so we opted for bitbucket which gives you private repositories
for free. But we had to juggle around its limitation of 5 developers per
repository and choice of mercurial as DVCS. Having them private turned
out to be unimportant.

So pick tools most are comfortable with and set up your own server
(before the event of course) if publicly available options might not be
good enough. You want everyone to start contributing as soon and as
easily as possible.

Running event
-------------

Our hackday was as open as it gets. We used
[Eventbrite](http://www.eventbrite.com/) for registration, but didn't
enforce it so everyone who came was welcome no matter how long they
stayed. It's fantastic when people show up offering free help and it
would be plain crazy to turn them away. There is always something they
can do no matter what their skill set.

Here are a few tips I wish I followed:

**Lead.** Self-organization is great, but the likelihood of
misunderstandings and duplication of effort quickly increases with the
size of a group. If you have dependencies in your project roadmap, then
it's also important that showstopper tasks are done before those that
rely on them. That's why someone usually has to lead development and if
a project doesn't have that someone, you either have to find or be him.

**Talk to everyone.** Find out what they are doing or what they would
like to do. Find out also how long they intend to stay, since that might
limit the choice of suitable tasks. Talking is pretty much the only
reliable way to find these things out.

Even better might be to have short group meetings throughout the day for
everyone to catch up and I regret I didn't think of this then. This
however doesn't absolve you from talking, especially if contributors are
free to come and go whenever they please as they might have not been
around yet the last time you were catching up.

**Delegate.** As much as possible to as many as possible. Don't play a
hero trying to do too much. You can always pick another task later or
help someone with theirs if you finish too soon.

In fact it's probably better to help less experienced members with their
tasks than doing whatever you are doing. Having a healthy contributing
community is what makes or breaks voluntary projects so nurturing one is
even more important than finishing the first version. This goes even
more so for projects that can't ever be really finished.

Morning after
-------------

Hackday is over and everyone has gone for a beer. Hopefully everyone is
happy with results, but ambitious projects almost by definition can't be
finished in a day and the next morning it was amazing to see people
continuing hacking where they left off the day before.

Not every hacking community is as engaged as ours. However we all have
more or less the same needs. It's nice to hear our work was appreciated
and even better that it mattered. We like to help if we are not alone
and if it is clear how. Thus I found email sent by Gašper a few days
later a pitch perfect post-hackday message. He first thanked everyone
involved, then listed what each and all together achieved and ended by
what he intends to do next.

So, this is it. A long, but not exhaustive run through my experience of
our last hackday which also took way longer to write than I expected.
It's time to go back to hacking!

