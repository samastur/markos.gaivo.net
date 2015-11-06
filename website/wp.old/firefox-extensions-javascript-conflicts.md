Title: Firefox extensions Javascript conflicts
Date: 2006-05-29 12:23
Author: markos
Category: Javascript, Web
Slug: firefox-extensions-javascript-conflicts

I like Firefox extensions and use a few myself. Web development without
[Web Developer toolbar](http://chrispederick.com/work/webdeveloper/) and
[LiveHTTPHeaders](http://livehttpheaders.mozdev.org/) extension would be
pretty gruesome. However, there's a downside to their use that is slowly
starting to bother me.

They often influence the way Javascript on page gets executed and can
produce weird errors.

I first noticed this while using Web Developer toolbar. Every now and
then I got a strange exception, but I didn't worry too much. After all,
it wasn't really surprising coming from an extension that by its very
nature dabbled with the way browser interprets and displays a page and
it didn't really stop the script from working. Not pretty, but you learn
to live with it.

Comes this weekend and I get a report that file upload doesn't work in
latest Firefox. I suspected extension conflicts and further examination
proved the point. Page worked just fine in the same environment sans
extensions.

So what can you do, when you stumble on a problem like that?

Testing your site in various browsers can be troublesome enough. Testing
all combinations of extensions even for one browser would simply be
impossible. You can't exactly expect your users to uninstall their
extensions just for you, but making workarounds for them doesn't seem
feasible either.

So far I don't see a good solution. Any ideas?

