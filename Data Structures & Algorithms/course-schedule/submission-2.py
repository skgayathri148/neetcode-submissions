class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
