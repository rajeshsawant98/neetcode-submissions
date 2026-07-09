class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for course,preq in prerequisites:
            prereq[course].append(preq)
        
        visited,visiting = set(),set()

        output= []
        def dfs(c):
            if c in visiting:
                return False

            if c in visited:
                return True
            
            visiting.add(c)
            for preq in prereq[c]:
                if not dfs(preq):
                    return False
            
            visited.add(c)
            visiting.remove(c)
            output.append(c)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output 
