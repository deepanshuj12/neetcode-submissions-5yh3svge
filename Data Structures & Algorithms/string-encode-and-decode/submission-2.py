class Solution:

    def encode(self, strs: List[str]) -> str:
        rev=""
        for st in strs:
            rev=rev+ str(len(st))+"#" + st
        return rev
        

    def decode(self, s: str) -> List[str]:
        deco,i=[],0
        while i <len(s):
            j=i
            while s[j]!="#":
                j=j+1
            length=int(s[i:j])
            i=j+1
            j=i+length
            deco.append(s[i:j])
            i=j
        return deco
        


