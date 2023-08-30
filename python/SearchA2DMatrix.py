#leetcode #74
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def convert(index : int) -> int: 
            rowIndex = index // len(matrix[0])
            colIndex = index - rowIndex * len(matrix[0])
            return rowIndex, colIndex 
        
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r: 
            mid = l + (r - l) // 2

            rowIndex, colIndex = convert(mid)
            if matrix[rowIndex][colIndex] == target: 
                return True 
            elif matrix[rowIndex][colIndex] < target: 
                l = mid + 1 
            elif matrix[rowIndex][colIndex] > target: 
                r = mid - 1 
        
        return False 