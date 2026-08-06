class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = { i:[] for i in range(numCourses)}

        for course, preq in prerequisites:
            prereq[course].append(preq)
        
        visited, visiting = set(), set()

        res = []

        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False

            visiting.add(course)

            for preq in prereq[course]:
                if not dfs(preq):
                    return False

            visited.add(course)
            visiting.remove(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res