import math


def friendnumbers(n, m):
    l = int(max(math.log10(n), math.log10(m))) + 2
    t1 = [-1 for _ in range(l)]
    t2 = [-1 for _ in range(l)]
    ptr1 = 1
    while n > 0:
        d = n % 10
        n //= 10
        notFound = True
        for i in range(ptr1):
            if t1[i] == d:
                notFound = False
                break
        if notFound:
            Insert(t1, ptr1, d)
            ptr1 += 1
    ptr2 = 1
    while m > 0:
        d = m % 10
        m //= 10
        notFound = True
        for i in range(ptr2):
            if t2[i] == d:
                notFound = False
                break
        if notFound:
            Insert(t2, ptr2, d)
            ptr2 += 1
    if ptr2 != ptr1:
        return False
    for i in range(ptr1):
        if t1[i] != t2[i]:
            return False
    return True



def Insert(t, l, k):
    ix = l
    for i in range(l):
        if k < t[i]:
            ix = i
            break
    for i in range(l - 1, ix - 1, -1):
        t[i + 1] = t[i]
    t[ix] = k


def z11(t):
    n = len(t)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            k = t[y][x]
            if x < n - 1 and friendnumbers(k, t[y][x + 1]):
                matrix[y][x] += 1
                matrix[y][x + 1] += 1
            if y < n - 1:
                for x1 in range(x - 1, x + 2):
                    if 0 <= x1 < n and friendnumbers(k, t[y + 1][x1]):
                        matrix[y][x] += 1
                        matrix[y + 1][x1] += 1
    counter = 0
    for y in range(n):
        for x in range(n):
            if 0 < x < n - 1:
                if 0 < y < n - 1:
                    expected = 8
                else:
                    expected = 5
            elif 0 < y < n - 1:
                expected = 5
            else:
                expected = 3
            if matrix[y][x] == expected:
                counter += 1
    return counter



