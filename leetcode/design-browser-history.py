class Node:
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.length = 1
        self.cur = self.home
    def visit(self, url: str) -> None:
        visit = Node(url)
        self.cur.next = visit
        visit.prev = self.cur
        self.cur = visit
        self.length += 1

    def back(self, steps: int) -> str:
        #should reduce length
        for _ in range(steps):
            if self.cur != self.home:
                self.cur = self.cur.prev
                self.length -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        #should increase length
        for _ in range(steps):
            if self.cur.next != None:
                self.cur = self.cur.next
                self.length += 1
        return self.cur.url
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)