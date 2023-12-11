class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #run through array, each time you discover 1, count steps to bring it by 
        #itself back to the index you're on.
        #but can you take care of this with a single run-through?

        #001011
        #2 + 4 + 5 = 11
        #2 - 1 + 4 - 1 + 5 - 1 = 8
        #4 - 2 + 5 - 2 = 5
        #4 - 3 + 5 - 3 you have to account for the balls to the left of the indices*
        #abs(2 - 4) + 4 - 3 + 5 - 3
        
        n = len(boxes)
        output = [0] * n
        ones = []
        for i in range(n):
            if boxes[i] == "1":
                ones.append(i)
        for i in range(n):
            for j in range(len(ones)):
                output[i] += abs(i - ones[j])
        return output
