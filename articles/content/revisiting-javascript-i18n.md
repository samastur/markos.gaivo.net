Title: Revisiting javascript i18n
Date: 2006-02-25 16:55
Author: markos
Category: Javascript, UI, Web
Slug: revisiting-javascript-i18n
Status: published
Id: 130

<div>
 <p>
  This week I had an interesting discussion with Ratnadeep Bhattacharjee about my
  <a href="news-at-seven-javascript-i18n-that-almost-doesnt-suck.html" title="Older post with js i18n library">
   previous try
  </a>
  to solve javascript i18n needs and it quickly become obvious that my library is not sufficient and likely also wrong approach to the problem.
 </p>
 <p>
  There are at least two unresolved issues with my current javascript i18n library:
 </p>
 <ul>
  <li>
   It doesn’t detect browser language settings and act accordingly.
  </li>
  <li>
   It’s one way only. After you changed the language used, you can’t change it again easily.
  </li>
 </ul>
 <p>
  I’m sure these are not the only two problems, since I have a vague uneasiness about a few more things. Therefore I’d love to hear more thoughts about what you’d expect and need from such a library, before I continue down the possibly wrong path.
 </p>
</div>
