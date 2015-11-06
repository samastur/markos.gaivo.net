Title: Missing refer(r)ers
Date: 2011-09-20 18:29
Author: markos
Category: General development, Web
Slug: missing-referrers

I was talking to my wife today about why an "Unknown Source" is becoming
the most common source of visits on
[Flickr](http://flickr.com "Flickr"). My guess is that it is almost
certainly because a
[*Referer*](http://en.wikipedia.org/wiki/HTTP_referrer "HTTP referrer")
header field is missing in page requests and Flickr is only relying on
presence of this piece of data to discern sources. This might have made
sense when browsers ruled the web, but we don't live then anymore.

Simply put referrer field [can be
added](http://tools.ietf.org/html/rfc2616#section-14.36 "Link to Referer field definition")
to request only when request was triggered from source which also has an
[URI](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier "Uniform Resource Identifier")
address. Every web page has it since its address is also an URI, but
most programs don't.

That's why referrers aren't missing only from visitors using paranoid
browsers or security software that stripped it out of requests, but also
when page is visited from a link embedded in emails or instant messages.

Requests without referrers used to present a small enough subset of
visits that most of us didn't care. I first noticed this changing when
Twitter clients became popular and now there are tons of apps behaving
like this. With [XMLHttpRequest Level
2](http://www.w3.org/TR/XMLHttpRequest2/ "Link to specification")﻿ even
web developers will get a choice of making anonymous requests which
won't include potentially private data like referrers.

That's nice. I have certainly visited places which I wouldn't want to
share with strangers. But I suspect this is not the common case and most
of the time we don't care telling which page or application sent us
there.

Nobody can precisely predict future so specifications can never be
perfect. But I am always amazed when reading core web specs like HTTP's
how insightful their authors were. That most programs don't have a URI
does not mean that they couldn't. Practically anything can and
definitely more things should.

In principle it is possible for each program to have its own address
which could be used as referrer *when a better option doesn't exist*. I
suspect this would be against the spirit of specification, but likely
not against its text.

However better options often do exist. Lets take
[Twitter](http://twitter.com "Twitter") as a popular example. Every link
that triggers a visit from Twitter was included in at least one tweet
and every tweet is also published on web. It might not be accessible to
everyone, but it does have an address. I see no reason why that address
could not be used as referrer by Twitter clients.

It is originating content or its address that interest me, but really,
almost anything truthful beats an unknown source. Just knowing name of
the service (like Twitter) or app used (e.g. Tweetdeck) would be better
than nothing. By the way there is another header field that could
provide such insight: *User-Agent*. Sadly it is notoriously unreliable
and often missing as well, but that's another long story.

So, if I come back to Flickr. I can't really tell how much Flickr can or
could know. I suspect more than it tells, but I would be astonished if
they are not mostly in the dark too. Web was largely built by people too
busy (and often too lazy) not to cut corners. Meaning: learning and
doing as little as possible to get something to work and sometimes we
pay price for our ignorance. But it's a small price compared to waiting
for
[Xanadu](http://en.wikipedia.org/wiki/Project_Xanadu "Description of project Xanadu on Wikipedia").

<div class="zemanta-pixie">

![](http://img.zemanta.com/pixy.gif?x-id=860d2c48-a1dc-49c5-85d1-277e4734d096)

</div>
