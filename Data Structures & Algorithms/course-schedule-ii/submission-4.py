class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preqMap = defaultdict(list)

        for course,preq in prerequisites:
            preqMap[course].append(preq)
        
        completed = []
        visiting = set()
        visited = set()
        def dfs(c):
            if c in visiting:
                return False
            
            if c in visited:
                return True
            
            visiting.add(c)

            for preq in preqMap[c]:
                if not dfs(preq):
                    return False

            visited.add(c)
            visiting.remove(c)
            completed.append(c)
            return True

            

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return completed