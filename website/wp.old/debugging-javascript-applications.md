Title: Debugging Javascript applications
Date: 2008-04-14 16:50
Author: markos
Category: Javascript
Slug: debugging-javascript-applications

Debugging web applications used to be simple. You generated a page and
sent it to client. Visitors performed actions and you got back their
response. Since filling a form was practically the most complicated
action they could perform, it was relatively easy to find bugs if you
were smart enough to include debugging support on server. You just had
to trace user's steps to find the one where things went amiss.

Javascript heavy applications changed that. Now a lot of action is
happening far from your eyes and even when application does communicate
with a server, it might just be a request to store or fetch more data
without any hints about what's happening over there. That's fine and we
are all happy as long as everything works. Too bad that sooner or later
it usually doesn't.

That's why I decided to write a simple debugging support I can plug in
my older projects that I still need to support and use in any upcoming
ones that could benefit from it.

**Goals**

I want my script to have the following characteristics:

-   be short and simple enough so I can rely on it not to be a cause of
    new problems
-   it can be triggered through Javascript or by manipulating URL
-   adaptable to different scenarios
-   it avoids unnecessary replication by supporting Firebug's logging
    calls

Point two in the list means I should have a choice between automatic
start of debugging by changing URL a bit or through Javascript at the
time of my liking. This way I'm free to choose the best way and moment
to debug my application.

By adaptable I mean I have free hands when it comes to how much gets
logged, how far back do I keep logs and how does that information get
sent to me.

Supporting Firebug means that its logging calls are used. So same
debugging calls that might have been used during development can also be
used for debugging problems in deployed site and don't bother script
execution in non-debug mode.

**Implementation**

Here's
[result](http://markos.gaivo.net/blog/code/debug.js "Javascript debugging module"),
packed in around 100 lines of code. It should be included at the top of
your Javascript code or as quickly as you'd like to use it. I think it's
pretty self-explanatory, but you can also look at demonstration page
described a bit later.

Debugging is stored in an object *window.console* and gets started by
either including *dbg=true* parameter in URL or calling
*window.console.debugStart* method. In later case you can provide the
method with a function as first parameter that gets called on Javascript
error or when we stop debugging with a call of
*window.console.debugEnd*.

We can provide the same function by assigning it to
*window.console.debugDisplay*. It gets called the same way with one
parameter of an array of debugging messages. It's completely up to it to
decide what to do with that information and what value to return, but
return values have the same meaning as they have in *window.onerror*
handler. If processing Javascript error, *true* means that error was
processed and script can continue and *false* will lead to error message
dialog box.

*window.console.debugStart* can also receive a parameter object with
attributes *level*, *count* and *callback* for debugging level, number
of saved messages and *debugDisplay* function respectively. Level and
message count can also be set through URL by providing parameters
*dbglevel* and *dbgcount*.

**Demo**

You can see final result called in two ways. Using [modified
URL](http://markos.gaivo.net/blog/code/debug.html?dbg=true&dbglevel=3&dbgcount=10 "URL based debugging"),
where debugging parameters are set through URL, and [the
one](http://markos.gaivo.net/blog/code/debug.html "non-URL based debugging"),
where debugging isn't turned on by default. It's same page in both cases
and so is mostly its behavior.

In first case we start fetching debugging messages immediately and
display them with a press on **End debugging**. We can't restart
debugging in this scenario, but we can in second case.

In second case we start and continue debugging with a press on **Start
debugging** button, that got displayed in the first place because
*window.console.on* was set to *false*. *window.console.on* is a
*Boolean* that shows if debugging is currently turned on or off.

In both cases only messages of requested levels get saved.

**Discussion**

Even though I tried to leave things as open to extending as possible, I
mainly tried to cover use cases I already encountered. Therefore this
script, as it is, doesn't support graceful handling of browser crashes,
which it could, if it saved debug information to local storage when
available.

Script also doesn't support loading different libraries in debug mode.
That is, if you want to load libraries stripped of debugging calls when
not debugging, you can do that yourself, using *window.console.on*. This
script won't do it for you.

I do provide a skeleton *debugDisplay* in case you don't provide one
yourself. If you don't, then debug message gets displayed using *alert*,
which makes it hard to copy and paste, but easy enough to make a
screenshot of. Setting debugging level is probably not as nice as it
could be too.

It's not completely stupid though, takes note of *Array* object's
suitability mainly for sparse and small arrays and should perform
adequately when it comes to memory consumption even with new IE8 as long
as count parameter isn't too big.

At the end, it's a piece of code as any I've written. Bugs are likely,
so bug reports would be appreciated. Same goes for ideas and
suggestions. If you need it, feel free to use it any way you want, but I
would appreciate a ping just to see where my stuff ends up.

