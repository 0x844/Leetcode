class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, local, curr_sum, res, target, candidates):
            if curr_sum == target:
                n = []
                for i in range(len(local)):
                    n.append(local[i])
                res.append(n)
                return
            if curr_sum > target:
                return
            if index >= len(candidates):
                return
            local.append(candidates[index])
            curr_sum += candidates[index]
            backtrack(index, local, curr_sum, res, target, candidates) # dont increment index since you can reuse numbers
            local.pop() # pop prev index
            curr_sum -= candidates[index] # decrement curr_sum (keep looking for values)
            backtrack(index + 1, local, curr_sum, res, target, candidates) # move onto next index
            return
        backtrack(0, [], 0, res, target, candidates)
        return res
