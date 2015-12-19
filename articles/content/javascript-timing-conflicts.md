Title: Javascript timing conflicts
Date: 2005-09-17 19:01
Author: markos
Category: Javascript
Slug: javascript-timing-conflicts
Status: published
Id: 25

<div>
 <p>
  Play with fire and you’ll get burned.
 </p>
 <p>
  I’ve just spent two days hunting a bug that just didn’t make sense. No matter what I did, there was at least one browser, which didn’t want to behave properly and it was driving me nuts.
 </p>
 <p>
  Finally I gave up and decided there’s nothing wrong with my code and the fault must be with the browser. And so it was, up to a point. Or not, depending on your point of view.
 </p>
 <p>
  The problem was a timing conflict resulting from a use of
  <a href="framestack-technique-and-accessibility.html" title="Description of technique">
   framestack technique
  </a>
  and the way modern browsers work. Browsers don’t wait for the whole page with its data to load, before they display it to users. They display as reasonable presentation of received data as possible while they are trying to load the rest. For example, onload handler set to body tag is triggered when body of HTML document has loaded, but possibly before images and other external resources have. When they do, page layout might change somewhat and if your script is reading and using layout data in the meantime, it’s quite likely it’ll end up using wrong values.
 </p>
 <p>
  The easiest (and right) way to fix this is to start javascript with
  <em>
   window.onload
  </em>
  , which is triggered when everything has loaded. This might be a problem, if you’re using something like framestack to avoid reloading page on subsequent visits, but at least in my case I’ve decided that the cleanest and easiest solution was to use window.onload and just force reload of problematic page on each visit.
 </p>
 <p>
  It’s also possible to get in similar timing conflicts by using
  <em>
   innerHTML
  </em>
  method. If you try to stuck a large piece of HTML inside a page using innerHTML call, you may encounter an unwelcome surprise. Reason for this is that at least some browsers don’t wait to parse and insert data in DOM before they proceed to the next statement. Injection delay is usually barely noticeable, but big enough for statements that manipulate inserted data to fail, if they are in close proximity to innerHTML call.
 </p>
 <p>
  You can’t necessarily avoid innerHTML problems with window.onload, but you can by using (more cumbersome) DOM methods.
 </p>
 <p>
  It still annoys me though that I knew all of this and wasted two days just because I didn’t think of it.
 </p>
</div>
