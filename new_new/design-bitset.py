class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.ones = [1] * size
        self.bitset_counter = {0:size, 1:0}
    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 0:
            self.bitset_counter[1] += 1
            self.bitset_counter[0] -= 1
        self.bitset[idx] = 1
        self.ones[idx] = 0
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 1:
            self.bitset_counter[1] -= 1
            self.bitset_counter[0] += 1
        self.bitset[idx] = 0
        self.ones[idx] = 1
        
    def flip(self) -> None:
        self.bitset, self.ones = self.ones, self.bitset
        self.bitset_counter[0], self.bitset_counter[1] = self.bitset_counter[1], self.bitset_counter[0]
        #0001
        #1110
    def all(self) -> bool:
        if self.bitset_counter[1] == len(self.bitset): return True
        else: return False

    def one(self) -> bool:
        if self.bitset_counter[1] >= 1: return True
        elif self.bitset_counter[1] == 0: return False

    def count(self) -> int:
        return self.bitset_counter[1]

    def toString(self) -> str:
        string = "".join(str(num) for num in self.bitset)
        return string


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()