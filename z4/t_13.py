def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def z13(t):
    n = len(t)
    matrix = [[True for _ in range(n)] for _ in range(n)]
    for i in range(1, n ** 2):
        if matrix[i // n][i % n]:
            a = t[i // n][i % n]
            for j in range(i + 1, n ** 2):
                b = t[j // n][j % n]
                if isPrime(a + b):
                    matrix[i // n][i % n] = matrix[j // n][j % n] = False
    for i in range(1, n ** 2):
        if matrix[i // n][i % n]:
            t[i // n][i % n] = 0

