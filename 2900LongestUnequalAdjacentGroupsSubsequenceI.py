class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words) == 1:
            return words

        stack = [words[0]]
        bstack = [groups[0]]
        for i in range(1,len(groups)):
            if bstack[-1] != groups[i]:
                stack.append(words[i])
                bstack.append(groups[i])
        return stack
