class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(comb, curSum, start):
            if curSum == target:
                res.append(comb[:])
                return

            if curSum > target:
                return

            i = start
            while i < len(candidates):
                comb.append(candidates[i])
                curSum += candidates[i]

                backtrack(comb, curSum, i + 1)

                removedCandidate = comb.pop()
                curSum -= removedCandidate

                # Skip duplicate numbers
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1

                i += 1

        backtrack([], 0, 0)
        return res
