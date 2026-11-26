class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        profit = 0
        left = 0
        for right in range(len(prices)):
            while prices[left] > prices[right]:
                left += 1
            profit = prices[right] - prices[left]
            best = max(best, profit)
        return best

            
            
