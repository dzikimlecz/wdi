from math import log2


def fourCompliant(a, b):
    if a == b:
        return True
    if a * b == 0:
        return False
    a, b = min(a, b), max(a, b)
    digs, dptr = [-1 for _ in range(int(log2(a) / 2) + 1)], 0
    while a > 1:
        digs[dptr] = a % 4
        dptr += 1
        a //= 4
    while b > 1:
        d = b % 4
        if d not in digs:
            return False
    return True


def f(T):
    N = len(T)
    flags = [True for _ in range(N)]
    maxcnt = 0
    for i in range(N):
        if flags[i]:
            cnt = 0
            for j in range(i + 1, N):
                if fourCompliant(T[i], T[j]):
                    cnt += 1
                    flags[j] = False
            maxcnt = max(cnt, maxcnt)
    return maxcnt