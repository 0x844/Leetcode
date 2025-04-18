class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        occurence = defaultdict(int)
        arr = []
        for num in nums:
            occurence[num] += 1
        for num in nums:
            if occurence[num+1] or occurence[num] > 1 or occurence[num-1]:
                continue
            arr.append(num)
        return arr
