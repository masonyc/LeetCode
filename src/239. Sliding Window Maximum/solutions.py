class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        result = []
        i = 1
        j = k+1
        _max = max(nums[:k])
        result.append(_max)
        while j <= len(nums):
            if _max == nums[i-1]:
                _max = max(nums[i:j])
                result.append(_max)
            elif _max < nums[j-1]:
                _max = nums[j-1]
                result.append(_max)
            else:
                result.append(_max)
            i += 1
            j += 1
        return result
