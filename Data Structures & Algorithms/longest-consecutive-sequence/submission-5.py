class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hmap,outp,maxm={},1,1
        for num in nums:
            hmap[num]=hmap.get(num,0)+1
        sortd=sorted(hmap.items(),key=lambda item:item[0])
        # fir=sortd[0][0]
        
        for i in range(1,len(sortd)):
            if sortd[i][0]==sortd[i-1][0]+1:
                outp=outp+1
            else:
                outp=1
            maxm=max(maxm,outp)
        return maxm
