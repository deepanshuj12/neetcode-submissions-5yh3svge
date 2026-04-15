class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap= {}
        for i in nums:
            hmap[i]= hmap.get(i,0)+1
        # for k, v in sorted(hmap.items(), key=lambda item: item[1]): pass
        sortd = sorted(hmap.items(), key=lambda item: item[1], reverse=True)
        arr=[]
        for i in range(k):
            arr.append(sortd[i][0])
        return arr