from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        # Build graph: course -> prerequisites
        for course, preq in prerequisites:
            graph[course].append(preq)

        visiting = set()   # Nodes in current DFS path
        visited = set()    # Nodes already processed
        order = []

        def dfs(course):
            if course in visiting:
                return False          # Cycle detected

            if course in visited:
                return True           # Already processed

            visiting.add(course)

            for preq in graph[course]:
                if not dfs(preq):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order