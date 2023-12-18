def f(T):

    def isPrime(n):
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def req(T):
        N = len(T)
        if N == 0:
            return True
        x = T[0]
        for l in range(2, min(30, N)+1):
            x *= 2
            x += T[l - 1]
            prime = (x == 2) or (T[l - 1] != 0 and isPrime(x))
            if prime and req(T[l:N]):
                return True
        return False
    return req(T)


if __name__ == '__main__':
    print(f([1,1,0,1,0,0]))