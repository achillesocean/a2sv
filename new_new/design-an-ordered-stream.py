class OrderedStream:

    def __init__(self, n: int):
        self.storage = [0] * (n + 1)
        self.ptr  = 1
        
    def insert(self, idKey: int, value: str) -> List[str]:
    #a chunk is a list of the inserted 
        self.storage[idKey] = value
        if self.ptr == idKey:
            while self.ptr < len(self.storage) and self.storage[self.ptr] != 0:
                self.ptr += 1
            return self.storage[idKey:self.ptr]
        else: return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)