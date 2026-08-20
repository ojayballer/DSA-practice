class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
          res=[0] * len(temperatures)
          stack=[] #index temprature 
          for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1] :
                old,temp = stack.pop()
                res[old] = i -old
            stack.append([i,temperatures[i]])
          return  res 
                 
              