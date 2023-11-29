class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            self.balanceHeaps()

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -(self.maxHeap[0])) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]

    def balanceHeaps(self) -> None:
        while len(self.minHeap) - len(self.maxHeap) > 1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
