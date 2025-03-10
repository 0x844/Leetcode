class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        
        left = 0
        total_sum = 0
        min_val = float('inf')

        for right in range(len(nums)):
            total_sum += nums[right]
            while total_sum >= target:
                if right - left + 1 < min_val:
                    min_val = right - left + 1
                total_sum -= nums[left]
                left += 1
        if min_val != float('inf'):
            return min_val
        else:
            return 0
