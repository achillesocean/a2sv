class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_count = 0
        close_count = 0
        ans = []

        def helper(cur):
            nonlocal open_count
            nonlocal close_count
            nonlocal ans
            # add an open then explore further. 
            # pop that, add a closer then explore further.
            # the added constraint of validity. this will even help us prune
            if open_count == close_count and open_count == n:
                ans.append("".join(cur[:]))
                return
            if open_count > n or close_count > n or close_count > open_count: return
            # if open_count == 0:
            #     cur+="("
            #     open_count += 1
            #     helper(cur)
            cur.append("(")
            open_count += 1
            helper(cur)
            cur.pop()
            open_count -= 1
            cur += ")"
            close_count += 1
            helper(cur)
            cur.pop()
            close_count -= 1

        helper([])
        return ans