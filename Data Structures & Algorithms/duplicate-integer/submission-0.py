class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for x in nums:
            dict[x] = x
        if len(dict.values()) < len(nums):
            return True
        return False