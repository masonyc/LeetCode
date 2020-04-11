class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchIndex(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, self.searchIndex(nums, target, False)-1]

    def searchIndex(self, nums, target, left):
        i, j = 0, len(nums)
        while i < j:
            m = (i+j)//2
            if nums[m] > target or (left and nums[m] == target):
                j = m
            else:
                i = m+1
        return i
