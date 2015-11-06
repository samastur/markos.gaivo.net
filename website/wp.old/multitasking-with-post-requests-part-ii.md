Title: Multitasking with POST requests - part II
Date: 2005-12-16 13:55
Author: markos
Category: Javascript, UI, Web
Slug: multitasking-with-post-requests-part-ii

Yesterday I wrote about my wish of making background *POST* requests
that don't get accidentally canceled. I wasn't specific enough. You can
create background *POST* requests just fine with *XMLHttpRequest*, but
you can't use such requests for file uploads, which is what I want.

My first try was to post *form* to *iframe* in a different window. This
didn't work because browsers pay attention to source of request.
Activating new request in source window immediately cancels previous
unfinished one.

A better idea was provided by always helpful
[dojo](http://dojotoolkit.org/ "Dojo toolkit") developers. Clone *form*
to progress window and submit it from there. This one works great in
Firefox, but hardly anywhere else. It certainly doesn't work in IE,
since IE is very picky about what you do with nodes created with
*cloneNode* and you can't clone form yourself, since it's not possible
to set the value of file upload elements.

Is this game over for unobtrusive file upload?

Not yet. There are still at least two posibilities, both with downsides,
but one of them definitely works. You can open file upload form in new
window and change that window to progress bar. It works and I use it
occasionally, but it's not nice if you care about accessibility. It's
something users can do now, if they want, by opening upload page in new
tab or window.

The other, yet untried, possible solution would be to avoid cloning.
Just rip the form out from original page, move it to status one and
submit form there. Obvious problems with this one are that users lose
information about what they're uploading and that it can look confusing
if not executed well.

I'll try it anyway and will let you know how it goes.

Update: IE also dislikes ripping and moving.

