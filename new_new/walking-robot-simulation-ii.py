class Robot:

    def __init__(self, width: int, height: int):
        self.h = height
        self.w = width
        self.x = 0
        self.y = 0
        self.curdir = "East"
    def step(self, num: int) -> None: 
        if num != 0:
            self.num = num % ((self.w + self.h - 2) * 2) 
            if self.num == 0:
                if self.x == 0 and self.y == 0:
                    self.curdir = "South"
                if self.x == self.w - 1 and self.y == 0:
                    self.curdir = "East"
                if self.x == self.w - 1 and self.y == self.h - 1:
                    self.curdir = "North"
                if self.x == 0 and self.y == self.h - 1:
                    self.curdir = "West"

            while self.num: 
                if self.curdir == "East":
                    prev = min(self.num, self.w - 1 - self.x)
                    self.x += prev
                    self.num -= prev
                    if self.num > 0: 
                        self.curdir = "North"
                if self.curdir == "North":
                    prev = min(self.num, self.h - 1 - self.y)
                    self.y += prev
                    self.num -= prev
                    if self.num > 0:
                        self.curdir = "West"
                if self.curdir == "West":
                    prev = min(self.num, self.x)
                    self.x -= prev
                    self.num -= prev
                    if self.num > 0:
                        self.curdir = "South"
                if self.curdir == "South":
                    prev = min(self.num, self.y)
                    self.y -= prev
                    self.num -= prev
                    if self.num > 0:
                        self.curdir = "East"

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.curdir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()