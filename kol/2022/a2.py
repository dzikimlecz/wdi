def inSeq(a, b, c):
    if nxt(a, b) != c:
        return False
    while a > 1:
        b, a = a, b - a + 1
    return a == 1

def nxt(a, b):
    return a + b - 1

def seq(T):
    N = len(T)
    l, maxlen = 0, 0
    y = 0
    for y in range(N - 2):
        for x in range(N - 2):
            if T[y][x + 1] == T[y + 1][x] and T[y][x + 2] == T[y + 2][x] and \
                inSeq(T[y][x], T[y][x + 1], T[y][x + 2]):
                l = 3
                while y + l < N and x + l < N and\
                        (nxt(T[y][x + l - 2], T[y][x + l - 1]) != T[y][x + l]
                        or nxt(T[y + l - 2][x], T[y + l - 1][x]) != T[y + l][x]):
                        l += 1
                        maxlen = max(l, maxlen)
    maxlen = max(l, maxlen)
    return maxlen


if __name__ == '__main__':
    t = [[14, 22, 35],
         [22, 35, 56],
         [35, 56, 90]
         ]
    print(seq(t))