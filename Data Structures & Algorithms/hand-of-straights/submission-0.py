from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        Count = {}
    
        for n in hand:
            Count[n] = 1 + Count.get(n,0)
        
        minHeap = list(Count.keys())
        heapify(minHeap)

        while minHeap:
            start = minHeap[0]

            for i in range(start,start+groupSize):
                if i not in Count:
                    return False
                Count[i] -= 1
                if Count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True
                
