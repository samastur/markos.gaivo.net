Title: Universal Encoding Detector
Date: 2006-03-17 22:22
Author: markos
Category: Python
Slug: universal-encoding-detector
Status: published
Id: 138

<div>
 <p>
  Few months ago, while exporting vCards from Apple’s Address Book (which uses UTF-16 instead of to me more common UTF-8), I discovered that there’s really no general agreement on which encoding should be used for storing vCards. It was quite a disheartening discovery, since you can’t get this information from a filesystem and it’s difficult to transform encoding to a uniform one, if you don’t know the encoding of the source.
 </p>
 <p>
  I decided to tackle this problem once other problems were solved and I’m happy to say my procrastination payed off. Mark Pilgrim wrote another excellent
  <a href="http://chardet.feedparser.org/" title="Universal Encoding Detector">
   module
  </a>
  which solves my problem better than I ever could.
 </p>
 <p>
  Universal Encoding Detector is a python port of code used by Mozilla to accomplish the same thing and is really very simple to use. Obviously it can’t be perfect since it’s not possible detect encoding completely reliably. But it works quite well and if you need such functionality, you should really give it a try.
 </p>
 <p>
  And people say laziness doesn’t pay off.
 </p>
</div>
