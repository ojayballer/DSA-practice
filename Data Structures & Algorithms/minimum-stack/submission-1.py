class MinStack:

    def __init__(self):
        self.store=[]
        

    def push(self, val: int) -> None:
        self.store.append(val)
        

    def pop(self) -> None:
        if self.store :
          return self.store.pop(-1)
        return None 

        

    def top(self) -> int:
        if self.store:
           return self.store[-1]
        return None

    def getMin(self) -> int:
        return min(self.store) if self.store else None 
        
