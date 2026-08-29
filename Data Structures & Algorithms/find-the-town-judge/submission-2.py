class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        delta = defaultdict(int) # incoming - outgoing 

        for a1,b1 in trust:
            delta[b1] += 1
            delta[a1] -= 1
        
        for i in range(1,n+1):
            if delta[i] == n - 1:
                return i

        return -1