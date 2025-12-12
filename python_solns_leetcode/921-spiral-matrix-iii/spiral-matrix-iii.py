from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        r, c = rStart, cStart
        steps = 1
        total = rows * cols
        res.append([r, c])

        while len(res) < total:
            for i in range(4):
                dr, dc = directions[i]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                if i % 2 == 1:  # Increase steps after moving in 2 directions
                    steps += 1
        return res
