import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        return sum(self.dfs(i, j, grid)
                   for i, row in enumerate(grid)
                   for j, cell in enumerate(row)
                   if not cell)

    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        # 出边界了
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        # 如果是1 返回1
        if grid[i][j]:
            return 1
        # 填一个值 继续递归
        grid[i][j] = 2
        return (self.dfs(i + 1, j, grid)
                * self.dfs(i - 1, j, grid)
                * self.dfs(i, j + 1, grid)
