# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left_bound = 1
        right_bound = n
        
        while left_bound <= right_bound:
            mid = (left_bound + right_bound) // 2
            guess_s = guess(mid)
            
            if (guess_s == 0):
                return mid

            # if mid higher
            if (guess_s == -1):
                right_bound = mid-1
            # if mid lower
            elif (guess_s == 1):
                left_bound = mid+1
