class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for u,v in edges:
            adj[v].append(u)
        

        Output = []
        visited = set()
        visiting = set()

        def dfs(vert):
            if vert in visited:
                return True
            
            if vert in visiting:
                return False
            
            visiting.add(vert)
            for nei in adj[vert]:
                if not dfs(nei):
                    return False
            
            visited.add(vert)
            visiting.remove(vert)
            Output.append(vert)
            return True
        
        for vert in range(n):
            if not dfs(vert):
                return []

        return Output