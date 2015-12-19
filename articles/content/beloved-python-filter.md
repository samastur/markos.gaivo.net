Title: Beloved python filter
Date: 2005-12-17 23:07
Author: markos
Category: Python
Slug: beloved-python-filter
Status: published
Id: 98

<div>
 <p>
  Is it just me or does anybody else find it easier to write:
 </p>
 <p>
  <code>
   elmList = filter( len, elmList )
  </code>
 </p>
 <p>
  then
 </p>
 <p>
  <code>
   elmList = [ x for x in elmList if len(x) ]
  </code>
 </p>
 <p>
  I don’t know why, but if I want to use the second form, I always have to look it up
  <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=98196">
   somewhere
  </a>
  . I know
  <em>
   filter
  </em>
  and friends are frowned upon, but I can’t stop liking them.
 </p>
</div>
