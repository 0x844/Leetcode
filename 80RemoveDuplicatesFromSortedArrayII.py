class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    hmap = {}
    count = 0
    for i in range(len(nums)):
      if nums[i] in hmap:
        hmap[nums[i]] += 1
        if hmap[nums[i]] >= 3:
          count += 1
          nums[i] = float('inf') # invalidate entry
      else:
        hmap[nums[i]] = 1
    nums.sort() # inf will be at end of arr
    return len(nums[count:])
