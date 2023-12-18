def f(T, mass):
    cache = [False for _ in range(mass + 800)]
    cache[0] = True

    def rec(T, mass):
        n = len(T)
        if cache[mass]:
            return True
        for i in range(n):
            m1 = mass - T[i]
            m2 = mass + T[i]
            t1 = T[0:i] + T[i+1:n]
            if m1 >= 0:
                if rec(t1, m1):
                    cache[mass] = True
                    return True
            if rec(t1, m2):
                cache[mass] = True
                return True
        else:
            return False

    return rec(T, mass)


if __name__ == '__main__':
    print(f([2, 2, 2, 1], 5))
