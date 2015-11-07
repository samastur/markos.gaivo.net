Title: Preventing download of javascript on mobile web
Date: 2006-10-29 21:55
Author: markos
Category: Javascript, Web
Slug: preventing-javascript-download-on-mobile-web
Status: published
Id: 209

<html>
 <body>
  <div>
   <p>
    Every year I spend a few weeks somewhere where internet connection is either slow or metered and expensive. Usually it’s both which makes me rather twitchy when it comes to big web page sizes. Yet I’m also certain that my new web home, however it may turn out at the end, will have a significant chunk of it written in Javascript. None of it necessary for working, but more than I’d probably like to download over flimsy mobile phone connection.
   </p>
   <p>
    The problem are not really old mobile browsers which don’t support Javascript. They won’t download any of it anyway. The question is how to prevent eager browsers, who would, from downloading this stuff when you don’t want them to. My first, rather primitive attempt was
    <a href="http://markos.gaivo.net/examples/envcheck/index.html" title="Demo of javascript ondemand loading depending on media">
     this demonstration
    </a>
    , which only works in Opera 9, Safari and Firefox, but most certainly doesn’t work in all browsers.
   </p>
   <p>
    What it does is check font size of a title and based on its value resolves which media style sheet was used. If it was
    <em>
     mobile.css
    </em>
    , which is used only when media is set to
    <em>
     handheld
    </em>
    , then it was probably done from a mobile environment, so it includes the mobile version of a Javascript or it could, if I wanted, none at all.
   </p>
   <p>
    There are several problems with this approach. First one is that it doesn’t recognize notebook users connecting over a  cellphone. It can’t really, since browser environment is literally the same, unless it would try to measure latency and bandwidth of page elements and guess from those results, which is neither easy nor reliable. 3G networks can be rather fast and have a better latency than a wired connection from somewhere like Tanzania.
   </p>
   <p>
    But let’s say we don’t care about this case. We can always turn Javascript off in Firefox if it’s important enough to us, which leads us to the next problem. Support for handheld media type is still rather spotty. If browser doesn’t support it, it may load the wrong style sheet if any at all and the wrong CSS value results in wrong turn in Javascript. However
    <em>
     handheld media
    </em>
    support is getting better. Since I decided from the start that my personal page is a good place where leading edge can also be a bit of bleeding one, that is good enough. On a different site this probably wouldn’t be true.
   </p>
   <p>
    So it sort of works in principle, but it is crude and error prone. Javascript check is not self-contained and I could easily break it by changing font size value of a title in CSS files while forgetting to do a corresponding correction in code. What would be much better is to learn from the browser which media types style sheets were actually used and act accordingly. Now that would be grand.
   </p>
   <p>
    There are two ways you could go about this. My first go was finding style nodes in DOM and looking at their
    <em>
     disabled
    </em>
    property, which is commonly used in style sheet switchers for turning sheets on and off. It doesn’t work, since ‘wrong’ media types in Firefox are ignored, not disabled. Their
    <em>
     disabled
    </em>
    value is still set to
    <em>
     false
    </em>
    .
   </p>
   <p>
    A proper way of doing it would be using DOM Style Sheets methods. Basic idea is to compare actual values as set in the page with values read from style sheets and resolving which ones were used. While not exactly trivial, by little forethought it can be made to work fine in Opera and Firefox. It can also work in Explorer using its own methods, but it’s a pain to make it  work in Safari, which in this case is not only an incompetent liar, it’s also lying in some weird accent. If you’d like to learn more about it, then there’s a
    <a href="http://www.howtocreate.co.uk/tutorials/javascript/domstylesheets" title="Problems with DOM Style Sheets use">
     great
    </a>
    page describing current state but the gist of it is that you can’t rely on methods being there and even when they are, in some form or another, they might not work reliably (Safari) or might produce weird results (yup, Safari again).
   </p>
   <p>
    Well, it could still work, but would require an unreasonable amount of code. Hence I made a different tradeoff, which can be seen
    <a href="http://markos.gaivo.net/examples/envcheck/index2.html" title="Second attempt">
     here
    </a>
    . A bit less automation for a lot less code. It keeps the idea of first demo with a small twist. First rule of every media style sheet targets the same element that gets created by Javascript if necessary and compares its font size value with those found in style sheets. It returns media types of all sheets where this value was found.
   </p>
   <p>
    The end result certainly isn’t perfect or pretty, but it keeps amount of bookkeeping to minimum and limited to CSS files. Even using a “safe” property like font size can lead to problems (e.g. 0.9em is sometimes interpreted as 0.90em), but nothing difficult to overcome.
   </p>
   <p>
    It might not be of production quality, but it will work as good starting point for further exploration.
   </p>
  </div>
 </body>
</html>