class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        firstNums = []
        print(nums)
        for first in range(len(nums)):
            # if (nums[first] not in firstNums):
                L = first + 1
                R = len(nums) - 1
                while (L < R):
                    Left = nums[L]
                    Right = nums[R]
                    firstNum = nums[first]
                    if Left + Right + firstNum == 0:
                        if ([firstNum, Left, Right] not in res):
                            res.append([firstNum, Left, Right])
                            print([firstNum, Left, Right])

                            # firstNums.append(firstNum)
                        R -= 1
                    elif Left + Right + firstNum > 0:
                        R -= 1
                    else:
                        L += 1
        return res