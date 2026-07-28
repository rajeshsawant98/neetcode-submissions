class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}
        res=[]

        for i in nums:
            freq[i]= 1 + freq.get(i,0)
        
       
        for j in range(k):
            m1 = max(freq, key=freq.get)
            res.append(m1)
            del freq[m1]

        return res