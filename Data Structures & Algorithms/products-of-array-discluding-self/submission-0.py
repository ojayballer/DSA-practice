class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' ##brute-force ->o(n^2)
        res=[0]*len(nums)  #create the array and initialise all of them to 0
        for i in range(len(nums)):
          product=1
          for j in range(len(nums)):  #[1,2,3,4]
            if i!= j:
                product*=nums[j]
            else :
                pass  ## else do nothing 
          res[i]=product

        return res '''



        ##using prefix and suffix 
        prefix=[0]*len(nums) ; suffix=[0]*len(nums) ; res=[0]*len(nums)  #[1,2,3,4]
        prefix[0]=1 ; suffix[-1]=1 ; #set the prefix left index to zero and the suffix last index to zero
        for i in range(1,len(nums)):  #compute prefix
            prefix[i] = prefix[i-1] *nums[i-1] 
        
        for i in range(len(nums)-2,-1,-1):  #start at index 3 and move towards index 0
            suffix[i]= suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res[i]=prefix[i] * suffix[i]
        

        return res





            

        