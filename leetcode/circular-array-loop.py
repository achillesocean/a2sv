class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next(i):
            return (i + nums[i]) % n
        for i in range(len(nums)):
            slow, fast = i, next(i)
            if nums[i] == 0: continue
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow != next(slow): return True
                    break
                slow = next(slow)
                fast = next(next(fast))
            ind = i
            while nums[i] * nums[next(i)] > 0:
                nums[i] = 0
                i = next(i)
        return False