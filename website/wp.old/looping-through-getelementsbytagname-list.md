Title: Looping through getElementsByTagName list
Date: 2005-08-20 15:37
Author: markos
Category: Javascript
Slug: looping-through-getelementsbytagname-list

There's a small quirk that developers hit now and then when they are
processing a list of elements returned by getElementsByTagName function.
Usual, but still unexpected behavior is that not all elements of the
list have been processed and if you are using javascript console, it
might complain that there's no element in the list at index, where
you're certain it should be.

The reason for this is that returned list of elements is not really a
list. It's a live view of matching elements. If you delete one of them
in document, it will be removed from the list as well. List will become
shorter and some elements in it may change their position to fill empty
slot formerly occupied by deleted element.

Therefore, if you loop through such a list and its possible that you
might remove current element, it's best to loop from last element to the
first. This keeps positions stable and predictable even when you delete.

It can be a bit trickier to handle if you add matching elements inside
such loop. Sadly there's no easy solution that would work all the time
and you have to take in account your situation.

