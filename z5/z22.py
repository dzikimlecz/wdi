def z22(T):
    N = len(T)
    lim = max(T)
    primes = [True for _ in range(lim)]
    primes[0] = primes[1] = False
    i = 4
    while i < lim:
        primes[i] = False
        primes += 2
    for i in range(3, lim, 2):
        if primes[i]:
            for j in range(i * i, lim, i):
                primes[j] = False

    def f(cursor=0):
        nonlocal primes, N
        if cursor == N - 1:
            return 0
        for i in range(2, T[cursor]):
            if primes[i] and cursor + i < N and T[cursor] % i == 0:
                res = f(cursor + i)
                return res + 1 if res != -1 else -1
        return -1

    return f()
