class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            #what's returned is always a choice? or is that only when there's one choice left?
            #the functionality/RR holds for both: return the respective player's score to its caller.
            #choose the bigger score (for that player) out of the two paths they can take, which canbe seen from a game of nums.length == 2.
            #then the return score will be deducted from the choice of the other player?
            if left == right: return nums[right]
            pick_left = nums[left] - helper(left + 1, right)
            pick_right = nums[right] - helper(left, right - 1)

            return max(pick_left, pick_right)

        return helper(0, len(nums) - 1) >= 0
            # if turn:
            #     #player 1 is the player
            #     #he picks one of the two options definitely.
            #     pick1 = nums[left] - helper(not turn, left + 1, right)#player 1 chooses the first, but minus from that, player 2's best play.
            #     pick2 = nums[right] - helper(not turn, left, right - 1)
            # # regarless of which player it may be, return the best choice, the best play for him
            # else:
            #     #not same as above. you want player 
            #     pick1 = 