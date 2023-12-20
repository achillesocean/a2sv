import random
class RandomizedSet:

    def __init__(self):
        self.temp = {}
        self.nums = []
    def insert(self, val: int) -> bool:
        if val not in self.temp:
            self.temp[val] = len(self.nums)
            self.nums.append(val)
            return True
        else: return False

    def remove(self, val: int) -> bool:
        if val in self.temp:
            idx = self.temp[val]
            last = self.nums[-1]
            self.nums[idx] = last
            self.nums.pop()
            self.temp[last] = idx
            del self.temp[val]
            return True
        else: return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()