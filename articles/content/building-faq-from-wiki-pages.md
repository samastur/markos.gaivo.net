Title: Building FAQ from wiki pages
Date: 2005-11-22 17:17
Author: markos
Category: Company, Python, Web
Slug: building-faq-from-wiki-pages
Status: published
Id: 75

<div>
 <p>
  We use
  <a href="http://moinmoin.wikiwikiweb.de/" title="MoinMoin's homepage">
   MoinMoin
  </a>
  for all our documentation needs, since it simplifies almost all related tasks. It’s nice when everything is available at one place through a familiar and easy to use interface.
 </p>
 <p>
  This is why I also wanted to use it to build a FAQ for our site, which is more needed with each day. There’s an abundance of software for building and managing such documents, but I haven’t found anything that would match our needs. Apart from using wiki pages as the source of wisdom, I also wanted:
 </p>
 <ol>
  <li>
   A good and fairly easy integration with our site (but not automatic).
  </li>
  <li>
   A very malleable solution, where it would be easy to change FAQ organization as requirements change.
  </li>
 </ol>
 <p>
  At the end I decided to build our own thing using
  <a href="http://www.crummy.com/software/BeautifulSoup/index.html">
   Beautiful Soup
  </a>
  , a python package I raved about a while ago. Since we wanted each question to have a permanent link that could be bookmarked, we had to give them an identifier that wouldn’t change even if we rephrased the question or changed the answer. The simplest way was to assign a unique number to each question as it can be seen on a
  <a href="http://markos.gaivo.net/examples/samplefaq/faq.html">
   sample FAQ page
  </a>
  . This way it’s easy to add and remove questions as long as you can count.
 </p>
 <p>
  MoinMoin produces very sensible HTML that is easy to work with.
  <a href="http://markos.gaivo.net/examples/samplefaq/faq.py">
   Here’s
  </a>
  a proof of concept module that extracts information from a page like the sample one and packs it in a dictionary with identifiers as keys and a list
  <em>
   [ question, answer ]
  </em>
  as value.
 </p>
 <p>
  It’s not something very useful on its own, but I think it’s a nice example of what can be done quickly with existing tools like MoinMoin and BeautifulSoup.
 </p>
 <p>
  Notes: In principle there’s no need to use MoinMoin as long as produced HTML fits following assumptions:
 </p>
 <ol>
  <li>
   FAQ is stored inside a
   <em>
    div
   </em>
   element with
   <em>
    id
   </em>
   set to
   <em>
    content
   </em>
   .
  </li>
  <li>
   Questions are inside a heading element which also acts as a delimiter between them.
  </li>
  <li>
   Identifiers are integers.
  </li>
 </ol>
 <p>
  If it doesn’t, you’ll need to change code a bit.
 </p>
</div>
