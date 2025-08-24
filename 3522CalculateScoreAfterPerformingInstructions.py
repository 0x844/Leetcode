class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        i = 0
        seen_idx = {}

        while True:
            if i in seen_idx or i < 0 or i >= len(values):
                return score
            if instructions[i] == "jump":
                seen_idx[i] = 1
                i = i + values[i]
            elif instructions[i] == "add":
                score += values[i]
                seen_idx[i] = 1
                i += 1
