class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        C = Counter(nums)

        maxHeap = []

        for key ,val in C.items():
            heapq.heappush(maxHeap, (-val,key))
        
        res =[]
        while k>0:
            val,key =heapq.heappop(maxHeap)
            res.append(key)
            k-=1
        
        return res
