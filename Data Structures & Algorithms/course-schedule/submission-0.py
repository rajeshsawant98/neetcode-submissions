class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()

        CMAP = { i:[] for i in range(numCourses)}

        #create dependency map

        for course, prereq in prerequisites:
            CMAP[course].append(prereq)
        
        def dfs(c):
            if c in visit:
                return False
            
            if CMAP[c] == []:
                return True

            visit.add(c)

            for prereq in CMAP[c]:
                if not dfs(prereq):
                    return False
            
            visit.remove(c)
            CMAP[c] = []

            return True
        
        for c in CMAP.keys():
            if not dfs(c): return False
        
        return True


        


