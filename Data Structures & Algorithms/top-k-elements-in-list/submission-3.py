class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        C = Counter(nums)

        maxHeap = [ (-val, key) for key, val in C.items()]

        heapq.heapify(maxHeap)

        for _ in range(k):
            val , key = heapq.heappop(maxHeap)
            res.append(key)
        
        return res
            

    