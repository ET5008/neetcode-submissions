class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = []
        anagramDict = {}
        for string in strs:
            sortedString = "".join(sorted(string))

            if sortedString not in anagramDict.keys():
                anagramDict[sortedString] = []
            anagramDict[sortedString].append(string)
        for anagram in anagramDict.keys():
            returnList.append(anagramDict[anagram])

        return returnList