Title: Framestack technique  and accessibility
Date: 2005-08-27 18:40
Author: markos
Category: Javascript
Slug: framestack-technique-and-accessibility

I like to spend my vacation as far from crowds as possible and Ireland
was perfect spot for this. Sadly I had to stay connected to my work this
year so I had my laptop with me. However, we often stayed at places,
where we could forget a broadband connection and could be happy to catch
a GSM signal.

So I spent a lot of time being connected over GPRS and quickly started
to dislike huge pages that take ages to load (if they don't timeout) and
cost you a fortune. It seemed to validate our decision to make our
interfaces as fast and small as possible and to do this by **loading
data only when needed and never twice**.

We became convinced we’ll need frames to do that or one huge page to
store
everything.^[1](#fmstck1-2005-08-27)<a name="fmstck01-2005-08-27"></a>^
Since we were under false impression that accessibility went out of the
window with Javascript, we tried to push things as far as possible and
frames seemed a more manageable and less evil way of doing things.

**Description of approach**

The idea was simple. Load parts of UI in separate frames, when you first
need it and switch to it later, if you need it again. Switching is done
by manipulating cols/rows attribute of frameset node by setting a value
that hides all frames except the one you want to show, which of course
occupies whole available space. You can
[download](http://markos.gaivo.net/examples/framestack.zip) or [look
at](http://markos.gaivo.net/examples/framestack/ "Framestack demo") a
simple demo and study it at your leisure.

*This is just a technical demo that works in Firefox and Safari and
takes certain liberties when it comes to achieving its goals. Real
implementation would necessarily be more complicated and if there's
enough interest, will be a subject of a separate article.*

Those not interested in technical details of the approach can just
proceed to the next section.

Everything of interest is happening in index.html, which defines frames
for this demo and also contains Javascript needed to enable it. Relevant
part of HTML:  
<codeins ="framestack1"></codeins>

It probably doesn't need much explanation, since it just defines
frameset with 3 frames, assigns IDs to them and uses frameborder
attribute to hide borders. For some reason I had to use non-standard
frameset frameborder to really get rid of all borders. It loads and
displays second frame and loads stub pages in first and third frame.

Now we just need a following Javascript function:  
<codeins ="framestack2"></codeins>

It takes an ID of a frame to which we are switching as an argument,
first makes a sanity check and then initializes a few variables. Action
holds a reference to frameset and variable frame has a reference to the
new frame. We also have to check if we actually have those references,
since it doesn't make sense to proceed if we don't.

Then we loop through frames and set size of each to 0, unless we found
the right frame. We first maximize its size and then check, if the frame
has been loaded yet. We use frameID plus html extension as an easy way
to connect frame with its filename, but could make this more complicated
if needed. In case it hasn't been loaded yet (its source is a different
file), we load it.

**Analysis**

Benefits of this approach:

-   fast
-   smaller files which are loaded when needed result in cheaper use
    when bandwidth is metered (e.g. GPRS in most of Europe)
-   keeps state since it leaves hidden pages intact, which at least for
    us is more often than not the preferred behavior (clearly seen in
    demo by paying attention to dates)

Downsides of this approach:

-   it's most likely unaccessible
-   it doesn't work at all without Javascript
-   can't bookmark and other reasons against frames in general

And this is where I cry for help. Jaws is prohibitively expensive, so
I'd really appreciate anyone capable of doing so to try provided demo in
a screen reader and report his findings. I don't expect good news, but
would like to know how bad it really is.

I'd also appreciate any ideas on how to make this thing actually
accessible. I don't see how I could come to this approach by following
Jeremy's advice of first building an html version of a tool and then
improve it with
Javascript.^[2](#fmstck2-2005-08-27)<a name="fmstck02-2005-08-27"></a>^
Hence I don't know how to backtrack to that happy state either.

Author of the first solution will receive a book of his/her choice, a
drink on me when we meet and my eternal gratitude.

Notes:

1.  <a name="fmstck1-2005-08-27"></a>Of course we were wrong. There are
    other approaches to load HTML and Javascript dynamically. However,
    with all to me known techniques you keep more or less same problems
    as with framestack approach and result is arguably more difficult to
    maintain. The only thing in my opinion that might make such
    approaches worth while is, if it’s more accessible and that I
    honestly don’t know. [↑](#fmstck01-2005-08-27)
2.  <a name="fmstck2-2005-08-27"></a>I do think his advice is sound and
    shouldn't be lightly or often discarded. [↑](#fmstck02-2005-08-27)

