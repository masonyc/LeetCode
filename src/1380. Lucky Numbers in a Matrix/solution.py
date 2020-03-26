import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [c
                for i, r in enumerate(matrix)
                for j, c in enumerate(r)
                if mi[i] == mx[j]]
