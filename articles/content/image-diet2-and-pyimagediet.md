Title: image-diet2 and pyimagediet
Date: 2016-01-11 21:00:17
Author: markos
Category:
Slug: image-diet2-and-pyimagediet
Status: draft
Tags: low-bandwidth, django, compression, image, optimisation

Couple of years ago I hacked together a small Django app called [image-diet](http://) which automatically compresses images handled by easy_thumbnails as they are uploaded to a website. It was ugly, limited, inflexible, but worked and at [Aptivate](http://aptivate.org) we have been using it ever since.

However it bothered me greatly. Atrocious code with configuration for external tools baked in, it only worked with easy_thumbnails (because it used signals) and only with Python2 and...I could go on. Well, I finally found time and rewrote the whole thing.

New version is now called [image-diet2](https://github.com/samastur/image-diet2) because it is completely backwards incompatible and I screwed up versioning of the original one. Mea culpa.

### pyimagediet


### Next steps