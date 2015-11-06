Title: Speeding up Levenshtein
Date: 2006-11-10 02:17
Author: markos
Category: General development, Python, Web
Slug: speeding-up-levenshtein

[Simon](http://markos.gaivo.net/blog/?p=210#postcomment) proposes using
a dictionary to match mistyped URLs with real ones. I'd probably like
the idea better if I actually understood it. Still using
[Levenshtein](http://en.wikipedia.org/wiki/Levenshtein_distance "description of the algorithm")
can be a bit easier than using a spell checker responsively.

Easier, but slow. I used existing
[implementation](http://hetland.org/python/distance.py "python implementation")
by Magnus Lie Hetland and made a test with 245 blog titles using a
simple
[script](http://markos.gaivo.net/examples/distance/test_distance "Link to test script").
100 iterations on aging powerbook produced:

1.766s, 29.152s, 9.399s (min, max, avg)

Average time to calculate distance between randomly chosen title and
rest of them is 9.4 seconds, which is far too much to be useful. And
there's not even 250 of them.

There are two obvious ways to speed things up. Since minimum distance is
at least as much as a difference in length of both strings, there's no
point in calculating it when difference already exceeds a limit we
chose.

The other trick took into an account that Levenshtein's algorithm of two
strings of comparable length has complexity of O(n2) and that my blog
titles are form quite sparse space. If strings are longer than a certain
limit (I arbitrarily chose 10 letters), then first calculate edit
distance on a small sparse substring and then calculate the real
distance only if first one was close enough.

When I made 1000 iterations of randomly chosen title using only first
test, I got following results:

0.003s, 0.284s, 0.167s (min, max, avg)

However, if I used both checks, the same 1000 iteration test got me:

0.003s, 0.162s, 0.027s (min, max, avg)

So, [two simple
checks](http://markos.gaivo.net/examples/distance/distance.py "Extended distance functions")
can speed up search up to 350 times. Not bad, but I'm not happy. This is
certainly fast enough for a personal website or sites where site
structure effectively divides searching to relatively small sets of
possible hits, but there are plenty of sites where it would be too slow.

I tried to simplify searching using distance to map strings to
coordinate system, which was at least hopelessly naive if not downright
dumb. A much better approach would be to read more, which is what I'm
doing now.

By the way, I've also tried to speed it up using Pyrex, but got pretty
much same results, which means I either don't know how to use Pyrex or
Python optimizes well. Or both.

