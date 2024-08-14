from collections import defaultdict
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        output = 0

        rows = defaultdict(int)
        cols = defaultdict(int)

        l_matrix = len(grid)
        for col_index in range(l_matrix):
            row_index = 0
            col = []

            while row_index < l_matrix:
                col.append(grid[row_index][col_index])
                row_index += 1

            if tuple(col) in cols:
                cols[tuple(col)] += 1
            else:
                cols[tuple(col)] = 1

            if tuple(grid[col_index]) in rows:
                rows[tuple(grid[col_index])] += 1
            else:
                rows[tuple(grid[col_index])] = 1

        return sum([rows[row] * cols[row] for row in rows.keys() if row in cols])

if __name__ == "__main__":
    s = Solution()
    assert s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3


"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 
Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""