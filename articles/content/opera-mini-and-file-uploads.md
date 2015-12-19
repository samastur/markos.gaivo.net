Title: Opera mini and file uploads
Date: 2006-05-24 10:35
Author: markos
Category: Web
Slug: opera-mini-and-file-uploads
Status: published
Id: 172

<div>
 <p>
  A Marela member notified us, that file upload doesn’t work in
  <a href="http://www.opera.com/products/mobile/operamini/">
   Opera Mini
  </a>
  . It’s true, because Opera Mini doesn’t support file uploads which you can easily check by visiting two
  <a href="http://markos.gaivo.net/examples/inputfile/index.html">
   demo pages
  </a>
  with valid XHTML. You shouldn’t see a file input element on either of them.
 </p>
 <p>
  I believe (but as an outsider obviously can’t prove) it lacks upload support for security reasons. Every web request handled by Opera Mini gets transported over a proxy, which fetches the page in questions and translates it in a compressed format suitable for viewing on small screen devices. This means that file uploads would be sent to proxy as well which depending on what is sent can be seen as a security violation.
 </p>
 <p>
  Of course it does allow logging in websites, a potentially unsafe action, which puts my speculation on shaky grounds. But the true point of this article still stands. Opera Mini doesn’t support file uploads.
 </p>
</div>
