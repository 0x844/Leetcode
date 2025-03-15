class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_k = float("-inf")
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1

            max_k = max(max_k, right - left + 1)
        return max_k
