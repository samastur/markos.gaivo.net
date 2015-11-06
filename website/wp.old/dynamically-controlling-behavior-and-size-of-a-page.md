Title: Dynamically controlling behavior and size of a page
Date: 2007-12-12 20:37
Author: markos
Category: Javascript, Web
Slug: dynamically-controlling-behavior-and-size-of-a-page

It's not a secret that Javascript is interpreted and not statically
compiled. Personally I find this an advantage that is not used often
enough. If you look around the Web you can find plenty of cases to prove
this, but I'd like to add another example.

A few months ago I was developing a library which had a goal of
providing an improved Javascript experience for standardized components
without requiring any knowledge of the language to use. I also wanted to
support different load scenarios so library could be smaller when
needed.

Sadly I ran out of time before I ended my work to my satisfaction.
Still, I'd like to discuss one approach that also demonstrates aspects
that I'd like to see used more in the wild.

Let's start with a demo. I created two almost identical pages. Can you
spot the difference between
[first](http://markos.gaivo.net/examples/richswitch/index.html "First demo")
and
[second](http://markos.gaivo.net/examples/richswitch/index2.html "Second demo")?

First one simply toggles visibility of the text, while second one does
the same with a bit more style. If you look at files, you'll notice that
the only difference is that first calls
*[switch.js](http://markos.gaivo.net/examples/richswitch/switch.js)* and
second uses
*[rswitch.js](http://markos.gaivo.net/examples/richswitch/rswitch.js)*.
Both files look the same because they are. In fact, it's really just one
file. Hard link to the rescue for us, Unixheads.

But first a small warning. This code is not production ready. I
simplified it to keep example clear and concise. In that capacity I
think it will do.

Javascript basically consists of two functions. A *window.onload*
handler that's triggered when page is loaded and an animation function
attached to button. A *window.onload* handler is a one trick pony. Its
main idea is to find Javascript file in DOM and based on the name with
which it was loaded set up the execution environment. This is just a
fancy name (to make me look smart) for setting a global variable that is
private to this name space and possibly loading a few additional
resources, like YUI animation support in our case. It is also the first
case where not being static helps. We can decide at run time what's
necessary and load only what we need.

However, I find *toggleVisible* a tad bit more interesting and the
reason is its *if* statement. What happens when we include *switch.js*
in a page?

Well, variable *rich* remains set to *false* and YUI components don't
get loaded. This means *YAHOO.util* and its descendants aren't defined.
Yet as we've seen from first demo page script works just fine. Reason
for this is that *if* statement in *toggleVisible* evaluates to *false*
and those undefined statements never get reached. This wouldn't work in
a language like Java, which would notice a call to undefined methods at
compile time and refuse to finish compile, but it works perfectly fine
in Javascript.

Of course if rich was set true, then we load YUI files. It might happen
with this code that we press button before they get loaded, which is one
of the reasons why this isn't a production quality code, but if we
assume for a moment that they did, then those same lines in
*toggleVisible* are perfectly fine and it works as hopefully seen on
second page.

We therefore have a page where we control its behavior and size only by
the way we call javascript file. There's literally only one letter of
difference. With dynamic loading of resources and cordoning potentially
nonexistent methods we could fairly easily create a spectrum of
possibilities where our users could choose their own compromise between
functionality and its price in terms of page size and speed or better
handle differences between mobile and desktop browsers.

