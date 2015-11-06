Title: The callee is not available
Date: 2006-05-24 13:38
Author: markos
Category: Javascript
Slug: the-callee-is-not-available

Sometimes you get this feeling of really mastering a technology. As if
nothing can surprise you and you've seen it all. If you're lucky, you'll
get a message like this before you become too cocky:

> Error: The callee (server [not server application]) is not available
> and disappeared; all connections are invalid. The call did not
> execute.

Do you know what it means? Neither did I, but somebody else
[did](http://www.thescripts.com/forum/post297987-2.html):

> It occurs in the context of pages using javascript to generate page  
>  content and communicate between windows, one of which windows is
> closed.
>
> Possibly  
>  \* page A pops up page B in the link and page B wants to communicate
> with  
>  page A, but page A has been closed (possibly by you or a popup
> killer?), or  
>  \* Internet Explorer has become totally confused and it will work in  
>  another browser, or  
>  \* poor page design.

Or in my case forgetting Javascript passes references when assigning
objects which become null, if referenced object was stored in now
defunct window. The problematic browser in question was of course
Internet Explorer.

