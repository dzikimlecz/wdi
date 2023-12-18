def primebased(n):
    if not n:
        return False
    primes = [2, 3, 5, 7]
    while n > 0:
        if (n % 10) not in primes:
            return False
        n //= 10
    return True


def z16(t):
    for row in t:
        for n in row:
            if primebased(n):
                break
        else:
            return False
    return True
