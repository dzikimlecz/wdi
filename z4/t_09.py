def z9(t, k):
    n = len(t)
    side = 3
    while side <= n:
        for x in range(n - side + 1):
            for y in range(n - side + 1):
                theSum = t[y][x] + t[y][x + side - 1] + t[y + side - 1][x] + \
                        t[y + side - 1][x + side - 1]
                if theSum == k:
                    return True, y + ((side - 1) // 2), x + ((side - 1) // 2)
        side += 2
    return False, None, None


if __name__ == '__main__':
    t = [
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]
    print(z9(t, 5))
