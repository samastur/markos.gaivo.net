Title: Impostor for Django
Date: 2011-02-22 20:11
Author: markos
Category: Django, Python, Web
Slug: impostor-for-django

A class of bugs I really dislike debugging are those that depend on
specific data and affect only a very small subset or just one user.
Things could sometimes be fixed so much faster if you could just log in
as him to see what is happening. Sometimes this is exactly what we do
**with his explicit permission**, but I really dislike asking for
passwords.

First it inconveniences user. He has to come up with either a new good
password or go through two password changes. Second it implicitly
teaches wrong behavior. Passwords simply should never be revealed.

That is why I wrote
[Impostor](https://github.com/samastur/Impostor "Impostor's home at GitHub"),
a Django app that allows staff members (and only them) to login with
their own credentials as a different user. Idea is not mine (kudos goes
to [Ned
Batchelder](http://nedbatchelder.com/blog/201008/django_superuser_login_trapdoor.html "Ned's post where idea comes from")),
but I like it. To discourage abuse every such authentication is recorded
and can be seen in Django admin interface, but can not be altered from
there.

So how does it work in practice?

Lets say that I would need to log in as user *fry*. To do this I would
enter as my username *markos as fry,* provide my password and voila, I'm
him. This has been recorded so anyone with access to ImpostorLog part in
admin can see all such cases, mine included.

Impostor may also ease your development by removing need to remember
different passwords for testing. This is usually not a problem unless
you happen to develop with fake data but real accounts. Like me.

And again for morally challenged out there: **you should never login as
somebody else without his explicit permission**.

**Update**: Thanks Ross for reminding me where idea came from. I updated
text accordingly.

<div class="zemanta-pixie">

[![Enhanced by
Zemanta](http://img.zemanta.com/zemified_e.png?x-id=db7c9f53-423e-4b56-bbe3-b717fde54c16)](http://www.zemanta.com/ "Enhanced by Zemanta")

</div>
