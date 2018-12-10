"""Get LD distance of 1 only from list of strings for Day 2 part 2."""
"""Author: James Campbell"""

# imports
from Levenshtein import distance, matching_blocks, editops

# globals
neardupes = dict()

# functions


def calculateDistance(input):
    """Look for where Levenshtein Devereau distance is 1 only."""
    for i in strings:
        distancevalue = distance(input, i)
        if distancevalue == 1:
            neardupes[input] = i


def getMatches(a, b):
    """Get matched characters only for answer."""
    mb = matching_blocks(editops(a, b), a, b)
    print("The answer is the following string:")
    print(''.join([a[x[0]:x[0]+x[2]] for x in mb]))


# main
if __name__ == "__main__":
    with open('input.txt') as f:
        strings = f.read().splitlines()
    for item in strings:
        calculateDistance(item)
    # print(neardupes) # testing to see dict
    for k, v in neardupes.items():
        getMatches(k, v)
        break  # only need to run once
