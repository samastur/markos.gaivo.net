Title: Error logging and failed authentication attempts
Date: 2007-04-06 20:01
Author: markos
Category: General development, Javascript, Python, Web
Slug: error-logging-and-failed-authentication-attempts
Status: published
Id: 221

<div>
 <p>
  People make mistakes and that’s why we log every error that happens on
  <a href="http://www.marela.si" title="Photo-sharing website">
   Marela
  </a>
  pages or its API. I imagine most services that care about quality do more or less the same, since it is a great way to find yet undiscovered bugs.
 </p>
 <p>
  There’s an additional benefit when it comes to an API. You can also get an insight in what developers would like to do and how they go about doing it. With a bit of care you may even correct badly designed calls before they get too widely adopted.
 </p>
 <p>
  What may not be as obvious is that not all calls are equal and some of them probably need more careful reporting. A good example would be failed authentication attempts.
 </p>
 <p>
  Marela is one of services supported by
  <a href="https://addons.mozilla.org/en-US/firefox/addon/3945">
   Fotofox
  </a>
  , a popular photo sharing Firefox add-on, which is great. However support for multiple different services invariably leads to a problem, where users send their usernames and passwords to the wrong site. We weren’t prepared for this and our first reaction was to simply religiously delete all such reports from our logs to prevent any possibility of an abuse.
 </p>
 <p>
  I think this was wrong, so we changed it. Probably the best way is to record failed authentication attempts the way Unix systems do, by logging just username that was used in an attempt and its success, while ignoring provided password completely. This way we still obtain valuable information while protecting data that we clearly shouldn’t have access to.
 </p>
 <p>
  This is of course just an example. My main point is that a sufficiently large API will have calls with different privacy needs and API designers should think carefully about what needs to be recorded in service logs and what mustn’t.
 </p>
</div>
