class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Total = 0
        stack = []

        for i,c in enumerate(operations):
            if c == "+":
                S = stack[-1]+stack[-2]
                stack.append(S)
                Total += S
            
            elif c == "D":
                stack.append(2*stack[-1])
                Total += stack[-1]
            
            elif c == "C":
                Total -= stack[-1]
                stack.pop()
            
            else:
                stack.append(int(c))
                Total += int(c)
        
        return Total