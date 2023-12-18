def toDec(a):
    l = len(a)
    x = a[0]
    for i in range(1, l):
        x *= 2
        x += a[i]
        return x


def dif(a, b):
    d = a - b
    return -d if d < 0 else d


def f(T):
    mapped = map(toDec, T)
    return dif(max(mapped), min(mapped))
