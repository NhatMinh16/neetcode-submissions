class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index in range(len(nums)-1):
            if target - nums[first_index] in nums[first_index+1:]:
                remaining = target - nums[first_index]
                second_index = nums[first_index+1:].index(remaining) + first_index + 1
                return [first_index, second_index]