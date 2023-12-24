class ATM:

    def __init__(self):
        self.notes = [20, 50, 100, 200, 500]
        self.count = [0] * 5

    def deposit(self, banknotes: List[int]) -> None:
        for idx in range(5):
            self.count[idx] += banknotes[idx]

    def withdraw(self, amount: int) -> List[int]:
        used = [0] * 5
        for idx in range(4, -1, -1):
            need = amount // (self.notes[idx])
            used[idx] = min(need, self.count[idx])
            amount -= (self.notes[idx] * used[idx])

        if amount != 0: return [-1]
        for idx in range(5):
            self.count[idx] -= used[idx]
        return used


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)