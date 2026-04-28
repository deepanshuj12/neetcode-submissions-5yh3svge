class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i=0
        arr=[]
        lent=len(temperatures)
        while(i<lent):
            j=i
            while(j<lent):
                if temperatures[j]>temperatures[i]:
                    arr.append(j-i)
                    break
                if j==lent-1:
                    arr.append(0)
                j=j+1
            i=i+1
        return arr