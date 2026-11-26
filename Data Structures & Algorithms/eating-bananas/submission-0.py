class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        lowerBound = 1
        res = upperBound
        while lowerBound <= upperBound:
            mid = (upperBound + lowerBound) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p) / mid)
            if total <= h:
                res = mid
                upperBound = mid - 1
            else:
                lowerBound = mid + 1
        return res

