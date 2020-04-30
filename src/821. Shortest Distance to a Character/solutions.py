from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        #初始化dp 如果目标c在当前位置 则距离为0 其他的都初始为数组的长度
        dp = [0 if c == C else n for c in S]
        for i in range(1, n):
            #从头到尾 和前一个数字对比 选最小的+1 因为最小的代表与C的距离 +1 因为如果是0 则距离为1
            dp[i] = min(dp[i], dp[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            #从尾到头 和后一个数字对比 选最小的+1 因为最小的代表与C的距离 +1 因为如果是0 则距离为1
            dp[i] = min(dp[i], dp[i + 1] + 1)
        return dp
