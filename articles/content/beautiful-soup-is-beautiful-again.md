Title: Beautiful Soup is beautiful again
Date: 2005-09-06 10:16
Author: markos
Category: Python, Web
Slug: beautiful-soup-is-beautiful-again
Status: published
Id: 19

<div>
 <p>
  This is probably the last part in series of post dealing with Beautiful Soup. At least for a while. Good news is, I found the bug that caused observed weird behavior and it was partly self-inflicted.
 </p>
 <p>
  My problem appeared, because I was using variables that resembled html tags (e.g. imgs, ul…) and didn’t put space after &lt; in statements as good practice dictates. So I  had statements like:
  <br/>
  <code>
   <br/>
   if (i&lt;imgs.length)
   <br/>
  </code>
 </p>
 <p>
  Beautiful Soup relies on
  <em>
   sgmllib.py
  </em>
  for processing of documents and it’s sgmllib that causes havoc by processing CDATA (found in script and style blocks), when it shouldn’t. But the problem is not really with sgmllib, which has a literal switch to turn processing off. It’s just that Beautiful Soup doesn’t use it.
 </p>
 <p>
  So fix is really adding one line
  <br/>
  <code>
   <br/>
   self.literal = 1
   <br/>
  </code>
  <br/>
  after
  <em>
   if
  </em>
  statement on line 835. Or
  <a href="http://markos.gaivo.net/blog/code/BeautifulSoup.py" title="Link to fixed version">
   downloading fixed version
  </a>
  .
 </p>
 <p>
  Reading source I also realized another potential pitfall. If you use javascript to inject javascript with document.write method, you’ll probably confuse sgmllib (and hence Beautiful Soup). When processing CDATA, it doesn’t try to understand it, it just copies data until it finds an endtag (&lt;/script&gt; in javascript’s case). But if you’re doing that, you have yourself to blame.
 </p>
 <p>
  <em>
   BeautifulSoup 2.1.1 is
   <a href="http://www.crummy.com/software/BeautifulSoup/index.html">
    out
   </a>
   , which fixes my bug and several others. So you better fetch that version.
  </em>
 </p>
</div>
