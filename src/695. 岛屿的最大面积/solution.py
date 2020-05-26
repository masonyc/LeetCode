# DFS
# Time R * C
# Space R * C
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def dfs(r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = 0
            return dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(
                r, c - 1) + 1
        return 0

    ans = -inf
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ans = max(ans, dfs(r, c))
    return ans
