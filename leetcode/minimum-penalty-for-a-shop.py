class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers) + 1
        right = customers + "N"
        rPen = [0] * n
        for i in range(n):
            if right[i] == "Y":
                rPen[i] -= 1
        left = "Y" + customers 
        lPen = [0] * n
        for i in range(n):
            if left[i] == "N":
                lPen[i] -= 1
        acc = 0
        for i in range(n):
            acc += lPen[i]
            lPen[i] = acc
        acc = 0
        for i in range(n - 1, -1, -1):
            acc += rPen[i]
            rPen[i] = acc
        ans = [-1 * (rPen[i] + lPen[i]) for i in range(n)]
        return ans.index(min(ans))



        