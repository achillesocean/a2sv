class Solution:
    def splitString(self, s: str) -> bool:
        # path = [] at first.

        def helper(cur_ind, path):
            # Basecase
            if cur_ind >= len(s):
                print(path)
                return len(path) > 1

            step = ""
            for ind in range(cur_ind, len(s)):# Notice how cur_ind for every call is one greater than whatever called it.
                                        # That's why you can just start your loop from it and catch it at first within every loop 
                step += s[ind] # Create the new possible path from that given index
# Why step += s[ind]? because say your current path had you take steps 0, 5. your next step choices are
# 0, 00, 004, and 0043. That's true for all the steps; even the ones you had already gone through.
                if not path or int(path[-1]) - int(step) == 1:
                    path.append(step)
                # Backtrack to explore further standing on that place within the path.
                    if helper(ind + 1, path): 
                        return True# Catch the True return to cause a chain reaction of True returns
                # that goes all the way up.
                
                # But after exploring that path, what if you had taken a different step?
                    path.pop()
                # So exploring a different path is to remove the one you just took and to instead take a longer one.
            # !!!Once the chain of reactions is set, it doesn't stop until everything is done.
            # That's why you return False just once; after every path is tried.
            return False
        
        return helper(0, [])