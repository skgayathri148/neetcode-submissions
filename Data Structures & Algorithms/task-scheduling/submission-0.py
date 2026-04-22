class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = defaultdict(int)
        for task in tasks:
            frequency[task] += 1

        max_heap = [-freq for freq in frequency.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque([])

        while max_heap or queue:
            time += 1

            if not max_heap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])
                
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time