Title: Latency, bandwidth and speed of applications - part II
Date: 2005-09-16 00:03
Author: markos
Category: General development, Javascript, Python
Slug: latency-bandwidth-and-speed-of-applications-part-ii

This is the second post on this subject. You can find the first part
[here](http://markos.gaivo.net/blog/?p=23 "First par of this article").

So, how do latency and bandwidth relate to the speed of execution?

As mentioned, latency is time needed for any amount of information to
travel a certain distance and bandwidth is the amount of data that can
flow through it at the same time.

Let me give you a real-life example. If you imagine people walking down
the corridor, then latency is amount of time one person needs to walk
from start to its end and bandwidth is number of people who can do this
at the same time.

You can measure latency quite easily with ping, a tool available on
every major OS, which will give you a round-trip time from client to
server (2+5 from our original 7 intervals). The only problem is that it
will tell you just your personal latency at that time, which can vary
significantly for people on different networks and even for you at
different times. There are similar tools for measuring bandwidth and
they have more or less the same problems.

However, sometimes you can tell a bit about what you can expect. For
example, if you're building an application aimed at mobile users using
GPRS, then it's quite reasonable to assume that bandwidth will be scarce
and latency will be high. On local networks it's usually the opposite of
that.

In general, latency rises with distance between server and client and
bandwidth can't be wider than the narrowest bandwidth on the way and the
question is how do we react to our situation?

Basic rules are:

-   if latency is high, then we should make as few round-trips to server
    as possible
-   if bandwidth is wide, then we can transfer more data at each trip

In practice we should always try for the most balanced approach between
this two factors. If latency is fairly high, but bandwidth is not
severely limited, then we might transfer also data we don't need
immediately, if it might spare us another request later on. If latency
is low and bandwidth is narrow, then it might make more sense to
transfer only what's needed, but make those requests more often.

Another way we can sometimes cut down response time, when bandwidth is
not the limiting factor, is to multiplex connections, which is a bit
fancy way of saying to simultaneously open multiple connections from
client to server. It's nice to keep in mind that some browsers like
Internet Explorer will limit number of simultaneous connections for HTTP
protocol to 4 (as specified by its standard), but you are more free to
do what you want, if you write your own program. It's also nice to keep
in mind that if order in which responses are coming is important, you'll
have to handle that yourself.

A different approach is to simulate multiplex connections over one
connection. In this case client sends multiple commands inside of one
network request and receives answers to all of them at once. It's easier
to handle order, since you get all data at the same time, but you give
up possibly faster response for some of the data.

There are other factors that can influence our decisions, such as
possibly increased load on server from more requests. Or the speed with
which we can generate a request and process reply, if we need to pack
and unpack more data. But this are issues worth exploring in some other
post, if interest justifies it.

