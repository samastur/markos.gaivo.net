Title: Simplifying registration forms
Date: 2008-12-29 07:30
Author: markos
Category: Javascript
Tags: forms, Web, Javascript, UI, Password
Slug: simplifying-registration-forms
Status: published
Id: 312

<div>
 <p>
  As I am leaving on a short vacation that will probably take me off grid for few days, there is still a time for a hopefully short, but definitely last post of this year. I don’t like how registration forms ask me twice for password and I think I can offer a better way.
 </p>
 <p>
  Most registration forms these days still want you to type password of your choice twice. They probably do it to reduce risk of mistyping it. I deeply dislike Facebook, but I think this is one thing it
  <a href="http://www.facebook.com/" title="Registration form on Facebook's homepage">
   got right
  </a>
  . You only have to do it once. Those with FB accounts can see this in action if they log out for a moment and visit front page.
 </p>
 <p>
  There are several reasons why once is enough. First one is that every decent page provides a way to reset password in case you have forgotten it. So even if password was mistyped, it’s easy to reset it again to a different value. Second reason is that by now it’s quite well known that most people use a low single-digit number of passwords and don’t come up with a new one each time they are asked to do so. Hence it’s quite unlikely they’ll make an error now after so much practice.
 </p>
 <p>
  Third reason is that in most cases you can
  <a href="http://markos.gaivo.net/examples/html_pattern/onepass.html" title="Demonstration of show password switch">
   help them
  </a>
  <a href="http://markos.gaivo.net/examples/html_pattern/onepass.html" style="font-size: 29.25px; line-height: 42.75px;" title="Demonstration of show password switch">
  </a>
  .
 </p>
 <p>
  When registration forms first appeared internet access was rare and expensive enough that most common environment in which it was used was work or school. It was therefore likely that when you were registering for a service, you weren’t alone and entered password had to be hidden from people around you. Today it’s probably opposite. Most of the time I am quite private and could see what I type with no additional security risk.
 </p>
 <p>
  So as in demo we could offer a switch that let visitors see what they are typing if they choose to do so. It should still be hidden by default, since we can’t really tell the environment visitor is in or if Javascript is available. It is always better to err on side of safety.
 </p>
 <p>
  As a side note for those who might have peaked at implementation. I’m replacing password input field because of Internet Explorer, which doesn’t tolerate type attribute change on input fields. Every other browser tested (FF, Opera, Safari and Chrome) would work perfectly fine by just switching field type from password to text.
 </p>
 <p>
  Anyhow, that’s it for this year. If you leave a comment, which I hope you will, and I don’t answer, it’s because I lack Internet access.
 </p>
</div>
