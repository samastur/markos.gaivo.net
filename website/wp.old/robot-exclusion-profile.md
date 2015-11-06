Title: Robot Exclusion Profile
Date: 2006-04-13 22:54
Author: markos
Category: UI, Web
Slug: robot-exclusion-profile

As could be expected, I wasn't the first one who thought about
controlling spiders more granularly. Even though I prefer deny-allow
idea that [Fry](http://friedcellcollective.net/outbreak/) and I came up
with after a lively debate yesterday, I think [Robot Exclusion
Profile](http://microformats.org/wiki/robots-exclusion "Link to format specification")
(REP) microformat is not a bad start. Actually, it's quite good with a
few open [issues](http://microformats.org/wiki/robots-exclusion#Issues)
that mostly shouldn't be too difficult to resolve.

#### Precedence

I don't think it matters what policy you have when dealing with
conflicting classes set on the same element, as long as you choose one.
Personally, I'd mimic CSS way and go for last definition stays. So
*class="robots-nofollow robots-follow"* would be equal to
*class="robots-follow"*. I'd say the same order precedence also should
stand in *class="robots-follow" rel="nofollow"* case.

Toolkits might have a problem with this approach, since you often can't
tell in which order were attributes set. If this is deemed important,
then I think a reasonable approach in case of conflict is to simply
ignore **all** exclusion attributes.

However, I think there's another ambiguity that hasn't been mentioned.
What should a spider do, if it encounters something like this:  
<codeins ="robots-exclusion"></codeins>

It's a valid scenario. Imagine your average blog sidebar, which includes
navigational items like archives that probably don't belong in index,
but can also include stuff like current post categories, which should.

I think specification heavily implies CSS approach to this (the most
specific value wins) and that spider should process all elements, even
those included inside of parts that might later get ignored. Still, it
would be nice if this was explicitly written.

#### Specificity

I simply don't care. Even without control of specific UA it's clearly a
superset of today's behavior. It doesn't remove anything. It only adds
control and in a way, where default behavior is today's behavior. So it
could hardly be less intrusive.

I also think proposed solution for the problem is good enough, but we
could add this later on, if needed.

#### Suitability as a microformat

Well, this is the though one. I don't think there's much if any
difference between
[relnofollow](http://microformats.org/wiki/relnofollow) and this
specification (REP being really only a moderate extension of
relnofollow). In both cases human's don't really come first before
computers or at least not directly. In both cases you want to influence
search engines to produce better search results, which consequently
helps humans.

I see myself as a technological pragmatist so I care more about the end
result then sticking to some high ideal. If it's accepted that
controlling spider behavior would be beneficial and I see no opposition
to this idea, then it seems obvious that a reasonable end product
(specification) will look a lot like a defined microformat.

So is the problem really only in daring to call it a microformat and
sticking it on a microformats website?

