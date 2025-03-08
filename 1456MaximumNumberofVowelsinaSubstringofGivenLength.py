class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count
        left = 0
        

        # before sliding window: 
        # check if left ptr was vowel, decrement count
        # if right ptr vowel, increment count
        for right in range(k, len(s)):
            if (s[left] in vowels):
                count -= 1
            if (s[right] in vowels):
                count += 1
            max_count = max(max_count, count)
            left += 1
            right += 1
        return max_count

        


        
