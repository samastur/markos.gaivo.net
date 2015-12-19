Title: Leaving App Engine - for now
Date: 2008-08-30 21:50
Author: markos
Category: Python, Web
Tags: Google, Python, Google App Engine, Django, App Engine
Slug: leaving-app-engine-for-now
Status: published
Id: 287

<div>
 <p>
  Jonathan
  <a href="http://spyced.blogspot.com/2008/08/app-engine-conclusions.html#">
   wrote
  </a>
  his thoughts about
  <a class="zem_slink" href="http://appengine.google.com" rel="homepage" title="Google App Engine">
   App Engine
  </a>
  . They are well worth a read if you are thinking about using it, but haven’t so far. I used App Engine sporadically for a couple of months on a project of mine, but I finally gave up and ended porting my code to pure
  <a class="zem_slink" href="http://www.djangoproject.com" rel="homepage" title="Django (web framework)">
   Django
  </a>
  , which admittedly wasn’t too hard to do at this point in time.
 </p>
 <p>
  Some of my reasons match Jonathan’s. There were too many rough edges to feel really productive and too much time was wasted on trying to find out if problem lies in poor documentation, incomplete implementation or stupid programmer. I probably will never get answers to questions like how can a simple Django view that doesn’t do anything beside rendering a static template, consume above expected amount of CPU and risk triggering quota blockage, but right now I really don’t care anymore.
 </p>
 <p>
  Integrating
  <a class="zem_slink" href="http://www.crunchbase.com/company/google" rel="crunchbase" title="Google">
   Google
  </a>
  accounts is indeed easy, but it is also very shallow to the point of being practically useless.  You basically can only rely on fact that reference to a particular user won’t change. Anything else you may think you know (like an email address), can’t be relied upon. You can’t create an account and you can’t even control login form of your service. In essence you don’t have your own users, you can just offer a service to Google’s.
 </p>
 <p>
  For me this was one of two major reasons for my decision. Every person who would need an account to use what I am building would need to agree to Google’s
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Terms_of_service" rel="wikipedia" title="Terms of service">
   TOS
  </a>
  agreement which defines many things, among others the highest level of privacy I can offer.
 </p>
 <p>
  The other reason was that current limitations of App Engine really lead you to rely heavily on provided APIs, which may be similar to stuff out there (like Django), but aren’t anywhere close to being a drop-in replacement. This can be — depending on application you’re writing — a heavy investement in a platform you don’t control a bit.
 </p>
 <p>
  Put more profanely, you are a Google’s bitch.
 </p>
 <p>
  Having said all this, I do think App Engine is a very valuable service. If you want to write a mini-app, a web tool like
  <a href="http://simonwillison.net/" title="Simon's homepage">
   Simon
  </a>
  <a href="http://simonwillison.net/2008/Jul/29/jsonhead/" title="Post about json-head service">
   does
  </a>
  , then App Engine is brilliant. You can do this easily with little deployment and zero administration hassle. In fact I can’t think of any other service better suited to this task.
 </p>
 <p>
  I’m sure this is not the only scenario in which App Engine makes sense and there are others I haven’t named or thought of. Issues, like accounts, can with some effort be solved now. But App Engine also isn’t (yet) what some of us were hoping for and it’s prudent to really think through what you want, what you need and what App Engine actually offers.
 </p>
 <div class="zemanta-pixie">
  <a class="zemanta-pixie-a" href="http://reblog.zemanta.com/zemified/28ddae75-72ba-4a45-892e-7841f893395b/" title="Zemified by Zemanta">
   <img alt="Reblog this post [with Zemanta]" class="zemanta-pixie-img" src="http://img.zemanta.com/reblog_e.png?x-id=28ddae75-72ba-4a45-892e-7841f893395b" style="border: medium none; float: right;"/>
  </a>
 </div>
</div>
