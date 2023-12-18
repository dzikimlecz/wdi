def weight(w):
    VOWELS = ['e', 'y', 'u', 'i', 'o', 'a']
    vowelsCount = 0
    ordinalsSum = 0
    for c in w:
        if c in VOWELS:
            vowelsCount += 1
        ordinalsSum += ord(c)
    return vowelsCount, ordinalsSum


def wyraz(s1, s2):
    if s1 == "":
        return ""
    vowelsCount, ordinalsSum = weight(s1)
    found = None

    def rec(s=s2):
        nonlocal vowelsCount, ordinalsSum, found
        if found is not None:
            return
        if len(s) == 1:
            return [s]
        withoutFirst = rec(s[1:])
        llen = len(withoutFirst)
        withFirst = [withoutFirst[i] if i < llen else None for i in range(2 * llen)]
        ptr = 0
        for i in range(llen):
            combi = withoutFirst[i]
            newWord = s[0] + combi
            wvc, wos = weight(newWord)
            if (wvc, wos) == (vowelsCount, ordinalsSum):
                found = newWord
                break
            elif wos < ordinalsSum:
                withFirst[llen + ptr] = newWord
                ptr += 1
        return withFirst[:llen + ptr]

    rec()
    return found


if __name__ == '__main__':
    word = wyraz("ula", "grehuighsxuieghedagygifhae")
    if word is None:
        print(None)
    else:
        print('{', end='')
        for c in word:
            print(c, end=', ')
        print('\b\b}', end='')
