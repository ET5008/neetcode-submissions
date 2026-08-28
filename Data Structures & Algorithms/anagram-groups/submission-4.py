class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = {}
        returnList = []
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in anagramsDict.keys():
                anagramsDict[sortedString] = []
            anagramsDict[sortedString].append(string)
        for key, items in anagramsDict.items():
            returnList.append(items)
        return returnList