class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        def palindrome(left, right):
            while left < right:
                if (s[left] != s[right]):
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if (s[left] != s[right]):
                return palindrome(left, right - 1) or palindrome(left + 1, right)
            left += 1
            right -= 1

        return True

    
