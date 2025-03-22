class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        seen = []
        for val in hashmap.values():
            if val in seen:
                return False
            else:
                seen.append(val)
        return True
