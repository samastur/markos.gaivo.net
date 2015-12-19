Title: Usefulness of AJAX
Date: 2006-05-13 07:53
Author: markos
Category: Javascript, Web
Slug: usefulness-of-ajax
Status: published
Id: 164

<div>
 <p>
  At least one participant of our recent
  <a href="ajax-workshop-2.html" title="Previous announcement of AJAX workshop">
   workshop
  </a>
  was under impression that I’m an AJAX advocate. It’s certainly a reasonable and not completely wrong conclusion. However, it seems I failed in limited time available to explain my perspective.
 </p>
 <p>
  As any other useful tool AJAX has its advantages, but it can also create problems when used inappropriately. I won’t dwell on advantages. More than enough has already been said about them. There are three important aspects that still don’t get enough attention and bear repeating.
 </p>
 <p>
  <strong>
   Write unobtrusive and degradable Javascript.
  </strong>
  It’s really not that hard with a bit of planning and it makes things easier in the long run. It’s easier to find, fix and change code when it’s cleanly separated from HTML and CSS. I’d expect everyone learned this lesson by now from PHP. Also, creating HTML version first and then carefully improving it with use of Javascript/AJAX can get us maximum reach without sacrificing flexibility.
 </p>
 <p>
  <strong>
   Pay attention to usability.
  </strong>
  This one is much harder to get right, but if nothing else, you should have in mind at least next three advices. Show a progress indicator when doing something that might take more than a second. Put action trigger as close as possible to the part of a page it will change, so user has a good chance of noticing it and whenever possible assist them with change indicators like
  <a href="http://www.axentric.com/posts/default/7" title="Example of yellow fade-in">
   yellow fade-in
  </a>
  .
 </p>
 <p>
  <strong>
   Accessibility shouldn’t be forgotten either.
  </strong>
  This is probably
  <a href="http://domscripting.com/blog/display/64" title="Accessibility problems with DOM manipulation">
   the hardest problem
  </a>
  to tackle. It’s the most important reason (but not the only one) why I try to use Javascript/AJAX only when benefits of doing so significantly outweigh the problems it might cause.
 </p>
 <p>
  Everyone makes mistakes and I certainly have. I’m sure they weren’t last ones either, but we can all strive for better.
 </p>
</div>
