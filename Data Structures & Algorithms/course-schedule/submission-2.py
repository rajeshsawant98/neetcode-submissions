class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, preReq in prerequisites:

            preMap[course].append(preReq)

        visit = set()

        def dfs(c):

            if c in visit:

                return False

            if preMap[c] == []:

                return True

            visit.add(c)

            for preReq in preMap[c]:

                if not dfs(preReq):

                    return False

            visit.remove(c)

            preMap[c] = []

            return True

        for c in range(numCourses):

            if not dfs(c):

                return False

        return True

        for c in preMap.keys():
            if not dfs(c): return False
        
        return True