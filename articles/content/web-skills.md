Title: Web skills
Date: 2016-06-27 18:45:31
Author: markos
Category: web
Slug: web-skills
Status: published
Tags: web, skills, programming, trick, wikipedia

While following news about Brexit developments and its impact on FTSE100, my wife and I wondered how many people work for companies that are included in that index. Wikipedia provides [a list of FTSE100 companies](https://en.wikipedia.org/wiki/FTSE_100_Index) including their employees numbers, but without the total that interested us.

I did not feel like summing them manually as it is tedious, slow and error prone. Luckily I do not have to as this is a nice example how we can use even limited web development skills to solve every day problems.

All I needed to do is select table cells in last column, transform their values to numbers that Javascript understands and sum them.

On a modern browser this can be accomplished by opening developer tools and executing two lines of code in its console:

	var nodes = [].slice.call(document.querySelectorAll("#constituents tbody td:last-child"));
	nodes.map((a) => parseInt(a.innerText.replace(/,/g, ''), 10)).reduce((a, b)=> a+b, 0);
	
What the first line does is select last table cell (`td:last-child`) in each company row of the table (`#constituents tbody`). `[].slice.call` is used to make the resulting list a Javascript array because it is easy to work with.

In second line we first transform the list of page elements to a list of cell values, by picking them with `.innerText`, removing comma separators (`.replace(/,/g, '')`) and changing them to numbers using `parseInt`. This is immediately followed with a call to `reduce` which sums all the values in our list.

Alternatively I could have also used [jQuery](http://jquery.com) library already included on Wikipedia pages and not much more code to get to the same result.

Turns out that according to Wikipedia there are 5,618,496 people working for FTSE100 companies out of 31.59m in total.