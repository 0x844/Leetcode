class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def binary_search(row, target):
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (high + low) // 2
                if (row[mid] == target):
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        rows = len(matrix)

        for i in range(rows):
            if (binary_search(matrix[i], target) == True):
                return True
        return False
