class Node:
    def __init__(self, key=None, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.record = {}
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.record:
            get = self.record[key]
            temp = get.next
            get.prev.next = temp
            temp.prev = get.prev
            get.next = self.head.next
            get.prev = self.head
            self.head.next.prev = get
            self.head.next = get
            return get.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.record:
            get = Node(val=value, key=key, next=self.head.next, prev=self.head)
            self.head.next.prev = get
            self.head.next = get
            self.record[key] = get
        else:
            get = self.record[key]
            get.val = value
            temp = get.next
            get.prev.next = temp
            temp.prev = get.prev
            get.next = self.head.next
            get.prev = self.head
            self.head.next.prev = get
            self.head.next = get
        if len(self.record) > self.capacity:
            temp = self.tail.prev
            temp.prev.next = self.tail
            self.tail.prev = temp.prev
            del self.record[temp.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)