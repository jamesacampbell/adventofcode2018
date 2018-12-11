from collections import namedtuple
import numpy as np
from matplotlib import pyplot as plt
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

ra = Rectangle(3., 3., 5., 5.)
rb = Rectangle(1., 1., 4., 3.5)
# intersection here is (3, 3, 4, 3.5), or an area of 1*.5=.5

datalist = list()
overlaps = set()
nparrayready = list()


def area(a, b):  # returns None if rectangles don't intersect
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if a.min_x > b.max_x or a.max_x < b.min_x:
        return False
    if a.min_y > b.max_y or a.max_y < b.min_y:
        return False
    if (dx >= 0) and (dy >= 0):
        return True
    else:
        return False


def areaeach(a):  # returns None if rectangles don't intersect
    count = 0
    for b in datalisted:
        # dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
        # dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
        # if (dx >= 0) and (dy >= 0):
        if a.xmin < b.xmax and a.ymax > b.ymin:
            count = count + 1
    print(count)
    if count >= 2:
        return True
    else:
        return False


def loadData(input):
    with open(input, 'r') as f:
        listofitems = f.read().splitlines()
    rects = [i.split('@')[1] for i in listofitems]
    for item in rects:
        x1 = int(item.split(',')[0])
        y1 = int(item.split(',')[1].split(':')[0])
        x2 = x1+int(item.split(':')[1].split('x')[0])
        y2 = y1+int(item.split('x')[1])
        datalist.append(Rectangle(x1, y1, x2, y2))
    return datalist


def explodeRect(rect):
    i = 0
    z = 0
    print(rect)
    tinycoords = list()
    while i < (rect.xmax - rect.xmin):
        while z < (rect.ymax - rect.ymin):
            #fillin = (rect.xmin + i, rect.ymin + z)
            Matrix[rect.xmin + i][rect.ymin + z] += 1
            tinycoords.append([rect.xmin + i, rect.ymin + z])
            z = z + 1
        z = 0
        i = i + 1
    # print(tinycoords)
    return tinycoords, Matrix


def checkfor2():
    i, z, totaloverlap = 0, 0, 0
    while i < 1000:
        while z < 1000:
            if Matrix[i][z] > 1:
                totaloverlap += 1
            z += 1
        z = 0
        i += 1
    return totaloverlap


def checkfor0():
    i, z, zerooverlap = 0, 0, 0
    while i < 1000:
        while z < 1000:
            if Matrix[i][z] < 1:
                zerooverlap += 1
                print("matrix:", i, z)
            z += 1
        z = 0
        i += 1
    return zerooverlap


if __name__ == "__main__":
    datalisted = loadData('input.txt')
    Matrix = [[0 for x in range(1000)] for x in range(1000)]
    print(Matrix[1][1])
    for item in datalisted:
        tinycoordslist, Matrix = explodeRect(item)
        nparrayready = nparrayready + tinycoordslist
    lol = np.array(nparrayready)
    x, y = lol.T
    plt.scatter(1000, 1000)
    plt.scatter(x, y)
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    plt.show()
    print(checkfor2())
    print(checkfor0())
    exit()

    # print(datalisted)
    for item in datalisted:
        overlap = False
        overlap = areaeach(item)
        if overlap == True:
            overlaps.add(item)
    print(len(overlaps))
