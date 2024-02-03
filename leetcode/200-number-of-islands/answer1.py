# https://leetcode.com/problems/number-of-islands/
# First solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island(i, j) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return 0
            if grid[i][j] == "0" or grid[i][j] == "X":
                grid[i][j] = "X"
                return 0
            else:
                grid[i][j] = "X"
                return (
                    1
                    + island(i + 1, j)
                    + island(i - 1, j)
                    + island(i, j + 1)
                    + island(i, j - 1)
                )

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "X":
                    if island(i, j):
                        islands += 1

        return islands
