class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1==[] :
            newlis=nums2
        elif nums2==[]:
            newlis=nums1
        else:
            newlis=nums1+nums2
        newlis.sort()
        lenn=len(newlis)
        if lenn%2==0:
            one=newlis[lenn//2-1]
            two=newlis[(lenn//2)]
            med=float((one+two)/2)
        else:
            med=float(newlis[lenn//2])
        return med
        # lent1=len(nums1)
        # lent2=len(nums2)
        # total=lent1+lent2
        # if total//2>lent1 and total%2==0:
        #     firev=nums2[total-lent1]
        #     secev=nums2[total-lent1+1]
        # elif total//2>lent1 and total%2!=0:
        #     firod=nums2[total-lent1]
        # elif
        # while i<lent1:
        #     while j<lent2:
        #         if total%2==0:
