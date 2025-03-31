class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 0:
            return True

        count = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] != 1 and flowerbed[i+1] != 1:
                count +=1 
                flowerbed[i] = 1
                continue
            if i+1 == len(flowerbed) and flowerbed[i] != 1 and flowerbed[i-1] != 1:
                count += 1
                flowerbed[i] = 1
                continue
            if flowerbed[i] != 1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1 
        return count >= n
