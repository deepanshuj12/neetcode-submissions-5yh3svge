class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           nums1=nums[i]
           for j in range(i+1, len(nums)):
            tar=nums1+nums[j]
            if (tar==target):
                return [i,j]