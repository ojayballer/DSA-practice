class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''BRUTE FORCE APPROACH(0(n)^3)
        nums.sort()
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.add((nums[i],nums[j],nums[k])) # A set removes duplicates automatically
        return [list(i) for i in res] '''
    

        #Two pointers solution
        nums.sort() #i.e [-4, -1, -1, 0, 1, 2]
        result=[]

        for i in range(0,len(nums)):
            # we want to terminate the program if the first element is positive,
            #because this means that we can never get a sum of 0 since the array is sorted 
            if nums[i] > 0:
                break
            # if i is >0 we want use >0 because nums[-1] (gotten from i=0) returns sumn else,
            #so i>0 works here and if i ==i-1,we skip because they are duplicates
            if i>0 and  nums[i]==nums[i-1]:
                continue

            l,r=i+1,len(nums)-1

            while l<r:
                sum=nums[i]+nums[l]+nums[r]

                if sum< 0:
                    l+=1
                elif sum>0:
                    r-=1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    #
                    # Keep moving left while next number is same
                    while l<r and nums[l] ==nums[l +1]:
                        l+=1

                    while l < r and  nums[r] == nums[r - 1]:
                        r-=1

                    l+=1
                    r-=1
        return result