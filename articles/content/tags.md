Title: Tags
Date: 2006-02-08 18:01
Author: markos
Category: General development, UI, Web
Slug: tags_
Status: published
Id: 120

<div>
 <p>
  Tags are increasingly popular and rightfully so. I’ve built my share of applications with their own taxonomies and I’m certain they simply don’t work. They sort of work if they were built for specialized needs and are used only by trained, disciplined people with excellent organizational skills.
 </p>
 <p>
  Which means almost never.
 </p>
 <p>
  Tags (aka folksonomies) are messy. There’s no real system, any bozo can attach whatever it wants and you’d be a fool to blindly trust any specific tag. They are the worst possible system apart from everything else we tried so far.
 </p>
 <p>
  That’s why we decided to implement them in Marela. Language used on Marela is Slovene and that led to slightly different design that commonly found elsewhere.
 </p>
 <p>
  We decided to treat multiple words separated with spaces as one tag and use commas as a delimiters between different tags. First reason for this is that tagging something like
  <em>
   New Zealand
  </em>
  becomes more natural. The other was that in Slovene compound words like handbag are very often separate words. For example, handbag would be
  <em>
   ro??na torbica
  </em>
  .
 </p>
 <p>
  Another problem, which we haven’t tackled yet, but probably will have to, is that Slovene is
  <a href="http://en.wikipedia.org/wiki/Slovene_grammar" title="Short description on Wikipedia">
   a complicated language
  </a>
  in ways that make tagging a nasty problem. There are six cases, but nominative is usually used. Still three different grammatical numbers (singular, dual and plural) together with three different genders (masculine, feminine and neutral) leave multiple options for the same thing. If you were looking for
  <em>
   blue
  </em>
  objects, you’d need to search at least for tags
  <em>
   modra
  </em>
  ,
  <em>
   modro
  </em>
  ,
  <em>
   modri
  </em>
  and
  <em>
   modre
  </em>
  . Right now you have to do this manually.
 </p>
 <p>
  And then there are problems that plaque other tagging systems as well. Most common of them are misspelled words, like
  <em>
   Wein
  </em>
  instead of
  <em>
   Wien
  </em>
  for Vienna.
 </p>
 <p>
  All these lead to a fairly flat tag space with a ratio of 5.6 between all tags and unique ones. I’m not sure how it would change if we treated spaces differently or even what is a common ratio for other languages and other applications. I’m guessing it wouldn’t change the ratio too much because of noun cases, but it remains to be investigated.
 </p>
 <p>
  So, why does it matter?
 </p>
 <p>
  Well, that’s a matter for another post, which I’ll probably write tomorrow.
 </p>
</div>
