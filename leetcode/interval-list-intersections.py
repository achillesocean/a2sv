class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        # an intersection start from the left limit of one of the intervals, and 
        # ends at the right of one of the intervals.
        a, b = 0, 0
        ans = []

        while a < len(first) and b < len(second):
            left_of_B = second[b][0]
            right_of_B = second[b][1]
            right_of_A = first[a][1]
            left_of_A = first[a][0]
            if right_of_A < left_of_B:
                a += 1
            elif left_of_A > right_of_B:
                b += 1
            elif left_of_A >= left_of_B:
                temp = [left_of_A, min(right_of_A, right_of_B)]
                ans.append(temp[:])
                # which one ends first?
                if right_of_A < right_of_B:
                    a += 1
                else:
                    b += 1
            # maybe this B interval is between the left of A and right of A
            elif left_of_B >= left_of_A:
                temp = [left_of_B, min(right_of_B, right_of_A)]
                ans.append(temp[:])
                # which one ends first?
                if right_of_A < right_of_B:
                    a += 1
                else:
                    b += 1
            
        return ans