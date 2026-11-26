class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRow = 0
        rightRow = len(matrix) - 1
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                left = 0
                right = len(matrix[midRow]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[midRow][mid] == target:
                        return True
                    if matrix[midRow][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            if target > matrix[midRow][-1]:
                leftRow = midRow + 1
            else:
                rightRow = midRow - 1
        return False