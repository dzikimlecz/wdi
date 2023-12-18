from z5.z18 import movable


def f():
    global T
    N = 8

    def route(dest, vectors):
        nonlocal good

        def findNext(ptr) -> bool:
            nonlocal dest, vectors
            if ptr[0] == dest[0] and ptr[1] == dest[1]:
                return True
            found = False
            for v in vectors:
                y, x = ptr[0] + v[0], ptr[1] + v[1]
                if 0 <= y < N and 0 <= x < N and good[y][x] and movable(ptr, (y, x)):
                    found = findNext((y, x))
                    if found:
                        return True

            if not found:
                good[ptr[0]][ptr[1]] = False
                return False

        return findNext((0, 0))

    dests = [(N - 1, N - 1), (N - 1, 0), (0, N - 1)]
    vectorsList = [[(0, 1), (1, 0), (1, 1)],
                   [(0, 1), (-1, 0), (-1, 1)],
                   [(0, -1), (1, 0), (1, -1)]
                   ]
    for i in range(len(dests)):
        good = [[True for _ in range(N)] for _ in range(N)]
        if route(dests[i], vectorsList[i]):
            return True
    return False

