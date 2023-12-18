def out(x):
    print(x, end='')


def divide(a: int, b: int):
    out(a // b)
    out(',')
    a -= (a // b) * b
    x = b
    c2 = 0
    while x % 2 == 0:
        x /= 2
        c2 += 1
    x = b
    c5 = 0
    while x % 5 == 0:
        x /= 5
        c5 += 1
    c = max(c2, c5)
    for i in range(c):
        if a == 0:
            break
        a *= 10
        out(a // b)
        a -= (a // b) * b
    if a == 0:
        return
    a *= 10
    fa = a
    d = a // b
    out('(')
    out(d)
    a -= d * b
    a *= 10
    while a != fa:
        d = a // b
        out(d)
        a -= d * b
        a *= 10
    print(')')


if __name__ == '__main__':
    divide(99, 97)
    divide(2, 97)
