class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        C = Counter(nums)

        res=[0,0]

        for i in range(1,len(nums)+1):
            if C[i] == 2:
                res[0] = i
            elif i not in C:
                res[1] =i
        
        return res

                


