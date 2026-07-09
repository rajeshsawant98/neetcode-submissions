class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) -1

        Total = 0

        while l<r:

            Total = numbers[l] + numbers[r]

            if Total == target:
                return [l+1,r+1]
            elif Total > target:
                r-=1
            else:
                l+=1
        