Title: Shipping software frequency
Date: 2008-11-30 20:45
Author: markos
Category: General development
Tags: Programming, shipping, Paul Graham
Slug: shipping-software-frequency
Status: published
Id: 304

<div>
 <p>
  I was
  <a href="http://www.paulgraham.com/artistsship.html" title="Paul's article on cost of checks">
   reading
  </a>
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Paul_Graham" rel="wikipedia" title="Paul Graham">
   Paul Graham
  </a>
  today, who among other things touched on a subject that has been on my mind lately. Software shipping.
 </p>
 <p>
  At Zemanta, we usually don’t ship daily although when needed we do. We try to do a release of new features and bug fixes every 2-3 weeks and on the whole we are succeeding. Still, this is not as often as many startups profess to do and it’s certainly not as often as most of us would like. Even though I probably bear the majority of “blame” for this, I too wish we shipped more often.
 </p>
 <p>
  So why don’t we?
 </p>
 <p>
  There are many factors that define how quickly can something be shipped and even though I don’t think I have an exhaustive list, I find following most important (listed in no particular order):
 </p>
 <ul>
  <li>
   code base
  </li>
  <li>
   shipping changes
  </li>
  <li>
   team
  </li>
  <li>
   tolerance of failure
  </li>
  <li>
   time
  </li>
 </ul>
 <h4>
  Code base
 </h4>
 <p>
  Simply put,
  <strong>
   better code is easier to change
  </strong>
  and evolve with new features without introducing new bugs.
 </p>
 <p>
  Speed of development rarely results in pristine code, so we need to clean things up every now and then, which creates a need to regularly evaluate the quality of our code base and its impact on our ability to deliver.
 </p>
 <h4>
  Shipping changes
 </h4>
 <p>
  <strong>
   Smaller changes are easier to check
  </strong>
  and quicker to develop. More intrusive new code is, harder it is to reliably avoid detrimental effect on already existing code.
 </p>
 <p>
  Fixing, testing and shipping a CSS bug can be done almost instantly. Changing core of the widget usually takes a bit more effort to avoid regressions.
 </p>
 <h4>
  Team
 </h4>
 <p>
  <strong>
   Better developers produce better code
  </strong>
  more quickly.
 </p>
 <p>
  Some testing is always necessary, but there’s a direct connection between code author’s reputation and experience and trust we put in his code.
 </p>
 <h4>
  Tolerance of failure
 </h4>
 <p>
  Tolerance of users and tolerance of system to change is crucial.
 </p>
 <p>
  If you provide a service where failure is not an option, then this should affect at least how deeply tested new release has to be. It’s also important for your system to be able to revert to last working state, but sometimes this is not desired and important glitches need to be fixed as they are encountered.
 </p>
 <h4>
  Time
 </h4>
 <p>
  If your
  <strong>
   schedule
  </strong>
  is
  <strong>
   too tight to fix bugs
  </strong>
  found in new release, it’s
  <strong>
   too tight for release
  </strong>
  .
 </p>
 <p>
  No matter how much you test your software and at Zemanta we do this a lot, new code will introduce new bugs. It will happen that some of them will be too big to wait for next scheduled release and need an immediate fix. If you for some reason can’t afford this, then it may be better not to ship yet.
 </p>
 <h4>
  Pendulum of change
 </h4>
 <p>
  It should be obvious from this list that no factor is set in stone and what might have been a right decision few months ago might not be best one now.
 </p>
 <p>
  A lot has changed in last few months, so the next time we address this topic, I suspect my opinion will be different than last time.
 </p>
</div>
