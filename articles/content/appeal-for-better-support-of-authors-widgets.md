Title: Appeal for a better support of authors widgets
Date: 2010-03-03 18:06
Author: markos
Category: Company, General development, Web
Tags: editors, platforms, future, widgets, blogging, browser
Slug: appeal-for-better-support-of-authors-widgets
Status: published
Id: 572

<div>
 <p>
  Goal of
  <a class="zem_slink" href="http://www.zemanta.com" rel="homepage" title="Zemanta">
   Zemanta
  </a>
  widget has always been to present contextually relevant information to text being written and to enable writers to add that information easily in places of their choice. We want to do this in as unobtrusive manner as possible, which means that act of writing should not be impeded by us and that published text should only have as little markup added as it is necessary to add items picked by user  (images, links…).
 </p>
 <p>
  Zemanta widget in various incarnations today works in all major browsers (
  <a class="zem_slink" href="http://www.mozilla.com/en-US/firefox/" rel="homepage" title="Firefox">
   Firefox
  </a>
  ,
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Internet_Explorer" rel="wikipedia" title="Internet Explorer">
   Internet Explorer
  </a>
  ,
  <a class="zem_slink" href="http://www.google.com/chrome" rel="homepage" title="Google Chrome">
   Chrome
  </a>
  ,
  <a class="zem_slink" href="http://www.apple.com/safari" rel="homepage" title="Safari">
   Safari
  </a>
  and
  <a class="zem_slink" href="http://www.opera.com" rel="homepage" title="Opera Software">
   Opera
  </a>
  ) and on all major blogging platforms. This wide support is presenting ever bigger challenge to us  and to anyone who wants to follow our path.
 </p>
 <p>
  Most blogging platforms today support enhancement of blogs with widgets. I think it is time for them to add support for widgets on content creation side and go beyond current one-interface-fits-all state of affairs.
 </p>
 <p>
  Open platform would enable tool makers like us to build specialized tools that might cater to specific niches and empower writers to customize their workflow to their needs .
 </p>
 <p>
  Such platforms should at minimum have a common shared feature set, but I hope for at least partially shared
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Application_programming_interface" rel="wikipedia" title="Application programming interface">
   API
  </a>
  .
 </p>
 <p>
  <strong>
   Current state
  </strong>
 </p>
 <p>
  Some platforms like
  <a class="zem_slink" href="http://wordpress.org" rel="homepage" title="WordPress">
   WordPress
  </a>
  already have a plug-ins API which can be used to customize parts of creation process. However it is usually very low level, highly platform specific and available only to self-hosted users.
 </p>
 <p>
  Creators of rich text editors have also recognized a need to let outside developers extend writing experience. Most major editors have an API that admittedly we might not be using enough. But this is not true of all editors so we end up with common development problems like not enough feature overlap and missing,  undocumented or poorly documented interfaces.
 </p>
 <p>
  There is a lot of activity, but the end result is still a very fragmented landscape that in my opinion limits developers creativity. You either add wanted functionality to your favorite platform or if you are more ambitious, you end up seeking the right balance between ironing out  platform peculiarities and building features users actually care about.
 </p>
 <p>
  And since blogging environment that most people use lets them little control over it, we develop browser extensions that are really just a patch for this problem. The only reason why we bloat browsers (a little bit) with an extension that most of the time does nothing is because we have to. Extensions are great, but they also present a risk and in this case one that should not be necessary.
 </p>
 <p>
  <strong>
   My vision of future
  </strong>
 </p>
 <p>
  What I would like to do as a developer can best be explained with examples translated from code to English (well, approximation of it anyhow).
 </p>
 <p>
  I would like to write: ?Take image at this address, upload it to writer?s image repository and return me its new address.?
 </p>
 <p>
  I would like to write: ?When DOM node is added to text (or removed from it), run this function.?
 </p>
 <p>
  I would like to write: ?Before text is published, run it through this filter function and save its result.?
 </p>
 <p>
  I would like to write: ?Store this information and let me retrieve when I need it.?
 </p>
 <p>
  I would like our users to add our widget with only a few clicks. Maybe a click on our side to trigger installation and a confirmation on blogging platform with a list of permissions sought (like
  <a class="zem_slink" href="http://oauth.net" rel="homepage" title="OAuth">
   OAuth
  </a>
  ).
 </p>
 <p>
  When user interface needs to be shown, I would want it to be well integrated. So if elements of interface can be rearranged, hidden or otherwise handled, then our widget would behave as expected.
 </p>
 <p>
  <strong>
   In conclusion
  </strong>
 </p>
 <p>
  Creating and supporting a tool like Zemanta is difficult. Front end development is challenging enough when you are against few browsers on your platform, but it is far worse when you try to deliver the same high level of experience on multiple platforms none of which you actually control.
 </p>
 <p>
  You keep hitting at browser quirks and unexpected platform changes and ironically it keeps getting worse as other people?s code gets better. For example, wrapping your Javascript code in anonymous namespace is good practice, but it often removes hooks on which you relied and you need to come up with a new solution.
 </p>
 <p>
  My work often feels like war of attrition, which is odd because there is no enemy. We work to complement blogging platforms, not replace them.
 </p>
 <p>
  Surely it is time we do better.
 </p>
</div>
