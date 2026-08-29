class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s == "":
                res = res + "+++" + "----"
            else:
                res = res + s + "----"
        return res
    def decode(self, s: str) -> List[str]:
        res = s.split("----")
        res.remove("")
        for x in range(len(res)):
            if res[x] == "+++":
                res[x] = ""
    
        
        return res