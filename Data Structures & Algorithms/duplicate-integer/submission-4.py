class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        '''for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False'''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]== nums[j] :
                    return True
        return False 

'''
         list=[]
        for i in nums:
            if i in list:
                return True
            else:
                list.append(i)
        return False



        hash_map= {}
      
        for i in nums:
            if hash_map[i] in hash_map:
                return True
            else:
                hash_map[i]=False
        return False
'''





    
