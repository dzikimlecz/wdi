vectors = [[1, -2], [1, 2], [2, -1], [2, 1]]
def lookFor(k, t, y, x, n):
    global vectors
    cnt = 0
    for v in vectors:
        y1, x1 = y + v[0], x + v[1]
        if 0 <= y1 < n and 0 <= x1 < n and t[y1][x1] == k:
            cnt += 1
    return cnt


def z19(t, k):
    n = len(t)
    cnt = 0
    for i in range(n ** 2):
        y, x = i // n, i % n
        if k % t[y][x] == 0:
            cnt += lookFor(k // t[y][x], t, y, x, n)
    return cnt
