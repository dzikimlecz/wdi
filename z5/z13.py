def z13(n):

    def P(n, k):
        if k < 1 or n < k:
            return []
        if k == 1:
            return [[n]]
        if n == k:
            return [[1 for _ in range(n)]]
        p1 = P(n - 1, k - 1)
        p2 = P(n - k, k)
        for part in p1:
            part += [1]
        for part in p2:
            for i in range(len(part)):
                part[i] += 1
        return p1 + p2

    for k in range(n+1):
        for p in P(n, k):
            print(p)


if __name__ == '__main__':
    z13(7)
