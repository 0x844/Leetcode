class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_list = []
        s = list(s)
        for char in s:
            if char in vowels:
                vowel_list.append(char)
        vowel_list.reverse()
        idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list[idx]
                idx += 1
            
        return ''.join(s)
