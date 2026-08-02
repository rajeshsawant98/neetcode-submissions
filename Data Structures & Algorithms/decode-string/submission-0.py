class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:

            if c != "]":
                stack.append(c)
            else:
                substring = ""

                while stack and stack[-1] != "[":
                    chara = stack.pop()
                    substring = chara + substring
                
                stack.pop()

                multi = ""

                while stack and stack[-1].isdigit() :
                    num = stack.pop()
                    multi = num + multi
                
                stack.append(int(multi)*substring)
        
        return "".join(stack)