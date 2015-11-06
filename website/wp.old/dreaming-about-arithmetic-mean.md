Title: Dreaming about arithmetic mean
Date: 2010-01-24 11:44
Author: markos
Category: General development, Javascript
Slug: dreaming-about-arithmetic-mean

I had a crazy dream, where I was back at University, but this time
studying computer science. We were writing a function to calculate an
[arithmetic
mean](http://en.wikipedia.org/wiki/Arithmetic_mean "Arithmetic mean") of
an array of numbers. A task obviously too simple for college course, but
with dreams you get what you are given.

Discussion started with this function:

<codeins ="dreamjs"></codeins>

Dream me, who by the way is significantly more bitchy than I ever am,
wasn't pleased and thought he could save few bytes by storing counter
and sum inside of the array:

<codeins ="dreamjs2"></codeins>

This looked ugly, but what bothered him (me?) was more that it also had
a bug. Integer in
[Javascript](http://en.wikipedia.org/wiki/JavaScript "JavaScript") is
limited to 2^53^, which is a lot, but sum can still
[overflow](http://en.wikipedia.org/wiki/Arithmetic_overflow "Arithmetic overflow")
or underflow it. Since mean can never be smaller than smallest or bigger
than biggest number in a list, I could fix it by writing:

<codeins ="dreamjs3"></codeins>

End of dream. Everything edited for sanity and brevity.

I don't have much to say about second program except that I would never
write something so ugly just to save 16 bytes in a function like this. I
wouldn't even use Javascript if memory was that important.

I am more intrigued by third program. Bug in second is definitely there,
even though few of us operate with numbers big enough to encounter it.

It's interesting, because if I was awake, I would probably never think
of it. I used to worry about bugs like this all the time, when I was
coding in C. It was an unavoidable consequence of the language.

I guess what I am getting at is that it is nice to code in a high-level
language and for the most part not think about implementation details
like this, but only as long as you actually know them so your brain gets
triggered when they matter. Speaking of details, I bet those divisions
can cause rounding errors.

<div class="zemanta-pixie">

[![Reblog this post [with
Zemanta]](http://img.zemanta.com/reblog_e.png?x-id=7ab2d445-07ff-4ec6-bed9-f29a2797d7a3)](http://reblog.zemanta.com/zemified/7ab2d445-07ff-4ec6-bed9-f29a2797d7a3/ "Reblog this post [with Zemanta]")<span
class="zem-script paragraph-reblog"></span>
<script type="text/javascript" src="http://static.zemanta.com/readside/loader.js" defer="defer"></script>
</span>

</div>
