def z20(t):
    n = len(t)
    rsums = [0 for _ in range(n)]
    csums = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rsums[i] += t[i][j]
            csums[j] += t[i][j]
    maxC1 = maxC2 = -1
    yx1 = yx2 = None
    for i in range(n ** 2):
        y, x = i // n, i % n
        k = rsums[y] + csums[x] - t[y][x]
        if k > maxC1:
            maxC1 = k
            yx1 = y, x
        elif k > maxC2:
            maxC2 = k
            yx2 = y, x
    return yx1, yx2
