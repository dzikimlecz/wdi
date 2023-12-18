def inBounds(ptr, N):
    return 0 <= ptr[0] < N and 0 <= ptr[1] < N


def trans(pt, v):
    return pt[0] + v[0], pt[1] + v[1]


def good(T):
    N = len(T)
    checkedColumns = set()
    checkedRows = set()
    for y in range(N):
        for x in range(N):
            if T[y][x]:
                checkedColumns.add(y)
                checkedRows.add(x)
    return len(checkedColumns) == len(checkedRows) == N


def move(T):
    N = len(T)
    checkedColumns = set()
    checkedRows = set()
    rooks = set()
    for y in range(N):
        for x in range(N):
            if T[y][x]:
                rooks.add((y, x))
                checkedColumns.add(y)
                checkedRows.add(x)
    assert len(checkedColumns) == len(checkedRows) == N - 1
    y = x = None
    for i in range(N):
        if y not in checkedRows:
            y = i
        if i not in checkedColumns:
            x = i
    T[y][x] = True
    for r in rooks:
        T[r[0]][r[1]] = False
        if good(T):
            return r, (y, x)
        T[r[0]][r[1]] = True
    assert False

