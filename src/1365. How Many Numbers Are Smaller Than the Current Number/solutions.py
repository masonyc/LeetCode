import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for i, num in enumerate(sorted(nums)):
            # setdefault 设置key value
            indices.setdefault(num, i)
        return (indices[i] for i in nums)
