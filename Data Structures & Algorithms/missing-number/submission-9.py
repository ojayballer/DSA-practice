class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n=len(nums)
      total=n*(n+1)//2
      expected=sum(nums)
      return total-expected
      
