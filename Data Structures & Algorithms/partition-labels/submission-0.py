class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {}

        for i,n in enumerate(s):
            lastIndex[n] = i
        
        res = []
        
        count,end =0,0

        for i,c in enumerate(s):
            count +=1
            end = max(lastIndex[c] ,end)
            if i == end:
                res.append(count)
                count = 0
        
        return res
