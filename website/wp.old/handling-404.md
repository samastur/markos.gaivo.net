Title: Handling 404
Date: 2006-11-08 12:31
Author: markos
Category: General development, Web
Slug: handling-404

This blog doesn't use descriptive URLs, which is not the only time I
screwed this up for no good reason. In this case it was mainly laziness
and smug i-don't-care-if-people-find-me attitude, but I hadn't really
realized how stupid this decision was until I started thinking about the
problem of missing pages (error 404).

It always bugged me how useless most 404 pages are. Sure, I could notify
the webmaster about a broken link, but that won't help me find what I'm
looking for. Can't we do better than that?

As it happens we often can. There's an unlimited number of ways in which
visitors can fail to reach their destination, but majority of them
probably fall in four categories:

-   content moved elsewhere
-   broken links
-   typos
-   bad memory recall

**Content moved elsewhere**

Many believe that pages should be permanent and links shouldn't break
over time. Yet sometimes we either have little control over this or
there are good reasons for breakage. We should still try to mitigate
such situation by guiding visitors to correct new location when
possible.

This is done with HTTP redirects. If content was moved only temporary,
then response should have a status code of 302 and contain a link in the
header to correct current address. If move was permanent, then the same
thing is achieved with code 301.

Missing pages amount to around 0.6% of hits on this website. They would
be around 8% if redirects weren't used.

**Broken links**

Broken links appear when email clients break URL longer than maximum
line length or from botched copy operation. This usually means that
address is cut off and part we have is incomplete, but otherwise
correct. Handling such links can range from trivial to impossible. Let's
look at one Wikipedia link as an example:

<http://en.wikipedia.org/wiki/Longest_common_subsequence_problem>

Let's say that link was broken near the end of it and there was *lem*
missing in *problem*. Resulting address might not be complete, but there
probably aren't that many Wikipedia articles where such string forms
first part of their address and it would be reasonable to assume that
Wikipedia could find the right article. Alas it doesn't.

On the other side of the spectrum are impossible or almost impossible
guesses. If address was broken anywhere before *Longest*, then we could
learn nothing from it about visitors expectations. This would look like
a good place to give up.

However, if we are lucky, then our visitors came from one of popular
search engines, which means their referrer attribute includes search
string that led to our page. We can extract those keywords, use them and
hopefully find that page or failing that offer a list of related pages.
Not perfect, but beats plain "Not here" sign.

<strong>Typos

</strong>Typos are what happens when people use keyboards. I can't live
without one, but I still recognize that my fingers and my brain are not
always of the same mind about how to spell a word. Letters get added,
dropped or just switch places, all being a problem for a program that
usually looks for that one perfect match.

There's help. Edit distance algorithms, like
[Levenshtein's](http://en.wikipedia.org/wiki/Levenshtein_distance "Description of Levenshteins algorithm"),
can be used to measure how similar two strings really are. Matching then
becomes finding the page with shortest distance from a list of its
closest neighbors.

Downside is that algorithm is fairly computationally expensive and it
might take time to find a match. I'll explore this problem in tomorrows
article.

**Bad memory requests**

The main purpose of descriptive URLs is the same as catchy domain names.
Make it easy to remember address for later use, when bookmarks or
browsers autocomplete can't be used.

But memory is notoriously unreliable and it doesn't work any better with
web addresses. So addresses used may vary enough from the right one that
they don't get caught with edit distance algorithms. As an example,
someone might try to access aforementioned Wikipedia's article with:

http://en.wikipedia.org/wiki/Longest\_subsequence\_problem

Calculated distance between this address and the real one is 7, which is
probably more than would be real limit for matching. We can still look
at referrer for clues, but we can also use requested address. In our
case, we can extract keywords *longest*, *subsequence* and *problem* and
use them to search for possible hits. Wikipedia doesn't do this either,
but neither do I, so I shouldn't complain.  
**Time to wrap it up**

I believe this approaches make a good case for logical and descriptive
addresses, since most of them don't work (well) otherwise. If someone
requests an article with a nonexistent ID 145, it's impossible to
resolve which of existing ones with IDs 155, 245 or 149 he really
wanted.

Still, sometimes descriptive addresses are not an option. I'd love to
hear ideas or practical experience of how to handle such cases.

