class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        flag = False
        n = arr.index(max(arr))

        if n == len(arr) - 1: return False
        if n == 0: return False
        for i in range(1, n):
            if arr[i] <= arr[i - 1]: return False
            if arr[i] > arr[i - 1]:
                flag = True
            if flag and arr[i] == arr[i - 1]: return False

        for i in range(n + 1, len(arr)):
            if arr[i] == arr[i - 1]: return False
            if arr[i] >= arr[i - 1]: return False 
           
        return True