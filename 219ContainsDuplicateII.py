class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasmp = {}

        for i, num in enumerate(nums):
            if num in hasmp and i - hasmp[num] <= k:
                return True
            hasmp[num] = i
        return False
        
