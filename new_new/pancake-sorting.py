class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        #find cur_max index. k = i + 1
        #flip upto k
        #flip 0 to length
        #add k = length, i + 1
        #repeat for n -= 1
        #find second cur_max = for n = n - 1
        #blah blah
        ans = []
        n = len(arr)
        for diff in range(len(arr)):
            #finally u append k, len - diff
            cur = arr.index(max(arr[:n - diff])) + 1
            l, r = 0, cur - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
            l, r = 0, n - 1 - diff
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1 
            ans += [cur, n - diff]

        return ans
