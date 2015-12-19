Title: Javascript accessibility woes - part 1
Date: 2005-06-14 19:44
Author: markos
Category: Javascript
Slug: javascript-accessbility-woes-part-1
Status: published
Id: 4

<div>
 <p>
  It’s been really great talking to
  <a href="http://www.andybudd.com/">
   Andy
  </a>
  ,
  <a href="http://www.adactio.com">
   Jeremy
  </a>
  ,
  <a href="http://www.kryogenix.org/">
   Stuart
  </a>
  and
  <a href="http://www.boxofchocolates.ca/">
   Derek
  </a>
  at javascript get-together and they certainly convinced me that I could and should do more to make my web applications accessible. However after a few days of thinking, I still have issues that seem to lack a good solution.
 </p>
 <p>
  First of them is
  <em>
   window.onload
  </em>
  .  Ppk already
  <a href="http://www.quirksmode.org/blog/archives/2005/06/11_june_london.html">
   explained
  </a>
  the problem quite well. There’s also a workaround, which I admit I’m using right now, and that is to have an inline event handler on body tag.  There are only two problems with this approach:
 </p>
 <ol>
  <li>
   inline event handlers are even more despised than inline CSS styles
  </li>
  <li>
   we are mixing XHTML/HTML with Javascript, which is a no-no as well
  </li>
  <li>
   it doesn’t really work if you don’t have at least a simple function to check and handle, if external javascript code has been loaded yet
  </li>
 </ol>
 <p>
  Personally, I think all points make a lot of sense when not taken to extreme. I sincerely doubt that webpage/application suffers a lot, if this is the only inline event handler in the whole document and inlined code in head is kept to minimum. We often use CSS to add behavior (a:hover), where it just makes sense and I think we should be able to use inline Javascript on occasions as well.
 </p>
 <p>
  In my case, I’m living in a country, where majority of users are still on a dial-up and most of them will stay there for a while. Since parts of my application can fetch 20 or more 5-10K sized images on a single page, I don’t want to force users to wait 20 seconds or more before application starts to behave reasonably. I also can’t rely on x/html layer behavior because of framestack javascript technique and their problems, about which I plan to write more in the following few days.
 </p>
 <p>
  The only other alternative I see right now is to hide UI by default and display it using Javascript, which is hardly an improvement. If anything, it’s a step back.
 </p>
 <p>
  I guess I’m in this mess because I didn’t build an html version first and upgraded it with Javascript. Why this happened and how come I don’t think it was necessarily a bad thing, is a topic for another day. But it certainly left me with a puzzle to solve.
 </p>
 <p>
  So, any ideas, apart from obvious one of having a working html version with added javascript?
 </p>
 <p>
  <strong>
   Update:
  </strong>
  Ppk
  <a href="http://www.quirksmode.org/blog/archives/2005/06/you_shouldve_be_1.html">
   does
  </a>
  .
 </p>
</div>
