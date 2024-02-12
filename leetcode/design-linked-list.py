class Node:
    def __init__(self, val, next=None):
        self.val  = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        #self.head = None
        self.length = 0
        self.dummy = Node(0, None)

    def get(self, index: int) -> int:
        if index >= self.length: return -1
        else:
            cur = self.dummy
            for _ in range(index):
                cur = cur.next
            return cur.next.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.dummy.next)
        self.dummy.next = node
        self.length += 1
    def addAtTail(self, val: int) -> None:
        tail = Node(val, None)
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = tail
        self.length += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return
        node = Node(val)
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length: return
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)