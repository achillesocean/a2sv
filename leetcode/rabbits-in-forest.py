class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        pref = 0
        zeros = 0
        answers.sort(reverse=True)
        for i in range(len(answers) - 2, -1, -1):
            if answers[i] == 0:
                zeros += 1
                answers.pop()
        answers.sort()
        count = Counter(answers)
        ret = 0
        for ans in count:
            pref = 0
            for ind in range(count[ans]):
                if ans >= pref:
                    pref += ans + 1
                elif ind > pref - 1:
                    pref += ans + 1
            print(pref)
            ret += pref
        return ret + zeros