Title: Updated sgmllib
Date: 2006-04-01 15:05
Author: markos
Category: Python
Slug: updated-sgmllib
Status: published
Id: 144

<html>
 <body>
  <div>
   <p>
    I
    <a href="sgmllibpy-parser-woes.html">
     wrote
    </a>
    about a sgmllib problem a few days ago. I still may be a dolt and my code certainly needed fixing, but the bug remained nevertheless.
   </p>
   <p>
    Hence I’ve made some small changes to sgmllib that fix problems I’ve had. New version, which passes all unit tests included in Python distribution, can be found
    <a href="http://markos.gaivo.net/examples/sgmllib/sgmllib.py" title="fixed sgmllib.py">
     here
    </a>
    and I’d really appreciate if users of sgmllib could give it a go (that includes users of htmllib and BeautifulSoup).
   </p>
   <p>
    <strong>
     Update:
    </strong>
    As suggested I’ve added an
    <a href="http://markos.gaivo.net/examples/sgmllib/test_sgmllib.py" title="Test cases for new library">
     updated version
    </a>
    of test_sgmllib.py, which includes an example where the old library fails and new one doesn’t.
   </p>
   <p>
    <strong>
     Update 2
    </strong>
    : It
    <a href="sgmllibpy-parser-woes.html">
     seems
    </a>
    this is valid, even required SGML behavior.
   </p>
  </div>
 </body>
</html>