Title: Hide email address from spammers with Javascript
Date: 2005-09-11 15:59
Author: markos
Category: Javascript, Web
Slug: hide-email-address-from-spammers-with-javascript
Status: published
Id: 22

<html>
 <body>
  <div>
   <p>
    <strong>
     Update: I
     <a href="hide-email-address-from-spammers-with-javascript-a-new-attempt.html">
      published
     </a>
     a new, more safe but less friendly version of this script.
    </strong>
   </p>
   <p>
    Wouldn’t it be nice, if you could post your email address on your web site without worrying spammers will pick it up?
   </p>
   <p>
    Now you can, by applying a little bit of javascript to your web page. Just import
    <a href="/blog/code/mangle.js" title="Javascript file with mangle function">
     this javascript file
    </a>
    in head of your document and call
    <em>
     mangle()
    </em>
    inside your onload handler. What it does, is replace elements of form
    <br/>
    <code>
     <br/>
     &lt;span class="change"&gt;billg at microsoft dot com&lt;/span&gt;
    </code>
    <br/>
    with
    <br/>
    <code>
     <br/>
     &lt;a href="mailto:billg@microsoft.com"&gt;billg@microsoft.com&lt;/a&gt;
    </code>
   </p>
   <p>
    There are few caveats to its use. You’re not allowed to use any HTML tag inside of span blocks, which have class set to change. The script also expects such blocks to have only one class definition. If change is only part of class attribute value, this script won’t work.
   </p>
   <p>
    You are free to use script as you please and to make any changes necessary. But if you choose to replace “at” and “dot” as delimiters, pick replacements that make address easily recognizable for those who don’t use javascript.
   </p>
   <p>
    <em>
     Note: The reason why this script works is that spammers use programs which search for email like pattern in page. They don’t interpret pages using javascript interpreter, since it would make collecting addresses significantly slower and more expensive.
    </em>
   </p>
   <p>
    <em>
     Update: Jay Samec let me know there’s a bug in my code, since it didn’t handle emails with multiple dots (e.g. those with subdomains). Script has been fixed now.
    </em>
   </p>
   <p>
    <em>
     Update 2: Holger Rindermann pointed out another bug and provided a patch to fix it that is now a part of the script.
    </em>
   </p>
  </div>
 </body>
</html>