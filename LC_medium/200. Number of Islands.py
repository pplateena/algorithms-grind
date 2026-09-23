class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque

        seen = set()
        counter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    counter += 1
                    dq = deque([(r, c)])
                    while dq:
                        ci, cj = dq.popleft()  # current
                        for fi, fj in ((0, 1), (1, 0), (-1, 0), (0, -1)):  # flood
                            di, dj = ci + fi, cj + fj
                            if 0 <= di < rows and 0 <= dj < cols and (di, dj) not in seen:
                                seen.add((di, dj))
                                if grid[di][dj] == "1":
                                    dq.append((di, dj))

        return counter


if __name__ == "__main__":

    s = Solution()

    assert s.numIslands(grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]) == 1
    assert s.numIslands(grid = [
    ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]) == 3
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
