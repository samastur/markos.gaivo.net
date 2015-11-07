Title: Latency, bandwidth and speed of applications - part I
Date: 2005-09-14 21:10
Author: markos
Category: General development, Javascript, Python
Slug: latency-bandwidth-and-speed-of-applications-part-i
Status: published
Id: 23

<html>
 <body>
  <div>
   <p>
    It seems we’re back to discussing the importance of bandwidth and latency on perceived speed of application. In a way it’s amazing that after 10 years of widespread use of Internet and local networks, we developers still discuss these issues.
   </p>
   <p>
    So, what contributes to speed of execution in network applications?
   </p>
   <p>
    Each network request can be divided into seven time intervals:
   </p>
   <ol>
    <li>
     time needed to send a request
    </li>
    <li>
     latency, which is time spent for any amount of data to travel between client and server
    </li>
    <li>
     data transfer time
    </li>
    <li>
     time needed to process a request, form a response and send it
    </li>
    <li>
     latency again, but this time in other direction
    </li>
    <li>
     data transfer time for response
    </li>
    <li>
     time needed to process response and present result to user
    </li>
   </ol>
   <p>
    Sum of all these parts is time lapsed between issued command and presented result. How fast this needs to be depends on application and our experiences. For example, we expect faster response to our key presses in SSH client than we do waiting for search results.
   </p>
   <p>
    However, if this sum is under a quarter of a second, it will be generally regarded as instantaneous, but you really should aim for 1/10th of a second to satisfy even the most twitchy users.
   </p>
   <p>
    Usually, we might get to control all parts of this equation only when client and server are located on a local network and we develop both of them. So, a well behaving application needs to take in account environment in which it will run and act accordingly.
   </p>
   <p>
    This means, among other things, to give user feedback that something is happening whenever there is even a remote chance that response might take a while, to react sensibly to network disruptions (such as timeouts) and offer a way to abort user actions.
   </p>
   <p>
    So, how do we speed up the application itself?
   </p>
   <p>
    Absolutely the best way to speed up a network request is to not make one. The usual way to do this is to cache result over its life span and use it when possible.
   </p>
   <p>
    The other way, lately often mentioned in relation to AJAX, is to make our requests asynchronously. Unlike synchronous requests, which are direct results of user actions, asynchronous are those were data is transfered in expectation of future user actions.
   </p>
   <p>
    An example would be a mail program where we transfer message headers of yet unread mail in background before we actually need to display them to user, since it’s fairly likely that he’ll want to check them in near future.
   </p>
   <p>
    There are also downsides to this approach. It can be difficult to predict what to transfer next if no user action is more probable than rest. It can also incur significant costs if bandwidth is expensive as often is on GPRS networks in Europe. And when number of simultaneous connections is limited (HTTP allows 4, but not all browsers comply), it can occupy a resource when you need one.
   </p>
   <p>
    Still, it’s a useful tool when it can be applied.
   </p>
   <p>
    More about saving time with our seven intervals in part two due tomorrow.
   </p>
   <p>
    <em>
     Update: second part has been
     <a href="latency-bandwidth-and-speed-of-applications-part-ii.html" title="Second part">
      posted
     </a>
     .
    </em>
   </p>
  </div>
 </body>
</html>