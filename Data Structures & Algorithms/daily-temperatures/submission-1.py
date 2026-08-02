class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      res=[]
      for i in range(len(temperatures)):
        count=0 #for the last element since it has nothing to compare to,it becomes 0 
        for j in range(i+1,len(temperatures)):
            if temperatures[j] <=temperatures[i]:
                count+=1
            else :
               count+=1
               break
        count =0 if j==len(temperatures)-1  and temperatures[j] <=temperatures[i] else count 
        res.append(count)
      return res 
                 