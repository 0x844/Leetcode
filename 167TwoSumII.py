def twoSum(numbers, target):
  ptr1 = 0
  ptr2 = len(numbers)-1

  for i in range(len(numbers)):
    if numbers[ptr1] + numbers[ptr2] == target:
      return [ptr1+1, ptr2+1]
    elif numbers[ptr1] + numbers[ptr2] > target:
      ptr2 -= 1
    else:
      ptr1 += 1
    