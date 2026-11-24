class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, target in enumerate(nums):
            if target > 0:
                break
            if i > 0 and target == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = target + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

            