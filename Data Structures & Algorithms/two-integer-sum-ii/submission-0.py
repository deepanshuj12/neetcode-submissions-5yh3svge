class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        lent=len(numbers)
        i,j=0,lent-1
        while(numbers[i]+numbers[j]!=target):
            if i==j or i>j:
                break
            if numbers[i]+numbers[j]>target:
                j=j-1
            if numbers[i]+numbers[j]<target:
                i=i+1
        return [i+1,j+1]
