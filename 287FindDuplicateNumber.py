def findDuplicate(nums):
  hp = {}
  for num in nums:
    if num in hp:
      return num
    else:
      hp[num] = 1