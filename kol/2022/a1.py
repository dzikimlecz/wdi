def sequence(T):
    N = len(T)
    for i in range(N):
        for j in range(i + 1, (N - i) // 2):
            l = j - i + 1
            q = T[i] / T[j + 1]
            good = True
            for k in range(1, l):
                if T[i + k] / T[j + k + 1] != q:
                    good = False
                    break
            if good:
                return i, j


if __name__ == '__main__':
    print(sequence( [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2] ))