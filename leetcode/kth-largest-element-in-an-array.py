import heapq

# Time complexity: O(n*logk) better than sort O(n*logn)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                if minHeap[0] < n:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, n)

        return minHeap[0]
