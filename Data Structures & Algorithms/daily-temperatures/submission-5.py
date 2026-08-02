class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      res=[0]*len(temperatures)
      stack=[]# index,temperature 

      for i,n in enumerate(temperatures):
        while stack and n > stack[-1][1]:
            StackIndex,Temp =stack.pop()
            res[StackIndex]=i-StackIndex
        stack.append((i,n))
      return res 
