class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       counTstrs=defaultdict(list)
       
       for j in strs :  # over each word 
        count=[0] *26
        for i in j : # over each letter in j 
            count[ord(i)-ord('a')] +=1
            
        counTstrs[tuple(count)].append(j)
       return list(counTstrs.values())


        
             


