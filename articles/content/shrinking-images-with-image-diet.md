Title: Shrinking images with image-diet
Date: 2013-01-20 23:53
Author: markos
Category: Django, Python, Web
Tags: Django, low-bandwidth, images, page size, speed, shrink
Slug: shrinking-images-with-image-diet
Status: published
Id: 1087

<div>
 <p>
  I like
  <a href="https://github.com/SmileyChris/easy-thumbnails">
   easy-thumbnails
  </a>
  and use it often in my Django projects, but I wished for a long time that its
  <a href="http://www.pythonware.com/products/pil/">
   PIL
  </a>
  generated thumbnails would be smaller. That’s why I wrote
  <a href="https://github.com/samastur/image-diet">
   image-diet
  </a>
  , a drop-in extension for those easy-thumbnails users who use file system for storing images. Images remain visually the same, but can be significantly smaller (mine by more than 50% but your mileage my vary).
 </p>
 <p>
  This matters because images are together with Javascript main cause for ever larger page sizes which leads to slower websites, especially in low-bandwidth environments. But really, don’t we all want our websites to be as fast as possible?
 </p>
 <p>
  <a href="https://github.com/samastur/image-diet">
   image-diet
  </a>
  was inspired by
  <a href="http://imageoptim.com/">
   ImageOptim
  </a>
  and
  <a href="https://github.com/Kilian/Trimage">
   Trimage
  </a>
  and I’m grateful to authors of both. It uses jpegtran, Jpegoptim, Gifsicle, OptiPNG, AdvanceCOM PNG and Pngcrush to do the heavy work of squeezing redundant bytes. Getting them should be easy as they are part of Ubuntu distribution and can be installed on Mac with brew. For more information please check documentation or ask.
 </p>
 <p>
  I would love to hear any comments and ideas you may have, even more so if you try it.
 </p>
</div>
