Title: Javascript: The Good Parts and string.split problem
Date: 2009-03-29 11:15
Author: markos
Category: Javascript, Web
Tags: Javascript, JavaScript: The Good Parts, Programming, Douglas Crockford, Regular expression, ie, bug
Slug: javascript-the-good-parts-and-stringsplit-problem
Status: published
Id: 322

<div>
 <p>
  I just read
  <a class="zem_slink" href="http://crockford.com/" rel="homepage" title="Douglas Crockford">
   Douglas Crockford
  </a>
  ‘s book
  <a href="http://www.amazon.com/gp/product/0596517742?ie=UTF8&amp;tag=devel-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=0596517742">
   JavaScript: The Good Parts
  </a>
  . It’s what a technical book should be. Concise yet full of useful information as a result of clear scope and sticking to it. If my experience is anything to go by, then there are not many Javascript programmers who wouldn’t benefit from it.
 </p>
 <p>
  I did found one bit that wasn’t quite right. On pages 91-92 Douglas discusses
  <em>
   string.split
  </em>
  method, which can take a regular expression as a separator with which to split string. Douglas rightly points out that if regular expression includes capturing group (stuff between paranthesis like
  <em>
   b(mmm)c
  </em>
  ), then strings matching those groups will be included in the split.
 </p>
 <p>
  However Douglas is not completely correct when he says that some implementations drop empty strings in the output array when separator is regular expression. If you run
  <a href="http://markos.gaivo.net/examples/jssplit/index.html">
   this demo
  </a>
  in
  <a class="zem_slink" href="http://www.firefox.com/" rel="homepage" title="Mozilla Firefox 3">
   Firefox3
  </a>
  and IE7, you’ll see that IE7 drops even non-empty strings from capturing groups, while Firefox3 includes them.
 </p>
 <p>
  Still, I would find a bug in my code faster this week if I read his book sooner.
 </p>
</div>
