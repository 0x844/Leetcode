class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        sums = [x-1, x, x+1]
        if (sum(sums) == num):
            return sums
        else:
            return []
