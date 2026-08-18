class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       counTstrs={}
       
       for j in strs :  # over each word 
        count=[0] *26
        for i in j : # over each letter in j 
            count[ord(i)-ord('a')] +=1
            
        countimm=tuple(count) #convert count to tuple 
        
       
        if countimm not in counTstrs :
            counTstrs[countimm] =[] #new group 
        
        counTstrs[countimm].append(j)

       return list(counTstrs.values())


        
             


