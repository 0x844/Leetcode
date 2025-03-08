class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        max_amt = max(candies)

        for i in range(len(candies)):
            if (candies[i] + extraCandies >= max_amt):
                results.append(True)
            else:
                results.append(False)
        return results
            
