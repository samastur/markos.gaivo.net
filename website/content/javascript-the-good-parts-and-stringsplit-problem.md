Title: Javascript: The Good Parts and string.split problem
Date: 2009-03-29 11:15
Author: markos
Category: Javascript, Web
Slug: javascript-the-good-parts-and-stringsplit-problem
Status: published
Id: 322

<html>
 <body>
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
    <img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=devel-20&amp;l=as2&amp;o=1&amp;a=0596517742" style="border:none !important; margin:0px !important;" width="1"/>
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
   <div class="zemanta-pixie">
    <a class="zemanta-pixie-a" href="http://reblog.zemanta.com/zemified/098a0fec-e31c-40fe-a1d4-701ecad46969/" title="Zemified by Zemanta">
     <img alt="Reblog this post [with Zemanta]" class="zemanta-pixie-img" src="http://img.zemanta.com/reblog_e.png?x-id=098a0fec-e31c-40fe-a1d4-701ecad46969"/>
    </a>
    <span class="zem-script more-related">
     <script src="http://static.zemanta.com/readside/loader.js" type="text/javascript">
     </script>
    </span>
   </div>
  </div>
 </body>
</html>