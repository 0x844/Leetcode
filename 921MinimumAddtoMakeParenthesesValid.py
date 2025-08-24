class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        closed_count = 0

        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")" and open_count > 0:
                open_count -= 1
            else:
                closed_count += 1
        return open_count + closed_count
