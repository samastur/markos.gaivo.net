Title: Securing web applications
Date: 2019-05-14 18:01:00
Author: markos
Category: Web
Slug: securing-web-applications
Tags: web, secure, webapp, applications

I recently finished work on a project with more than usually strict security requirements. While my work on the project is done and I am deciding on what to do next, I keep thinking about what I did and what I could do better next time beyond following established good implementation practices. This is my attempt to jot down my (unpolished) thinking, but will be light on technical details as I am not allowed to divulge them.

First thing I did was to create [a threat model](https://www.owasp.org/index.php/Category:Threat_Modeling) for the app’s frontend. It is not something I would see done on every project, but it really should be a standard practice even if it is simplified to a “living” list of assets to protect, identified threats and planned countermeasures.

An under-appreciated part of web frontend development using client-side frameworks is that practically speaking, it is not possible to secure the app you are building on your own. Every major framework depends on and installs hundreds of packages (usually more than a thousand) and it is not feasible to audit all of them and their updates. Even a smaller problem of tracking license compliance is a nightmare. Therefore managing risk also involves managing trust in external parties.

When using such frameworks is beneficial enough, I favour libraries built **and in use** by major tech companies such as Google and Facebook, especially if their documentation does not ignore security. They may not be better in all aspects I might care about, but will have both more resources invested in their development and more likely to be properly audited as those companies present a much bigger and valuable target than companies I work with. I avoid adding 3rd party libraries as much as economically possible and when not, prefer to copy parts actually used (with license and reference to original) when only small bit of that library is needed.

Loading 3rd party code directly in browser should be frowned upon. Even with modern toolbox for avoiding/limiting abuse ([iframe sandboxing](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe), [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)…) nothing is remotely as safe as not loading unknown resources in the first place. Since this is not always possible or desirable it is best to treat them as an existing exploit of unknown severity and decide where they must be avoided and how to best manage their risk elsewhere.

Similar risk is posed by browser extensions. User fingerprinting is a very good reason for trying to prevent discovery of loaded extensions, but I would still find it useful to at least know if there is *any* extension loaded that has access to my app’s contents without explicit user request.  It seems this is not possible. Admittedly this is not a wide-spread desire and most applications would not changed their behaviour based on this information, but few should (e.g. banking web apps).

In simpler, more naïve times we used to discuss if DOM is a good place to store state of a page. Clearly this is not a good idea for anything beyond storing state of UI controls and even then every change should be reflected on screen with an appropriate user notification (change transition, alert…). I remain undecided on how much uni-directional data flow helps with security, but it does some, similarly to how private class properties do and I find it easier to track possible attack points, if interface is a rendered reflection of application’s state and I can focus my attention on interactive parts with which user changes it.

Protecting code and data from nosy scripts with Javascript closures is already effectively done by frameworks and rarely requires manual intervention. This is mostly enough, but an unsolved problem for me was to keep data private and survive a browser window reload as I can only do one with any kind of certainty. I am reasonably sure this is not possible since every available storage is also available to other scripts as is requesting data from server without authentication.

[sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) is preferred to localStorage. Any personal data should be removed with sessions that shouldn’t be long either.

It would be nice, if all my research and effort provided me with more comfort than they do. Maybe fear is just the price paid for remaining vigilant.
