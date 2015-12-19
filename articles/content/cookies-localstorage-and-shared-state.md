Title: Cookies, localStorage and shared state
Date: 2011-12-19 17:05
Author: markos
Category: General development, Web
Tags: cookies, Firefox, chrome, shared state, stylesheet, localstorage, html5, http, css, browser
Slug: cookies-localstorage-and-shared-state
Status: published
Id: 898

<div>
 <p>
  I’ve been fiddling with my website again, changing theme switching from somewhat dumb class based system to a more proper one using alternate style sheets. I learned that picking a style sheet in browser applies those changes only to currently open page, so for style sheet selection to persevere it needs a bit of Javascript support from website owner. Personally I find this just stupid.
 </p>
 <p>
  The easiest way to remember visitor’s preference is to store it in his browser. Cookies used to be popular before they were deemed evil, but they have other limitations as well. Hence popular switch to HTML5 in-browser storage technologies like
  <a href="http://www.w3.org/TR/webstorage/">
   localStorage
  </a>
  .
 </p>
 <p>
  I think there is one important difference between cookies and tools like localStorage that is often overlooked and it’s not the size of data that can be stored. Cookies are sent with
  <em>
   each page request
  </em>
  while data stored elsewhere isn’t. Changing them on any side will automatically share state with the other. I use localStorage in my theme switcher because I think server doesn’t need and should not know which theme is used. But for storing shared data, especially one that expires, cookies remain a reasonable if not best choice.
 </p>
 <p>
  None of this is exactly new, but I think it is worth remembering. In other news I dislike interface limitations of Chrome more and more (exceptions are Developer Tools and extensions framework).
 </p>
</div>
