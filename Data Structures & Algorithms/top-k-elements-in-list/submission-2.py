from _heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        
        maxHeap = [(-val,key) for key,val in count.items()]
        heapify(maxHeap)
        
        res=[]
        while k>0:
            res.append(heapq.heappop(maxHeap)[1])
            k-=1
        return res
