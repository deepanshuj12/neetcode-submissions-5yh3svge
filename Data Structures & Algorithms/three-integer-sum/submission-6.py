class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums.sort()
        for i in range(len(nums)-1):
            k=len(nums)-1
            j=i+1
            
            while j<k:
                adds=nums[i] + nums[j] + nums[k] 
                if adds>0:
                    k=k-1
                elif adds<0:
                    j=j+1
                else:
                    if [nums[i], nums[j], nums[k]] not in arr:
                        arr.append([nums[i], nums[j], nums[k]])
                    j=j+1
                    k=k-1
        return arr










        [-2,-1,0,1,2,3]