class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l=0 
      r=1 
      maxP=0 
      while r < len(prices):
         maxP= max(maxP,prices[r] - prices[l])
         while prices[r] < prices[l]:
           l+=1 
         
         r+=1 
      
      return maxP 
      #
         

          