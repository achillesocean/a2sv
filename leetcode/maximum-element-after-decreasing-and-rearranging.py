class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        g = 0
        counter = Counter(arr)
        for i in arr:
            g += i > n
    
        ans = n 
        for i in range(n, 0, -1):
            if counter[i] > 0:
                g += counter[i] - 1
            else:
                if g > 0:
                    g -= 1
                else:
                    ans -= 1

        return ans
        #put and check for its surplus    


        return min(len(arr), max(arr))
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]