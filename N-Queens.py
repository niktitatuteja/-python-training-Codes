class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                # Format the board into the required list of strings
                formatted_board = ["".join(row) for row in board]
                res.append(formatted_board)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to the next row
                backtrack(r + 1)

                # Backtrack (remove queen)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
