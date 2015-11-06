Title: Javascript: The Good Parts and string.split problem
Date: 2009-03-29 11:15
Author: markos
Category: Javascript, Web
Slug: javascript-the-good-parts-and-stringsplit-problem

I just read [Douglas
Crockford](http://crockford.com/ "Douglas Crockford")'s book
[JavaScript: The Good
Parts](http://www.amazon.com/gp/product/0596517742?ie=UTF8&tag=devel-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0596517742)![](http://www.assoc-amazon.com/e/ir?t=devel-20&l=as2&o=1&a=0596517742).
It's what a technical book should be. Concise yet full of useful
information as a result of clear scope and sticking to it. If my
experience is anything to go by, then there are not many Javascript
programmers who wouldn't benefit from it.

I did found one bit that wasn't quite right. On pages 91-92 Douglas
discusses *string.split* method, which can take a regular expression as
a separator with which to split string. Douglas rightly points out that
if regular expression includes capturing group (stuff between
paranthesis like *b(mmm)c*), then strings matching those groups will be
included in the split.

However Douglas is not completely correct when he says that some
implementations drop empty strings in the output array when separator is
regular expression. If you run [this
demo](http://markos.gaivo.net/examples/jssplit/index.html) in
[Firefox3](http://www.firefox.com/ "Mozilla Firefox 3") and IE7, you'll
see that IE7 drops even non-empty strings from capturing groups, while
Firefox3 includes them.

Still, I would find a bug in my code faster this week if I read his book
sooner.

<div class="zemanta-pixie">

[![Reblog this post [with
Zemanta]](http://img.zemanta.com/reblog_e.png?x-id=098a0fec-e31c-40fe-a1d4-701ecad46969)](http://reblog.zemanta.com/zemified/098a0fec-e31c-40fe-a1d4-701ecad46969/ "Zemified by Zemanta")<span
class="zem-script more-related"></span>
<script src="http://static.zemanta.com/readside/loader.js" type="text/javascript"></script>
</span>

</div>
