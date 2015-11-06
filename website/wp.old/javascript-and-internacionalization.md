Title: Javascript and i18n
Date: 2005-11-05 19:15
Author: markos
Category: Javascript, Web
Slug: javascript-and-internacionalization

I've been looking for Javascript localization resources on Google and
came up fairly empty handed. There seems to be
[little](http://www.codeproject.com/aspnet/MultilingualWebsites3.asp#4)
useful information and even less useful code. The only thing I found,
that is actually usable, is a
[library](http://johnnydebris.net/javascripts/i18n.js?frames=no "Link to javascript i18n library")
by Guido Wesdorp.

I find this utterly amazing after a decade of Javascript being in wide
use, although I probably shouldn't be. A likely explanation for this is
that Javascript is most often used for short scripts inside web pages.
If used on a multilingual website, it's usually fairly easy to have
separate javascript files for each language.

I expect this will change with rise of more complicated, involved web
applications. However, so far AJAX toolkits that seem to spring up these
days like mushrooms after rain, have been busy with obviously more
important things like animations.

I could be wrong. In fact, I hope I'm wrong. Is there a javascript i18n
library with following characteristics:

-   easy to use
-   supports translation of javascript code and HTML
-   small and relatively fast
-   translations are separated from HTML and javascript code
-   handles properly nodes with superfluous whitespace and those where
    it can't be collapsed
-   supports translation of nodes with other HTML tags as ancestors (not
    only text nodes)

Guido's library is a good tool that meets many of these needs, but sadly
not all of them. Writing my own one seems to be the only solution.

