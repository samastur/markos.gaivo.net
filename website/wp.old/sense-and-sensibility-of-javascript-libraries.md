Title: Sense and sensibility of javascript libraries
Date: 2006-06-22 14:01
Author: markos
Category: Javascript, Web
Slug: sense-and-sensibility-of-javascript-libraries

As mentioned in previous post, I think @media javascript panel deserves
its own post and this large blob of text that follows is my take on it.
You can also read
[PPK's](http://www.quirksmode.org/blog/archives/2006/06/media_impressio.html)
view or Paul Hammond's
[transcription](http://www.paulhammond.org/2006/06/atmedia2/javascript).
I'll be relying on them to augment my memory.

I started my programming career pretty far from web stack and it took me
a while to accept that this is what I'm mostly doing. As I listened to
the panelists, I was wondering if this may be the reason why I perceive
things a bit differently, although I doubt it. Still, @media javascript
panel raised some good questions.

**Are Javascript libraries unnecessary?  
**  
It seems obvious that panelists would be disinclined to say yes, since
they are the people who need them the least. I don't use them yet
either, but on the other hand I'm certain that they are needed and that
I eventually will. Their proliferation is one of more obvious
confirmations for this and even if some of them are pretty daft
(especially [those](http://code.google.com/webtoolkit/) who try to twist
Javascript to look and behave like some other language), it doesn't
follow that all of them are.

I don't buy the argument that they obscure too much. I don't see what
would distinguish them from programming libraries used in other
environments. You don't use them if you don't need to, but it also
doesn't make sense to develop a complex piece of code, if there's an
existing version out there, which was tested and debugged by many and is
actively maintained.

If you hit a bug in a library, you are left with same situation as
otherwise. You can report a bug and wait for the fix or dive into code
yourself and try to solve it. As with open source software you're
actually better off than you'd be if you worked with closed source.

Nothing actually stops you from learning how the library works, if
that's what you want or need. It would be great if we all knew
intrinsically what is happening on the computer and how the whole
process of displaying a page works, but let's face it, we don't and
there's for all intents and purposes a huge black box underneath that
sort of does what we want and we sort of understand why and how it does
it. Using a well developed and documented library doesn't change much.

I also don't buy [Simon Willison's](http://simon.incutio.com/) argument
that libraries should be obsolete and that browser should be enough.
Libraries happened because browsers take too much time to develop and
spread and I don't see this changing any time soon. It would be nice, if
parts of todays libraries were standardized in tomorrow's browsers, but
I'm sure innovative people out there will always find stuff they'd like
to do which their current environment doesn't let them. And when that
stuff can be generalized, it should be put in a library.

**So what's really wrong with libraries?  
**  
One problem is that many of them are quite large and it may take a
while before they get downloaded. Even worse, downloaded versions don't
get shared when used by different websites, since they don't come from
the same network resource. However, as already said, I think
circumventing this problem by simply using an installed version on some
other servers (you can use Dojo installed on AOL's server) is daft too.

Computer networks are fairly fragile and in some parts of the world even
more so. It's not a rare event when at least parts of the world are
inaccessible. Do you really want to bet your success on your visitors
accessibility of some resource completely away from your control?

I think caching is not a bad idea, but it needs support from browsers.
The same problem could be solved by giving each library plus its version
a unique fingerprint, which browsers could use to identify possible hits
in their cache. The most nonhackish way of calling a script that I could
come up with was:  

` <script type="text/javascript" src="http://some.server.on.the.net/coollib.js?jslibPrint=sdrt32svg"></script>`  
A different approach would be to simply include most popular Javascript
libraries as a part of a browser installation. But this approach has at
least two downsides. First, it would be limited to chosen few and
second, which is one of my real objections to current crop of libraries
out there, you'd need a fairly mature libraries.

One problem with current libraries which was pointed out is namespace
collision. It is not a new problem and although some languages (Python,
Java...) provide a mechanism to avoid it, others like C don't. For me
even more annoying is lack of stable APIs. It's simply hard to rely on a
library that changes interfaces too often.

But none of these problems is either new or insurmountable. I think
libraries are here to stay and that's a good thing. I prefer a web with
plenty of well-done web sites than one with a handful of masterpieces
swimming in a sea of crap.

And [Stuart Langridge](http://www.kryogenix.org/) is right. [Alex
Russell](http://alex.dojotoolkit.org/) certainly is (too?) clever.

