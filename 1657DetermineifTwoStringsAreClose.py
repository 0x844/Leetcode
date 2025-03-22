class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)):
            return False
        if (set(word1) == set(word2)):
            lst1 = []
            lst2 = []
            hashmap = {}
            for c in word1:
                if c in hashmap:
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1
            for value in hashmap.values():
                lst1.append(value)
            hashmap = {}
            for c in word2:
                if c in hashmap:
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1
            for value in hashmap.values():
                lst2.append(value)
            return sorted(lst1) == sorted(lst2)
        return False
