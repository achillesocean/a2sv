class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #no matter what, the first and last elements will be added into a partition.
        #wherever you put a partition, both that are on its either end, will be added.
        ends = weights[0] + weights[len(weights) - 1]
        #think of how many commas you would have to put given some k.
        if k == 1: return 0

        ret = []

        for ind in range(len(weights) - 1):
            ret.append(sum(weights[ind:ind + 2]) + ends)
        
        ret.sort()

        #what should you choose? remember that you'd be putting the commas all at once, simultaneously. 
        #so you can choose to put them where you'd have the max sum.
        #also remember, one comma=>two bags, two commas=>three bags...so by considering k - 1 commas, you're considering
        #k bags.
        #above, you calculated if you had only put one comma each place. so putting two commas, you can choose to put
        #them in the best two or worst two places possible.

        worst_places = sum(ret[:k - 1])#remember the k - 1 commas
        ret.sort(reverse=True)
        best_places = sum(ret[:k - 1])

        return best_places - worst_places