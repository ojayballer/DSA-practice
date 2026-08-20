class MinStack:

    def __init__(self):
        self.store=[]
        self.minstore = []
        

    def push(self, val: int) -> None:
       self.store.append(val) 
       curr_min=min(val,self.minstore[-1] if self.minstore else val)
       self.minstore.append(curr_min)

    def pop(self) -> None:
        self.store.pop()
        self.minstore.pop()


    def top(self) -> int:
        return self.store[-1]


    def getMin(self) -> int:
        return self.minstore[-1]