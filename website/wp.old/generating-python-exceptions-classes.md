Title: Generating Python Exceptions Classes
Date: 2008-07-22 09:39
Author: markos
Category: General development, Python
Slug: generating-python-exceptions-classes

It's been a while since I used
[Python](http://www.python.org/ "Python (programming language)") for
anything larger than scripts few tens lines long, so it feels really
great to do it again. I did discover however that I became a bit rusty.
Not so much in not being able to achieve what I want as not being sure
that I do it in a sensible and pythonic way.

I've been working on a private project where I came to a following
problem.
[API](http://en.wikipedia.org/wiki/Application_programming_interface "Application programming interface")
calls can trigger various responses, somewhat like
[HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol"),
containing status codes together with a short description. Every faulty
response should trigger its own exception, which led me to my first
implementation:

    class Unauthorized(Exception):
        status = 101
        value = "Unauthorized."

I didn't like it even though it looks and behaves like it should. What I
wanted was a better overlook of possible responses in a way where I have
to make any possible changes easily and only at one place.

My [second
attempt](http://markos.gaivo.net/examples/pyexceptions/exceptions1.txt "Example")
was auto-generating exception classes using type. Since class definition
took only a line instead of three, it certainly achieved better
transparency, but I still had to make changes at two places.

[Final
step](http://markos.gaivo.net/examples/pyexceptions/exceptions2.txt) was
to auto-generate classes in a loop. To do this I attached them to module
namespace using globals() dictionary. Actually I used \_\_builtin\_\_
one at first, but it obviously didn't work that great.

So this is what I have now. It works and achieves my goals. I only need
to change dictionary to add a new response or change existing one and it
could hardly be more readable.

But is it pythonic enough? If not, what would be, apart from traditional
way described in first step?

<div class="zemanta-pixie" style="margin-top: 10px; height: 15px;">

[![Zemanta
Pixie](http://img.zemanta.com/reblog_e.png?x-id=67741c44-cb65-4003-8f66-f8ceb221a025)](http://reblog.zemanta.com/zemified/67741c44-cb65-4003-8f66-f8ceb221a025/ "Zemified by Zemanta")

</div>
