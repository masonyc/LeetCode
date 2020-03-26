import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        for i, num in enumerate(nums[:-1]):
            # 从左往右遍历 获得i左边的乘积
            left_prod[i+1] = left_prod[i] * num
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            # 从右往左遍历 乘上i右边的乘积
            left_prod[i] *= right
            # 右边的乘积
            right *= nums[i]
        return left_prod
