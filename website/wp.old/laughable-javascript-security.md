Title: Laughable Javascript security
Date: 2013-07-11 22:57
Author: markos
Category: Django, Javascript, Web
Slug: laughable-javascript-security

Building a secure web application is not easy, unless you also use 3rd
party code such as Facebook's Like widget in which case it is
impossible. What you have is just an illusion of security, a door to
abuse that you can't even check if it is currently closed.

Or that's what I thought for years. A once substantiated belief that
grew into an almost dogmatic certainty until I recently got a chance to
revisit it when trying to design a secure Javascript-based web
application living inside of a likely untrusted environment.

There are obvious things you can do to protect your application such as
delivery over secure connections and use of anonymous functions to
sandbox your code from outside interference. However you will probably
need to interact with external code at some point in which case is that
*XMLHTTPRequest* object you are using really the built-in one or has it
been replaced (cloaked) with an impostor object to perform [the
man-in-the-middle
attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)?

I don't know of a way to check if an object is untouched. What is
sometimes used instead is a *.toString* method which on functions and
methods returns their source unless they are native to browser in which
case it returns a string saying so.

Since you can replace any attribute and method on any object some [go
even
further](http://stackoverflow.com/questions/6598945/detect-if-function-is-native-to-browser#comment8044242_6599105)
in search of a certainty and use *.toString* from the *Function* object.

At first thought that looked clever until I came up with:  
<codeins ="nativecheck"></codeins>

The code above replaces *Function's .toString* method with a one that
lies when executed on an also cloaked *window.postMessage*. Instead of
displaying source of the new *postMessage* it prints whatever browser
would print for the original one.

It simultaneously demonstrates how you can cloak native Javascript
objects and hide that you are doing it. If you put malicious code into
an anonymous function and remove *\<script\>* node that added it after
it gets executed, then there is no way for scripts loading later to know
that it happened. There will be no traces of crime.

It might be difficult to cloak literals like {} and [], but you
certainly can their methods so even if your code is wrapped in an
anonymous function, it isn't really secured from outside peeking and
poking. Hence you even **can't trust your own code**.

Turns out that this particular dogma is also true. Depressing.

