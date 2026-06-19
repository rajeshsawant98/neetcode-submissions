class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]* len(temperatures)
        
        stack =[] # would contain [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                res[topIndex] = (i - topIndex)
            stack.append([t,i])
        
        return res