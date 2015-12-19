Title: Scaling image buttons
Date: 2005-09-28 10:53
Author: markos
Category: Web
Slug: scaling-image-buttons
Status: published
Id: 31

<div>
 <p>
  There’s one thing that really bothers me, when it comes to design of forms. Well, more than one really, but let’s limit this discussion to just one.
 </p>
 <p>
  Submit buttons.
 </p>
 <p>
  I can’t stand their look, especially geek chic design of early nineties presented in Firefox and its relatives. I guess industrial look and Motif widgets were never really my taste. But even more pleasant design of buttons in Safari can look out of place with some designs.
 </p>
 <p>
  There’s also an alternative that is often used. Image input buttons (type=image) can provide a more pleasant look, but they have one big disadvantage compared to submit buttons. They don’t scale. Not really something I’d want in an accessible interface.
 </p>
 <p>
  I used a hardly novel
  <a href="http://clagnut.com/sandbox/imagetest/" title="Clagnut's image tests">
   idea
  </a>
  of defining image measurements in relative units. Browsers usually don’t do this. They lay it out in original size using absolute values. Hence, when you change the size of fonts, the size of image stays the same. But if you use relative units, you get desired scaling effect. It might look like crap, but at least it can be readable for people with impaired vision.
 </p>
 <p>
  As you can see in simple
  <a href="http://markos.gaivo.net/examples/imgbutton/index.html">
   demo
  </a>
  , experiments with em’s haven’t worked really well. There are two distinct problems. First is to find the relative size that doesn’t stretch an image in either direction. Second, to do this in a cross-browser compatible way.
 </p>
 <p>
  My demo kind of works in Safari, but not really in Firefox and I have no idea about rest of the bunch. So, has anyone solved this problem?
 </p>
 <p>
  <em>
   Update: I managed to get a better result. You can read about it
   <a href="scaling-image-buttons-part-2.html">
    here.
   </a>
  </em>
 </p>
</div>
