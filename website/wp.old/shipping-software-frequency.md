Title: Shipping software frequency
Date: 2008-11-30 20:45
Author: markos
Category: General development
Slug: shipping-software-frequency

I was
[reading](http://www.paulgraham.com/artistsship.html "Paul's article on cost of checks")
[Paul Graham](http://en.wikipedia.org/wiki/Paul_Graham "Paul Graham")
today, who among other things touched on a subject that has been on my
mind lately. Software shipping.

At Zemanta, we usually don't ship daily although when needed we do. We
try to do a release of new features and bug fixes every 2-3 weeks and on
the whole we are succeeding. Still, this is not as often as many
startups profess to do and it's certainly not as often as most of us
would like. Even though I probably bear the majority of "blame" for
this, I too wish we shipped more often.

So why don't we?

There are many factors that define how quickly can something be shipped
and even though I don't think I have an exhaustive list, I find
following most important (listed in no particular order):

-   code base
-   shipping changes
-   team
-   tolerance of failure
-   time

#### Code base

Simply put, **better code is easier to change** and evolve with new
features without introducing new bugs.

Speed of development rarely results in pristine code, so we need to
clean things up every now and then, which creates a need to regularly
evaluate the quality of our code base and its impact on our ability to
deliver.

#### Shipping changes

**Smaller changes are easier to check** and quicker to develop. More
intrusive new code is, harder it is to reliably avoid detrimental effect
on already existing code.

Fixing, testing and shipping a CSS bug can be done almost instantly.
Changing core of the widget usually takes a bit more effort to avoid
regressions.

#### Team

**Better developers produce better code** more quickly.

Some testing is always necessary, but there's a direct connection
between code author's reputation and experience and trust we put in his
code.

#### Tolerance of failure

Tolerance of users and tolerance of system to change is crucial.

If you provide a service where failure is not an option, then this
should affect at least how deeply tested new release has to be. It's
also important for your system to be able to revert to last working
state, but sometimes this is not desired and important glitches need to
be fixed as they are encountered.

#### Time

If your **schedule** is **too tight to fix bugs** found in new release,
it's **too tight for release**.

No matter how much you test your software and at Zemanta we do this a
lot, new code will introduce new bugs. It will happen that some of them
will be too big to wait for next scheduled release and need an immediate
fix. If you for some reason can't afford this, then it may be better not
to ship yet.

#### Pendulum of change

It should be obvious from this list that no factor is set in stone and
what might have been a right decision few months ago might not be best
one now.

A lot has changed in last few months, so the next time we address this
topic, I suspect my opinion will be different than last time.

<div class="zemanta-pixie">

[![Reblog this post [with
Zemanta]](http://img.zemanta.com/reblog_e.png?x-id=81d6b87c-78c1-4e73-877d-43a1db60b537)](http://reblog.zemanta.com/zemified/81d6b87c-78c1-4e73-877d-43a1db60b537/ "Zemified by Zemanta")

</div>
