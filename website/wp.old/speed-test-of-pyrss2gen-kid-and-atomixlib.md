Title: Speed test of PyRSS2Gen, kid and atomixlib
Date: 2005-11-05 02:04
Author: markos
Category: Python, Web
Slug: speed-test-of-pyrss2gen-kid-and-atomixlib

I've spent this evening building RSS2 and Atom feeds with
[PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html),
[kid](http://kid.lesscode.org/index.html) and
[atomixlib](http://www.defuze.org/oss/atomixlib/), as
[proposed](http://markos.gaivo.net/blog/?p=55) by helpful people few
days ago.

We'd like to add feeds promiscuously to our service (right now we have
exactly one). But before we can decide how to tackle this, we need to
know how fast we can generate a feed on average.

**DISCLAIMER: I tried to generate feeds with same data using what seemed
a reasonable python code to do so, but I didn't try to save every
millisecond as I only cared about crude speed approximations. I have no
problem believing that someone else might get completely different
results. No serious statistical analysis has been made and rigorous
scientific approach has been almost completely absent. Better make your
own tests, if speed (or anything else really) is important to you. But
if dubious numbers delight you, then please continue.**

So, here are my results. Time to generate a feed with 10 entries on 1GHz
G4 Powerbook:

-   with PyRSS2Gen somewhere around 70ms
-   with atomixlib around 120-140ms
-   and with kid around 30-35ms

In other words, you can generate between 8 and 30 feeds per second on my
notebook and (I guess) 2-3x as many on a modern server. This is more
than enough for most cases, but I'm afraid it probably won't be enough
for us. Which means either producing feeds by gluing strings together or
having a more intelligent approach than building a new one on every
request.

As a side note, I found all three packages easy to work with.  
<em>  
Update: Sylvain has released atomixlib 0.3 which makes it even easier
to create atom feeds and brings also significant speed improvements. On
my computer it takes now around 60-65ms to build a feed.

Another update: I made a couple of quick tests with mixed results on
fairly new Opteron server. PyRSS2Gen was actually slower with 80-85ms
and I have no idea why. kid was blazing fast with times between 8 and
9ms. Definitely good enough.

But I couldn't get atomixlib to work, because 4Suite failed to build, so
it will have to wait until I can figure out why it chokes on a perfectly
legitimate XSLT.

Update 3: 4Suite has been promptly fixed (thanks!) and atomixlib 0.3
takes now 18-19ms. I believe this is an excellent time.</em>

