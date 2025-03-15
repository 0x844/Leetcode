class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_k = float("-inf")
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            max_k = max(max_k, right - left)
        return max_k
