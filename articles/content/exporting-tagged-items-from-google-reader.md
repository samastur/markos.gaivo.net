Title: Exporting tagged articles from Google Reader
Date: 2013-03-24 19:48
Author: markos
Category: Python
Tags: backup, backup, export, export, Google, Google, openweb, openweb, Python, Python, reader, reader, script, script
Slug: exporting-tagged-items-from-google-reader
Status: published
Id: 1097

<html>
 <body>
  <div>
   <p>
    Google Reader for me was never just a way to plow through a large number of feeds, but also a database of important articles that I lovingly annotated with tags and notes when they still existed. Apparently I was in minority, judging by Reader clients and more importantly its own exporting tools which lets you take away most of your stuff, but not tagged items themselves.
   </p>
   <p>
    Hence I wrote a quick and dirty Python script which allows you to do just that using
    <a href="https://pypi.python.org/pypi/libgreader">
     libgreader
    </a>
    . You can find
    <a href="https://github.com/samastur/GReader-hoover">
     it on Github
    </a>
    and it has few other features like exporting all feed articles. Who knows how long Feedburner will be around so next step will be resolving those links.
   </p>
   <p>
    My current backup amounts to almost 500MB so script is obviously useful to me. Hopefully it is also to others.  If you find bugs or data that is not exported, but should be, please do let me know.
   </p>
   <p>
    I am also looking for a good alternative that is
    <strong>
     not hosted only
    </strong>
    service, supports archiving and can process most feeds. Currently I am biased to modifying Newsblur to support tagging and running my own instance, but I would definitely prefer to avoid this work if possible.
   </p>
  </div>
 </body>
</html>