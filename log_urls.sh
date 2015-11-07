grep -v " 404 "|grep -v "%5C%5C%5C"|awk -F" " '{print $7}'|grep blog|sort|uniq -c|sort
