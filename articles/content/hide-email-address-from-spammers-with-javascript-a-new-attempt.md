Title: Hide email address from spammers with Javascript - a new attempt
Date: 2006-05-08 12:23
Author: markos
Category: Javascript, Web
Slug: hide-email-address-from-spammers-with-javascript-a-new-attempt
Status: published
Id: 162

<div>
 <p>
  In true Don Quixote fashion, I made a new attempt to make email harvesting more difficult. It won’t work forever, but it will work longer than
  <a href="hide-email-address-from-spammers-with-javascript.html">
   previous
  </a>
  one, which hasn’t fail yet either.
 </p>
 <p>
  This time I use a bit different approach. Instead of replacing spam-proof, but not directly usable email addresses with mail links on page load, I create mail links on page load, but populate them when mouse moves over them. This way they are still perfectly usable, but less likely to be abused. They are also less friendly, since you can’t see email address until you move your pointer over it. But that was the point, to prevent javascript enabled scrappers.
 </p>
 <p>
  You can download
  <a href="http://markos.gaivo.net/blog/code/mangle2.js">
   new version
  </a>
  or check a
  <a href="http://markos.gaivo.net/examples/mangle2.html">
   demonstration
  </a>
  on alternative version of my homepage.
 </p>
</div>
