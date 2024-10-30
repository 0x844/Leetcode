class Solution:

    def topKFrequent(self, nums, k):

        map = {}
        lst = []

        if len(nums) == 1:
            return nums

        if len(nums) == 0:
            return None

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for key, value in map.items():
            lst.append(value)
        print(map)
        lst.sort()

        results = []

        for key, value in map.items():
            if value in lst[-k::]:
                results.append(key)

        return results
