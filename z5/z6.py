def combi(n, k):
    zbior = [0 for _ in range(k)]
    for i in range(k):
        zbior[i] = i + 1
    j = 1
    while j >= 0:
        yield zbior
        if zbior[k - 1] < n:
            j = k - 1
        else:
            j = k - 2
            while j >= 0 and zbior[j] + 1 == zbior[j + 1]:
                j -= 1
        if j >= 0:
            zbior[j] += 1
            for i in range(j + 1, k):
                zbior[i] = zbior[i - 1] + 1

def f(T):
    N = len(T)
    for llen in range(1, N):
        cs = combi(N, llen)
        for c in cs:
            s1 = s2 = 0
            for i in c:
                s1 += i - 1
                s2 += T[i - 1]
            if s1 == s2:
                return map(lambda x: x - 1, c)
    return None




if __name__ == '__main__':
    print(f([1, 7, 3, 5, 11, 2]))
