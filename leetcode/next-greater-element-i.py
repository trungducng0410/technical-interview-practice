class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = [], {}

        for num in nums2:
            # Decreasing stack
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(hashmap.get(num, -1))

        return res
