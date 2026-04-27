class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            adj[pre].append(course)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completion = []
        while q:
            curr = q.popleft()
            completion.append(curr)

            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return completion if len(completion) == numCourses else []