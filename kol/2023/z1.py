def compliant(a, b, primes):
    sqa, sqb = int(a ** 0.5 + 1), int(b ** 0.5 + 1)
    for i in range(2, max(sqa, sqb)):
        if primes[i]:
            if sqa % i == 0 and sqb % i != 0:
                return False
            elif sqa % i != 0 and sqb % i == 0:
                return False
    return True


def getPrimes(T):
    lim = len(T)
    T[0] = T[1] = False
    for i in range(2, lim):
        if T[i]:
            j = i * i
            while j < lim:
                T[j] = False
                j += i


def jakMialoByc(T):
    n = len(T)
    primes = [True for _ in range(1000)]
    getPrimes(primes)
    cnt = 0
    previousResults = [[False, False], [False, False]]
    for i in range(n):
        complWithNext = [i < n - j and compliant(T[i], T[i + j], primes) for j in [1, 2]]
        if (complWithNext[0] or complWithNext[1] or previousResults[0][1] or
                previousResults[1][0]):
            cnt += 1
        previousResults[0] = previousResults[1]
        previousResults[1] = complWithNext
    return cnt


def coOdjebalem(T):
    n = len(T)
    primes = [True for _ in range(1000)]
    getPrimes(primes)
    cnt = 0
    previousResult = False
    for i in range(n):
        complWithNext = i < n - 1 and compliant(T[i], T[i + 1], primes)
        if complWithNext or previousResult:
            cnt += 1
        previousResult = complWithNext
    return cnt
