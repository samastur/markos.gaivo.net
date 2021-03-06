Title: Using canvas and Javascript to blur images
Date: 2010-04-01 10:59
Author: markos
Category: Javascript, Web
Tags: function, canvas, Firefox, algorithm, image, blur
Slug: using-canvas-and-javascript-to-blur-images
Status: published
Id: 591

<div>
 <p>
  I admire the look and feel of
  <a href="http://www.mikematas.com/">
   Mike Matas’ new website
  </a>
  . It is really well thought through. I was also intrigued by how he did it, especially after getting a pop-up on my first visit advising me to use a more modern browser than a recent version of Firefox.
 </p>
 <p>
  There is no point in speculating why some of its features don’t work in more browsers. But I was surprised to see that blurred images are served that way and don’t get blurred in browser. I am playing with an idea of implementing a gallery inspired by Mike’s work, but I would like to reduce manual labor needed for maintaining it.
 </p>
 <p>
  So I wrote a function that blurs an image on canvas. You can
  <a href="http://markos.gaivo.net/examples/canvas_blur/" title="Javascript blur demo page">
   see it in action
  </a>
  or copy its code, if you find it useful.
 </p>
 <p>
  The algorithm used is described in
  <a href="http://web.archive.org/web/20060718054020/http://www.acm.uiuc.edu/siggraph/workshops/wjarosz_convolution_2001.pdf" title="Link to PDF version of paper">
   2001 paper
  </a>
  by Wojciech Jarosz. Page contains two implementations, second trading algorithm purity for in my opinion nicer code. Increase number of passes or run it few times over an image, if you need a blurrier result.? Please ask, if you need help with its use.
 </p>
 <p>
  I also measured its speed to see if it fits my needs. That brought a new surprise. Firefox 3.5.8? on my Linux powered VAIO with 1.2GHz processor blurs image twice as fast as same browser on a Mac with a 2.8Ghz processor. Numbers between runs may vary slightly, but never much. No idea why this is happening, since all functions do is some basic math over items in array that should be well optimized everywhere.
 </p>
 <p>
  I am sure somebody can optimize it further, but I find it good enough for my use. Image isn’t very blurred after one pass, but one pass over a small image is also a good way to measure how fast a particular computer-browser combination is. On fast combinations I might go for multiple passes over images in view, but fall back to a single pass or no pass on slower systems.
 </p>
</div>
