Title: Hiding form buttons as text
Date: 2005-12-02 15:49
Author: markos
Category: Spletne urice, UI, Web
Slug: hiding-form-buttons-as-text
Status: published
Id: 84

<html>
 <body>
  <div>
   <p>
    I love going to our weekly web talks not so much for the talks themselves (although they are great), but conversations you get to have there. A part of a recent one rendered from memory and shortened for readers pleasure:
   </p>
   <blockquote>
    <p>
     <strong>
      Fry:
     </strong>
     Those delete strings of yours should really be post requests.
     <a href="http://webaccelerator.google.com/" title="Link to web accelerator that shouldn't be used">
      GA’s
     </a>
     pre-fetching might destroy user’s data.
     <br/>
     <strong>
      Me:
     </strong>
     &lt;beeeeep&gt; Google. RFC says should not must.
     <br/>
     <strong>
      Fry:
     </strong>
     Well, since it also says multiple GET requests should yield same result, it really is a must for delete.
     <br/>
     <strong>
      Me
     </strong>
     (not ready to give up): True, but so many form buttons will look like crap.
     <br/>
     <strong>
      Fry:
     </strong>
     Well, you can hide them by removing border, setting background-color to background and fixing font size to 1 em.
     <br/>
     <strong>
      Me:
     </strong>
     Uhm, this might work, but probably doesn’t, because browsers use controls from operating system.
     <br/>
     <strong>
      Fry:
     </strong>
     Well, try it.
    </p>
   </blockquote>
   <p>
    I may be stubborn, but I’m not a complete moron. So I did and here’s
    <a href="http://markos.gaivo.net/examples/hidebutton.html" title="Demo">
     the result
    </a>
    .
   </p>
   <p>
    As can be seen, it works beautifully in Firefox (1.0+) and Opera 8 (I share my visitors indifference to earlier versions). It doesn’t work in Safari at all, but since its buttons are not obnoxiously ugly, I can live with that.
   </p>
   <p>
    However, it has unseemly big padding in Internet Explorer, which is the real deal-breaker for now.
   </p>
   <p>
    I think demo’s style sheet is pretty self explanatory, but here’s what I did by mostly following Fry’s instructions:
   </p>
   <ul>
    <li>
     set border to 0
    </li>
    <li>
     same for padding and margin
    </li>
    <li>
     set background-color of the button to the same value as background of the document
    </li>
    <li>
     did the same for color of text
    </li>
    <li>
     set the size of button text to 1 em so it’s displayed in right size in every browser
    </li>
    <li>
     set cursor to pointer, since it’s not done automatically for buttons
    </li>
   </ul>
   <p>
    <a href="http://www.friedcellcollective.net/" title="Fry's web home">
     Fry
    </a>
    was also correct that bold and italics work and underline doesn’t, but you can simulate later with border-bottom. Except in IE of course, on account of padding.
   </p>
   <p>
    There’s another shortcoming to consider. If background is an image or a color gradient instead of a solid color, this trick won’t work.
   </p>
   <p>
    So, any ideas about what to do with IE?
   </p>
  </div>
 </body>
</html>