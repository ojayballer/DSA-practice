class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      #position,speed 
      pair= [(p,s) for p,s in zip(position,speed)]
      pair.sort(reverse=True)
      stack=[]
      for  p,s in pair:
        time=(target-p)/s
        if not stack or time >stack[-1]: # add first element when stack is empty 
            stack.append(time)
      return len(stack)
