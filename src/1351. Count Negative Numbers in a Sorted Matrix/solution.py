import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(cell < 0 for row in grid for cell in row)
