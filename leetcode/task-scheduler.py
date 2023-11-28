import heapq
from collections import deque


# Time complexity: O(n)
# Space complexity: O(n) - n number of unique tasks
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-count for count in counter.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)

                if count != 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                pair = queue.popleft()
                heapq.heappush(maxHeap, pair[0])

        return time
