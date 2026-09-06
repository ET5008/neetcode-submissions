class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        firstIndex = 0
            
        if target >= nums[firstIndex]:
            i = firstIndex
            while i < len(nums) and target >= nums[i]:
                if target == nums[i]:
                    return i
                i += 1
            return -1
            #iterate forward until nums[index] > target, then return -1
        elif target < nums[firstIndex]:
            i = len(nums) - 1
            while ( i > -1 and target <= nums[i]):
                if (target == nums[i]):
                    return i
                i -= 1
            return -1
            #iterate backwards until the index < target (-1) or =
