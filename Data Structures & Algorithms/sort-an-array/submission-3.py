import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quickSort(arr, low=0, high=None):
            if high is None:
                high = len(arr) - 1
            
            if low < high:
                pivot_index = partition(arr, low, high)
                quickSort(arr, low, pivot_index - 1)
                quickSort(arr, pivot_index + 1, high)
        quickSort(nums)
        return nums