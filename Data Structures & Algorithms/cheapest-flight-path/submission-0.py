class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            sorc, dest, price = flight[0], flight[1], flight[2]
            adj[sorc].append([dest, price])
        
        minHeap = [(nei[1], nei[0], 0) for nei in adj[src]]
        

        while minHeap:
            currPrice, currDest, currK = heapq.heappop(minHeap)
            if currDest == dst and currK <= k:
                return currPrice
            
            for nextStop in adj[currDest]:
                heapq.heappush(minHeap, (currPrice + nextStop[1], nextStop[0], currK + 1))
        
        return -1
            
