""""
The main class, player, consists of :
    player.lh =    player.left_player value
    player.rh =    player.right_player value
    player.op =    (player.lh, player.rh)
    player.[l/r]h.live = True/False             [Whether player is alive]
 """


class Player:
    def __init__(self,computer):
        global opp
        opp = computer
        self.lh = 1
        self.rh = 1
        self.op = [self.lh, self.rh]
        self.lh.live = self.rh.live = True

    def checkvals(self):
        if self.lh == 0 or self.lh == 5:
            self.lh.live = False
            self.lh = 0
        else:
            self.lh.live = True
        if self.rh == 0 or self.rh == 5:
            self.rh.live = False
            self.rh = 0
        else:
            self.lh.live = True
        

    def rearrange(self, h1, h2, n):
        # Takes 3 values h1, h2, n
        # Moves n values from h1 to h2
        if h1 > 0 and h1 - n >= 0:
            h2 = h2 + n
            h1 = h1 - n
            if self.op.index(h1):
                self.op = [h1, h2]  # If index of h1 is True i.e. index == 1, h1 is right hand
                # And hence h2 is left hand
            else:
                self.op = [h2, h1]
            self.checkvals()
        elif h1 == 0:
            self.movefail("Not enough points in hand to give!")

    def moveFail(self, msg):
        global opp
        print("Encountered an error!\n", msg)
        self.getinp(self,opp)

    def getInp(self):
        global opp
        h1,h2,n = input("Enter with spaces between values, hand(l/r), opposing hand(l/r/self), no. to give \n\nEnter Here : ").split(" ")
        n = int(n)
        if n == 0:
            self.moveFail("Can't move 0 chopstics!")
        if h2 == "self":
            if h1 == "l":
                self.rearrange(self,self.lh,self.rh,n)
            if h1 == "r":
                self.rearrange(self,self.rh,self.lh,n)
            self.op = [self.lh,self.rh]
        elif h2 == "l":
            if h1 == "l":
                if self.lh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.lh += n
            else:
                if self.rh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.lh += n
        else: # h2 == "r"
            if h1 == "l":
                if self.lh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.rh += n
            else:
                if self.rh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.rh += n
        self.checkvals()