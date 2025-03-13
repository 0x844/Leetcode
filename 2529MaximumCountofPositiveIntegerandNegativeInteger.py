class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        hashmap = {"neg" : 0, "pos" : 0}

        for num in nums:
            if num < 0:
                hashmap["neg"] += 1
            elif num > 0:
                hashmap["pos"] += 1
        return max(hashmap["neg"], hashmap["pos"])
