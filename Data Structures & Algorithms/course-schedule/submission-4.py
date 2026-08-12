class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)

        for course,preq in  prerequisites:
            preMap[course].append(preq)
        
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False

            visiting.add(course)

            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            
            visited.add(course)
            visiting.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True