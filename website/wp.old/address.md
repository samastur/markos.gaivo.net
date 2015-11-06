Title: <address>
Date: 2011-08-26 17:26
Author: markos
Category: General development, Web
Slug: address

After years of personal embarrassment I finally managed to update look
and code of my website. This actually happened last week and I wanted to
write this post sooner, but [other
things](http://supervizor.kpk-rs.si "Supervizor") came in-between. There
are still bugs I need to fix (iPad footer is better than it was, but not
fine), but﻿ overall I'm pretty happy with how it turned out.

This was a second site I built using [media
queries](http://www.w3.org/TR/css3-mediaqueries/ "media queries") and I
learned lots. When I learn a bit more about mobile web, I might write a
post about few gotchas for new developers, but this is not that post.
This post is about `<address>` tag because it bugged me when I made that
first design and I spent a remarkable amount of time on it again.

My problem with it came down to its definition. `<address>` can be used
only to mark up contact information about content's author. In HTML 4
this was limited to authorship of whole page. For HTML5 it [was
"widened"](http://dev.w3.org/html5/spec/sections.html#the-address-element "Definition of <address> in HTML5 specification")
to authorship of sectioning element like `<article>` (so if you have
more than one article on page, each can contain its own, different,
address for its author). You can't however mark any address with it and
after lots of searching I found [this old
message](http://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2008-February/014023.html "Ian's message from February 2008")
from [Ian
Hickson](http://en.wikipedia.org/wiki/Ian_Hickson "Ian Hickson") which
explains why (I'm not aware of any later clarifications).

I don't agree with everything said. Mostly correct use is not
necessarily a proof of well-designed element. My bet would be that
`<address>` was a rather unknown tag exactly because of its limited use
and was thus used mostly by those that dig deeper into standards, which
sound also like people who care  how things are used as expected.

Still most points are valid. Loosening definition would make it less
meaningful.
[There](http://microformats.org/wiki/hcard "Specification of hCard microformat")
[are](http://microformats.org/wiki/adr "Specification of adr microformat")
microformats that you can use instead and most annoying problems
(allowing only inline content) have been fixed. We also have better
tools for parsing HTML so  it really doesn't matter much if its
definition feels completely right or not. It's good enough.

At the end I still decided to mark my contact information on [my
homepage](http://markos.gaivo.net) with `<address>` anyhow (augmented
with [hCard](http://en.wikipedia.org/wiki/HCard "HCard")), because I
am after all the sole author of this website.

<div class="zemanta-pixie">

![](http://img.zemanta.com/pixy.gif?x-id=9e03fdb6-c5dc-4878-b734-7bec34cd9ced)

</div>
