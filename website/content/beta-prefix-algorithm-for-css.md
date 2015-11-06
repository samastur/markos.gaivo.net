Title: -beta- prefix algorithm for CSS
Date: 2012-02-10 18:21
Author: markos
Category: General development, Web
Slug: beta-prefix-algorithm-for-css
Status: published
Id: 929

<html>
 <body>
  <div>
   <p>
    These have been eventful couple of days for web developers. CSS Working Group chair
    <a href="http://www.glazman.org/weblog/dotclear/index.php?post/2012/02/09/CALL-FOR-ACTION%3A-THE-OPEN-WEB-NEEDS-YOU-NOW">
     called on everyone
    </a>
    to use all (most?) vendor prefixes and stop making websites for WebKit which is becoming a new (mobile) IE6. Responses have been numerous,
    <a href="http://www.quirksmode.org/blog/archives/2012/02/the_vendor_pref.html" title="PPK's first article about prefixes">
     including
    </a>
    <a href="http://www.quirksmode.org/blog/archives/2012/02/alpha_and_beta.html" title="PPK's follow up to first article">
     ppk
    </a>
    who in his usual obnoxious manner
    <sup>
     <a href="#beta-prefix-note-1" id="beta-prefix-1">
      [1]
     </a>
    </sup>
    made some good points. Testing on mobile devices is an unsolved problem (who wants or can afford to buy so many almost immediately obsolete gadgets?) and introducing -beta- (maybe also -alpha-) prefix would simplify our lives while keeping most benefits of vendor prefixes.
   </p>
   <p>
    I like -beta- idea and I think adding -alpha- might be even better. There’s still a problem of resolving syntax conflicts between different implementation which I think has a simple solution that closely mimics what browsers already do:
   </p>
   <p>
    <em>
     When parsing CSS browsers
    </em>
    <em>
     should apply the last matching -beta-/-alpha- directive they fully understand.
    </em>
   </p>
   <p>
    Browsers already ignore directives they don’t understand and they apply last directive found when there are multiple candidates for a DOM node.
   </p>
   <p>
    Such behavior would give us less CSS code to write and maintain, have predictable behavior and keep browser experimentation without favoring one. I have troubles finding negative sides of this approach, but do let me know if you can think of one.
   </p>
   <ol>
    <li id="beta-prefix-note-1">
     I deeply dislike his complaining about simplistic view of others while himself generalizing and name-calling (the lazy and stupid lot of us). Alas it’s not good to read only people you like and agree with.
     <a href="#beta-prefix-1">
      ↩
     </a>
    </li>
    <li>
     Almost everything I write on this blog has an intended  audience of one:  me (no, really!). Why I sometimes write posts like  this, which don’t, is a mistery  since their expected and actual effect on anyone  is…none.
    </li>
   </ol>
  </div>
 </body>
</html>