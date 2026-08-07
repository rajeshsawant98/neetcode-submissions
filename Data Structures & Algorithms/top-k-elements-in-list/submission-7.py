class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count = {}
        res = []

        for n in nums:
            Count[n] = 1 + Count.get(n,0)

        maxHeap = [ (- count, n) for n, count in Count.items()]
        heapq.heapify(maxHeap)

        while k > 0 and maxHeap:
            count, n = heapq.heappop(maxHeap)
            res.append(n)
            k -=1
        
        return res
            



