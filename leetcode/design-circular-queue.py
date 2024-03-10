class MyCircularQueue:
    #some remarks:'rear' should point to the empty slot, to the next insertion position.
    #if rear overwrites front, the queue is full. 
    #if front becomes equal to rear, the queue is empty.
    #both pointers are -1 if the queue is empty.

    def __init__(self, k: int):
        self.q = [None] * k
        self.front = k-1
        self.rear = k-1
        self.full = False
        self.empty = True
    def enQueue(self, value: int) -> bool:
        #can't enqueue if full.
        #if self.rear == self.front and self.front != -1: return False
        if self.full: return False
        #else, enqueue
        #enqueue at where 'rear' is, then update rear.
        self.q[self.rear] = value
        self.rear += 1
        self.rear %= len(self.q)
        if self.rear == self.front: 
            self.full = True
        self.empty = False
        return True

    def deQueue(self) -> bool:
        if self.empty: return False
        self.full = False#regardless of anything 
        self.front += 1
        self.front %= len(self.q)
        #if while you're dequeueing, you dequeue everything:
        if self.front == self.rear:
            self.empty = True
        return True

    def Front(self) -> int:
        if self.empty: return -1
        return self.q[self.front]

    def Rear(self) -> int:
        #should return what currently is at the rear
        if self.empty: return -1
        return self.q[(self.rear - 1) % len(self.q)]

    def isEmpty(self) -> bool:
        return self.empty

    def isFull(self) -> bool:
        return self.full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()