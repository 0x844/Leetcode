class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx = []
        res = [-1] * len(queries)
        for i in range(len(nums)):
            if nums[i] == x:
                idx.append(i)
        for i in range(len(queries)):
            if queries[i] <= len(idx):
                res[i] = idx[queries[i]-1]
        return res
