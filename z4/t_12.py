def isComplex(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False


def inBounds(x, y, n, x1, y1):
    return (x != x1 or y != y1) and 0 <= x < n and 0 <= y < n


def z12(T):
    N = len(T)
    firstSliceComplexCount = None
    for surface in T:
        matrix = [[isComplex(surface[y][x]) for x in range(N)] for y in range(N)]
        sliceComplexCount = 0
        for x in range(0, N):
            for y in range(0, N):
                complexCount = 0
                for y1 in range(y - 1, y + 2):
                    for x1 in range(x - 1, x + 2):
                        if inBounds(x1, y1, N, x, y) and matrix[y1][x1]:
                            complexCount += 1
                if complexCount >= 6:
                    sliceComplexCount += 1
        if firstSliceComplexCount is None:
            firstSliceComplexCount = sliceComplexCount
        elif firstSliceComplexCount != sliceComplexCount:
            return False
    return True


if __name__ == '__main__':
    t = [
        [
            [
                4, 4, 0, 0
            ],
            [
                4, 0, 4, 0
            ],
            [
                4, 4, 0, 0
            ],
            [
                0, 0, 0, 0
            ]
        ],
        [
            [
                4, 4, 0, 0
            ],
            [
                4, 0, 4, 0
            ],
            [
                4, 4, 0, 0
            ],
            [
                0, 0, 0, 0
            ]
        ],
        [
            [
                4, 4, 0, 0
            ],
            [
                4, 0, 4, 0
            ],
            [
                4, 4, 0, 0
            ],
            [
                0, 0, 0, 0
            ]
        ],
        [
            [
                4, 4, 0, 0
            ],
            [
                4, 0, 4, 0
            ],
            [
                4, 4, 0, 0
            ],
            [
                0, 0, 0, 0
            ]
        ],
    ]
    print(z12(t))


