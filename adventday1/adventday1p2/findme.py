# Author: James Campbell
# What: Solves day 1 part 2 adventofcode2018

import os
import subprocess

# globals
filedata = 'info.txt'

# functions


def loaddata(filedata):
    """Loads list of numbers into list"""
    with open(filedata, 'r') as f:
        loadeddata = f.read().splitlines()
    return loadeddata


def iteratethrough(listdata):
    i = 0
    x = 0
    addedlist = list()
    while i < len(listdata):
        x = x + int(listdata[i])
        addedlist.append(x)
        i = i + 1
    print(x)
    return addedlist, x


def samenesschecker(startingvalue, listdata, iteratedvalues):
    i = 0
    x = startingvalue
    while i < len(listdata):
        x = x + int(listdata[i])
        if x in iteratedvalues:
            print(f'found x! {x} at {i} {listdata[i]}')
            exit('done')
        else:
            iteratedvalues.append(x)
        i = i + 1
    return iteratedvalues


def main():
    # subprocess.call('clear')
    loadedlist = loaddata(filedata)
    iteratedvalues, finalvalue = iteratethrough(loadedlist)
    newiteratedvalues = samenesschecker(finalvalue, loadedlist, iteratedvalues)
    newiteratedvalues = samenesschecker(
        finalvalue, loadedlist, newiteratedvalues)


# make sure we are running this from this file
if __name__ == "__main__":
    main()
