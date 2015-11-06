Title: Beautiful Soup is beautiful again
Date: 2005-09-06 10:16
Author: markos
Category: Python, Web
Slug: beautiful-soup-is-beautiful-again

This is probably the last part in series of post dealing with Beautiful
Soup. At least for a while. Good news is, I found the bug that caused
observed weird behavior and it was partly self-inflicted.

My problem appeared, because I was using variables that resembled html
tags (e.g. imgs, ul...) and didn't put space after \< in statements as
good practice dictates. So I had statements like:  
`     if (i<imgs.length)`

Beautiful Soup relies on *sgmllib.py* for processing of documents and
it's sgmllib that causes havoc by processing CDATA (found in script and
style blocks), when it shouldn't. But the problem is not really with
sgmllib, which has a literal switch to turn processing off. It's just
that Beautiful Soup doesn't use it.

So fix is really adding one line  
`     self.literal = 1`  
after *if* statement on line 835. Or [downloading fixed
version](http://markos.gaivo.net/blog/code/BeautifulSoup.py "Link to fixed version").

Reading source I also realized another potential pitfall. If you use
javascript to inject javascript with document.write method, you'll
probably confuse sgmllib (and hence Beautiful Soup). When processing
CDATA, it doesn't try to understand it, it just copies data until it
finds an endtag (\</script\> in javascript's case). But if you're doing
that, you have yourself to blame.

*BeautifulSoup 2.1.1 is
[out](http://www.crummy.com/software/BeautifulSoup/index.html), which
fixes my bug and several others. So you better fetch that version.*

