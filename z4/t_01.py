def z1(t):
    n = len(t)
    h, w = n, n
    vectors, vi = [1, -1], 0
    k, lim = 1, n ** 2 + 1
    c = [0, 0]
    for _ in range(n):
        for _ in range(w):
            t[c[0]][c[1]] = k
            k += 1
            c[1] += vectors[vi]
        c[0] += vectors[vi]
        c[1] -= vectors[vi]
        h -= 1
        for _ in range(h):
            t[c[0]][c[1]] = k
            k += 1
            c[0] += vectors[vi]
        w -= 1
        c[0] -= vectors[vi]
        vi = ~vi
        c[1] += vectors[vi]


if __name__ == '__main__':
    t = [[0 for _ in range(7)] for _ in range(7)]
    z1(t)
    for line in t:
        for e in line:
            print(e, end='\t')
        print()
