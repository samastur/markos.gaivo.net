Title: Latency, bandwidth and speed of applications - part I
Date: 2005-09-14 21:10
Author: markos
Category: General development, Javascript, Python
Slug: latency-bandwidth-and-speed-of-applications-part-i

It seems we're back to discussing the importance of bandwidth and
latency on perceived speed of application. In a way it's amazing that
after 10 years of widespread use of Internet and local networks, we
developers still discuss these issues.

So, what contributes to speed of execution in network applications?

Each network request can be divided into seven time intervals:

1.  time needed to send a request
2.  latency, which is time spent for any amount of data to travel
    between client and server
3.  data transfer time
4.  time needed to process a request, form a response and send it
5.  latency again, but this time in other direction
6.  data transfer time for response
7.  time needed to process response and present result to user

Sum of all these parts is time lapsed between issued command and
presented result. How fast this needs to be depends on application and
our experiences. For example, we expect faster response to our key
presses in SSH client than we do waiting for search results.

However, if this sum is under a quarter of a second, it will be
generally regarded as instantaneous, but you really should aim for
1/10th of a second to satisfy even the most twitchy users.

Usually, we might get to control all parts of this equation only when
client and server are located on a local network and we develop both of
them. So, a well behaving application needs to take in account
environment in which it will run and act accordingly.

This means, among other things, to give user feedback that something is
happening whenever there is even a remote chance that response might
take a while, to react sensibly to network disruptions (such as
timeouts) and offer a way to abort user actions.

So, how do we speed up the application itself?

Absolutely the best way to speed up a network request is to not make
one. The usual way to do this is to cache result over its life span and
use it when possible.

The other way, lately often mentioned in relation to AJAX, is to make
our requests asynchronously. Unlike synchronous requests, which are
direct results of user actions, asynchronous are those were data is
transfered in expectation of future user actions.

An example would be a mail program where we transfer message headers of
yet unread mail in background before we actually need to display them to
user, since it's fairly likely that he'll want to check them in near
future.

There are also downsides to this approach. It can be difficult to
predict what to transfer next if no user action is more probable than
rest. It can also incur significant costs if bandwidth is expensive as
often is on GPRS networks in Europe. And when number of simultaneous
connections is limited (HTTP allows 4, but not all browsers comply), it
can occupy a resource when you need one.

Still, it's a useful tool when it can be applied.

More about saving time with our seven intervals in part two due
tomorrow.

*Update: second part has been
[posted](http://markos.gaivo.net/blog/?p=24 "Second part").*

