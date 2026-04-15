class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hdict={}
        for num in nums:
            hdict[num]=hdict.get(num,0)+1
        sortdict= sorted(hdict.items(), key=lambda item:item[1], reverse=True)
        arr=[]
        for i in range(k):
            arr.append(sortdict[i][0])
        return arr