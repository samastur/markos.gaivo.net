Title: Problem with public javascript hosting
Date: 2007-03-06 16:56
Author: markos
Category: Javascript, Web
Slug: problem-with-public-javascript-hosting

Yahoo recently
[announced](http://yuiblog.com/blog/2007/02/22/free-yui-hosting/) free
public hosting of YUI library, just like AOL
[did](http://blog.dojotoolkit.org/2006/01/30/dojo-iamalpha-and-cdns) a
while ago for Dojo toolkit. A great move. You don't have to pay
bandwidth for hosting YUI and there's a better likelihood that scripts
will already be in visitors browser cache, since some other previously
visited page might have used them too.

However there's a real downside to it. What happens if Yahoo servers are
unaccessible or connection to them is just slow?

If you're lucky, then its former and the page will be rendered quickly
but with some (javascript) functionality missing. If later, then it
might take forever to render a page since modern browsers can't and
won't do it until all javascript has been loaded.

This might seem an unlikely scenario, unless you've been around the last
time when access problems to Google Analytics stopped displaying a large
part of slovenian web, least important of which being this very blog.
Yahoo is not stupid, but neither is Google and problem can literally
appear anywhere between their servers and your visitors computer.

So what can be done if this possibility is not acceptable to you, but
you'd still want to use free hosting?

Nothing pretty it seems. The only thing that I can think of is to add
local links to yui, put them together with Yahoo links at the bottom of
the page and trigger Javascript when content has been loaded. Then you
only have to wait for YUI objects to appear before you start processing
your scripts.

This way you can probably avoid crippled or blank pages, but you're
still paying for the bandwidth. Unless of course you go one step further
and include local links only when Yahoo objects don't appear in a
reasonable amount of time.

Does anyone have any idea how to solve this problem gracefully?

