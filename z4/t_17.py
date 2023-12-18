def z17(t):
    maxSum = 0
    yx = None
    n = len(t)
    for i in range(n ** 2):
        y0, x0 = i // n, i % n
        s = 0
        for y in range(y0 - 1, y0 + 2):
            for x in range(x0 - 1, x0 + 2):
                if (x != x0 or y != x0) and 0 <= x < n and 0 <= y < n:
                    s += t[y][x]
        if maxSum < s:
            maxSum = s
            yx = y0, x0
    return yx
