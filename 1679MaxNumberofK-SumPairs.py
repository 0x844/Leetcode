class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if (nums[right] + nums[left] == k):
                count += 1
                right -= 1
                left += 1
            elif (nums[right] + nums[left] < k):
                left += 1
            else:
                right -=1
        return count
"""
[1,3,3,3,4]
 ^
         ^
"""
