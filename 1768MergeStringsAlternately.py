class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        count = 0
        if (len(word1) < len(word2)):
            for i in range(len(word1)):
                merged += word1[i]
                merged += word2[i]
                count += 1
            merged += word2[count:]
        elif (len(word1) > len(word2)):
            for i in range(len(word2)):
                merged += word1[i]
                merged += word2[i]
                count += 1
            merged += word1[count:]
        else:
            for i in range(len(word2)):
                merged += word1[i]
                merged += word2[i]
        return merged

