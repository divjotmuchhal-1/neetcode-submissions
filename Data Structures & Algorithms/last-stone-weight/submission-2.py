class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0:
            return 0
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if (stone1-stone2) > 0:
                heapq.heappush_max(stones,stone1-stone2)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]



        