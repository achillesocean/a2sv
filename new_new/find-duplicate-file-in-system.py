class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #a group is made based on its content
        files = []
        res = defaultdict(list)

        for path in paths:
            files = path.split()
            for fl in range(1, len(files)):
                l = files[fl].index("(")
                r = files[fl].index(")")
                res[files[fl][l + 1:r]].append(files[0]+"/"+files[fl][:l])
        
        res = [value for value in res.values() if len(value) > 1]
        #res = [val for key, val in enumerate(res)]
        return res
        