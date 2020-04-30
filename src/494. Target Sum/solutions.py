from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        #knapsack 问题需要定义 一个 当前index 一个当前sum
        m = len(nums) - 1
        cur_sum = 0
        self.memo = {}
        return self.dp(S, m, cur_sum, nums)

    def dp(self, target: int, index: int, cur: int, nums: List[int]) -> int:
        if (index, cur) in self.memo:
            return self.memo[(index, cur)]
        #定义base 两种 一种是valid 当前sum == target 而且index为0
        # 另一种不可行 index<0 而且sum != target
        if index < 0 and target == cur:
            return 1
        if index < 0 and target != cur:
            return 0

        #decision or guess做决策 来更新dp
        #这题里只有两种决策 一种做加法 一种做减法
        positive = self.dp(target, index - 1, nums[index] + cur, nums)
        negative = self.dp(target, index - 1, -nums[index] + cur, nums)
        self.memo[(index, cur)] = positive + negative
        return self.memo[(index, cur)]  #返回统计出的1
