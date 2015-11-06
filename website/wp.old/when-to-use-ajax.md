Title: When to use AJAX
Date: 2005-11-11 19:10
Author: markos
Category: Javascript, Spletne urice, Web
Slug: when-to-use-ajax

Wednesday's conversation with [Fry](http://www.friedcellcollective.net/)
provoked me to think more about where and when to use AJAX. I thought
I've got it figured it out, but I've discovered that my opinions don't
really match my behavior and I find this a problem.

AJAX rage of 2005 hasn't brought many articles exploring benefits and
downsides to AJAX. There were few, even very good ones, but I'd like to
see more of them and less articles describing latest gimmick or service
which would probably be overlooked if it didn't use an AJAX trick or
two.

I had a dentist appointment today, something I'm sure everyone looks
forward to, which at least provided me with ample time to think about
this. My basic premise was that we should use technology that already
works and use AJAX to build on top of that.

Since basic web model has been around for a long time, is well
understood and mostly works, I tried to look at places where it doesn't
or at least not as it should and came to a short list of possible
criteria for choosing when to apply AJAX:

-   **Browsers ought to support this, but mostly can't or don't.**
    Example: autosave support for textarea, which is the most requested
    feature among my friends.
-   **Browsers support it, but badly.** Example: progress bar for
    uploads. I don't know why you can get a usable dialog for downloads,
    but you're out of luck if you want to upload.
-   **Connection problems (narrow bandwidth or high latency).** If this
    is a known, but otherwise unsolvable problem, AJAX can be used to
    reduce ammount and frequency of traffic.

Have I forgot anything else?

I don't think these are only valid scenarios for AJAX use, but we did
discover that fast serving of well designed pages greatly reduces the
need for AJAX.

