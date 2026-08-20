class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
          res= [0] *len(temperatures)
          stack=[] # i,temp 
          r=0 
          while r < len(temperatures) :
            while stack and temperatures[r] > stack[-1][1] :
               old ,temp = stack.pop()
               res[old] = r - old 
            stack.append([r,temperatures[r]])
            r+=1 
          return res 
            
