def cross(ptr, T):
    N = len(T)
    res = [[0 for _ in range(N - 1)] for _ in range(N - 1)]
    for y in range(ptr[0]):
        for x in range(ptr[1]):
            res[y][x] = T[y][x]
        for x in range(ptr[1] + 1, N):
            res[y][x - 1] = T[y][x]
    for y in range(ptr[0] + 1, N):
        for x in range(ptr[1]):
            res[y - 1][x] = T[y][x]
        for x in range(ptr[1] + 1, N):
            res[y - 1][x - 1] = T[y][x]
    return res

def f(T, sumVal):
    N = len(T)
    if N == 1:
        return T[0][0] == sumVal
    for y in range(N):
        for x in range(N):
            if f(cross((y, x), T), sumVal - T[y][x]):
                return True
    return False
