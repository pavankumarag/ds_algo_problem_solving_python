class permutations:
    used = dict()
    out = ""  
    str = ""
    def __init__(self,input):
        self.str = input
        

    def permute(self):
        if len(self.out) == len(self.str):
            print self.out
            return
        for i in range(len(self.str)):
            try:
                if self.used[i] == 1 :
                    continue
            except:
                pass
            self.out = self.out + self.str[i]
            self.used[i] = 1
            self.permute()
            self.used[i] = 0
            self.out = self.out[0:len(self.out)-1]    

       
     
p = permutations("abc")
p.permute()