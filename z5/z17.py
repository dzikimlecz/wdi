import math


def isPrime(n):
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def llen(n):
    if not n:
        return 0
    return int(math.log10(n)) + 1


def insertDigit(d, n, ix):
    l = llen(n)
    factor = int(10 ** (l - ix))
    if factor < 10:
        return n * 10 + d
    return ((n // factor) * 10 + d) * factor + (n % factor)


def f(A, B):
    primes = set()

    def rec(a=A, b=B, minIndex=0):
        nonlocal primes
        la = llen(a)
        lb = llen(b)
        if lb - minIndex + 1 < la:
            return
        if la == 1:
            for i in range(minIndex, lb + 1):
                n = insertDigit(a, b, i)
                if isPrime(n):
                    primes.add(n)
            return

        d = a // int(10 ** (la - 1))
        withoutFirst = a % int(10 ** (la - 1))
        for i in range(minIndex, lb + 1):
            n = insertDigit(d, b, i)
            rec(withoutFirst, n, i + 1)
    rec()
    return len(primes)


if __name__ == '__main__':
    print(f(13, 12))
