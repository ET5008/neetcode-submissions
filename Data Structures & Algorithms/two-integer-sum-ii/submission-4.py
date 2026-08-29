class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            Left = numbers[L]
            Right = numbers[R]
            if Left + Right == target:
                return [L + 1, R + 1]
            elif Left + Right > target:
                R -= 1
            else:
                L += 1

