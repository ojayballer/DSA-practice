class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False   
        
        hashs1= {}
        hashs2={}
        for i in range(len(s1)):
            hashs1[s1[i]] =hashs1.get(s1[i],0)+1

        for j in range(len(s1)):
            hashs2[s2[j]] = hashs2.get(s2[j],0)+1

        if hashs1 ==hashs2:
            return True 


        l=0
        r=0
        #slide across the rest of the window 
        #for i  in range(s1,s2,1):
        r=len(s1)
        l=0
        while r < len(s2):
            hashs2[s2[r]]=hashs2.get(s2[r],0)+1
            hashs2[s2[l]] -=1 
            
            if hashs2[s2[l]] == 0 :
                del hashs2[s2[l]]

            if hashs1==hashs2 :
                return True 
            r+=1
            l+=1
        
        return False 
        


               