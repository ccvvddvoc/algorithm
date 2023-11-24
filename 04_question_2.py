class BrowserHistory(object) :
    def __init__(self, homepage) :
        self.li = [homepage]
        self.index = 0
    
    def visit(self, url) :
        if self.index != len(self.li) - 1:
            for i in range(self.index+1, len(self.li)) :
                self.li.pop()
        self.li.append(url)
        self.index += 1

    def back(self, steps) :
        if (self.index - steps < 0) :
            self.index = 0
            return self.li[0]
        else :
            self.index = self.index - steps
            ret = self.li[self.index]
            return ret
             
    def forward(self, steps) :
        if (self.index + steps > (len(self.li) - 1)) :
            self.index = len(self.li) - 1
            ret = self.li[self.index]
            return ret
        else :
            self.index = self.index + steps
            ret = self.li[self.index]
            return ret
        
bh = BrowserHistory("leetcode.com")
bh.visit('google.com')
bh.visit('facebook.com') 
bh.visit('youtube.com')
print(bh.back(1))
print(bh.back(1))
print(bh.forward(1))
bh.visit('linkedin.com')
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))