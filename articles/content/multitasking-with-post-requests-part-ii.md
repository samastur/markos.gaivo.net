Title: Multitasking with POST requests - part II
Date: 2005-12-16 13:55
Author: markos
Category: Javascript, UI, Web
Slug: multitasking-with-post-requests-part-ii
Status: published
Id: 96

<div>
 <p>
  Yesterday I wrote about my wish of making background
  <em>
   POST
  </em>
  requests that don’t get accidentally canceled. I wasn’t specific enough. You can create background
  <em>
   POST
  </em>
  requests just fine with
  <em>
   XMLHttpRequest
  </em>
  , but you can’t use such requests for file uploads, which is what I want.
 </p>
 <p>
  My first try was to post
  <em>
   form
  </em>
  to
  <em>
   iframe
  </em>
  in a different window. This didn’t work because browsers pay attention to source of request. Activating new request in source window immediately cancels previous unfinished one.
 </p>
 <p>
  A better idea was provided by always helpful
  <a href="http://dojotoolkit.org/" title="Dojo toolkit">
   dojo
  </a>
  developers. Clone
  <em>
   form
  </em>
  to progress window and submit it from there. This one works great in Firefox, but hardly anywhere else. It certainly doesn’t work in IE, since IE is very picky about what you do with nodes created with
  <em>
   cloneNode
  </em>
  and you can’t clone form yourself, since it’s not possible to set the value of file upload elements.
 </p>
 <p>
  Is this game over for unobtrusive file upload?
 </p>
 <p>
  Not yet. There are still at least two posibilities, both with downsides, but one of them definitely works. You can open file upload form in new window and change that window to progress bar. It works and I use it occasionally, but it’s not nice if you care about accessibility. It’s something users can do now, if they want, by opening upload page in new tab or window.
 </p>
 <p>
  The other, yet untried, possible solution would be to avoid cloning. Just rip the form out from original page, move it to status one and submit form there. Obvious problems with this one are that users lose information about what they’re uploading and that it can look confusing if not executed well.
 </p>
 <p>
  I’ll try it anyway and will let you know how it goes.
 </p>
 <p>
  Update: IE also dislikes ripping and moving.
 </p>
</div>
