class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        output = []
        for dom in cpdomains:
            temp = dom.split()
            temp = ".".join(temp)
            temp = temp.split(".")
            for i in range(1, len(temp)):
                key = ".".join(temp[i:])
                domains[key] += int(temp[0])
            
        for key in domains:
            output.append(str(str(domains[key]) + " " + str(key)))
            
        return (output)
        