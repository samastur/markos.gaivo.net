Title: Generating Python Exceptions Classes
Date: 2008-07-22 09:39
Author: markos
Category: General development, Python
Tags: Class, Class, Exceptions, Exceptions, Languages, Languages, Programming, Programming, Python, Python
Slug: generating-python-exceptions-classes
Status: published
Id: 281

<html>
 <body>
  <div>
   <p>
    It’s been a while since I used
    <a class="zem_slink" href="http://www.python.org/" rel="homepage" title="Python (programming language)">
     Python
    </a>
    for anything larger than scripts few tens lines long, so it feels really great to do it again. I did discover however that I became a bit rusty. Not so much in not being able to achieve what I want as not being sure that I do it in a sensible and pythonic way.
   </p>
   <p>
    I’ve been working on a private project where I came to a following problem.
    <a class="zem_slink" href="http://en.wikipedia.org/wiki/Application_programming_interface" rel="wikipedia" title="Application programming interface">
     API
    </a>
    calls can trigger various responses, somewhat like
    <a class="zem_slink" href="http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol" rel="wikipedia" title="Hypertext Transfer Protocol">
     HTTP
    </a>
    , containing status codes together with a short description. Every faulty response should trigger its own exception, which led me to my first implementation:
   </p>
   <pre><code>
class Unauthorized(Exception):
    status = 101
    value = "Unauthorized."
</code></pre>
   <p>
    I didn’t like it even though it looks and behaves like it should. What I wanted was a better overlook of possible responses in a way where I have to make any possible changes easily and only at one place.
   </p>
   <p>
    My
    <a href="http://markos.gaivo.net/examples/pyexceptions/exceptions1.txt" title="Example">
     second attempt
    </a>
    was auto-generating exception classes using type. Since class definition took only a line instead of three, it certainly achieved better transparency, but I still had to make changes at two places.
   </p>
   <p>
    <a href="http://markos.gaivo.net/examples/pyexceptions/exceptions2.txt">
     Final step
    </a>
    was to auto-generate classes in a loop. To do this I attached them to module namespace using globals() dictionary. Actually I used __builtin__ one at first, but it obviously didn’t work that great.
   </p>
   <p>
    So this is what I have now. It works and achieves my goals. I only need to change dictionary to add a new response or change existing one and it could hardly be more readable.
   </p>
   <p>
    But is it pythonic enough? If not, what would be, apart from traditional way described in first step?
   </p>
   <div class="zemanta-pixie" style="margin-top: 10px; height: 15px;">
    <a class="zemanta-pixie-a" href="http://reblog.zemanta.com/zemified/67741c44-cb65-4003-8f66-f8ceb221a025/" title="Zemified by Zemanta">
     <img alt="Zemanta Pixie" class="zemanta-pixie-img" src="http://img.zemanta.com/reblog_e.png?x-id=67741c44-cb65-4003-8f66-f8ceb221a025" style="border: medium none; float: right;"/>
    </a>
   </div>
  </div>
 </body>
</html>