Title: Impostor for Django
Date: 2011-02-22 20:11
Author: markos
Category: Django, Python, Web
Tags: Python, Security, Impostor, Password, Django
Slug: impostor-for-django
Status: published
Id: 649

<div>
 <p>
  A class of bugs I really dislike debugging are those that depend on specific data and affect only a very small subset or just one user. Things could sometimes be fixed so much faster if you could just log in as him to see what is happening. Sometimes this is exactly what we do
  <strong>
   with his explicit permission
  </strong>
  , but I really dislike asking for passwords.
 </p>
 <p>
  First it inconveniences user. He has to come up with either a new good password or go through two password changes. Second it implicitly teaches wrong behavior. Passwords simply should never be revealed.
 </p>
 <p>
  That is why I wrote
  <a href="https://github.com/samastur/Impostor" title="Impostor's home at GitHub">
   Impostor
  </a>
  , a Django app that allows staff members (and only them) to login with their own credentials as a different user. Idea is not mine (kudos goes to
  <a href="http://nedbatchelder.com/blog/201008/django_superuser_login_trapdoor.html" title="Ned's post where idea comes from">
   Ned Batchelder
  </a>
  ), but I like it. To discourage abuse every such authentication is recorded and can be seen in Django admin interface, but can not be altered from there.
 </p>
 <p>
  So how does it work in practice?
 </p>
 <p>
  Lets say that I would need to log in as user
  <em>
   fry
  </em>
  . To do this I would enter as my username
  <em>
   markos as fry,
  </em>
  provide my password and voila, I’m him. This has been recorded so anyone with access to ImpostorLog part in admin can see all such cases, mine included.
 </p>
 <p>
  Impostor may also ease your development by removing need to remember different passwords for testing. This is usually not a problem unless you happen to develop with fake data but real accounts. Like me.
 </p>
 <p>
  And again for morally challenged out there:
  <strong>
   you should never login as somebody else without his explicit permission
  </strong>
  .
 </p>
 <p>
  <strong>
   Update
  </strong>
  : Thanks Ross for reminding me where idea came from. I updated text accordingly.
 </p>
</div>
