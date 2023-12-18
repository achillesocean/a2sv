class AuthenticationManager:

    def __init__(self, timeToLive: int):#all tokens live timetoLive seconds
        self.timeToLive = timeToLive
        self.tokens = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
    #renew only if unexpired
        if tokenId in self.tokens:
            if self.tokens[tokenId] + self.timeToLive > currentTime:
                self.tokens[tokenId] = currentTime
    def countUnexpiredTokens(self, currentTime: int) -> int:
    #number of unexpired tokens at given currenttime
       # print(self.tokens)
        self.count = 0
        for token in self.tokens:
        #if age < currentTime
            if self.tokens[token] + self.timeToLive > currentTime:
                self.count += 1
        return self.count 


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)