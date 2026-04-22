class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return finish == numCourses
