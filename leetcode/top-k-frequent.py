import heapq


class Solution:
    # O(k * log n) time, O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = self.countFrequency(nums)

        heap = []
        for num, count in frequency.items():
            heap.append((count, num))

        heapq.heapify(heap)

        # k * log n
        topK = heapq.nlargest(k, heap)

        result = []
        for item in topK:
            result.append(item[1])

        return result

    def countFrequency(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return frequency


class Solution:
    # O(n) time, O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
