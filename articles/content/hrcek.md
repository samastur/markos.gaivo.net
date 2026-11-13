Title: Hrček
Date: 2026-11-13 20:02:00
Author: markos
Category: Django, Web, Python,
Slug: hrcek
Status: published
Tags: python, django, hrček, bookmarks, webapp,

[Hrček](https://github.com/Hrcek-app/hrcek) is a simple self-hosted bookmark manager with support for wish lists. It stores everything in an SQLite database for easy backup, migration and further examination, and comes with published [browser](https://chromewebstore.google.com/detail/mdgabhlpgcmhlfnohpmlnllfppfhkfhb?utm_source=item-share-cb) [extensions](https://addons.mozilla.org/en-US/firefox/addon/hr%C4%8Dek/) and a so far unpublished [iOS client](https://github.com/Hrcek-app/hrcek-ios). I find it already useful, but not done.

It is also intended to be a usable experiment, a service which my family would want to use (and they do) as well as a learning project for processes and technologies I'm not well acquainted with. **All of it was written by AI** at my direction, but I intentionally did not write or directly change a single line of code, no matter how much my fingers itched.

I don't have anything of value to add to voices against generative AI's existence and use. Directionally they are correct. I can imagine how genAI could have been developed ethically, introduced carefully to societal benefit, but none of that happened nor will it, and at least in the short term, I mainly see a lot of societal harm. I also do not feel free to avoid its use and would therefore like to better understand its impact on me.

Beyond the desire to scratch my own itch and to see how useful and polished I can make a service as very much a side project in about a month of time, I wanted to see how well I would understand the whole at the end when I cannot use my preexisting understanding of the underlying system.

I expected a better result than what I got, but it's the result I should have expected. I expected the understanding of a diligent notetaker, but "finished" with one of an attentive reader. I'm sure I could do better if I slowed down and thought more about the underlying implementation instead of features and user experience, but that too was intentional as I wanted to see what AI could do with fairly light technical direction.

Generated code quality has been mixed with some duplication, inconsistent naming and bloviating comments. It is not a complicated application, so it wasn't a surprise that overall I find it fine, mostly following established norms. I did not end up merging anything I wouldn't be fine merging from a co-worker even when I would prefer to do it differently. I wonder if those more disappointed over quality are just better developers than me (many surely are) or whether there's also a different expectation of personal alignment with the end product.

From the beginning I wanted to make it multilingual and picked Slovenian as its second language. It's a great choice for testing because it has complex rules that stretch i18n tools, especially naive ones, with a small enough corpus that it might give problems to AI models, and it is also one I speak reasonably well as its native speaker.

I spent more time than I expected guiding the model to a reasonable system for translating (essentially standardising on `gettext`) and I am almost certainly going to break my rule and fix translations myself at some point. The automatic translations are not good, but I've been pleasantly surprised a few times. To be fair, I am not even sure it is possible to make translations into Slovenian that will work in all contexts.

I also wanted to generate documentation, which is something I've been experimenting with in my other work as well. AI models clearly have no clue what good documentation is without guidance that I did not provide. Developer documentation was often too detailed and read as a redundant explanation of code. Documentation meant for users of Hrček is functional and better than nothing, but again mainly a detailed descriptive reference instead of a more task-oriented guide. I could write another post just on creating documentation and related issues, and hopefully I will.

It was difficult for me to maintain mental engagement with numerous and more often than not large pull requests. I did not have the same mental model of the whole as I have with code I am already familiar with, and my self-imposed limitations meant it was difficult to create it. Stacked PRs that GitHub finally introduced helped, but not enough, and I felt like a student who has to keep learning new information on top of ever more leaky foundations, which was the premise of nightmares I used to have.

Another reason why I insisted on not contributing directly beyond "project managing" or, as some would probably describe it, meat-proxying the development, is that I wanted to generate enough commits and changes that I would get a statistically meaningful dataset. Like many, I have had the impression that commits, PRs or whatever measurement you take have grown even when the code part does not seem overly complicated. However, this will also have to wait for its own post as this one is already tryingly long.

P.S. Other unordered observations from development that don't fit elsewhere:

 * Excessive tests hinder engagement; remedy unclear.  
 * Minor changes affect many files, raising questions about scope or prior neglect.  
 * I think function comments should rarely exceed code length; unclear how to translate it into an effective rule.  
 * Likely duplication in test setup.  
 * Documentation placed alongside code is nice.  
 * Browser tests are beneficial but conflict with CI speed and stability.  
 * Absence of design style guide affects project consistency.  
 * Goal explanations differ from implementation understanding.  