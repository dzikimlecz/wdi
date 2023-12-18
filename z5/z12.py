def z12(t, q, n):
    def f(T=t, Q=q, N=n):
        llen = len(T)
        res = []
        if llen == 0:
            return []
        if N == 1:
            for e in T:
                if e == Q:
                    res += [[Q]]
            return res
        r1 = f(ohne(T, 0), Q, N)
        if Q % T[0] != 0:
            return r1
        res = f(ohne(T, 0), Q // T[0], N - 1)
        for i in range(len(res)):
            res[i] = [T[0]] + res[i]
        return r1 + res
    return f()


def ohne(T, ix):
    return T[:ix] + T[ix + 1:]


if __name__ == '__main__':
    T = [2, 1, 2, 1]
    for x in z12(T, 2, 2):
        print(x)
