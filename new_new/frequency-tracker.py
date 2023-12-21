class FrequencyTracker:

    def __init__(self):
        self.nums = collections.Counter()
        self.freq = collections.Counter()


    def add(self, number: int) -> None:
        #delete pair if it is the only one of its kind.
        prev = self.nums[number]
        self.nums[number] += 1
        self.freq[prev] -= 1
        self.freq[prev + 1] += 1

    def deleteOne(self, number: int) -> None:
        prev = self.nums[number]
        if prev == 0: return

        self.nums[number] -= 1
        self.freq[prev] -= 1
        self.freq[prev - 1] += 1
            
            #self.frequencies[self.freq[number]] = 1 + self.frequencies.get(self.freq[number], 0)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] >= 1
        print(self.frequencies)
        if frequency in self.frequencies and self.frequencies[frequency] >= 1: return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)