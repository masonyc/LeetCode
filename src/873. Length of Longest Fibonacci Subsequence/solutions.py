from typing import List
import collections


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        #要解决 (i, j) and (j, k) are connected if and only if A[i] + A[j] == A[k]
        reversedDict = {v: k for k, v in enumerate(A)}
        #dp table为路径节点总数
        dp = collections.defaultdict(lambda: 2)  #初始化dp table为2
        ans = 0

        for k, v in enumerate(A):
            for j in range(k):
                i = reversedDict.get(v - A[j], None)
                if i is not None and i < j:
                    dp[j, k] = dp[i, j] + 1  #j到k的路径数 为i到j + 1
                    ans = max(ans, dp[j, k])  #找最长的路径
        return ans if ans >= 3 else 0
