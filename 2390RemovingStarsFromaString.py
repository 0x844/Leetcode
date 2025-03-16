class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
                continue
            stack.append(s[i])
        
        return ''.join(stack)
