import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for i in range(len(points)):
            heapq.heappush(maxHeap, (-self.distance(points[i]), i))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for item in maxHeap:
            res.append(points[item[1]])

        return res

    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2
