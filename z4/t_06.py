def z6(T1, T2):
    N = len(T1)
    M = N * N
    ptrs = [0 for _ in range(N)]
    prev = None
    mi = 0
    for _ in range(M):
        minN, mini = None, None
        for i in range(N):
            if ptrs[i] < N:
                n = T1[i][ptrs[i]]
                if minN is None or n < minN:
                    minN, mini = n, i
        if prev is None or prev != minN:
            T2[mi] = minN
            mi += 1
        elif T2[mi - 1] == minN:
            T2[mi - 1] = 0
            mi -= 1
        prev = minN
        ptrs[mini] += 1
    for i in range(mi, M):
        T2[i] = 0


if __name__ == '__main__':
    T1 = [[1, 4, 6, 7], [2, 3, 5, 7], [3, 4, 7, 9], [1, 1, 1, 1]]
    T2 = [0 for _ in range(16)]
    z6(T1, T2)
    print(T2)