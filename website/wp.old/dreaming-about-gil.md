Title: Dreaming about GIL
Date: 2005-10-11 15:38
Author: markos
Category: Python
Slug: dreaming-about-gil

I've been thinking about Python's global interpreter lock (GIL) again.
Since I'm a glutton for punishment and haven't been crucified in a week,
you get to hear about it too.

Has anybody thought and wrote about avoiding GIL until you need it? What
I mean is creating and using GIL only when you start using code that
might not be thread-safe.

So, what's wrong with this idea?

Things that come to my mind:

-   garbage collector is not thread-safe
-   majority of interesting modules are not thread-safe, so there would
    be little ROI
-   dynamic nature of Python means you can't know in advance if you'll
    need GIL and it would a bitch to fall back when you do
-   ...

I guess it's just a really stupid idea.

