class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        

        bracketMap = { ")" : "(" , "]" : "[" , "}" : "{"}

        stack =[]


        for c in s:

            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack