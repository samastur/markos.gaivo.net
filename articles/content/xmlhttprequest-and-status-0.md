Title: XMLHttpRequest and status 0
Date: 2006-01-19 19:23
Author: markos
Category: Javascript
Slug: xmlhttprequest-and-status-0
Status: published
Id: 109

<div>
 <p>
  Have you ever encountered a problem with XMLHttpRequest (XHR), where its handler couldn’t read request status or the status was set to 0?
 </p>
 <p>
  Well, I did, a few days ago.
 </p>
 <p>
  It took me a while to find the cause of this problem and in my case it was form submission. It’s stupid to use AJAX to submit a form, but nevertheless it’s what I’m doing for dubious reasons that I’ll probably be ashamed of in a few months or years. And it used to work fine, until I changed submit buttons from
  <em>
   type=”button”
  </em>
  to
  <em>
   type=”image”
  </em>
  .
 </p>
 <p>
  First type needs javascript to do anything worthwhile, while second type submits form when pressed, which I somehow missed. So, when I thought I was sending only a normal XHR request, I was actually also submitting my form which lead to described strange behavior.
 </p>
 <p>
  I have no idea why, since XHR state change handler shouldn’t be triggered by other requests, but it was and it was fixed by simply canceling form submission in image button
  <em>
   onclick
  </em>
  handler.
 </p>
 <p>
  If you ever encounter this problem, check your forms and their submit buttons. It’s very likely that solution is hiding there.
 </p>
</div>
