def containsEvenDigit(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return True
        n //= 10
    return False


def z3(t):
    for row in t:
        for k in row:
            if not containsEvenDigit(k):
                break
        else:
            return True
    return False
