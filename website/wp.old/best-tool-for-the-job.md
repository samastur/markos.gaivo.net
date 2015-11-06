Title: Best tool for the job
Date: 2005-09-28 20:57
Author: markos
Category: Python
Slug: best-tool-for-the-job

Sometimes, I really am an idiot. A couple of years ago I was involved in
development of a front-end Zope application for a major Slovenian ISP
with more than 100 000 users. No matter what we did, Zope just wasn't
fast. In fact it was so slow, it was soon abandoned for one more
suitable solution.

The failure of our project was largely my fault, because I haven't made
sure Zope was a good fit for what we wanted. I learned a lot, but it
also left a bitter aftertaste and a question, why are people using it?

The obvious answer is of course, because it DOES fit their needs. It's
just that they are not building a site or an application that needs to
handle few hundred simultaneous requests. They handle a few at most, so
Zope or Plone or what-have-you is more than speedy enough and it's their
features that count.

It really took me awhile to grasp this and it only became really clear
this week, after reading a little [Plone
benchmark](http://www.larsen-b.com/Article/217.html) and having a
discussion with
[Sebastjan](http://seba.antiwisdom.com "Sebastjan's blog") about
slowness of Slovenian sites.

On a positive note, we generate pages in less than 6 ms now and can
reduce it even further, if needed.

