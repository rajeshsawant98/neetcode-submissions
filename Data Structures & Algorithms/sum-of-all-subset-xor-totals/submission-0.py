class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def backtrack(i,path):
            if i == len(nums):
                runningSum = 0
                for n in path[:]:
                    runningSum = runningSum ^ n
                self.res += runningSum
                return
            
            path.append(nums[i])
            backtrack(i+1,path)

            path.pop()
            backtrack(i+1,path)
            return

        backtrack(0,[])

        return self.res
