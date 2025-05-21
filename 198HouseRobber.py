'''
Given an integer array nums representing the amount of money of each house.

will automatically contact the police if two adjacent houses were broken into on the same night.

return the maximum amount of money you can rob tonight without alerting the police.

nums = [2,1,1,2] output = 4
choose 2 ->
    - skip 1, skip 1, choose 2
    - skip 1, choose 1, skip 2
choose nums[i] ->
    - skip nums[i+1], skip nums[i+2], choose nums[i+3]
    - skip nums[i+1], choose nums[i+2], skip nums[i+3]

choose nums[i+1] ->
    - skip nums[i+2], choose nums[i+3]
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recurse(nums, i):
            if not nums or i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob = recurse(nums, i + 2) + nums[i]
            skip = recurse(nums, i + 1)
            memo[i] = max(rob,skip)
            return memo[i]
        max_val = recurse(nums,0)
        return max_val
