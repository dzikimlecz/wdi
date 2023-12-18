from z5.z17 import llen


def movable(fromPtr, toPtr):
    global T
    fromDigit = T[fromPtr[0]][fromPtr[1]] % 10
    toDigit = T[toPtr[0]][toPtr[1]]
    toDigit //= int(10 ** (llen(toDigit) - 1))
    return fromDigit < toDigit


def f():
    N = 8
    vectors = [(0, 1), (1, 0), (1, 1)]
    good = [[True for _ in range(N)] for _ in range(N)]

    def findNext(ptr) -> bool:
        if ptr[0] == ptr[1] == N - 1:
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


