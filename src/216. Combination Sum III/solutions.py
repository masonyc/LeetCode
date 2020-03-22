import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        # 限制了数字在1到9内
        self.dfs(range(1, 10), k, n, 0, [], result)
        return result

    def dfs(self, nums, k, n, index, path, result):
        # 小于0 代表没必要再尝试后面的数字
        if k < 0 or n < 0:
            return
        # 如果都等于0 代表条件满足 加入返回列表
        if k == 0 and n == 0:
            result.append(path)

        for i in range(index, len(nums)):
            # 把当前数字加入path
            # k位数 - 1
            # n总和 减去当前数
            # index + 1
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], result)
