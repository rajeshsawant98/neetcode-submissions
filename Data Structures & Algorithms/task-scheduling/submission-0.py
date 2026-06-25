class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Count = Counter(tasks)
        MaxHeap = [-C for C in Count.values()]
        heapq.heapify(MaxHeap)
        time = 0 
        q = collections.deque()
        while MaxHeap or q:
            time +=1
            if MaxHeap:
                C = 1 + heapq.heappop(MaxHeap)
                if C:
                    q.append([C,time + n])
            if q and time == q[0][1]:
                heapq.heappush(MaxHeap, q.popleft()[0])
        return time

