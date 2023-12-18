def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def f(T):
    N = len(T)
    q = 1
    pc = 0
    ix, pix = [-1 for _ in range(N)], 0
    for i in range(N):
        if pc > 2 and q == T[i]:
            ix[pix] = i
            pix += 1
        if isPrime(T[i]):
            pc += 1
            q *= T[i]
    mx = -1
    mix = None
    for i in range(pix):
        if T[ix[i]] > mx:
            mix = ix[i]
            mx = T[mix]
    return mix
