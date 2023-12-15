class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        #if it's a good integer, it won't exist in fronts once you've flipped it
        #(n^2) complexity is allowed
        valid = float("inf")
        counter = defaultdict(list)
        for i in range(len(fronts)):
            counter[backs[i]].append(i)
        for key in counter:
            invalid = False
            for i in counter[key]:
                if fronts[i] == key: 
                    invalid = True
            if not invalid:
                valid = min(valid, key)

        counter = defaultdict(list)
        for i in range(len(fronts)):
            counter[fronts[i]].append(i)
        for key in counter:
            invalid = False
            for i in counter[key]:
                if backs[i] == key: 
                    invalid = True
            if not invalid:
                valid = min(valid, key)

        return valid if valid != float("inf") else 0

