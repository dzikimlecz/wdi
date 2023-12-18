def f(T):
    N = len(T)
    lim = N ** 2
    vectors = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]
    for i in range(lim):
        T[i // N][i % N] = 0

    def findNext(ptr, i) -> bool:
        T[ptr[0]][ptr[1]] = i
        if i == lim:
            return True
        found = False
        for v in vectors:
            y, x = ptr[0] + v[0], ptr[1] + v[1]
            if 0 <= y < N and 0 <= x < N and not T[y][x]:
                found = findNext((y, x), i + 1)
                if found:
                    return True
        if not found:
            T[ptr[0]][ptr[1]] = 0
            return False
    assert findNext((0, 0), 1)


if __name__ == '__main__':
    t = [[0 for _ in range(6)] for _ in range(6)]
    f(t)
    for row in t:
        print(row)
