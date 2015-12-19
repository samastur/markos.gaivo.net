Title: Dreaming about arithmetic mean
Date: 2010-01-24 11:44
Author: markos
Category: General development, Javascript
Tags: Arithmetic mean, algorithm, Javascript, Programming, Computer science, bug
Slug: dreaming-about-arithmetic-mean
Status: published
Id: 549

<div>
 <p>
  I had a crazy dream, where I was back at University, but this time studying computer science. We were writing a function to calculate an
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Arithmetic_mean" rel="wikipedia" title="Arithmetic mean">
   arithmetic mean
  </a>
  of an array of numbers. A task obviously too simple for college course, but with dreams you get what you are given.
 </p>
 <p>
  Discussion started with this function:
 </p>
 <ol class="code">
  <li>
   <code>
    function average(arr) {
   </code>
  </li>
  <li class="tab1">
   <code>
    var i, sum = 0;
   </code>
  </li>
  <li class="tab1">
   <code>
    for(i=0;i&lt;arr.length;i++) {
   </code>
  </li>
  <li class="tab2">
   <code>
    sum += arr[i];
   </code>
  </li>
  <li class="tab1">
   <code>
    }
   </code>
  </li>
  <li class="tab1">
   <code>
    return sum/i;
   </code>
  </li>
  <li>
   <code>
    }
   </code>
  </li>
  <li>
  </li>
  <li class="download">
   Download this code:
   <a href="http://markos.gaivo.net/blog/code/dreamjs.txt" title="Download the above code as a text file">
    /code/dreamjs.txt
   </a>
  </li>
 </ol>
 <p>
  Dream me, who by the way is significantly more bitchy than I ever am, wasn’t pleased and thought he could save few bytes by storing counter and sum inside of the array:
 </p>
 <ol class="code">
  <li>
   <code>
    function average(arr) {
   </code>
  </li>
  <li class="tab1 cmnt">
   <code>
    // Store counter in array[0] and sum in array[1]
   </code>
  </li>
  <li class="tab1">
   <code>
    if (arr.length &lt; 3) {
   </code>
  </li>
  <li class="tab2">
   <code>
    return arr.length == 2 ? arr[0]+arr[1] : arr[0];
   </code>
  </li>
  <li class="tab1">
   <code>
    } else {
   </code>
  </li>
  <li class="tab2">
   <code>
    arr[1] = arr[0]+arr[1];
   </code>
  </li>
  <li class="tab2">
   <code>
    arr[0] = 2;
   </code>
  </li>
  <li class="tab2">
   <code>
    for(;arr[0]&lt;arr.length;arr[0]++) {
   </code>
  </li>
  <li class="tab3">
   <code>
    arr[1] += arr[arr[0]];
   </code>
  </li>
  <li class="tab2">
   <code>
    }
   </code>
  </li>
  <li class="tab1">
   <code>
    }
   </code>
  </li>
  <li class="tab1">
   <code>
    return arr[1]/arr[0];
   </code>
  </li>
  <li>
   <code>
    }
   </code>
  </li>
  <li>
  </li>
  <li class="download">
   Download this code:
   <a href="http://markos.gaivo.net/blog/code/dreamjs2.txt" title="Download the above code as a text file">
    /code/dreamjs2.txt
   </a>
  </li>
 </ol>
 <p>
  This looked ugly, but what bothered him (me?) was more that it also had a bug. Integer in
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/JavaScript" rel="wikipedia" title="JavaScript">
   Javascript
  </a>
  is limited to 2
  <sup>
   53
  </sup>
  , which is a lot, but sum can still
  <a class="zem_slink" href="http://en.wikipedia.org/wiki/Arithmetic_overflow" rel="wikipedia" title="Arithmetic overflow">
   overflow
  </a>
  or underflow it. Since mean can never be smaller than smallest or bigger than biggest number in a list, I could fix it by writing:
 </p>
 <ol class="code">
  <li>
   <code>
    function average(arr) {
   </code>
  </li>
  <li class="tab1">
   <code>
    var n = arr.length, sum=0;
   </code>
  </li>
  <li class="tab1">
   <code>
    while (arr.length) {
   </code>
  </li>
  <li class="tab2">
   <code>
    sum += arr.pop()/n;
   </code>
  </li>
  <li class="tab1">
   <code>
    }
   </code>
  </li>
  <li class="tab1">
   <code>
    return sum;
   </code>
  </li>
  <li>
   <code>
    }
   </code>
  </li>
  <li>
  </li>
  <li class="download">
   Download this code:
   <a href="http://markos.gaivo.net/blog/code/dreamjs3.txt" title="Download the above code as a text file">
    /code/dreamjs3.txt
   </a>
  </li>
 </ol>
 <p>
  End of dream. Everything edited for sanity and brevity.
 </p>
 <p>
  I don’t have much to say about second program except that I would never write something so ugly just to save 16 bytes in a function like this. I wouldn’t even use Javascript if memory was that important.
 </p>
 <p>
  I am more intrigued by third program. Bug in second is definitely there, even though few of us operate with numbers big enough to encounter it.
 </p>
 <p>
  It’s interesting, because if I was awake, I would probably never think of it. I used to worry about bugs like this all the time, when I was coding in C. It was an unavoidable consequence of the language.
 </p>
 <p>
  I guess what I am getting at is that it is nice to code in a high-level language and for the most part not think about implementation details like this, but only as long as you actually know them so your brain gets triggered when they matter. Speaking of details, I bet those divisions can cause rounding errors.
 </p>
 <div class="zemanta-pixie">
  <a class="zemanta-pixie-a" href="http://reblog.zemanta.com/zemified/7ab2d445-07ff-4ec6-bed9-f29a2797d7a3/" title="Reblog this post [with Zemanta]">
   <img alt="Reblog this post [with Zemanta]" class="zemanta-pixie-img" src="http://img.zemanta.com/reblog_e.png?x-id=7ab2d445-07ff-4ec6-bed9-f29a2797d7a3"/>
  </a>
  <span class="zem-script paragraph-reblog">
   <script defer="defer" src="http://static.zemanta.com/readside/loader.js" type="text/javascript">
   </script>
  </span>
 </div>
</div>
