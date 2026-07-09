class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minHeap = []

        for n in nums:

            heapq.heappush(minHeap, n * n)

        res = []

        while minHeap:

            res.append(heapq.heappop(minHeap))

        return res