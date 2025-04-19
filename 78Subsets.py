class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, nums, local, res):
            if index >= len(nums):
                n = []
                for i in range(len(local)): # append COPY of local (list can be changed while recursing)
                    n.append(local[i])
                res.append(n)
                return
            local.append(nums[index])
            backtrack(index + 1, nums, local, res)
            local.pop()

            backtrack(index + 1, nums, local, res)
            return
        backtrack(0, nums, [], res)
        return res
