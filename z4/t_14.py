from math import ceil


def z14(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    mincompl = ceil(0.33 * (n1 ** 2))
    for sx in range(0, n2 - n1):
        for sy in range(0, n2 - n1):
            complC = 0
            for i in range(n1 ** 2):
                if compl(t1[i // n1][i % n1], t2[sy + i // n1][sx + i % n1]):
                    complC += 1
                    if complC == mincompl:
                        return True
    return False
