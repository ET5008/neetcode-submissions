class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for x in range(len(nums)):
            if nums[x] < smallest:
                smallest = nums[x]
        return smallest