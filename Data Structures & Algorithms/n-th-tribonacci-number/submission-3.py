class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        T0 = 0
        T1 = 1
        T2 = 1

        for i in range(3,n+1):

            temp = T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = temp
        
        return T2