Title: rtvslo.si redesign
Date: 2006-06-04 14:18
Author: markos
Category: General development, Web
Slug: rtvslosi-redesign

Slovenian national television has a [new design](http://www.rtvslo.si).
It's certainly better than what they had before, but it's far from
perfect.

Fry already
[described](http://friedcellcollective.net/outbreak/2006/06/03/validity/)
some of the graver errors. But his list is not nearly complete and here
are some issues that bother me most:

-   not only is Javascript often inlined, it's also not degradable (crap
    like href="javascript:void really has no place in modern web
    development)
-   [divitis](http://en.wikipedia.org/wiki/Divitis "Description of divitis")
-   inline CSS
-   ridiculously long list of external resources (87 on main page),
    which result in excruciatingly long page loads on connections with
    high latency
-   poor contrast between text and background in large parts of a page
    can be an accessibility problem

I could go on, but I don't want to complain too much. As I've said
before, this page is a clear improvement over the previous one and it's
also obvious from it that their creators do care about modern
development and its often forgotten parts like accessibility. This is
exactly the reason why I decided to write about its failings and not
about some other, more atrocious one. [Zavod
Embrio](http://www.em3r10.com/) shows an ambition for good designs and
although I don't think they're quite there yet, I'm sure they soon will
be.

And I guess my notion that there's no need for workshops on XHTML, CSS
and web standards in general has been proven wrong.

