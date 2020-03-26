import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        #  生成全是0的2维 dp
        dp = [n*[0] for i in range(n)]
        for i in range(n):
            # 初始化对角线为原始值(0,0) (1,1) (2,2) (3,3)
            dp[i][i] = nums[i]
        for i in range(n, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1] >= 0
