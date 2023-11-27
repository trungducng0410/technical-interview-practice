import heapq


# Time complexity:
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            if stone1 != stone2:
                heapq.heappush(maxHeap, -(stone1 - stone2))

        if not maxHeap:
            return 0

        return -maxHeap[0]
