Title: Subtracting sets to get non-referenced rows in table.
Date: 2012-10-02 00:07
Author: markos
Category: General development
Tags: shell, algorithm, sql
Slug: subtracting-sets-to-get-non-referenced-rows-in-table
Status: published
Id: 1014

<div>
 <p>
  I had a problem today. Given two database tables with first having a foreign key pointing to second, find those rows in second table, which are not pointed to from first. Well, it was slightly more complicated than this, but this was the tricky part.
 </p>
 <p>
  I tried to solve my problem using
  <a href="http://en.wikipedia.org/wiki/SQL" title="SQL description on Wikipedia">
   SQL
  </a>
  , but I could not. I am not saying it can’t be done, but with my limited knowledge of SQL I could not produce a query that would not perform horribly. Working on production database under heavy use made this a real no-go.
 </p>
 <p>
  After trying to come up with pure solution I finally gave up and decided to solve this problem pragmatically with some scripting. Turns out that too was more complicated than necessary. Unix shell tools are all you actually need, provided your dataset is not too big for your computer limitations (mostly memory).
 </p>
 <p>
  Instead of searching for those rows directly, I changed my plan to create two sets of rows, first containing all possible candidates and second containing those from first set which are pointed to from first table. Subtracting second set from first would therefore give me exactly those rows which aren’t pointed to.
 </p>
 <p>
  If file
  <em>
   all
  </em>
  contains a row-per-line list of all candidates and
  <em>
   linked
  </em>
  a similar list of those that are linked to, then you can get non-linked by running following command:
 </p>
 <p>
  <code>
   cat all linked | sort | uniq -u &gt; non_linked
  </code>
 </p>
 <p>
  What this does is following.
  <em>
   Sort
  </em>
  will put duplicated rows together and
  <em>
   -u
  </em>
  option of
  <em>
   uniq
  </em>
  will display only unique lines which are those that can be found only in
  <em>
   all
  </em>
  . Problem solved.
 </p>
</div>
