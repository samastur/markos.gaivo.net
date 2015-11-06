Title: When to use degradable Javascript
Date: 2005-10-18 13:27
Author: markos
Category: Javascript, UI, Web
Slug: when-to-use-degradable-javascript
Status: published
Id: 44

<html>
 <body>
  <div>
   <p>
    <a href="http://encytemedia.com/blog/articles/2005/10/13/dispelling-the-myths-of-javascript-degredation" title="Link to Justin's article">
     Justin Palmer
    </a>
    wrote about myths of Javascript degradation and
    <a href="http://domscripting.com/blog/display.php/25" title="Link to Jeremy's article">
     Jeremy Keith
    </a>
    has written a response. This is just the lastest, but certainly not last exchange on this topic and I think we’ll continue to talk about it for some time to come.
   </p>
   <p>
    I think I find myself somewhere in the  middle. Part of our service follows Jeremy’s school of thought and part of it is firmly on Justin’s side. I think Jeremy’s argument that the problem is due lack of planning is just wrong. I spent literally months contemplating and trying different things before I finally accepted that not everything can be done in nicely degradable manner without making sacrifices.
   </p>
   <p>
    Or to use a misplaced example. You can start with a bicycle that more or less everyone can use and try to add features, that will enable it to go faster and with less physical strain, but you’ll never produce a
    <a href="http://www.ducati.com" title="Ducati motorbikes">
     Ducati
    </a>
    . At most you’ll finish with something like:
   </p>
   <p>
    <a href="http://www.ebikeshop.co.uk/detailscruiser.html">
     <img alt="Electric bicycle" src="http://markos.gaivo.net/images/ebike.jpg" style="width:190px;height:186px;border: 0;"/>
    </a>
    <br/>
    I’m not saying electric bike is bad. In fact it has many features that Ducati will never have. They are just different and what’s better depends on what you want and who you want to serve.
   </p>
   <p>
    I believe the same applies to Javascript degradation. You have to decide what you’re building and for whom. When developing our service, I probably haven’t thought about anything more than this issue and the choices I made were certainly not done lightly. I did discover a simple question, that often makes such decisions easier:
   </p>
   <p>
    <strong>
     “Would anyone ever want to bookmark this?”
    </strong>
   </p>
   <p>
    If yes, then degradable javascript is the only acceptable solution. If no, then there MIGHT be a case for non-degradable solution, but it certainly doesn’t immediately justify it.
   </p>
  </div>
 </body>
</html>