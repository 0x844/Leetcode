class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for char in s:
            if char.isalnum():
                formatted += char.lower()
        left = 0
        right = len(formatted) - 1
        while left <= right:
            if formatted[left] == formatted[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
