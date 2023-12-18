def hanoi(n):
    NULL = ""
    T = [[NULL if pole else n - i for i in range(n)] for pole in range(3)]
    print(T, end='\n\n')

    def move(begin=0, end=2, maxBlockSize=n):
        assert begin != end
        nonlocal T
        if maxBlockSize == 0:
            return
        target = 1 if begin + end == 2 else 0 if begin + end == 3 else 2
        move(begin, target, maxBlockSize - 1)
        targetBlock = None
        beginBlock = None
        i = 1
        while targetBlock is None or beginBlock is None:
            assert i <= n
            if targetBlock is None and T[end][i - 1] == NULL:
                targetBlock = i - 1
            if beginBlock is None and T[begin][n - i] == maxBlockSize:
                beginBlock = n - i
            i += 1
        # end while
        T[end][targetBlock], T[begin][beginBlock] = \
            T[begin][beginBlock], T[end][targetBlock]
        print(T, end='\n\n')
        move(target, end, maxBlockSize - 1)
    # end def
    move()
# end def


if __name__ == '__main__':
    hanoi(5)
