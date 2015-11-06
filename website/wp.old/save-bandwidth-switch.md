Title: Save bandwidth switch
Date: 2012-03-15 08:52
Author: markos
Category: General development, Web
Slug: save-bandwidth-switch

Michal Migurski recently posted [an
article](http://mike.teczno.com/notes/bandwidth.html) about download
sizes of popular websites. I couldn't replicate his results^<span
id="save-bandwidth-1">[[1]](#save-bandwidth-note-1)</span>^, but it is
obvious that gist of Michal's article is correct, websites have indeed
ballooned significantly in last few years.

This blog's homepage has a footprint of around 250KB-270KB^<span
id="save-bandwidth-2">[[2]](#save-bandwidth-note-2)</span>^. About 90%
of its size are fonts and [jQuery](http://jquery.com/) which is a big
penalty for making it look and behave a bit nicer. So should I remove
those parts?

Well, for most visitors to this website that difference doesn't matter.
Pages for them are neither slow nor expensive to load. Unless of course
they are doing it over your average hotel Wi-Fi or a slow mobile network
where speed around 56Kb/s is not unheard of. On such connection it would
take about half a minute to load this blog. It can also cost more than
10 euro cents to load it when roaming in Europe.

It would be great if I could offer a choice of serving bigger and nicer
or smaller and faster version depending on visitors needs.

Measuring speed is not easy, but certainly doable as Gmail has
demonstrated. You could start a timer immediately in page header,
measure how much time it takes to load a smaller version of a website
and if that happened quickly enough upgrade it to full bling. Android
browser also added support for
[navigator.connection](http://dvcs.w3.org/hg/dap/raw-file/tip/network-api/index.html)
Javascript property which, where it exists, probably has more details
than you would need.

However there is no way to measure price of a visit. Even if I could,
how would I decide what is too expensive for an anonymous reader and
should I make such decisions at all? I think not.

Gmail's approach is really just a band-aid over what should be a
visitor's decision. I use same laptop and browser at home and while I
travel, experiencing all combinations of connection speed and pricing. I
never know how much it will cost me to visit a page, but I always learn
quickly if I would prefer something small or full-featured. There is
just no way I can communicate that preference.

It would be great if my browser had a switch for this purpose, like
Firefox's "Work Offline" toggle. So if I switched to bandwidth saving
mode, then every subsequent request to web server would communicate my
preference with a HTTP header field like:

> X-Bandwidth: save

In principle you could have multiple levels of bandwidth consumption,
but that would likely be an overkill. Common practice suggests that at
most two levels would really get used, one aimed at mobile devices and
other at desktop.

Header like that might be enough, but even better would be if Javascript
environment got another property describing current state of user's
preference (like say *navigator.bandwidth*). Coupled with a bandwidth
event triggered on change you could really optimize every modern web
page, even those with more complicated loading of resources and
execution paths.

Right now such functionality doesn't exist or at least I couldn't find
it (I even searched Mozilla's bug database for any future plans). I
think my proposal is both user and developer friendly and workable. If
you can think of a reason why it would be problematic, then I would
really like to hear it.

1.  <div id="save-bandwidth-note-1">

    </div>

    Pages are often personalized for visitor. Developer tools of
    different browsers also don't report same sizes. They also report
    amount of data transferred not the size of that data once unpacked.
    Almost 2M of Twitter's Javascript is thus reduced into page of
    "only" about 1MB of data transferred. And that to display couple of
    sentences.[↩](#save-bandwidth-1)
2.  <div id="save-bandwidth-note-2">

    </div>

    Depends on browser used. Variation in sizes is probably due
    different formats of fonts used by browsers. It also changed once I
    published this post.[↩](#save-bandwidth-2)

