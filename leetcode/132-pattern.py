class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # FIND I, FIND J, FIND K
        #when you get to a k value, you wanna look backwards to see if there's any value greater than it.
        stack = [] # later, try to do it without keeping a pair, keeping the min in a variable..

        # you wanna maximize your j value, minimize your i value, and look for a k.
        # the max isn't gonna always be on the top of the stack.
        curMin = nums[0] # to update each pair's minimum element.
        # why mono decreasing? because we wanna max our j value, and we want to find a k that is less than that j.
        # why pop? because we may find a k value suitable for the current j value, but not suitable for that j value's i value...less than that i value.
        # so we'll wanna have a bigger k value, and that's why we pop.
        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]: return True
            stack.append([n, curMin])
            curMin = min(curMin, n)

        return False