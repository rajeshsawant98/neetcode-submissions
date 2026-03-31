from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            Count = [0] * 26 
            for c in s:
                Count[ ord(c) - ord("a")] += 1

            res[tuple(Count)].append(s)

        return list(res.values())

