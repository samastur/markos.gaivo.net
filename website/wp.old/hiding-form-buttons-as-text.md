Title: Hiding form buttons as text
Date: 2005-12-02 15:49
Author: markos
Category: Spletne urice, UI, Web
Slug: hiding-form-buttons-as-text

I love going to our weekly web talks not so much for the talks
themselves (although they are great), but conversations you get to have
there. A part of a recent one rendered from memory and shortened for
readers pleasure:

> **Fry:** Those delete strings of yours should really be post requests.
> [GA's](http://webaccelerator.google.com/ "Link to web accelerator that shouldn't be used")
> pre-fetching might destroy user's data.  
>  **Me:** \<beeeeep\> Google. RFC says should not must.  
>  **Fry:** Well, since it also says multiple GET requests should yield
> same result, it really is a must for delete.  
>  **Me** (not ready to give up): True, but so many form buttons will
> look like crap.  
>  **Fry:** Well, you can hide them by removing border, setting
> background-color to background and fixing font size to 1 em.  
>  **Me:** Uhm, this might work, but probably doesn't, because browsers
> use controls from operating system.  
>  **Fry:** Well, try it.

I may be stubborn, but I'm not a complete moron. So I did and here's
[the result](http://markos.gaivo.net/examples/hidebutton.html "Demo").

As can be seen, it works beautifully in Firefox (1.0+) and Opera 8 (I
share my visitors indifference to earlier versions). It doesn't work in
Safari at all, but since its buttons are not obnoxiously ugly, I can
live with that.

However, it has unseemly big padding in Internet Explorer, which is the
real deal-breaker for now.

I think demo's style sheet is pretty self explanatory, but here's what I
did by mostly following Fry's instructions:

-   set border to 0
-   same for padding and margin
-   set background-color of the button to the same value as background
    of the document
-   did the same for color of text
-   set the size of button text to 1 em so it's displayed in right size
    in every browser
-   set cursor to pointer, since it's not done automatically for buttons

[Fry](http://www.friedcellcollective.net/ "Fry's web home") was also
correct that bold and italics work and underline doesn't, but you can
simulate later with border-bottom. Except in IE of course, on account of
padding.

There's another shortcoming to consider. If background is an image or a
color gradient instead of a solid color, this trick won't work.

So, any ideas about what to do with IE?

