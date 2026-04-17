class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        strs=""
        for i in range(len(s)):
            if s[i].isalnum():
                strs=strs+s[i] 
            else:
                continue
        return strs==strs[::-1]
        