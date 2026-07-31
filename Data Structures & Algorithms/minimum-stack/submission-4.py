class MinStack:

    def __init__(self):
        self.store=[]
        self.minstore=[]
        

    def push(self, val: int) -> None:
        self.store.append(val)
        self.minstore.append(min(val,self.minstore[-1] if self.minstore else val ))

    def pop(self) -> None:
        if self.store :
          self.store.pop(-1)
          self.minstore.pop(-1)
        return None 

    def top(self) -> int:
        if self.store:
           return self.store[-1]
        return None

    def getMin(self) -> int:
        return self.minstore[-1]
        
