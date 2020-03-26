import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        #  生成全是0的1维 dp
        dp = n*[0]
        for i in range(n):
            # 初始化对角线为原始值
            dp[i] = nums[i]
        for i in range(n, -1, -1):
            for j in range(i+1, n):
                # 只储存相差值
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
        return dp[n-1] >= 0
