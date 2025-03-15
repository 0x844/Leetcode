class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        local_sum = 0
        for left in range(len(nums)):
            right = nums_sum - local_sum - nums[left] # nums[left] (pivot col) not included in total
            if right == local_sum:
                return left
            local_sum += nums[left]            
        return -1
"""
sum1=1 -> 8
sum2=6 -> 11
[1,7,3,6,5,6]
   ^
         ^
"""
