Title: When to use AJAX
Date: 2005-11-11 19:10
Author: markos
Category: Javascript, Spletne urice, Web
Slug: when-to-use-ajax
Status: published
Id: 62

<div>
 <p>
  Wednesday’s conversation with
  <a href="http://www.friedcellcollective.net/">
   Fry
  </a>
  provoked me to think more about where and when to use AJAX. I thought I’ve got it figured it out, but I’ve discovered that my opinions don’t really match my behavior and I find this a problem.
 </p>
 <p>
  AJAX rage of 2005 hasn’t brought many articles exploring benefits and downsides to AJAX. There were few, even very good ones, but I’d like to see more of them and less articles describing latest gimmick or service which would probably be overlooked if it didn’t use an AJAX trick or two.
 </p>
 <p>
  I had a dentist appointment today, something I’m sure everyone looks forward to, which at least provided me with ample time to think about this. My basic premise was that we should use technology that already works and use AJAX to build on top of that.
 </p>
 <p>
  Since basic web model has been around for a long time, is well understood and mostly works, I tried to look at places where it doesn’t or at least not as it should and came to a short list of possible criteria for choosing when to apply AJAX:
 </p>
 <ul>
  <li>
   <strong>
    Browsers ought to support this, but mostly can’t or don’t.
   </strong>
   Example: autosave support for textarea, which is the most requested feature among my friends.
  </li>
  <li>
   <strong>
    Browsers support it, but badly.
   </strong>
   Example: progress bar for uploads. I don’t know why you can get a usable dialog for downloads, but you’re out of luck if you want to upload.
  </li>
  <li>
   <strong>
    Connection problems (narrow bandwidth or high latency).
   </strong>
   If this is a known, but otherwise unsolvable problem, AJAX can be used to reduce ammount and frequency of traffic.
  </li>
 </ul>
 <p>
  Have I forgot anything else?
 </p>
 <p>
  I don’t think these are only valid scenarios for AJAX use, but we did discover that fast serving of well designed pages greatly reduces the need for AJAX.
 </p>
</div>
