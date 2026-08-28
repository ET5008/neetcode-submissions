class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s == "":
                res = res + "++++" + "---"
            else:
                res = res + s + "---" 
        return res[:len(res)-3]
    def decode(self, s: str) -> List[str]:
        res = s.split("---")
        if "" in res:
            res.remove("")
        for w in range(len(res)):
            if res[w] == "++++":
                res[w] = ""

        return res