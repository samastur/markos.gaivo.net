Title: I like SSE
Date: 2005-11-24 22:33
Author: markos
Category: General development, Web
Slug: i-like-sse

I've been a netizen since '93 and I saw web for the first time in '94,
when a friend showed me [Yahoo](http://www.yahoo.com). I felt dizzy just
thinking about possibilities.

I had no idea what was coming, but even though web came a long way since
then, I never felt so excited again up until now. It's hard to predict
future and I avoid revealing my stupidity if possible, but it really
looks like a no-brainer predicting a vastly different, more open and
collaborative web in few years time than we have now.

Feeds were a big step forward. It wasn't necessary to scrap pages to
reuse information anymore. Even more importantly, feeds changed the
attitude so sharing and reusing content is now again a normal and good
thing.

It seems [atom publishing
protocol](http://www.ietf.org/html.charters/atompub-charter.html) will
soon be ratified and with it a standard way of editing web resources. In
fact making sharing a two-way street. The final piece was provided by
[Ray
Ozzie](http://spaces.msn.com/members/rayozzie/PersonalSpace.aspx?_c01_blogpart=blogmgmt&_c=blogpart "Ozzie's blog")
and guys at Microsoft. A synchronization protocol for RSS feeds called
[SSE](http://msdn.microsoft.com/xml/rss/sse/ "Protocol specification")
published under creative commons license that should be really useful
for synchronizing calendars, contacts etc.

I've read it a couple of days ago and I couldn't find an obvious defect
in it (apart from a small error in the example at point 2.2.2, which I'm
sure has been spotted since). Truth be told, I didn't expect it to.

It's a simple, easy to understand specification. I wish people would
stop using date-time values conforming to RFC 822, but nevertheless SSE
shouldn't be difficult to implement.

It probably really is the easiest thing that could work and it's up to
programmers to show if it might be too easy. There's always a tension
between things you specify and things you leave to implementation.
Freedom given can and usually is a point of misunderstandings and until
there are enough implementations in the wild, it's hard to judge the
quality of compromise.

I won't be surprised though if final specification version won't be
significantly different than current one. I'll try to make our
implementation as soon as possible and hopefully by that time there will
be others to test it with.

