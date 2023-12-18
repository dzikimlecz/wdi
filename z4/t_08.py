import math


def z8(t):
    n = len(t)
    start = [n - 3, 0]
    maxlen = 0
    while start[0] >= 0:
        cursor = [start[0] + 1, start[1] + 1]
        q = None
        l = 1
        while cursor[0] < n and cursor[1] < n:
            a = t[cursor[0]][cursor[1]]
            b = t[cursor[0] - 1][cursor[1] - 1]
            if b != 0 and q is None:
                q = a / b
                l = 2
            elif b != 0 and a / b == q:
                l += 1
            else:
                maxlen = max(maxlen, l)
                if b == 0:
                    q = None
                    l = 1
                else:
                    q = a / b
                    l = 2
            cursor[0] += 1
            cursor[1] += 1
        start[0] -= 1
        maxlen = max(maxlen, l)
    return maxlen if maxlen >= 3 else 0


if __name__ == '__main__':
    t = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    print(z8(t))