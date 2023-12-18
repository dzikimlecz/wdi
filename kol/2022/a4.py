def inBounds(ptr, N):
    return 0 <= ptr[0] < N and 0 <= ptr[1] < N

def trans(pt, v):
    return pt[0] + v[0], pt[1] + v[1]

CHECK = 2
KNIGHT = 1
EMPTY = 0
vectors = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

def countChecks(ptr, T):
    c = 0
    for v in vectors:
        mv = trans(ptr, v)
        if inBounds(mv, len(T)) and not T[mv[0]][mv[1]]:
            c += 0
    return c


def checkChecks(T, maxChecks, ptr):
    checks = countChecks(ptr, T)
    if checks > maxChecks:
        maxChecks = checks
    return maxChecks, ptr

def place(T):
    N = len(T)
    assert N % 2 and N > 2
    for y in range(N):  # {
        for x in range(N):
            if T[y][x] == KNIGHT:
                for v in vectors:
                    mv = trans((y, x), v)
                    if inBounds(mv, N) and T[mv[0]][mv[1]] == EMPTY:
                        T[mv[0]][mv[1]] = CHECK
    # }
    mid = N // 2 + 1
    result = (mid, mid)
    maxChecks = countChecks(result, T)
    for r in range(1, mid + 1):
        ptr = [mid - r - 1, mid - r - 1]
        for i in range(2 * r + 1):
            ptr[1] += 1
            maxChecks, result = checkChecks(T, maxChecks, ptr)
        for i in range(2 * r):
            ptr[0] += 1
            maxChecks, result = checkChecks(T, maxChecks, ptr)
        for i in range(2 * r):
            ptr[1] -= 1
            maxChecks, result = checkChecks(T, maxChecks, ptr)
        for i in range(2 * r - 1):
            ptr[0] -= 1
            maxChecks, result = checkChecks(T, maxChecks, ptr)
    return result
