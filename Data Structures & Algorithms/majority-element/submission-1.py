class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = dict()
        for num in nums:
            maxCount.setdefault(num, 0)
            maxCount[num] += 1
        largest = 0
        res = 0
        for num, count in maxCount.items():
            if count > largest:
                res = num
                largest = count
        return res

        