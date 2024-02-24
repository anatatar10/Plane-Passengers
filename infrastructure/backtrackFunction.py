def backtrackFunction(k, l = [], result = [], firstElement = lambda x: x[0], isCorrect= lambda y: y == 2,
                      isSolution = lambda x, y: x == y):
    """
    Backtracking:
    :param k: length of the groups
    :param l: list from which the elements are selected
    :param result: the resulted list
    :param firstElement: initial element
    :param isCorrect: check if the new element is correct
    :param isSolution: check if the resulted list is the solution, if it has the k length
    :return:
    """
    result.append(firstElement(l))
    count = 0
    while count < len(l):
        if isCorrect(result):
            if isSolution(len(result), k):
                yield result
            else:
                yield from backtrackFunction(k, l[count:], result[:], firstElement, isCorrect, isSolution)
        count += 1
        if count < len(l):
            result[-1] = l[count]