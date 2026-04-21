class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lent=len(s1)
        st=""
        for i in range(len(s2)):
            st=s2[i:i+lent]
            if sorted(st)==sorted(s1):
                return True
            st=""
        return False