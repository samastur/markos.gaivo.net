Title: CSS pixels are a relative unit
Date: 2006-02-12 17:17
Author: markos
Category: UI, Web
Slug: css-pixels-are-a-relative-unit
Status: published
Id: 123

<div>
 <p>
  The pixel debate
  <a href="http://www.456bereastreet.com/archive/200602/setting_font_size_in_pixels/" title="Setting font size in pixels">
   is back
  </a>
  . Internet explorer out of the box doesn’t permit resizing text measured in pixels, which at the same time is the only reliable way of setting dimensions that produces same result everywhere.
 </p>
 <p>
  The crux of the matter is simply who should have the final word in how the page is displayed, designers or users?
 </p>
 <p>
  Personally I think it should be users. After all, it’s about them and if there’s a way for them to make their experience more pleasant or useful without degrading it for others, why shouldn’t they be allowed to do so? Good designs serve, not command.
 </p>
 <p>
  However, I find it more interesting how many people have no idea what px unit actually
  <a href="http://www.w3.org/TR/CSS21/syndata.html#length-units" title="Definitions of relative length units">
   means
  </a>
  . Pixels, as defined by W3C, are not the same as pixels used to define graphic resolution of a computer, even if they usually seem to be.
 </p>
 <p>
  For example, if we ever happen to get high-density monitors with say 300 dpi pixel density instead of these days common 96 dpi, then a 15″ display would have a graphic resolution of 3600×2700 dots, but it would still have only 1152×864 pixels in CSS model. Therefore one web pixel would be represented with around 9 graphic pixels.
 </p>
 <p>
  Well, that’s the theory. In practice there’s a lot of cheating. Monitors have various sizes which are only an approximation of the stated one (15″, 17″ etc.). Operating systems try to pay attention to pixel density, but often don’t or can’t. And so on.
 </p>
 <p>
  The result of this is that size of displayed text and images is device dependent even when in theory it shouldn’t be. So the only way is also good only up to a point.
 </p>
</div>
