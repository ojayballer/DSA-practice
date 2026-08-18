class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash ={}
       
       for i,n in enumerate(nums):
           difference = target - nums[i]
           if difference  in hash:
              return [hash[difference],i]
           
           hash[n] = i 


        
            
         
        
    
        