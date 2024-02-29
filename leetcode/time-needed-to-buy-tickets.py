class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Is there any other way than to simulate it?
        # If we had to simulate it, 
        tickets = deque(tickets)
        count = 0
        while tickets[k] > 0:
            #k-=1
            #k = k % len(tickets)
            if tickets[-1] == 0: 
                tickets.pop()
            if tickets[0] > 0:
                left = tickets.popleft()
                left -= 1
                tickets.append(left)
                k -= 1
                k = k % len(tickets)
                count += 1
            # 1 2 3   k = 0

        return count