Title: Tag frequency ratio
Date: 2006-02-09 14:43
Author: markos
Category: General development, UI, Web
Slug: tag-frequency-ratio
Status: published
Id: 121

<html>
 <body>
  <div>
   <p>
    Yesterday I talked about influence of language and tag design on ratio between the number of unique and all tags. I haven’t discussed why this number would be interesting and what would it tell us.
   </p>
   <p>
    Let’s start with a simple graph:
   </p>
   <p>
    <img alt="Tag space" class="image" src="http://markos.gaivo.net/images/tag-graph.jpg"/>
   </p>
   <p>
    Blue circles represent objects. Connections represent tags and rectangulars are pages with hits for a specific unique tag. As we can see, all images but one have two tags (number of connections from a circle) and the most popular tag is attached to 4 images (number of connections from a rectangular).
   </p>
   <p>
    What ratio tells us is an average frequency of a given tag (how many connections does a typical rectangular have). The higher it is, more hits will be returned by search.
   </p>
   <p>
    However, tag connections and rectangulars also form a path between objects. Therefore higher ratio also means a better connected graph with (again on average) shorter paths between different objects. For example if we look at the red path on example graph then left top object is at least two clicks away from the top one and at least four clicks away from the bottom right one.
   </p>
   <p>
    If tag browsing and searching are main methods of exploration, then a loner like the most right circle is practically unreachable and more tags an object has, the better chances it has to be discovered.
   </p>
   <p>
    Now, I presented a very simplified graph with a fairly even distribution of tags. Normally you wouldn’t have this. A word like cat is far more likely to be used as a tag than something like hippopotamus resulting in creation of super-nodes with far more connections to objects than system’s tag frequency ratio.
   </p>
   <p>
    With time you’d also expect this ratio to grow. Vocabulary, especially of commonly used words, is far more limited than number of pictures people can take and with time it becomes harder to create a unique tag. Flickr has tens or even hundred millions of tags, but certainly far less unique ones.
   </p>
   <p>
    Graph topography and things like super-nodes not only skew the picture, they can also change the perception and application use. I’ll write more about how in few months, when there will be more knowing and less guessing.
   </p>
  </div>
 </body>
</html>