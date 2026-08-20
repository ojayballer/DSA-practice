class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       
       points = [(position,speed) for position,speed in zip(position,speed)]
       points.sort(reverse=True) # sort by position in reverse from biggest to smallest 
       
       time =[(target -position)/speed for position ,speed in points]
       stack=[]
       r=0
       stack.append(time[0])
       r+=1
       while r < len(position) : 
          if stack and time[r] > stack[-1] :
              stack.append(time[r])
          r+=1 
       return len(stack)
          
           

