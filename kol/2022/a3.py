def inBounds(move, N):
    return 0 <= move[0] < N and 0 <= move[1] < N


def king(N, L):
    visited = [[False for _ in range(N)] for _ in range(N)]
    vectors = [(-1, 0), (1, 0), (0, 1)]
    maxLen = -1

    def rec(ptr=(0, 0), depth=0):
        nonlocal N, L, visited, vectors, maxLen

        if ptr == (N - 1, N - 1):
            maxLen = max(depth, maxLen)
            return
        visited[ptr[0]][ptr[1]] = True
        for v in vectors:
            move = (ptr[0] + v[0], ptr[1] + v[1])
            if inBounds(move, N) and not visited[move[0]][move[1]] and move not in L:
                rec(move, depth + 1)
        visited[ptr[0]][ptr[1]] = False

    rec()
    return maxLen if maxLen != -1 else None


if __name__ == '__main__':
    print(king(4, [(0,1), (3, 0)]))