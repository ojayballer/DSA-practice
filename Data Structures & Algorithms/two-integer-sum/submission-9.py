class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash={}
       for  i,n in enumerate(nums):
  
          difference = target - n
          if difference in hash : # h
            return [hash[difference],i]
          hash[n] =i 
      
            

    
        