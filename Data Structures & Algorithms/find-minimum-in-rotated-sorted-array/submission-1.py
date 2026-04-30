class Solution:
    def findMin(self, nums: List[int]) -> int:
        first,last=nums[0],nums[0]
        for i in range(1,len(nums)):
            
            if last<nums[i]:
                last=nums[i]
                continue
            if last>nums[i]:
                return nums[i]
            # if i==len(nums)-1:
            #     return first
        return first