Title: Triggering a server request on onunload event
Date: 2008-03-26 16:32
Author: markos
Category: Javascript, Web
Slug: triggering-a-server-request-on-onunload-event
Status: published
Id: 250

<div>
 <p>
  A while ago I tried to trigger an AJAX call to server in
  <em>
   onunload
  </em>
  handler and failed miserably. It simply didn’t work in major browsers and I filled the idea under can’t-be-done.
 </p>
 <p>
  I recently got another reason to revisit this problem and came up with a new-old idea. Since in my case I don’t care about server response, I don’t actually need XMLHttpRequest. Any technique that triggers a call to server is good enough, so why not try creating an image and setting its
  <em>
   url
  </em>
  attribute to appropriate value.
 </p>
 <p>
  It turns out that this works almost everywhere. It worked pretty flawlessly in Firefox, Opera and Internet Explorer, but it doesn’t work in Safari and Konqueror, which makes me think that KHTML/Webkit family of browsers in general don’t support it.
 </p>
 <p>
  This is not its only limitation. Technique obviously works only for GET calls, which is frowned upon and generally dangerous for actions that change state. I also suspect it works less well on slower computers or networks so you might need to delay event handler ending by buying some time with needless processing after you’ve set
  <em>
   url
  </em>
  attribute.
 </p>
 <p>
  Still, it might be another useful hack to have if you can live with its limitations.
 </p>
</div>
