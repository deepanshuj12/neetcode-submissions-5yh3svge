class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i]=="(":
                arr.append(")")
            elif s[i]=="{":
                arr.append("}")
            elif s[i]=="[":
                arr.append("]")
            else: #s[i]==")" or s[i]=="]" or s[i]=="}":
                if not arr:
                    return False
                endb=arr.pop()
                if endb!=s[i]:
                    return False
        return len(arr)==0
            
