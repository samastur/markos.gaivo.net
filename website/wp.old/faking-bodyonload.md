Title: Faking body.onload
Date: 2006-02-19 11:57
Author: markos
Category: Javascript, Web
Slug: faking-bodyonload

Here's a small Sunday tip for Javascript novices.

If you're following best development practices, then you're putting your
Javascript code in a separate file. Because you can't know which part of
a document will load first, you can't trigger javascript execution using
a body.onload handler. Most of the time it's good enough if we use
window.onload.

However, there is a workaround for times, when this is not good enough.
All you have to do is use a function like this:

<codeins ="bodyonload"></codeins>

The idea is very simple. Body element doesn't exist until HTML is loaded
and parsed. When Javascript is loaded, it checks for existence of body
element every 100 milliseconds and delays the execution until it exists.

