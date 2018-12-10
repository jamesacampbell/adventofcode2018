
"""Find all strings that have two and three chars repeating for Day 2 Part 1."""
"""Author: James Campbell"""

from collections import Counter

# globals
all2 = set()
all3 = set()
both = set()

# functions


def find_dup_char(input):

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
    print(WC)

    # Finding no. of  occurrence of a character
    # and get the index of it.
    for k, i in WC.items():
        if(i == 2):
            print(i, k, input)
            all2.add(input)
        if(i == 3):
            print(i, k, input)
            all3.add(input)
    if input in all2 and input in all3:
        both.add(input)


# main
if __name__ == "__main__":
    with open('input.txt') as f:
        strings = f.read().splitlines()
    for item in strings:
        find_dup_char(item)
    print(len(all2), len(all3), len(both))
