from math import inf


def getLeaders(sums):
    leaders = [None, None, None, None]
    ixes = [None, None, None, None]
    for i in range(len(sums)):
        s = sums[i]
        if s >= 0:
            if leaders[0] is None or leaders[0] < s:
                leaders[0] = s
                ixes[0] = i
            if leaders[1] is None or leaders[1] > s:
                leaders[1] = s
                ixes[1] = i
        elif leaders[2] is None or leaders[2] < s:
            leaders[2] = s
            ixes[2] = i
        elif leaders[3] is None or leaders[3] > s:
            leaders[3] = s
            ixes[3] = i
    return leaders, ixes


def z4(t):
    n = len(t)
    rsums = [0 for _ in range(n)]
    csums = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rsums[i] += t[i][j]
            csums[j] += t[i][j]
    rleaders, rixes = getLeaders(rsums)
    cleaders, cixes = getLeaders(csums)
    erste = rleaders[0] / cleaders[1] if rleaders[0] is not None and (cleaders[1] is not None and cleaders[1] != 0) else -inf
    zweite = rleaders[3] / cleaders[2] if rleaders[3] is not None and (cleaders[2] is not None and cleaders[2] != 0) else -inf
    dritte = rleaders[1] / cleaders[3] if rleaders[1] is not None and (cleaders[3] is not None and cleaders[3] != 0) else -inf
    vierte = rleaders[2] / cleaders[0] if rleaders[2] is not None and (cleaders[0] is not None and cleaders[0] != 0) else -inf
    if erste > zweite and erste > dritte and erste > vierte:
        return rixes[0], cixes[1]
    if zweite > erste and zweite > dritte and zweite > vierte:
        return rixes[3], cixes[2]
    if dritte > zweite and dritte > erste and dritte > vierte:
        return rixes[1], cixes[3]
    if vierte > zweite and vierte > dritte and vierte > erste:
        return rixes[2], cixes[0]




