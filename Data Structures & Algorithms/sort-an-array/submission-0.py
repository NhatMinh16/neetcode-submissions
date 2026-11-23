class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            leftHalf = arr[:mid]
            rightHalf = arr[mid:]
            sortedLeft = mergeSort(leftHalf)
            sortedRight = mergeSort(rightHalf)
            return merge(sortedLeft, sortedRight)
        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        sortedArr = mergeSort(nums)
        return sortedArr

