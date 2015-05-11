#!/usr/bin/env python

# distance written by Magnus Lie Hetland
def distance(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

def distance2(a,b,limit):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    if limit: # If limit is non-zero, than to approximated calculations
        if m-n>=limit:
            return m-n

    if m > 10:
        tmpdist = distance(a[:6],b[:6])
        if tmpdist > 2: # More than one misplaced character between first 6
            return tmpdist

    return distance(a,b)

def distance3(a,b,limit):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    if limit: # If limit is non-zero, than to approximated calculations
        if m-n>=limit:
            return m-n

    return distance(a,b)


if __name__=="__main__":
    from sys import argv
    print distance(argv[1],argv[2])
