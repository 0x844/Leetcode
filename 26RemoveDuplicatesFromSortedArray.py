class Solution:
  def removeDuplicates(self,nums:List[int]) -> int:
    if not nums:
      return nums
    hmap = {}
    count = 0
    for i in range(len(nums)):
      if nums[i] in hmap:
        nums[i] = 101 # invalidate entry
        count += 1
      else:
        hmap[nums[i]] = 1
    nums.sort()
    return len(nums[count:])
