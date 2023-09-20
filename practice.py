from math import inf
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        goal = float(inf)
        reached_target = False
        movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        visited = set()

        def dfs(r, c, pathCost):
            nonlocal goal, reached_target

            if r == rows - 1 and c == cols - 1:
                goal = min(goal, pathCost)
                reached_target = True
                return

            prev_height = heights[r][c]

            for i, j in movements:
                x, y = r + i, c + j

                if 0 <= x < rows and 0 <= y < cols:
                    if (x, y) in visited:
                        continue

                    height = heights[x][y]
                    cost = abs(height - prev_height)

                    if reached_target and cost > goal:
                        continue

                    visited.add((x, y))
                    dfs(x, y, pathCost)
                    visited.remove((x, y))

        visited.add((0, 0))
        dfs(0, 0, 0)
        return goal


s = Solution()
s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]])
