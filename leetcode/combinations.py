class Solution:
    # def helper(self, n, cur):
        # Because we're doing combinations, after exhausting for one number, 
        # don't back to it again.
        # It is not valid, the current number and all after it are valid

        # Handle the base-case
            # When current combination size reaches k
        # If valid, place number
        # Recurse/Backtrack. No!! Recurse=given a valid candidate, explore further
        # We recurse/call backtrack() on our current state.
        # Remove=Backtrack
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(first, cur):
            if len(cur) + n - first + 1 < k: return
            if len(cur) == k:
                ans.append(cur[:])
                return
            for num in range(first, n + 1):
                cur.append(num)
                helper(num+1, cur)
                cur.pop()
        helper(1, [])
        return ans