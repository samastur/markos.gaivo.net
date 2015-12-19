Title: Speed match: JSON vs. XML
Date: 2005-12-05 19:41
Author: markos
Category: Javascript, Web
Slug: speed-match-json-vs-xml
Status: published
Id: 87

<div>
 <p>
  I started playing with AJAX before it got its silly name and true to X I used XML in my application. At least at first.
 </p>
 <p>
  What I discovered is that flicker caused by processing data and simultaneously writing results to document can be completely removed if I do a Google and fetch javascript object instead (what later became
  <a href="http://www.crockford.com/JSON/index.html">
   JSON
  </a>
  ) and use that. Difference was so vivid, I dropped XML almost completely.
 </p>
 <p>
  Fast forward to autumn. There’s a debate after our regular weekly talk and a question comes up. Why would Google or anyone else for that matter choose to use something else than XML?
 </p>
 <p>
  Relying on personal experience I offered speed as obvious and most important reason. I couldn’t back it up, but since I’ve seen it with my own eyes, I didn’t doubt it either. It wasn’t the sole reason. I find dabbling with javascript objects simply easier than handling XML and I’ll care about XSLT when javascript in Safari can access it.
 </p>
 <p>
  I got reminded of our discussion when I read
  <a href="http://www.xml.com/lpt/a/2005/11/30/tuning-ajax-performance.html">
   this article
  </a>
  . Read it, if you haven’t yet, because it’s well worth it. Anyhow, I decided to make a new test. I wrote a simple
  <a href="http://markos.gaivo.net/examples/jsbench/test.html">
   test page
  </a>
  , that fetches
  <a href="http://markos.gaivo.net/examples/jsbench/jssample.raw">
   sample json file
  </a>
  and basically equal
  <a href="http://markos.gaivo.net/examples/jsbench/xmlsample.xml">
   xml sample
  </a>
  and measures how much time it takes to fetch same data.
 </p>
 <p>
  Result?
 </p>
 <p>
  After 15 minutes of wild reloading in different browsers (Safari 1.3+, FF1.0, IE6) and different local and non-local servers, I can’t see a difference that couldn’t be attributed to latency. It seems browsers have moved on and there’s little reason to avoid using XML today.
 </p>
 <p>
  So use whatever you like most.
 </p>
</div>
