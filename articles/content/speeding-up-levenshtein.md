Title: Speeding up Levenshtein
Date: 2006-11-10 02:17
Author: markos
Category: General development, Python, Web
Slug: speeding-up-levenshtein
Status: published
Id: 211

<html>
 <body>
  <div>
   <p>
    <a href="handling-404.html">
     Simon
    </a>
    proposes using a dictionary to match mistyped URLs with real ones. I’d probably like the idea better if I actually understood it. Still using
    <a href="http://en.wikipedia.org/wiki/Levenshtein_distance" title="description of the algorithm">
     Levenshtein
    </a>
    can be a bit easier than using a spell checker responsively.
   </p>
   <p>
    Easier, but slow. I used existing
    <a href="http://hetland.org/python/distance.py" title="python implementation">
     implementation
    </a>
    by Magnus Lie Hetland and made a test with 245 blog titles using a simple
    <a href="http://markos.gaivo.net/examples/distance/test_distance" title="Link to test script">
     script
    </a>
    . 100 iterations on aging powerbook produced:
   </p>
   <p style="text-indent:20pt;">
    1.766s, 29.152s, 9.399s (min, max, avg)
   </p>
   <p>
    Average time to calculate distance between randomly chosen title and rest of them is 9.4 seconds, which is far too much to be useful. And there’s not even 250 of them.
   </p>
   <p>
    There are two obvious ways to speed things up. Since minimum distance is at least as much as a difference in length of both strings, there’s no point in calculating it when difference already exceeds a limit we chose.
   </p>
   <p>
    The other trick took into an account that Levenshtein’s algorithm of two strings of comparable length has complexity of O(n2) and that my blog titles are form quite sparse space. If strings are longer than a certain limit (I arbitrarily chose 10 letters), then first calculate edit distance on a small sparse substring and then calculate the real distance only if first one was close enough.
   </p>
   <p>
    When I made 1000 iterations of randomly chosen title using only first test, I got following results:
   </p>
   <p style="text-indent:20pt;">
    0.003s, 0.284s, 0.167s (min, max, avg)
   </p>
   <p>
    However, if I used both checks, the same 1000 iteration test got me:
   </p>
   <p style="text-indent:20pt;">
    0.003s, 0.162s, 0.027s (min, max, avg)
   </p>
   <p>
    So,
    <a href="http://markos.gaivo.net/examples/distance/distance.py" title="Extended distance functions">
     two simple checks
    </a>
    can speed up search up to 350 times. Not bad, but I’m not happy. This is certainly fast enough for a personal website or sites where site structure effectively divides searching to relatively small sets of possible hits, but there are plenty of sites where it would be too slow.
   </p>
   <p>
    I tried to simplify searching using distance to map strings to coordinate system, which was at least hopelessly naive if not downright dumb. A much better approach would be to read more, which is what I’m doing now.
   </p>
   <p>
    By the way, I’ve also tried to speed it up using Pyrex, but got pretty much same results, which means I either don’t know how to use Pyrex or Python optimizes well. Or both.
   </p>
  </div>
 </body>
</html>