class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        for i in range(len(nums)):
            pri=1
            for j in range(len(nums)):
                if i!=j:
                    pri=pri*nums[j]
            prod.append(pri)
        return prod
