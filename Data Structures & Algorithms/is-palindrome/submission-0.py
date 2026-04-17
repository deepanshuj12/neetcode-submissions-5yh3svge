class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        strs,brr="",""
        for i in range(len(s)):
            if s[i].isalnum():
                strs=strs+s[i] 
            else:
                continue
        brr=strs[::-1]
        if brr!=strs:
            return False
        return True
        