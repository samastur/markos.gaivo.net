Title: Scaling image buttons - part 2
Date: 2005-10-01 09:28
Author: markos
Category: Web
Slug: scaling-image-buttons-part-2

A few days ago I
[wrote](http://markos.gaivo.net/blog/?p=31 "Previous post on this topic")
about a difficult goal of having a pleasantly looking submit button that
is also as accessible as possible. I also had a simple
[demo](http://markos.gaivo.net/examples/imgbutton/index.html) that
almost worked, but not quite.

I played with it a bit more and actually got it working as far as I
imagined I could. You can see the result
[here](http://markos.gaivo.net/examples/imgbutton2/index.html "New demo")
(just change the size of fonts).

What I did is set base font size in all browsers to a known value as
described by
[Richard](http://www.clagnut.com/blog/348/ "link to description on Clagnut blog").
It isn't really necessary to use 62.5%, but it does reset initial size
to 10 pixels, which is a value that is easy to work with.

Then I just set height of an image button to its real size, but using
em's instead of pixels. In my case that's 25 px or 2.5 em's. I also set
font-size of input button to 1 em, which for some reason is needed in
browsers other than Safari, to enforce 10px size for fonts and 25px
height for the button.

That's it. Button is now resizable and has its original size by default.

Solution, which is entirely CSS based, is not perfect and I don't
believe it will ever be. Or at least not using incarnations of XHTML and
CSS that we have now.

As can be clearly seen on the demo, it all comes down to a choice
between better legibility of scaled *type=submit* buttons and more
flexible design of *type=image* buttons.

I imagine I could do better with multiple sizes of an image for each
button and using javascript swapping, but it wouldn't work where
javascript is missing and multiple images would significantly add to
production costs.

Personally, I think web sites should have a design readable for vast
majority of its readers even without text scaling and this trick can be
good enough for the rest. However, at the same time I don't expect to
use it often.

