def solve():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    ans = 0

    def canPut(r, c):
        if board[r][c] == '*':
            return False

        for i in range(r):
            if board[i][c] == 'Q':
                return False

        i, j = r-1, c-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = r-1, c+1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueen(r):
        nonlocal ans
        if r == n:
            ans += 1
            return

        for c in range(n):
            if canPut(r, c):
                board[r][c] = 'Q'
                nQueen(r + 1)
                board[r][c] = '.'  # backtrack

    nQueen(0)
    print(ans)


if __name__ == "__main__":
    solve()