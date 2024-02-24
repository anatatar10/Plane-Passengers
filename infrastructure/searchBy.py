def searchBy(item1, l, condition = lambda x1, x2: x1 == x2):

    result = []
    for item2 in l:
        if condition(item1, item2):
            result.append(item2)
    return result[:]
