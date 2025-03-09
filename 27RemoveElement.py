class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (val not in nums):
            return len(nums)
        
        if (len(nums) <= 1 and val in nums):
            return 0
        
        if (len(nums) == 1):
            return len(nums)
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if (nums[left] == val):
                while nums[right] == val and left < right:
                    right -= 1
                temp1 = nums[left]
                temp2 = nums[right]
                nums[left] = temp2
                nums[right] = temp1
            else:
                left += 1
        return len(nums[0:right])

                    
