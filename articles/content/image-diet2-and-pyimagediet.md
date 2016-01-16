Title: image-diet2 and pyimagediet
Date: 2016-01-16 21:00:17
Author: markos
Category: Python
Slug: image-diet2-and-pyimagediet
Status: draft
Tags: low-bandwidth, django, compression, image, optimisation

Couple of years ago I hacked together a small Django app called [image-diet](http://) which automatically compresses images processed by Easy Thumbnails as they are uploaded to a website. Its code was atrocious with configuration for external tools baked in, it only worked with [Easy Thumbnails](https://github.com/SmileyChris/easy-thumbnails) and Python2 and...I could go on, but it worked and at [Aptivate](http://aptivate.org) we have been using it successfully ever since.

Well, I finally found time and rewrote the whole thing. New version is now called [image-diet2](https://pypi.python.org/pypi/image-diet2) because it is completely backwards incompatible and I screwed up versioning of the original one. Mea culpa.

It's implemented as a Django storage backend augmenting default one, but can easily be added as a mixin to any other so it should work no matter which tool or backend you use to upload files. Supporting new compression tools or changing configuration of existing does not require a new release or poking in virtualenv anymore. It is better [tested](https://travis-ci.org/samastur/image-diet2) and [documented](http://image-diet2.readthedocs.org/). You really should give it a try.

image-diet2 is actually a thin Django wrapper around separately packaged [pyimagediet](https://pypi.python.org/pypi/pyimagediet) that actually process files. My hope is that others may find it useful enough to use it on non-Django projects. It also comes with a tool to compress images and generate configuration file tailored to your system. If you can think of anything that would make integration even easier, then please let me know.

There are few bits still missing, but functionality is mostly complete. What I plan to do next is to test in different configurations to find how well they work and what are their tradeoffs. Prior useful work such as [this](http://www.css-ig.net/png-tools-overview) exists, but I'd like tests to be more expansive and in reusable format. They need to be easily replicable by anyone as their versions of processing tools might give different results than mine.