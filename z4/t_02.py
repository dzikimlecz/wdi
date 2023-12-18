def containsOddDigit(n):
    while n > 0:
        if (n % 10) % 2 == 1:
            return True
        n //= 10
    return False


def z2(t):
    for row in t:
        for k in row:
            if containsOddDigit(k):
                break
        else:
            return False
    return True

