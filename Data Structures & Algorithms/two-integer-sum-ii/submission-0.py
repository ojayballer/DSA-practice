class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' BRUTE FORCE
         for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]== 3 :
                    return [i+1,j+1]'''
         
        hash_map={} #0;1 ,1;2
        for i,n in enumerate(numbers):
               difference=target-numbers[i]
               if difference in hash_map:
                   return [hash_map[difference]+1,i+1]
               hash_map[n]=i