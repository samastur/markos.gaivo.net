Title: In search of easy templating
Date: 2006-02-03 22:07
Author: markos
Category: Python, Web
Slug: in-search-of-easy-templating

I find it a bit amusing that when Python community is eagerly discussing
which web framework and approach to web is better, I come around looking
to do my very own thing.

I'm looking for web templating that would meet the following criteria:

-   is fairly easy to implement
-   is even easier to use for templates (goal: accessible to hobbyists)
-   doesn't require a web server to develop and test a web template
-   doesn't require to learn another templating language or keeps it to
    minimum

In short, I want to be able to write a web template in any decent (web)
editor under the sun and test it locally in my browser. I'm not looking
for anything fancy. I only have to be able to recognize hotspots and
support very simple iterators.

What I mean by hotspots is recognizing template elements that can be
changed (e.g. images whose *src* attribute can be changed for special
needs). Iterators should only be able to specify how many times they can
iterate.

My current approach to this is using XHTML elements and attributes.
Hotspots could be defined with *class* and *id* attributes and iterators
would be defined with *div* elements, since by default they leave the
layout alone. Specifying an iterator would be a case of applying a class
*templIterator* to an element and using a custom attribute like
*tmplTimes*, that would be stripped from final page.

I would plan to add *tmplComment* class to specify sections that would
be removed from resulting page, since this could be used to build and
test a page without iterator actually working.

An example:  
<codeins ="template1"></codeins>

In this example we have an unordered list where *li* elements can be
iterated 3 times. Second and third one are there only for testing
purposes and would be replaced by real elements from an iterator.
Hotspot class would be used to mark an image for manipulation.

I hope it's obvious what I'm trying to do, although knowing me I doubt
it. Can anyone see a problem with this approach or knows a better way to
meet my needs?

