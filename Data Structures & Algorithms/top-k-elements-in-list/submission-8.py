class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        array = [[] for x in range(len(nums) + 1)]
        res = []
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        for n, c in countMap.items():
            array[c].append(n)
        for i in range(len(nums), 0, -1):
            for x in array[i]:
                res.append(x)
                if (len(res) == k):
                    return res