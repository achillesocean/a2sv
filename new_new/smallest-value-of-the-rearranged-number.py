class Solution:
    def smallestNumber(self, num: int) -> int:
        #use Counter to record the number of occurence of each digit, then use that to make the minimum number using successively least numbers
        #sort the digits in an array?
        if num == 0: return 0
        flag = False
        if num < 0:
            flag = True
            num = abs(num)
        num = list(str(num))
        num = [int(n) for n in num]
        num.sort()
        temp = num
        res = []
        if flag:
            temp.sort(reverse=True)
            res += temp
            res = [str(n) for n in res]
            res = "".join(res)
            res = -int(res)
            return res
        i = 0
        for r in range(len(num)):
            if num[r] == 0:
                i += 1
        
        res.append(num[i])
        num.remove(num[i])
        res += num
        res = [str(n) for n in res]
        res = "".join(res)
        res = int(res)
        return res
        