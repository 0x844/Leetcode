class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True 

        right = 0
        pos = 0 # position in s 

        while right < len(t):
            if pos < len(s) and t[right] == s[pos]:
                pos += 1
                right += 1
            else:
                right += 1
        return pos == len(s)
"""
right = 3
pos = 2
t = ahbgdc
         ^
s = abc
      ^
"""
