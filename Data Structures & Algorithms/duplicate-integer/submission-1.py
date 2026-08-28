class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums) != 0:
            numsInt = nums.pop();
            if (numsInt in nums):
                return True

        return False