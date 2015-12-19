Title: <address>
Date: 2011-08-26 17:26
Author: markos
Category: General development, Web
Tags: HTML, Data Formats, Markup Languages, Ian Hickson, HTML element
Slug: address
Status: published
Id: 734

<div>
 <p>
  After years of personal embarrassment I finally managed to update look and code of my website. This actually happened last week and I wanted to write this post sooner, but
  <a href="http://supervizor.kpk-rs.si" title="Supervizor">
   other things
  </a>
  came in-between. There are still bugs I need to fix (iPad footer is better than it was, but not fine), but﻿ overall I’m pretty happy with how it turned out.
 </p>
 <p>
  This was a second site I built using
  <a class="zem_slink" href="http://www.w3.org/TR/css3-mediaqueries/" rel="homepage" title="media queries">
   media queries
  </a>
  and I learned lots. When I learn a bit more about mobile web, I might write a post about few gotchas for new developers, but this is not that post. This post is about
  <code>
   &lt;address&gt;
  </code>
  tag because it bugged me when I made that first design and I spent a remarkable amount of time on it again.
 </p>
 <p>
  My problem with it came down to its definition.
  <code>
   &lt;address&gt;
  </code>
  can be used only to mark up contact information about content’s author. In HTML 4 this was limited to authorship of whole page. For HTML5 it
  <a href="http://dev.w3.org/html5/spec/sections.html#the-address-element" title="Definition of &lt;address&gt; in HTML5 specification">
   was “widened”
  </a>
  to authorship of sectioning element like
  <code>
   &lt;article&gt;
  </code>
  (so if you have more than one article on page, each can contain its own, different, address for its author). You can’t however mark any address with it and after lots of searching I found
  <a href="http://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2008-February/014023.html" title="Ian's message from February 2008">
   this old message
  </a>
  from
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Ian_Hickson" rel="wikipedia" title="Ian Hickson">
   Ian Hickson
  </a>
  which explains why (I’m not aware of any later clarifications).
 </p>
 <p>
  I don’t agree with everything said. Mostly correct use is not necessarily a proof of well-designed element. My bet would be that
  <code>
   &lt;address&gt;
  </code>
  was a rather unknown tag exactly because of its limited use and was thus used mostly by those that dig deeper into standards, which sound also like people who care  how things are used as expected.
 </p>
 <p>
  Still most points are valid. Loosening definition would make it less meaningful.
  <a href="http://microformats.org/wiki/hcard" title="Specification of hCard microformat">
   There
  </a>
  <a href="http://microformats.org/wiki/adr" title="Specification of adr microformat">
   are
  </a>
  microformats that you can use instead and most annoying problems (allowing only inline content) have been fixed. We also have better tools for parsing HTML so  it really doesn’t matter much if its definition feels completely right or not. It’s good enough.
 </p>
 <p>
  At the end I still decided to mark my contact information on
  <a href="http://markos.gaivo.net">
   my homepage
  </a>
  with
  <code>
   &lt;address&gt;
  </code>
  anyhow (augmented with
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/HCard" rel="wikipedia" title="HCard">
   hCard
  </a>
  ), because I am after all the sole author of this website.
 </p>
 <div class="zemanta-pixie">
  <img alt="" class="zemanta-pixie-img" src="http://img.zemanta.com/pixy.gif?x-id=9e03fdb6-c5dc-4878-b734-7bec34cd9ced"/>
 </div>
</div>
