def distFactorsCnt(n):
    i = 2
    cnt = 0
    while n > 1:
        if n % i == 0:
            cnt += 1
            n //= i
            while n % i == 0:
                n //= i
        i += 1
    return cnt

def square(T):
    N = len(T)
    for a in range(1, N):
        for y in range(0, N - a + 1):
            for x in range(0, N - a + 1):
                q = T[y][x] * T[y][x + a - 1] * T[y + a - 1][x] * T[y + a - 1][x + a - 1]
                if distFactorsCnt(q) == 2:
                    return a
    return 0

if __name__ == '__main__':
    t = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3],
    ]
    print(square(t))