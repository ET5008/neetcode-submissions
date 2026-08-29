class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numArray = []
        numArray = [[] for n in range(len(nums) + 1)]
        countMap = {}
        res = []
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        for i, c in countMap.items():
            numArray[c].append(i)
        for x in range(len(nums), 0, -1):
            for y in numArray[x]:
                res.append(y)
                if len(res) == k:
                    return res