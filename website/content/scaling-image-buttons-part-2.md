Title: Scaling image buttons - part 2
Date: 2005-10-01 09:28
Author: markos
Category: Web
Slug: scaling-image-buttons-part-2
Status: published
Id: 34

<html>
 <body>
  <div>
   <p>
    A few days ago I
    <a href="scaling-image-buttons.html" title="Previous post on this topic">
     wrote
    </a>
    about a difficult goal of having a pleasantly looking submit button that is also as accessible as possible. I also had a simple
    <a href="http://markos.gaivo.net/examples/imgbutton/index.html">
     demo
    </a>
    that almost worked, but not quite.
   </p>
   <p>
    I played with it a bit more and actually got it working as far as I imagined I could. You can see the result
    <a href="http://markos.gaivo.net/examples/imgbutton2/index.html" title="New demo">
     here
    </a>
    (just change the size of fonts).
   </p>
   <p>
    What I did is set base font size in all browsers to a known value as described by
    <a href="http://www.clagnut.com/blog/348/" title="link to description on Clagnut blog">
     Richard
    </a>
    . It isn’t really necessary to use 62.5%, but it does reset initial size to 10 pixels, which is a value that is easy to work with.
   </p>
   <p>
    Then I just set height of an image button to its real size, but using em’s instead of pixels. In my case that’s 25 px or 2.5 em’s.  I also set font-size of input button to 1 em, which for some reason is needed in browsers other than Safari, to enforce 10px size for fonts and 25px height for the button.
   </p>
   <p>
    That’s it. Button is now resizable and has its original size by default.
   </p>
   <p>
    Solution, which is entirely CSS based, is not perfect and I don’t believe it will ever be. Or at least not using incarnations of XHTML and CSS that we have now.
   </p>
   <p>
    As can be clearly seen on the demo, it all comes down to a choice between better legibility of scaled
    <em>
     type=submit
    </em>
    buttons and more flexible design of
    <em>
     type=image
    </em>
    buttons.
   </p>
   <p>
    I imagine I could do better with multiple sizes of an image for each button and using javascript swapping, but it wouldn’t work where javascript is missing and multiple images would significantly add to production costs.
   </p>
   <p>
    Personally, I think web sites should have a design readable for vast majority of its readers even without text scaling and this trick can be good enough for the rest. However, at the same time I don’t expect to use it often.
   </p>
  </div>
 </body>
</html>