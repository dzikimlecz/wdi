def inBounds(move, N):
    return 0 <= move[0] < N and 0 <= move[1] < N


def rook(N, L):
    minLen = N * 3

    def rec(ptr=(0, 0), depth=0):
        nonlocal N, L, minLen

        if ptr == (N - 1, N - 1):
            minLen = min(depth, minLen)
            return

        maxy = ptr[0]
        while maxy + 1 < N and (maxy + 1, ptr[1]) not in L:
            maxy += 1
        for y in range(maxy, ptr[0], -1):
            move = (y, ptr[1])
            rec(move, depth + 1)

        maxx = ptr[1]
        while maxx + 1 < N and (ptr[0], maxx + 1) not in L:
            maxx += 1
        for x in range(maxx, ptr[1], -1):
            move = (ptr[0], x)
            rec(move, depth + 1)

    rec()
    return minLen if minLen != N * 3 else None

