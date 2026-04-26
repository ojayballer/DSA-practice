class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       '''

      for i in range(len(nums)):

        for j in range(i+1,len(nums)):

            if nums[i] + nums[j]== target :

                return [i,j]'''


       hash_map={}    
       for i,n in enumerate(nums):
           difference=target-nums[i]
           if difference in hash_map :
                return [hash_map[difference],i]
           hash_map[n]=i


          
                
