class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
       counter =0 
       numset= set(nums)
       longest = 0 
       for num in numset :
         if (num-1) not in numset:
            streak =1 
            while (num+streak) in numset :
                streak+=1
            longest=max(longest,streak)
       
       return longest #longest streak
       