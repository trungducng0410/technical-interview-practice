import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            else:
                if self.heap[0] < n:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
