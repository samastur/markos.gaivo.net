Title: Updated sgmllib
Date: 2006-04-01 15:05
Author: markos
Category: Python
Slug: updated-sgmllib

I [wrote](http://markos.gaivo.net/blog/?p=142) about a sgmllib problem a
few days ago. I still may be a dolt and my code certainly needed fixing,
but the bug remained nevertheless.

Hence I've made some small changes to sgmllib that fix problems I've
had. New version, which passes all unit tests included in Python
distribution, can be found
[here](http://markos.gaivo.net/examples/sgmllib/sgmllib.py "fixed sgmllib.py")
and I'd really appreciate if users of sgmllib could give it a go (that
includes users of htmllib and BeautifulSoup).

**Update:** As suggested I've added an [updated
version](http://markos.gaivo.net/examples/sgmllib/test_sgmllib.py "Test cases for new library")
of test\_sgmllib.py, which includes an example where the old library
fails and new one doesn't.

**Update 2**: It
[seems](http://markos.gaivo.net/blog/?p=142#comment-1120) this is valid,
even required SGML behavior.

