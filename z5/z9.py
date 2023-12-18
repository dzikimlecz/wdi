def f(T, mass):
    NULL = [None]
    cache = [NULL for _ in range(mass + 800)]
    cache[0] = []

    def rec(T, mass):
        n = len(T)
        if cache[mass] != NULL:
            return cache[mass]
        for i in range(n):
            m1 = mass - T[i]
            m2 = mass + T[i]
            t1 = T[0:i] + T[i+1:n]
            if m1 >= 0:
                comb = rec(t1, m1)
                if comb != NULL:
                    cache[mass] = comb + [T[i]]
                    return cache[mass]
            comb = rec(t1, m2)
            if comb != NULL:
                cache[mass] = comb + [-T[i]]
                return cache[mass]
        else:
            return NULL

    return rec(T, mass)


if __name__ == '__main__':
    print(f([4, 4, 3, 1], 6))
