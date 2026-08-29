class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trustMap = {n: set() for n in range(1,n+1)}

        for ai, bi in trust:
            trustMap[bi].add(ai)
        
        judge = -1
        judgeNum = 0

        for i in range(1,n+1):
            if len(trustMap[i]) == n - 1:
                isJudge = True
                for j in range(1,n+1):
                    if j == i:
                        continue
                    
                    if i in trustMap[j]:
                        isJudge = False
                
                if isJudge:
                    judge = i
                    judgeNum += 1
        
        if judgeNum == 1:
            return judge
        else:
            return -1