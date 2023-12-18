def seq(T):
    N = len(T)
    starts, sptr = [-1 for _ in range(N)], 0
    ends, eptr = [-1 for _ in range(N)], 0
    l = 0
    for i in range(1, N):
        if T[i - 1] < T[i]:
            if l == 0:
                l = 2
            else:
                l += 1
        elif l > 2:
            starts[sptr] = i - l
            sptr += 1
            ends[eptr] = i - 1
            eptr += 1
            l = 0
        else:
            l = 0
    if l != 0:
        ends[eptr] = N - 1
        eptr += 1
    maxs1 = maxs2 = None
    mine1 = mine2 = None
    invalid1 = invalid2 = True
    for i in range(eptr):
        ch1 = False
        if maxs1 is None or maxs1 < T[starts[i]]:
            maxs1 = T[starts[i]]
            ch1 = True
            invalid1 = False
        elif maxs2 is None or maxs2 < T[starts[i]]:
            maxs2 = T[starts[i]]
            invalid2 = False
        if mine1 is None or mine1 > T[ends[i]]:
            mine1 = T[ends[i]]
            if ch1:
                ch1 = False
                invalid1 = True
        elif mine2 is None or mine2 > T[ends[i]]:
            mine2 = T[ends[i]]
    if not invalid1:
        return mine1 < maxs1
    elif not invalid2:
        return mine2 < maxs1 or mine1 < maxs2
    return False

if __name__ == '__main__':
    print(seq([2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]))
