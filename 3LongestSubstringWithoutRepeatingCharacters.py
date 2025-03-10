class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        total = 0
        seen = set()

        for i in range(len(s)):
            while (s[right] in seen):
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            total = max(total, right - left + 1)
            right += 1
        return total
