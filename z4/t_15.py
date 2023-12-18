def containsprime(n):
    primes = [2, 3, 5, 7]
    while n > 0:
        if (n % 10) in primes:
            return True
        n //= 10
    return False


def z15(t):
    for row in t:
        for n in row:
            if not containsprime(n):
                break
        else:
            return True
    return False
