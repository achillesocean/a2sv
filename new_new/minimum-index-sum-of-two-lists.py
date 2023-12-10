class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_val = float("inf")
        l1 = []

        for l in range(len(list1)):
            for r in range(len(list2)):
                if list1[l] == list2[r]:
                    if l + r < min_val:
                        if len(l1) > 0:
                            l1.pop()
                        l1.append(list1[l])
                        min_val = l + r
                    elif l + r == min_val:
                        l1.append(list1[l])
                        min_val = l + r
        return l1
