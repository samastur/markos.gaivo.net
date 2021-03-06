Title: Laughable Javascript security
Date: 2013-07-11 22:57
Author: markos
Category: Django, Javascript, Web
Tags: cloaking, Web, Security, Javascript
Slug: laughable-javascript-security
Status: published
Id: 1119

<div>
 <p>
  Building a secure web application is not easy, unless you also use 3rd party code such as Facebook’s Like widget in which case it is impossible. What you have is just an illusion of security, a door to abuse that you can’t even check if it is currently closed.
 </p>
 <p>
  Or that’s what I thought for years. A once substantiated belief that grew into an almost dogmatic certainty until I recently got a chance to revisit it when trying to design a secure Javascript-based web application living inside of a likely untrusted environment.
 </p>
 <p>
  There are obvious things you can do to protect your application such as delivery over secure connections and use of anonymous functions to sandbox your code from outside interference. However you will probably need to interact with external code at some point in which case is that
  <em>
   XMLHTTPRequest
  </em>
  object you are using really the built-in one or has it been replaced (cloaked) with an impostor object to perform
  <a href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack">
   the man-in-the-middle attack
  </a>
  ?
 </p>
 <p>
  I don’t know of a way to check if an object is untouched. What is sometimes used instead is a
  <em>
   .toString
  </em>
  method which on functions and methods returns their source unless they are native to browser in which case it returns a string saying so.
 </p>
 <p>
  Since you can replace any attribute and method on any object some
  <a href="http://stackoverflow.com/questions/6598945/detect-if-function-is-native-to-browser#comment8044242_6599105">
   go even further
  </a>
  in search of a certainty and use
  <em>
   .toString
  </em>
  from the
  <em>
   Function
  </em>
  object.
 </p>
 <p>
  At first thought that looked clever until I came up with:
 </p>
 <ol class="code">
  <li>
   <code>
    &lt;!DOCTYPE HTML&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;html lang="en"&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;head&gt;
   </code>
  </li>
  <li class="tab1">
   <code>
    &lt;meta charset="UTF-8"&gt;
   </code>
  </li>
  <li class="tab1">
   <code>
    &lt;title&gt;Break check if function is native&lt;/title&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;/head&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;body&gt;
   </code>
  </li>
  <li class="tab1">
   <code>
    &lt;script&gt;
   </code>
  </li>
  <li>
   <code>
    (function () {
   </code>
  </li>
  <li class="tab1">
   <code>
    var toS = Function.prototype.toString,
   </code>
  </li>
  <li class="tab2">
   <code>
    pM_str = window.postMessage.toString();
   </code>
  </li>
  <li>
  </li>
  <li class="tab1">
   <code>
    Function.prototype.toString = function () {
   </code>
  </li>
  <li class="tab2">
   <code>
    return this === window.postMessage ? pM_str : toS.call(this);
   </code>
  </li>
  <li class="tab1">
   <code>
    }
   </code>
  </li>
  <li class="tab1">
   <code>
    window.postMessage = function () { console.log('Fake'); };
   </code>
  </li>
  <li>
   <code>
    })();
   </code>
  </li>
  <li class="tab1">
   <code>
    &lt;/script&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;/body&gt;
   </code>
  </li>
  <li>
   <code>
    &lt;/html&gt;
   </code>
  </li>
  <li>
  </li>
  <li class="download">
   Download this code:
   <a href="http://markos.gaivo.net/blog/code/nativecheck.txt" title="Download the above code as a text file">
    /code/nativecheck.txt
   </a>
  </li>
 </ol>
 <p>
  The code above replaces
  <em>
   Function’s .toString
  </em>
  method with a one that lies when executed on an also cloaked
  <em>
   window.postMessage
  </em>
  . Instead of displaying source of the new
  <em>
   postMessage
  </em>
  it prints whatever browser would print for the original one.
 </p>
 <p>
  It simultaneously demonstrates how you can cloak native Javascript objects and hide that you are doing it. If you put malicious code into an anonymous function and remove
  <em>
   &lt;script&gt;
  </em>
  node that added it after it gets executed, then there is no way for scripts loading later to know that it happened. There will be no traces of crime.
 </p>
 <p>
  It might be difficult to cloak literals like {} and [], but you certainly can their methods so even if your code is wrapped in an anonymous function, it isn’t really secured from outside peeking and poking. Hence you even
  <strong>
   can’t trust your own code
  </strong>
  .
 </p>
 <p>
  Turns out that this particular dogma is also true. Depressing.
 </p>
</div>
