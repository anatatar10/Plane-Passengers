def bubbleSort(l, criterian = lambda p1, p2: p1 < p2):
    isSort = False
    while(not isSort):
        isSort = True
        for i in range(0, len(l) - 1):
            if criterian(l[i], l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                isSort = False
    return l[:]