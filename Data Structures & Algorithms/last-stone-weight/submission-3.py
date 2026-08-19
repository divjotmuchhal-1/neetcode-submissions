class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0:
            return 0
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if abs(x-y) > 0:
                heapq.heappush_max(stones, abs(x-y))
        if stones:
            return stones[0]
        else:
            return 0
            


        