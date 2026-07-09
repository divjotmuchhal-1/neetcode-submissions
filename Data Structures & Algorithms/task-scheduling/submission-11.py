class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap)-1
                if cnt:
                    q.append([cnt, time+n])
            while q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        return time


        