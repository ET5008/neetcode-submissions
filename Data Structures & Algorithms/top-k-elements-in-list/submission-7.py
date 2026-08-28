class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        for i, c in countMap.items():
            freq[c].append(i)
            
        
        res = []
        for x in range(len(freq) - 1, 0, -1):
            for i in freq[x]:
                res.append(i)
            if (len(res) == k):
                return res
