class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()

        def dfs(i, j):
            if (i == m or
                j == n or
                countTotal(i, j) > k or
                    (i, j) in visited):
                return
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i, j+1)

        def countTotal(x, y):
            total = 0
            while x > 0:
                total += x % 10
                x = x // 10
            while y > 0:
                total += y % 10
                y = y//10
            return total
        dfs(0, 0)
        return len(visited)
