class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            newTarget = target - nums[i]
            targetDupe = nums[:]
            targetDupe[i] = 'a'
            if newTarget in targetDupe:
                if i < targetDupe.index(newTarget):
                    return [i, targetDupe.index(newTarget)]
                return [targetDupe.index(newTarget), i]
