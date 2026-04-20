class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water1,water2=0,0
        i,j=0,len(heights)-1
        while i<j:
                water1=min(heights[i],heights[j])*(j-i)
                water2=max(water1,water2)
                if heights[i]<heights[j]:
                    i=i+1
                else:
                    j=j-1
        return water2



