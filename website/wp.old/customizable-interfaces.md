Title: Customizable interfaces
Date: 2006-03-23 20:32
Author: markos
Category: Javascript, UI, Web
Slug: customizable-interfaces

There's a vast number of potential Marela features that we are able, but
not willing to implement, since they are detrimental to our design
goals. There are also many, which we are willing and will implement, but
it doesn't change the fact that there will always be parts where we
won't compromise.

Still, even though it seems natural that benefits to many should be more
important than benefits to few, I never got quite comfortable with this.
That's why we also want to make Marela as open as possible to let our
members customize it without affecting other people.

First, there are public APIs. They tend to work well for building new
tools or interfaces, but offer little help in customizing existing ones.
Which is what our users want most of the time.

Every modern browser lets users define a custom style sheet to change
the presentation of websites. That's why we recently added ID to body
element, which lets users more [easily
customize](http://archivist.incutio.com/viewlist/css-discuss/13291) the
look of Marela alone.

Then there are tools like
[Greasemonkey](http://greasemonkey.mozdev.org/), which let proficient
users using Mozilla based browsers customizing existing interfaces.
Greasemonkey works quite well, if you're proficient in Javascript.

I think the biggest problem with Greasemonkey (and custom CSS for that
matter) is that it's tied to a browser and a computer. If you change
either of them, your customization won't work anymore without
significant effort on your part. Sometimes, in restricted environments,
it's not even possible to make it work. It's a bit easier to make and
transfer CSS customizations, but you're still forced to carry your file
around.

I'm not too bothered with CSS. I simply don't see much need for it
beyond what Marela's design and modern browsers already offer and I'm
still biased against skin-deep themes offered by some programs. In any
case a possible solution for it would be practically the same as what I
have in mind for a case that does trouble me.

Idea is pretty simple. Define javascript hooks that get called after
window.onload event when they exist. If there's an easy way to add your
javascript file to a page (say, by uploading it to our server), then you
can create a simple, but cross-browser and cross-computer Greasemonkey.

Question that remains is, is this appealing enough for you to use it?

