Title: image-diet2 and pyimagediet
Date: 2016-01-14 21:00:17
Author: markos
Category: Python
Slug: image-diet2-and-pyimagediet
Status: draft
Tags: low-bandwidth, django, compression, image, optimisation

Couple of years ago I hacked together a small Django app called [image-diet](http://) which automatically compresses images handled by Easy Thumbnails as they are uploaded to a website. Its code was atrocious with configuration for external tools baked in, it only worked with [Easy Thumbnails](https://github.com/SmileyChris/easy-thumbnails) and Python2 and...I could go on, but it worked and at [Aptivate](http://aptivate.org) we have been using it ever since.

Well, I finally found time and rewrote the whole thing. New version is now called [image-diet2](https://pypi.python.org/pypi/image-diet2) because it is completely backwards incompatible and I screwed up versioning of the original one. Mea culpa.

It's implemented as a Django storage backend augmenting default one, but can easily be added as a mixin to any other so it should work no matter which tool or backend you use to upload files. Supporting new compression tools or changing configuration of existing does not require a new release or poking in virtualenv anymore. It is better [tested](https://travis-ci.org/samastur/image-diet2) and [documented](http://image-diet2.readthedocs.org/). You really should give it a try.

### pyimagediet

To avoid unnecessary duplication I have also released [pyimagediet](https://pypi.python.org/pypi/pyimagediet), a small library on which image-diet2 depends, that actually process files. It also comes with a tool to compress images and generate configuration file tailored to your system. If you can think of anything that would make integration even easier, then please let me know.

### Next steps