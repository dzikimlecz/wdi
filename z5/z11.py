def z11(T, Q, N):
    llen = len(T)
    cnt = 0
    if llen == 0:
        return 0
    if N == 1:
        for e in T:
            if e == Q:
                cnt += 1
    else:
        if Q % T[0] == 0:
            cnt += z11(ohne(T, 0), Q // T[0], N - 1)
        cnt += z11(ohne(T, 0), Q, N)
    return cnt


def ohne(T, ix):
    return T[:ix] + T[ix + 1:]


if __name__ == '__main__':
    T = [2, 1, 2, 1]
    print(z11(T, 2, 2))
