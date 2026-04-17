class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(nums)
        mx,coun=1,1
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                coun=coun+1
            elif nums[i-1]==nums[i]:
                continue
            else:
                coun=1
            mx=max(mx,coun)
        return mx
            