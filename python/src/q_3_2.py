class Stack(list):
    def __init__(self):
        self.mins = []

    def push(self, i):
        if not len(self.mins) or i <= self.mins[-1]:
            self.mins.append(i)
        self.append(i)
    
    def pop(self):
        i = super().pop()
        if i == self.mins[-1]:
            self.mins.pop()
        return i

    def min(self):
        return self.mins[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    assert(s.min() == 2)
    s.push(1)
    assert(s.min() == 1)
    s.pop()
    assert(s.min() == 2)
    print("success") 
