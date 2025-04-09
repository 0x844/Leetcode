class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        output = ""
        a_count = 1
        formatted = list(sentence.split(" "))
        for word in formatted:
            if word[0] in vowels:
                output += (word + "ma" + ("a" * a_count))
            else:
                temp = word[0]
                output += (word[1:] + temp + "ma" + ("a" * a_count))
            output += " "
            a_count += 1
        return output.rstrip()
