class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(comb, curSum, start):
            if curSum == target:
                res.append(comb[:])
                return

            if curSum > target:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                curSum += candidates[i]

                backtrack(comb, curSum, i)

                removedCandidate = comb.pop()
                curSum -= removedCandidate

        backtrack([], 0, 0)
        return res
