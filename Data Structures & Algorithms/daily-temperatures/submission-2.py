class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = [] # would contain temp and index 
         # [ (40,5) , (28,6) ] 
         # res [1 4 1 2 1 0 0]

        for i,n in enumerate(temperatures):

            while stack and stack[-1][0] < n:
                _, topIndex = stack.pop()
                res[topIndex] = i - topIndex
            stack.append([n,i])
        
        return res



