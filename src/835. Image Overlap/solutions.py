from collections import Counter


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        # i / N 是行, i % N 是列
        # i / N * 100 + i % N 为了确保在Map里保持唯一性
        LA = [i / N * 100 + i % N
              for i in list(range(N * N))
              if A[i / N][i % N]]
        LB = [i / N * 100 + i % N
              for i in list(range(N * N))
              if B[i / N][i % N]]
        # i-j 是总距离 如果多个（i-j）的总距离相同 代表他们移动后重叠
        counter = Counter(i-j
                          for i in LA
                          for j in LB)
        return max(counter.values() or [0])
