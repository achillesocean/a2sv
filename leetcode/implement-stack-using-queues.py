class MyStack:

    def __init__(self):
        self.q1 = deque() # Main
        self.q2 = deque() # Temp Storage

    def push(self, x: int) -> None:
        # Only push to the back
        # So pushing will the same thing as appending.
        self.q1.append(x)

    def pop(self) -> int:
        # only pop from the front
        # but you wanna pop from the back, because LIFO.
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        left = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return left
        # if I'm supposed to popleft, 

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        left = self.q1.popleft()
        self.q2.append(left)
        self.q1, self.q2 = self.q2, self.q1
        return left

    def empty(self) -> bool:
        if len(self.q1) == 0: return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()